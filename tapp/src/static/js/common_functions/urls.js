export default class URLS {
    build_todo_list_URL(todo_list_id) {
        return `/todo-lists/${todo_list_id}`;
    }
    build_todos_URL(todo_list_id) {
        return `${this.build_todo_list_URL(todo_list_id)}/todos`;
    }
    build_todo_URL(todo_list_id, todo_id) {
        return `${this.build_todos_URL(todo_list_id)}/${todo_id}`;
    }
    build_add_todo_list_URL() {
        return `/todo-lists/create`;
    }
    build_add_todo_URL(todo_list_id) {
        return `${this.build_todos_URL(todo_list_id)}/create`;
    }
    build_delete_todo_list_URL(todo_list_id) {
        return `${this.build_todo_list_URL(todo_list_id)}/delete`;
    }
    build_delete_todo_URL(todo_list_id, todo_id) {
        return `${this.build_todo_URL(todo_list_id, todo_id)}/delete`;
    }
    build_update_todo_list_URL(todo_list_id) {
        return `${this.build_todo_list_URL(todo_list_id)}/update`;
    }
    build_update_todo_URL(todo_list_id, todo_id) {
        return `${this.build_todo_URL(todo_list_id, todo_id)}/update`;
    }
}