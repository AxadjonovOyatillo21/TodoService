from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from uuid import uuid4
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from datetime import datetime


db = SQLAlchemy()


def setup_db(app, db=db):
    db.app = app
    db.init_app(app)
    db.create_all()
    return db


now = datetime.now().strftime("%d/%m/%Y")


class DBcommands:
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(db.Model, UserMixin, DBcommands):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    public_id = db.Column(db.String(), nullable=False, unique=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    todo_lists = db.relationship(
        'TodoList', backref="owner", lazy=True, cascade="all, delete-orphan")
    todos = db.relationship('Todo', backref="owner",
                            lazy=True, cascade="all, delete-orphan")

    def __init__(self, username, email, password, public_id=uuid4):
        self.username = username
        self.email = email
        self.password_hash = self.generate_ph(password)
        self.public_id = str(public_id())

    def short(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "todo_lists": [todo_list.short() for todo_list in self.todo_lists],
            "total_todo_lists": len(self.todo_lists),
            "total_todos": len(self.todos)
        }

    def format(self):
        return {
            "id": self.id,
            "public_id": self.public_id,
            "username": self.username,
            "email": self.email,
            "todo_lists": [todo_list.short() for todo_list in self.todo_lists],
            "todos": [todo.short() for todo in self.todos],
            "total_todo_lists": len(self.todo_lists),
            "total_todos": len(self.todos),
        }

    def generate_ph(self, password):
        return generate_password_hash(password)

    def check_ph(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "User: {}".format(self.username)


class TodoList(db.Model, DBcommands):
    __tablename__ = "todo_lists"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    public_id = db.Column(db.String(), nullable=False, unique=True)
    title = db.Column(db.String, nullable=False)
    deadline = db.Column(db.String, nullable=False, default=now)
    completed = db.Column(db.Boolean, default=False)
    todos = db.relationship('Todo', backref='todo_list',
                            lazy=True, cascade='all, delete-orphan')
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __init__(self, title, deadline, completed=False, public_id=uuid4):
        self.title = title
        self.deadline = deadline
        self.completed = completed
        self.public_id = str(public_id())

    def short(self):
        return {
            "id": self.id,
            "public_id": self.public_id,
            "title": self.title,
            "deadline": self.deadline,
            "completed": self.completed,
            "owner_id": self.owner_id
        }

    def format(self):
        return {
            "id": self.id,
            "public_id": self.public_id,
            "title": self.title,
            "deadline": self.deadline,
            "completed": self.completed,
            "todos": [todo.format() for todo in self.todos],
            "owner_id": self.owner_id
        }

    def __repr__(self):
        return "TodoList: {}".format(self.title)


class Todo(db.Model, DBcommands):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    public_id = db.Column(db.String(), nullable=False, unique=True)
    title = db.Column(db.String(50))
    body = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.String, nullable=False, default=now)
    completed = db.Column(db.Boolean, default=False)
    todo_list_id = db.Column(db.Integer, db.ForeignKey(
        "todo_lists.id"), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __init__(self, title, body, deadline, completed=False, public_id=uuid4):
        self.title = title
        self.body = body
        self.deadline = deadline
        self.completed = completed
        self.public_id = str(public_id())

    def short(self):
        return {
            "id": self.id,
            "public_id": self.public_id,
            "title": self.title,
            "deadline": self.deadline,
            "completed": self.completed,
            "owner_id": self.owner_id
        }

    def format(self):
        return {
            "id": self.id,
            "public_id": self.public_id,
            "title": self.title,
            "deadline": self.deadline,
            "body": self.body,
            "completed": self.completed,
            "owner_id": self.owner_id,
            "todo_list_id": self.todo_list_id
        }

    def __repr__(self):
        return "Todo: {}".format(self.id)
