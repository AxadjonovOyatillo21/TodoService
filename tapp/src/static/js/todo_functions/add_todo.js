import URLS from '../common_functions/urls.js';
import Containers from '../common_functions/containers.js';
let active_list = document.querySelector(".active-list");
let active_list_public_id;
if (active_list) {
    active_list_public_id = active_list.id;
}
let add_todo_form = document.getElementById("add_todo_form");
add_todo_form.onsubmit = add_todo_function;
export default function add_todo_function(e) {
    e.preventDefault();
    let message = {
        "messages": [],
        "success": false,
        "code": 400
    };
    let todo_title = document.getElementById("add_todo_title").value;
    // if (!todo_title.trim()) {
    //     message.messages.push("Empty title!");
    // }
    let todo_body = document.getElementById("add_todo_body").value;
    // if (!todo_body.trim()) {
    //     message.messages.push("Empty body!");
    // }
    let deadline = document.getElementById("add_todo_deadline").value;
    // if (!deadline.trim()) {
    //     message.messages.push("Empty deadline!");
    // }
    let list_filter_id = null;
    if (active_list_public_id.includes("todo-list-")) {
        list_filter_id = active_list_public_id.replaceAll("todo-list-", "");
    }
    // if (todo_title.trim() && todo_body.trim() && deadline.trim()) {
        let BuildURLS = new URLS();
        let url = BuildURLS.build_add_todo_URL(list_filter_id || active_list_public_id);
        fetch(url, {
            method: "POST",
            body: JSON.stringify({
                "title": todo_title,
                "body": todo_body,
                "deadline": deadline,
            }),
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(response => response.json())
            .then(jsonResponse => {
                if (jsonResponse.success) {
                    let containers = new Containers();
                    let todos_wrapper = document.getElementById("todos");
                    let create_container = containers.create_full_todo_container(jsonResponse);
                    todos_wrapper.appendChild(create_container);
                    let todo_lists_count = document.getElementById("counter");
                    let value = todo_lists_count.innerHTML;
                    value = +value + 1;
                    todo_lists_count.innerHTML = value;
                    todo_lists_count.style.color = "green";
                }
                create_message_box(jsonResponse);
            })
    // } else {
    //     create_message_box(message);
    // }
}
