import URLS from '../common_functions/urls.js';
import Containers from '../common_functions/containers.js';
import selector_pattern from '../common_functions/selector_pattern_builder.js';

let open_updator_btns = document.querySelectorAll(".todo-item-open-updator-btns");
let active_list = document.querySelector(".active-list");
let active_list_public_id;

if (active_list) {
    active_list_public_id = active_list.id;
}

if (open_updator_btns) {
    for (let open_updator_btn of open_updator_btns) {
        open_updator_btn.onclick = todo_item_open_updator_function;
    }
}

export default function todo_item_open_updator_function(e) {
    let containers = new Containers();
    let parent_public_id = e.target.dataset["id"];
    let filter_id = parent_public_id.replaceAll("todo-item-", "");
    let parent_element = document.getElementById(parent_public_id);
    let todo_title = document.getElementById(selector_pattern("todo-item", "title", filter_id)).textContent.trim();
    let todo_body = document.getElementById(selector_pattern("todo-item", "body", filter_id)).textContent.trim();
    let todo_deadline = document.getElementById(selector_pattern("todo-item", "deadline", filter_id)).textContent.trim();
    let todo_completed = document.getElementById(selector_pattern("todo-item", "completed", filter_id)).checked;
    let jsonified = {
        "public_id": parent_public_id,
        "title": todo_title,
        "body": todo_body,
        "deadline": todo_deadline,
        "completed": todo_completed
    };
    let create_update_todo_container = containers.create_full_update_todo_container(jsonified, update_todo_function);
    parent_element.innerHTML = "";
    parent_element.appendChild(create_update_todo_container);
}

function update_todo_function(e) {
    let parent_element_public_id = e.target.dataset["id"];
    let list_filter_id = active_list_public_id.replaceAll("todo-list-", "");
    let filter_id = parent_element_public_id;
    let parent_element = document.getElementById(parent_element_public_id);
    if (parent_element_public_id.includes("todo-item-")) {
        filter_id = parent_element_public_id.replaceAll("todo-item-", "");
    }
    let todo_item_update_title = document.getElementById(`update-todo-item-title-${filter_id}`).value;
    let todo_item_update_body = document.getElementById(`update-todo-item-body-${filter_id}`).value;
    let todo_item_update_deadline = document.getElementById(`update-todo-item-deadline-${filter_id}`).value;
    let todo_item_update_completed = document.getElementById(`update-todo-item-completed-${filter_id}`).checked;
    let message = {
        "messages": [],
        "success": false,
        "code": 400
    };
    if (!todo_item_update_title.trim()) {
        message.messages.push("Empty title!");
    }
    if (!todo_item_update_body.trim()) {
        message.messages.push("Empty deadline!");
    }
    if (todo_item_update_title.trim() && todo_item_update_body.trim()) {
        let BuildURLS = new URLS();
        let url = BuildURLS.build_update_todo_URL(list_filter_id, filter_id);
        fetch(url, {
            method: "PATCH",
            body: JSON.stringify({
                "title": todo_item_update_title,
                "body": todo_item_update_body,
                "deadline": todo_item_update_deadline,
                "completed": todo_item_update_completed
            }),
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(response => response.json())
            .then(jsonResponse => {
                console.log(jsonResponse)
                if (jsonResponse.success) {
                    console.log(parent_element)
                    parent_element.innerHTML = "";
                    let containers = new Containers();
                    let create_container = containers.create_full_todo_container(jsonResponse, parent_element);
                }
                create_message_box(jsonResponse);
            })
    }
}