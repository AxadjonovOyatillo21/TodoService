import URLS from "../common_functions/urls.js";
import Containers from "../common_functions/containers.js";
import selector_pattern from "../common_functions/selector_pattern_builder.js";


let open_updator_btns = document.querySelectorAll(".todo-list-open-updator-btns");

if (open_updator_btns) {
    for (let open_updator_btn of open_updator_btns) {
        open_updator_btn.onclick = todo_list_open_updator_function;
    }
}

export default function todo_list_open_updator_function(e) {
    let containers = new Containers();
    let parent_public_id = e.target.dataset["id"];
    let filter_id = parent_public_id.replaceAll("todo-list-", "")
    let parent_element = document.getElementById(parent_public_id);
    let list_title = document.getElementById(selector_pattern("todo-list", "title", filter_id)).textContent.trim();
    let list_deadline = document.getElementById(selector_pattern("todo-list", "deadline", filter_id)).textContent.trim();
    let list_completed = document.getElementById(selector_pattern("todo-list", "completed", filter_id)).checked;
    let jsonified = {
        "public_id": parent_public_id,
        "title": list_title,
        "deadline": list_deadline,
        "completed": list_completed
    };
    let create_update_todo_list_container = containers.create_full_update_todo_list_container(jsonified, update_todo_list_function);
    parent_element.innerHTML = "";
    parent_element.appendChild(create_update_todo_list_container);
}

function update_todo_list_function(e) {
    let parent_element_public_id = e.target.dataset["id"];
    let filter_id = parent_element_public_id;
    let parent_element = document.getElementById(parent_element_public_id);
    if (parent_element_public_id.includes("todo-list-")) {
        filter_id = parent_element_public_id.replaceAll("todo-list-", "");
    }
    let list_update_title = document.getElementById(`update-todo-list-title-${filter_id}`).value;
    let list_update_deadline = document.getElementById(`update-todo-list-deadline-${filter_id}`).value;
    let list_update_completed = document.getElementById(`update-todo-list-completed-${filter_id}`).checked;
    let message = {
        "messages": [],
        "success": false,
        "code": 400
    };
    if (!list_update_title.trim()) {
        message.messages.push("Empty title!");
    }
    if (!list_update_deadline.trim()) {
        message.messages.push("Empty deadline!");
    }
    if (list_update_title.trim() && list_update_deadline.trim()) {
        let BuildURLS = new URLS();
        let url = BuildURLS.build_update_todo_list_URL(filter_id);
        fetch(url, {
            method: "PATCH",
            body: JSON.stringify({
                "title": list_update_title,
                "deadline": list_update_deadline,
                "completed": list_update_completed
            }),
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(response => response.json())
            .then(jsonResponse => {
                if (jsonResponse.success) {
                    console.log(parent_element)
                    parent_element.innerHTML = "";
                    let containers = new Containers();
                    let create_container = containers.create_full_todo_list_container(jsonResponse, parent_element);
                }
                create_message_box(jsonResponse);
            })
    } else {
        create_message_box(message);
    }
} 