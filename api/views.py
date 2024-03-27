from .app import app
from flask import request, jsonify
from .models import (
    db_all_lists, db_get_list, db_add_list, db_del_list, db_modify_list,
    db_all_items, db_get_item, db_add_item, db_del_item, db_modify_item
)

@app.route("/api/v1.0/list", methods=["GET"])
def get_all_lists():
    lists = db_all_lists()
    return [l.to_json_brief() for l in db_all_lists()]

@app.route("/api/v1.0/list/<id:int>", methods=["GET"])
def get_list(id):
    return db_get_list(id).to_json_brief()

@app.route("/api/v1.0/list", methods=["POST"])
def add_list():
    return db_add_list(json).to_json()

@app.route("/api/v1.0/list/<id:int>", methods=["DELETE"])
def del_list(id):
    db_del_list(id)

@app.route("/api/v1.0/list/<id:int>", methods=["PUT"])
def modify_list(id):
    db_modify_list(id, request.json)


@app.route("/api/v1.0/item/<id:int>", methods=["GET"])
def get_item(id):
    return db_get_item(id).to_json()

@app.route("/api/v1.0/item", methods=["POST"])
def add_item():
    return db_add_item(json).to_json()

@app.route("/api/v1.0/item/<id:int>", methods=["DELETE"])
def del_item(id):
    db_del_item(id)

@app.route("/api/v1.0/list/<id:int>", methods=["PUT"])
def modify_item(id):
    db_modify_item(id, request.json)
