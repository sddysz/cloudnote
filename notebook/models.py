
from extensions import db
from flask_login.mixins import CRUDMixin


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





