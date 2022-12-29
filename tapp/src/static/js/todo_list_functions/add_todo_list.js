import URLS from '../common_functions/urls.js';
import Containers from '../common_functions/containers.js';
let add_todo_list_form = document.getElementById("add_todo_list");

add_todo_list_form.onsubmit = add_todo_list_function;

export default function add_todo_list_function(e) {
    e.preventDefault();
    let message = {
        "messages": [],
        "success": false,
        "code": 400
    };
    let list_title = document.getElementById("add_todo_list_title").value;
    if (!list_title.trim()) {
        message.messages.push("Empty title!");
    }
    let deadline = document.getElementById("add_todo_list_deadline").value;
    if (!deadline.trim()) {
        message.messages.push("Empty deadline!");
    }
    if (list_title.trim() && deadline.trim()) {
        let BuildURLS = new URLS();
        let url = BuildURLS.build_add_todo_list_URL();
        fetch(url, {
            method: "POST",
            body: JSON.stringify({
                "title": list_title,
                "deadline": deadline
            }),
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(response => response.json())
            .then(jsonResponse => {
                if (jsonResponse.success) {
                    let containers = new Containers();
                    let todo_lists_wrapper = document.getElementById("todo_lists");
                    let create_container = containers.create_full_todo_list_container(
                        jsonResponse
                    );
                    todo_lists_wrapper.appendChild(create_container);
                    let todo_lists_count = document.getElementById("counter");
                    let value = todo_lists_count.innerHTML;
                    value = +value + 1;
                    todo_lists_count.innerHTML = value;
                    todo_lists_count.style.color = "green";
                }
                // publishing a message from the server
                create_message_box(jsonResponse);
            })
    } else {
        create_message_box(message);
    }
}