from crypt import methods
from urllib import response
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    abort,
    jsonify
)
from flask_login import login_required, current_user
from database.models import TodoList, Todo, User, db
from utils import (
    Pagination,
    deadline_validator,
    length_validator,
    data_rules
)
from sqlalchemy.exc import SQLAlchemyError
import math


main_manager = Blueprint(
    "main_manager",
    __name__,
    template_folder="templates"
)


@main_manager.route("/todo-lists/<string:list_public_id>")
@login_required
def todo_list_detail(list_public_id):
    user = User.query.get(current_user.get_id())
    todo_list = TodoList.query.filter_by(
        public_id=list_public_id).first() or abort(404)
    if todo_list in user.todo_lists:
        pagination = Pagination()
        todos = Todo.query.filter_by(owner=user).filter_by(
            todo_list=todo_list).order_by(Todo.id).all()
        todos = pagination.paginate_item(request, todos)
        return render_template(
            "main_manager/todo_list_detail.html",
            todo_list=todo_list.short(),
            user=user.short(),
            todos=todos,
            total_todos=len(todos),
            pages=math.ceil(len(todo_list.todos) / 5),
            data_rules=data_rules
        )
    else:
        abort(404)


@main_manager.route("/todo-lists/create", methods=["POST"])
@login_required
def create_todo_list():
    user = User.query.get(current_user.get_id())
    data = request.get_json()
    title = data.get("title", None)
    deadline = data.get("deadline", None)
    response = {
        "messages": [],
        "code": 200,
        "success": True
    }
    if not length_validator(title):
        response["messages"].append("Bad title! Try again!")
        response["code"] = 400
        response["success"] = False
    if not deadline_validator(deadline)["success"]:
        response["messages"].append(deadline_validator(deadline)["message"])
        response["code"] = 400
        response["success"] = False
    if length_validator(title) and deadline_validator(deadline)["success"]:
        try:
            new_todo_list = TodoList(title, deadline)
            new_todo_list.owner = user
            new_todo_list.insert()
            response["messages"].append(
                f"Todo List with id {new_todo_list.public_id} successfully created!")
            response["todo_list_data"] = new_todo_list.short()
        except:
            response["messages"].append("Something went wrong!")
            response["code"] = 422
            response["success"] = False
        finally:
            db.session.close()
    return jsonify(response), response["code"]


@main_manager.route("/todo-lists/<string:list_public_id>/update", methods=["PATCH"])
@login_required
def update_todo_list(list_public_id):
    user = User.query.get(current_user.get_id())
    todo_list = TodoList.query.filter_by(
        public_id=list_public_id).first() or abort(404)
    if todo_list in user.todo_lists:
        data = request.get_json()
        new_title = data.get("title", None)
        new_deadline = data.get("deadline", None)
        completed = data.get("completed", None)
        response = {
            "messages": [],
            "code": 200,
            "success": True
        }

        if new_title != todo_list.title:
            if length_validator(new_title):
                todo_list.title = new_title
            else:
                response["messages"].append(
                    "Bad title! So I didn't update title!")
                response["success"] = False
                response["code"] = 400

        if new_deadline != todo_list.deadline:
            if deadline_validator(new_deadline)["success"]:
                todo_list.deadline = new_deadline
            else:
                response["messages"].append(
                    deadline_validator(new_deadline)["message"])
                response["success"] = False
                response["code"] = 400

        if not (completed is None):
            todo_list.completed = completed
            for todo in todo_list.todos:
                todo.completed = completed
        if response["code"] == 200:
            try:
                todo_list.update()
                response["messages"].append(
                    f"Todo List with public_id {todo_list.public_id} successfully updated!")
                response["todo_list_data"] = todo_list.short()
            except SQLAlchemyError:
                response["messages"].append("Something went wrong!")
                response["code"] = 422
                response["success"] = False
            finally:
                db.session.close()
        return jsonify(response), response["code"]

    else:
        abort(404)


@main_manager.route("/todo-lists/<string:list_public_id>/delete", methods=["DELETE"])
@login_required
def delete_todo_list(list_public_id):
    user = User.query.get(current_user.get_id())
    todo_list = TodoList.query.filter_by(
        public_id=list_public_id).first() or abort(404)
    if todo_list in user.todo_lists:
        response = {
            "messages": [],
            "code": 200,
            "success": True
        }
        try:
            todo_list.delete()
            response["messages"].append(
                f"Todo List with id {todo_list.public_id} successfully deleted!")
        except SQLAlchemyError:
            response["messages"].append("Something went wrong!")
            response["code"] = 422
            response["success"] = False
        finally:
            db.session.close()
        return jsonify(response), response["code"]
    else:
        abort(404)


@main_manager.route("/todo-lists/<string:list_public_id>/todos/create", methods=["POST"])
@login_required
def add_todo_item(list_public_id):
    user = User.query.get(current_user.get_id())
    todo_list = TodoList.query.filter_by(
        public_id=list_public_id).first() or abort(404)
    data = request.get_json()
    title = data.get("title", None)
    body = data.get("body", None)
    deadline = data.get("deadline", None)
    response = {
        "messages": [],
        "code": 200,
        "success": True
    }
    if not length_validator(title):
        response["messages"].append("Bad title! Try again!")
        response["code"] = 400
        response["success"] = False

    if not len(body) >= 6:
        response["messages"].append("Bad body! Try again!")
        response["code"] = 400
        response["success"] = False

    if not deadline_validator(deadline)["success"]:
        response["messages"].append(deadline_validator(deadline)["message"])
        response["code"] = 400
        response["success"] = False

    if length_validator(title) and (len(body) >= 6) and deadline_validator(deadline)["success"]:
        try:
            new_todo = Todo(title, body, deadline)
            new_todo.todo_list = todo_list
            new_todo.owner = user
            new_todo.insert()
            todo_list.completed = new_todo.completed
            todo_list.update()
            response["messages"].append(
                f"Todo with id {new_todo.public_id} successfully created!")
            response["todo_data"] = new_todo.format()
        except:
            response["messages"].append("Something went wrong!")
            response["code"] = 422
            response["success"] = False
        finally:
            db.session.close()

    return jsonify(response), response["code"]


@main_manager.route("/todo-lists/<string:list_public_id>/todos/<string:todo_public_id>/update", methods=["PATCH"])
@login_required
def update_todo_item(list_public_id, todo_public_id):
    user = User.query.get(current_user.get_id())
    todo_list = TodoList.query.filter_by(
        public_id=list_public_id).first() or abort(404)
    todo = Todo.query.filter_by(public_id=todo_public_id).first() or abort(404)
    if (todo_list in user.todo_lists) and (todo in todo_list.todos) and (todo in user.todos):
        response = {
            "messages": [],
            "code": 200,
            "success": True
        }
        data = request.get_json()
        new_title = data.get("title", None)
        new_body = data.get("body", None)
        new_deadline = data.get("deadline", None)
        completed = data.get("completed", None)
        print(new_title, new_body, new_deadline, completed)
        if new_title != todo.title:
            if length_validator(new_title):
                todo.title = new_title
            else:
                response["messages"].append(
                    "Bad title! So I didn't update title!")
                response["code"] = 400
                response["success"] = False

        if new_body != todo.body:
            if length_validator(new_body):
                todo.body = new_body
            else:
                response["messages"].append(
                    "Bad body! So, I didn't update body!")
                response["code"] = 400
                response["success"] = False

        if new_deadline != todo.deadline:
            if deadline_validator(new_deadline)["success"]:
                todo.deadline = new_deadline
            else:
                response["messages"].append(
                    deadline_validator(new_deadline)["message"])
                response["success"] = False
                response["code"] = 400

        if not (completed is None):
            todo.completed = completed

        if response["code"] == 200:
            try:
                todo.update()
                response["messages"].append(
                    f"Todo with public_id {todo.public_id} successfully updated!")
                response["todo_data"] = todo.format()
            except SQLAlchemyError:
                response["messages"].append("Something went wrong!")
                response["code"] = 422
                response["success"] = False
            finally:
                db.session.close()
        return jsonify(response), response["code"]

    else:
        abort(404)


@main_manager.route("/todo-lists/<string:list_public_id>/todos/<string:todo_public_id>/delete", methods=["DELETE"])
@login_required
def delete_todo_item(list_public_id, todo_public_id):
    user = User.query.get(current_user.get_id())
    todo_list = TodoList.query.filter_by(
        public_id=list_public_id).first() or abort(404)
    todo = Todo.query.filter_by(public_id=todo_public_id).first() or abort(404)
    if (todo_list in user.todo_lists) and (todo in todo_list.todos) and (todo in user.todos):
        response = {
            "messages": [],
            "code": 200,
            "success": True
        }
        try:
            todo.delete()
            response["messages"].append(
                f"Todo with id {todo.public_id} successfully deleted!")
        except SQLAlchemyError:
            response["messages"].append("Something went wrong!")
            response["code"] = 422
            response["success"] = False
        finally:
            db.session.close()
        return jsonify(response), response["code"]
    else:
        abort(404)


@main_manager.route("/rules")
@login_required
def get_rules():
    return jsonify({
        "rules": data_rules
    })
