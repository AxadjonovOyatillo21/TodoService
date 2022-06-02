import URLS from "./urls.js";
let delete_btns = document.querySelectorAll(".delete-btns");
let active_list = document.querySelector(".active-list");
let active_list_public_id;
if (active_list) {
    active_list_public_id = active_list.id;
}

if (delete_btns) {
    for (let delete_btn of delete_btns) {
        delete_btn.onclick = delete_todo_or_list;
    }
}

export default function delete_todo_or_list(e) {
    let parent_public_id = e.target.dataset['id'];
    let url;
    let filter_id;
    let item_type;
    let BuildURLS = new URLS();
    // recognizing type of object
    if (parent_public_id.includes("todo-item-")) {
        // filtering public_id of an object
        filter_id = parent_public_id.replaceAll("todo-item-", "");
        let list_filter_id = null;
        if (active_list_public_id.includes("todo-list-")) {
            list_filter_id = active_list_public_id.replaceAll("todo-list-", "");
        }
        url = BuildURLS.build_delete_todo_URL(list_filter_id || active_list_public_id, filter_id);
        // defining object type
        item_type = "todo";
    } else if (parent_public_id.includes("todo-list-")) {
        filter_id = parent_public_id.replaceAll("todo-list-", "");
        url = BuildURLS.build_delete_todo_list_URL(filter_id);
        item_type = "todo_list";
    }
    let parameter = `${item_type}_id`;
    fetch(url, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        }
    })
        .then(response => response.json())
        .then(jsonResponse => {
            // removing parent object
            if (jsonResponse.success) {
                let parent_element = document.getElementById(parent_public_id);
                parent_element.remove();
                let todo_lists_count = document.getElementById("counter");
                let value = todo_lists_count.innerHTML;
                value = +value - 1;
                todo_lists_count.innerHTML = value;
                todo_lists_count.style.color = "red";
            }

            // publishing a message from the server
            create_message_box(jsonResponse);
        })
}
