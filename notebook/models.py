
from extensions import db
from utils.database import CRUDMixin


class Notebook(db.Model, CRUDMixin):
    __tablename__ = "notebooks"
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    parentNotebookId = db.Column(db.Integer, db.ForeignKey("notebooks.id"))
    seq = db.Column(db.Integer)
    title = db.Column(db.String(255))
    urlTitle = db.Column(db.String(255))
    numberNotes = db.Column(db.Integer)
    isTrash = db.Column(db.Boolean)
    isBlog = db.Column(db.Boolean)
    createdTime = db.Column(db.DateTime)
    updatedTime = db.Column(db.DateTime)
    # UpdateSequenceNum
    usn = db.Column(db.Integer)
    isDeleted = db.Column(db.Boolean)
    subs=[]

    def getNotebooks(self, userId):
        return self.query.filter(Notebook.userId == userId).all()


    def sortSubNotebooks(self,eachNotebooks):
        # 遍历子, 则子往上进行排序
        for eachNotebook in eachNotebooks:
            if (eachNotebook.subs != None) and (len(eachNotebook.subs) > 0):
                eachNotebook.subs = self.sortSubNotebooks(eachNotebook.subs)
                
        sorted(eachNotebooks,key=lambda x:x[3])

        # 子排完了, 本层排
        # sort.Sort(&eachNotebooks)
        return eachNotebooks


    # 整理(成有关系)并排序
    # GetNotebooks()调用
    # ShareService调用
    def parseAndSortNotebooks(self,userNotebooks , noParentDelete, needSort):
        # 整理成info.Notebooks
        # 第一遍, 建map
        # notebookId => info.Notebooks
        userNotebooksMap = {}
        for each in userNotebooks:
            newNotebooks=Notebook()
            newNotebooks.notebookId = each.notebookId
            newNotebooks.title = each.title
            #		newNotebooks.Title = html.EscapeString(each.Title)
            newNotebooks.title = each.title.replace("<script>", "").replace("</script", "")
            newNotebooks.seq = each.seq
            newNotebooks.userId = each.userId
            newNotebooks.parentNotebookId = each.parentNotebookId
            newNotebooks.numberNotes = each.numberNotes
            newNotebooks.isTrash = each.isTrash
            newNotebooks.isBlog = each.isBlog
            # 存地址
            userNotebooksMap[each.NotebookId] = newNotebooks
        

        # 第二遍, 追加到父下

        # 需要删除的id
        needDeleteNotebookId={}
        for (nbid, each) in userNotebooksMap:
            # 如果有父, 那么追加到父下, 并剪掉当前, 那么最后就只有根的元素
            if each.parentNotebookId==0 or each.parentNotebookId==None:
                if userNotebooksMap[each.parentNotebookId] != None:
                    userNotebooksMap[each.parentNotebookId].subs.append(each) # Subs是存地址
                    # 并剪掉
                    # bug
                    needDeleteNotebookId[nbid] = True
                    # delete(userNotebooksMap, id)
                elif noParentDelete:
                    # 没有父, 且设置了要删除
                    needDeleteNotebookId[id] = True
                    # delete(userNotebooksMap, id)
        # 第三遍, 得到所有根
        final = []
        i = 0
        for (nbid, each ) in userNotebooksMap:
            if not needDeleteNotebookId[id]:
                final[i] = each
                i=i+1
        # 最后排序
        if needSort:
            return self.sortSubNotebooks(final)
        return final
  


    def getNotebook(self, notebookId):
        return self.query.filter(and_(Notebook.userId == userId,Notebook.id == notebookId)).one()

    def geSyncNotebooks(self,userId , afterUsn, maxEntry ):
        return self.query.filter(_and(Notebook.userId==userId,Notebook.Usn>afterUsn)).order_by(Notebook.Usn).limit(maxEntry).all()
         
    # 得到用户下所有的notebook
    # 排序好之后返回
    # [ok]
    def getNotebooks(self,userId):
      
        query=self.query.filter(db.or_(Notebook.isDeleted==False,Notebook.isDeleted==None)).filter(Notebook.userId==userId)
        userNotebooks=query.all()
        if len(userNotebooks) == 0:
            return None

        return ParseAndSortNotebooks(userNotebooks, true, true)


        # 添加
    def addNotebook(self,notebook):

        notebook.UrlTitle = self.getUrTitle(notebook.userId, notebook.title, "notebook", notebook.NotebookId)
        notebook.Usn = userService.IncrUsn(notebook.userId)
        now = time.Now()
        notebook.CreatedTime = now
        notebook.UpdatedTime = now
        Notebooks.Insert(notebook)
        return true, notebook

    # 更新笔记, api
    