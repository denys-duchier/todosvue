from .app import db
from flask import url_for, jsonify


class TodoList(db.Model):

    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return f"<TodoList ({self.id}) {self.name}>"

    def to_json(self):
        json = {
            "url": url_for("todolist"
                id=self.id, _external=True),
            "name": self.name,
            "items": [i.to_json() for i in self.items.all()]
        }
        return json

    def to_json_brief(self):
        json = {
            "url": url_for("todolist"
                id=self.id, _external=True),
            "name": self.name
        }

    @staticmethod
    def add(json):
        l = TodoList(name=json["name"])
        db.session.add(l)
        db.session.commit()
        return l

    @staticmethod
    def delete(id):
        l = db_get_list(id)
        db.session.delete(l)
        db.session.commit()


class TodoItem(db.Model):

    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    list_id = db.Column(db.Integer, db.ForeignKey('todolist.id'))
    list = db.relationship("TodoList",
        backref=db.backref("items", 
        lazy="dynamic"))

    def __repr__(self):
        return f"<TodoItem ({self.id}) {self.name}>"

    def to_json(self):
        json = {
            "url": url_for("todoitem",
                id=self.id, _external=True),
            "id": self.id,
            "name": self.name
        }
        return json

    @staticmethod
    def add(json):
        l = db_get_list(json["list_id"])
        i = TodoItem(
            name = json["name"],
            list_id = json["list_id"]
        )
        db.session.add(i)
        db.session.commit()
        return i
        
    @staticmethod
    def delete(id):
        i = db_get_item(id)
        db.session.delete(i)
        db.session.commit()


def db_all_lists():
    return TodoLists.query.all()

def db_get_list(id):
    return TodoList.query.get_or_404(id)

def db_add_list(json):
    return TodoList.add(json)

def db_del_list(id):
    TodoList.delete(id)

def db_modify_list(id, json):
    l = db_get_list(id)
    if "name" in json:
        l.name = json["name"]
    db.session.commit()
    return l


def db_all_items():
    return TodoItem.query.all()

def db_get_item(id):
    return TodoItem.query.get_or_404(id)

def db_add_item(json):
    return TodoItem.add(json)

def db_del_item(id):
    TodoItem.delete(id)

def db_modify_item(id, json):
    i = db_get_item(id)
    if "name" in json:
        i.name = json["name"]
    db.session.commit()