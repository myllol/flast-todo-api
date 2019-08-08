from .. import db

class Todo(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    todo = db.Column(db.String(255), nullable=False)
    regdate = db.Column(db.DateTime, nullable=False, default=db.func.now())
    complete = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return "<User '{}'>".format(self.username)