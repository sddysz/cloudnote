
from extensions import db


class Note(db.Model):
    __tablename__ = "notes"
    noteId = db.Column(db.Integer, primary_key=True)           # 必须要设置bson:"_id" 不然mgo不会认为是主键
    userId = db.Column(db.Integer)                              # 谁的
    createdUserId = db.Column(db.Integer)                         # 谁创建的(UserId != CreatedUserId, 是因为共享). 只是共享才有, 默认为空, 不存 必须要加omitempty
    notebookId = db.Column(db.Integer)         
    title = db.Column(db.String) # 标题
    desc = db.Column(db.String)  # 描述, 非html

    src  = db.Column(db.String) # 来源, 2016/4/22
    imgSrc = db.Column(db.String) # 图片, 第一张缩略图地址
	# tags = db.Column(db.String[])
	# 现在没有合适的方法，以后再添加
	
    isTrash = db.Column(db.Boolean)	#是否是trash, 默认是false
    isBlog = db.Column(db.Boolean)	# 是否设置成了blog 2013/12/29 新加
    urlTitle = db.Column(db.String)     # 博客的url标题, 为了更友好的url, 在UserId, UrlName下唯一
    isRecommend = db.Column(db.Boolean) # 是否为推荐博客 2014/9/24新加
    isTop  = db.Column(db.Boolean)     # blog是否置顶
    hasSelfDefined  = db.Column(db.Boolean)       # 是否已经自定义博客图片, desc, abstract

	# 2014/9/28 添加评论社交功能
    readNum = db.Column(db.Integer)    # 阅读次数 2014/9/28
    likeNum = db.Column(db.Integer)    # 点赞次数 2014/9/28
    commentNum  = db.Column(db.Integer) # 评论次数 2014/9/28

    isMarkdown  = db.Column(db.Boolean) # 是否是markdown笔记, 默认是false

    attachNum = db.Column(db.Integer)  # 2014/9/21, attachments num

    createdTime = db.Column(db.DateTime) 
    updatedTime = db.Column(db.DateTime) 
    recommendTime = db.Column(db.DateTime)  # 推荐时间
    publicTime  = db.Column(db.DateTime)     # 发表时间, 公开为博客则设置
    updatedUserId = db.Column(db.Integer)  # 如果共享了, 并可写, 那么可能是其它他修改了

	# 2015/1/15, 更新序号
    usn = db.Column(db.Integer)  # UpdateSequenceNum

    isDeleted  = db.Column(db.Boolean)  # 删除位



    def getNotes(self, userId):
            return self.query.filter(Notebook.userId == userId).all()

    def getNoteByNoteId(self, noteId):
            return self.query.filter(Notebook.noteId == noteId).first()






class NoteContent(db.Model):
    __tablename__ = "notecontent"
    noteId = db.Column(db.Integer, primary_key=True) 
    userId = db.Column(db.Integer)
    isBlog  = db.Column(db.Boolean) # 为了搜索博客
    content = db.Column(db.String)
    abstract = db.Column(db.String)  #摘要, 有html标签, 比content短, 在博客展示需要, 不放在notes表中
    createdTime  = db.Column(db.DateTime)
    updatedTime = db.Column(db.DateTime)
    updatedUserId = db.Column(db.Integer) # 如果共享了, 并可写, 那么可能是其它他修改了

    def getNoteByNoteId(self, noteId, noteOwner):
        return self.query.filter( db.and_(NoteContent.noteId == noteId,NoteContent.userId == noteOwner)).first()