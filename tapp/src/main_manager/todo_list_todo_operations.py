from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from src.database.models import db, TodoList, Todo
from src.validators_tools.todo_list_todo_validators import (
    deadline_validator
)
from src.validators_tools.common_validators import (
    length_validator
)


def create_operation(user, data, todo_list=None):
    title = data.get("title", None)
    body = None
    deadline = data.get("deadline", None)
    response = {
        "messages": [],
        "code": 200,
        "success": True
    }

    if not length_validator(title):
        response["messages"].append("Invalid title! Try again!")
        response["code"] = 400
        response["success"] = False

    if "body" in data.keys():
        body = data.get("body", None)
        if not len(body) >= 6:
            response["messages"].append("Invalid body! Try again!")
            response["code"] = 400
            response["success"] = False

    if not deadline_validator(deadline)["success"]:
        response["messages"].append(deadline_validator(deadline)["message"])
        response["code"] = 400
        response["success"] = False

    if response["code"] == 200:
        try:
            if data["type"] == "todo":
                new_todo = Todo(title, body, deadline)
                new_todo.todo_list = todo_list
                new_todo.owner = user
                new_todo.insert()
                todo_list.completed = new_todo.completed
                todo_list.update()
                response["messages"].append(
                    "New todo is successfully created")
                response["todo_data"] = new_todo.format()
            else:
                new_todo_list = TodoList(title, deadline)
                new_todo_list.owner = user
                new_todo_list.insert()
                response["messages"].append(
                    "New todo list is successfully created!")
                response["todo_list_data"] = new_todo_list.short()

        except SQLAlchemyError:

            response["messages"].append("Something went wrong!")
            response["code"] = 422
            response["success"] = False

        finally:
            db.session.close()

    return response


def update_operation(user, todo_list, data):
    response = {
        "messages": [],
        "code": 200,
        "success": True
    }
    similar = True
    if not todo_list in user.todo_lists:
        response["messages"].append("resource not found")
        response["code"] = 404
        response["success"] = False
        return response
    

    new_title = data.get("title", None)
    new_deadline = data.get("deadline", None)
    new_completed = data.get("completed", None)
    

    if new_title != todo_list.title:
        similar = False
        if length_validator(new_title):
            todo_list.title = new_title
        else:
            response["messages"].append("Invalid title!")
            response["code"] = 400
            response["success"] = False
    

    if new_deadline != todo_list.deadline:
        if  similar:
            similar = False

        if not deadline_validator(new_deadline)["success"]:
            if response["code"] == 200:
                response["code"] = 400
                response["success"] = False
            response["messages"].append("Invalid deadline format or deadline!")

        elif response["code"] == 200:
            todo_list.deadline = new_deadline


    if new_completed != todo_list.completed:
        if similar:
            similar = False

        if not isinstance(new_completed, bool):
            if response["code"] == 200:
                response["code"] = 400
                response["success"] = False
            response["messages"].append("Invalid completed type!")

        elif response["code"] == 200:
            todo_list.completed = new_completed
    

    if response["success"] and not similar:
        try:
            todo_list.update()
            response["messages"].append("Successfully updated!")
            response["todo_list_data"] = todo_list.short()

        except SQLAlchemyError:
            response["messages"].append("Something went wrong")
            response["code"] = 422
            response["success"] = False
            db.session.rollback()
        
        finally:
            db.session.close()
    elif response["success"] and similar:
        response["messages"].append("Nothing to update")
        response["todo_list_data"] = todo_list.short()

    return response     


def delete_operation(user, todo_list, list_public_id, todo=None, todo_public_id=None):
    response = {
        "messages": [],
        "code": 200,
        "success": True
    }
    item_type = ""
    if todo:
        if (todo_list in user.todo_lists) \
                and (todo in todo_list.todos) \
                and (todo in user.todos):
            item_type = "todo"
        else:
            response["messages"].append(
                f"Todo with id {todo_public_id} not found!"
            )
            response["error_message"] = "resource not found"
            response["code"] = 404
            response["success"] = False
            return response
    else:
        if todo_list in user.todo_lists:
            item_type = "todo-list"
        else:
            response["messages"].append(
                f"Todo List with id {list_public_id} not found!"
            )
            response["error_message"] = "resource not found"
            response["code"] = 404
            response["success"] = False
            return response
    
    
    try:
        if item_type == "todo":
            todo.delete()
            response["messages"].append(
                f"Todo with id {todo.public_id} successfully deleted!")
        else:
            todo_list.delete()
            response["messages"].append(
                f"Todo List with id {todo_list.public_id} successfully deleted!")
    except SQLAlchemyError:
        response["messages"].append("Something went wrong!")
        response["error_message"] = "unprocessable entity"
        response["code"] = 422
        response["success"] = False
        db.session.rollback()
    finally:
        db.session.close()
    
    
    return response
