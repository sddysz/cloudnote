
from extensions import db
from flask_login.mixins import CRUDMixin


class Note(db.Model, CRUDMixin):
    __tablename__ = "notes"
    noteId = db.Column(db.Integer, primary_key=True)           # 必须要设置bson:"_id" 不然mgo不会认为是主键
    userId = db.Column(db.Integer)                              # 谁的
    createdUserId = db.Column(db.Integer)                         # 谁创建的(UserId != CreatedUserId, 是因为共享). 只是共享才有, 默认为空, 不存 必须要加omitempty
    notebookId = db.Column(db.Integer)         
    title = db.Column(db.String) # 标题
    desc = db.Column(db.String)  # 描述, 非html

    src  = db.Column(db.String) # 来源, 2016/4/22
    imgSrc = db.Column(db.String) # 图片, 第一张缩略图地址
    tags = db.Column(db.String[])

	IsTrash bool `IsTrash` # 是否是trash, 默认是false

	IsBlog         bool   `IsBlog,omitempty`      # 是否设置成了blog 2013/12/29 新加
	UrlTitle       string `UrlTitle,omitempty`    # 博客的url标题, 为了更友好的url, 在UserId, UrlName下唯一
	IsRecommend    bool   `IsRecommend,omitempty` # 是否为推荐博客 2014/9/24新加
	IsTop          bool   `IsTop,omitempty`       # blog是否置顶
	HasSelfDefined bool   `HasSelfDefined`        # 是否已经自定义博客图片, desc, abstract

	# 2014/9/28 添加评论社交功能
	ReadNum    int `ReadNum,omitempty`    # 阅读次数 2014/9/28
	LikeNum    int `LikeNum,omitempty`    # 点赞次数 2014/9/28
	CommentNum int `CommentNum,omitempty` # 评论次数 2014/9/28

	IsMarkdown bool `IsMarkdown` # 是否是markdown笔记, 默认是false

	AttachNum int `AttachNum` # 2014/9/21, attachments num

	CreatedTime   time.Time     `CreatedTime`
	UpdatedTime   time.Time     `UpdatedTime`
	RecommendTime time.Time     `RecommendTime,omitempty` # 推荐时间
	PublicTime    time.Time     `PublicTime,omitempty`    # 发表时间, 公开为博客则设置
	UpdatedUserId bson.ObjectId `bson:"UpdatedUserId"`    # 如果共享了, 并可写, 那么可能是其它他修改了

	# 2015/1/15, 更新序号
	Usn int `Usn` # UpdateSequenceNum

	IsDeleted bool `IsDeleted` # 删除位





