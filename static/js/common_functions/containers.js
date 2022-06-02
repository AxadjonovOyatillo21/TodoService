import URLS from '../common_functions/urls.js';
import delete_todo_or_list from '../common_functions/delete_todo_list_or_todo.js';
import todo_list_open_updator_function from '../todo_list_functions/update_todo_list.js';
import todo_item_open_updator_function from '../todo_functions/update_todo.js';
import selector_pattern from './selector_pattern_builder.js';

export default class Containers {
    create_full_todo_list_container(serverResponse, default_container=null) {
        let BuildURLS = new URLS();
        let list_data = serverResponse.todo_list_data || serverResponse;
        let list_public_id = list_data.public_id;
        if (list_public_id.includes("todo-list")) {
            list_public_id = list_public_id.replaceAll("todo-list-", "");
        }
        let list_title = list_data.title;
        let list_completed = list_data.completed;
        let string_list_completed = String(list_completed);
        let list_deadline = list_data.deadline;
        let create_container = default_container || document.createElement("li");
        let classes_of_container = [
            "display-flex",
            "justify-content-between",
            "shadow",
            "px-normal",
            "py-normal",
            "section",
            "flex-wrap"
        ];
        for (let class_of_container of classes_of_container) {
            create_container.classList.add(class_of_container);
        }
        create_container.setAttribute("id", `todo-list-${list_public_id}`);
        let main_child_of_container = document.createElement("div");
        let heading_child_of_main_child = document.createElement("h1");
        let child_of_heading_child_of_main_child = document.createElement("a");
        let get_url = BuildURLS.build_todo_list_URL(list_public_id);
        child_of_heading_child_of_main_child.setAttribute("href", get_url);
        child_of_heading_child_of_main_child.setAttribute("id", `todo-list-title-${list_public_id}`);
        child_of_heading_child_of_main_child.textContent = list_title;
        child_of_heading_child_of_main_child.classList.add("content");
        heading_child_of_main_child.appendChild(child_of_heading_child_of_main_child);
        let second_p_child_of_main_child = document.createElement("p");
        let second_p_child_of_main_child_classes = [
            "display-block",
            "py-normal"
        ]
        for (let class_of_child of second_p_child_of_main_child_classes) {
            second_p_child_of_main_child.classList.add(class_of_child);
        }
        let first_child_of_second_p_child = document.createElement("span");
        first_child_of_second_p_child.textContent = "Completed: ";
        let second_child_of_second_p_child = document.createElement("input");
        second_child_of_second_p_child.classList.add("completed-checkbox"); 
        second_child_of_second_p_child.setAttribute("type", "checkbox");
        second_child_of_second_p_child.setAttribute("id", `todo-list-completed-${list_public_id}`);
        second_child_of_second_p_child.classList.add("disabled");
        if (list_completed) {
            second_child_of_second_p_child.setAttribute("checked", true);
        }
        let third_child_of_second_p_child = document.createElement("span");
        third_child_of_second_p_child.textContent = string_list_completed.charAt(0).toUpperCase() + string_list_completed.slice(1, 10);
        let second_p_child_of_main_child_children = [
            first_child_of_second_p_child,
            second_child_of_second_p_child,
            third_child_of_second_p_child
        ]
        for (let child of second_p_child_of_main_child_children) {
            second_p_child_of_main_child.appendChild(child);
        }

        let third_p_child_of_main_child = document.createElement("p");
        let first_span_child_of_third_p_child = document.createElement("span");
        first_span_child_of_third_p_child.textContent = "Deadline: ";
        let second_span_child_of_third_p_child = document.createElement("span");
        second_span_child_of_third_p_child.classList.add("content");
        second_span_child_of_third_p_child.setAttribute("id", `todo-list-deadline-${list_public_id}`);
        second_span_child_of_third_p_child.textContent = list_deadline;
        let third_p_child_of_main_child_children = [
            first_span_child_of_third_p_child,
            second_span_child_of_third_p_child
        ];
        for (let child_of_third_p_child_of_main_child of third_p_child_of_main_child_children) {
            third_p_child_of_main_child.appendChild(child_of_third_p_child_of_main_child);
        }

        let main_child_of_container_children = [
            heading_child_of_main_child,
            second_p_child_of_main_child,
            third_p_child_of_main_child
        ]
        for (let child_of_main of main_child_of_container_children) {
            main_child_of_container.appendChild(child_of_main);
        }
        let second_main_child_of_container = document.createElement("div");
        second_main_child_of_container.classList.add("py-normal");
        let todo_list_open_updator_button_child_of_second_main_child_of_container = document.createElement("button");
        let todo_list_open_updator_button_child_classes = [
            "btn",
            "bg__yellow",
            "text__light",
            "btn-yellow",
            "pointer",
            "shadow",
            "todo-list-open-updator-btns"
        ]
        for (let todo_list_open_updator_btn_class of todo_list_open_updator_button_child_classes) {
            todo_list_open_updator_button_child_of_second_main_child_of_container.classList.add(todo_list_open_updator_btn_class);
        }
        todo_list_open_updator_button_child_of_second_main_child_of_container.setAttribute("data-id", `todo-list-${list_public_id}`);
        todo_list_open_updator_button_child_of_second_main_child_of_container.onclick = todo_list_open_updator_function;
        todo_list_open_updator_button_child_of_second_main_child_of_container.textContent = "Update";
        let delete_button_child_of_second_main_child_of_container = document.createElement("button");
        let delete_button_child_classes = [
            "btn",
            "bg__red",
            "text__light",
            "btn-red",
            "pointer",
            "shadow",
            "delete-btns"
        ]
        for (let delete_btn_class of delete_button_child_classes) {
            delete_button_child_of_second_main_child_of_container.classList.add(delete_btn_class);
        }
        delete_button_child_of_second_main_child_of_container.setAttribute("data-id", `todo-list-${list_public_id}`);
        delete_button_child_of_second_main_child_of_container.onclick = delete_todo_or_list;
        delete_button_child_of_second_main_child_of_container.textContent = "Delete";
        second_main_child_of_container.appendChild(todo_list_open_updator_button_child_of_second_main_child_of_container);
        second_main_child_of_container.appendChild(delete_button_child_of_second_main_child_of_container);
        let todo_lists_wrapper_children = [
            main_child_of_container,
            second_main_child_of_container
        ]
        for (let main_child of todo_lists_wrapper_children) {
            create_container.appendChild(main_child);
        }
        return create_container;
    }
    create_full_update_todo_list_container(list_data, update_todo_list_function) {
        let filter_id;
        if (list_data.public_id.includes("todo-list-")) {
            filter_id = list_data.public_id.replaceAll("todo-list-", "");
        }
        let create_container = document.createElement("div");
        // create_container.classList.add("py-normal");
        create_container.classList.add("w-100");
        let inner_container = document.createElement("div");
        let classes_of_inner_container = [
            "card-body",
            "display-flex",
            "flex-wrap",
            "justify-content-between",
            "align-items-flex-start",
            "w-100"
        ];
        for (let class_of_inner_container of classes_of_inner_container) {
            inner_container.classList.add(class_of_inner_container);
        }
        let main_div_child_of_container = document.createElement("div");
        let heading_child_of_container = document.createElement("h1");
        heading_child_of_container.textContent = "Update Todo List: ";
        let div_child_of_container = document.createElement("div");
        let title_input_child_of_main_div_child = document.createElement("input");
        main_div_child_of_container.classList.add("py-normal")
        div_child_of_container.classList.add("py-normal");
        let title_input_attributes = {
            "type": "text",
            "id": `update-todo-list-title-${filter_id}`,
            "value": list_data.title
        };
        for (let title_input_attribute of Object.keys(title_input_attributes)) {
            title_input_child_of_main_div_child.setAttribute(
                title_input_attribute,
                title_input_attributes[title_input_attribute]
            );
        }
        let deadline_input_child_of_main_div_child = document.createElement("input");
        let deadline_input_attributes = {
            "type": "text",
            "id": `update-todo-list-deadline-${filter_id}`,
            "value": list_data.deadline
        };
        for (let deadline_input_attribute of Object.keys(deadline_input_attributes)) {
            deadline_input_child_of_main_div_child.setAttribute(
                deadline_input_attribute,
                deadline_input_attributes[deadline_input_attribute]
            );
        }
        let p_child_of_main_div_child = document.createElement("p");
        let p_child_of_main_div_child_classes = [
            "display-block",
            "my-normal"
        ]
        for (let class_of_p_child of p_child_of_main_div_child_classes) {
            p_child_of_main_div_child.classList.add(class_of_p_child);
        }
        let first_child_of_p_child = document.createElement("span");
        first_child_of_p_child.textContent = "Completed: ";
        let second_child_of_p_child = document.createElement("input");
        let second_child_of_p_child_attributes = {
            "type": "checkbox",
            "id": `update-todo-list-completed-${filter_id}`,
        };
        second_child_of_p_child.classList.add("completed-checkbox");
        for (let second_child_of_p_child_attribute of Object.keys(second_child_of_p_child_attributes)) {
            second_child_of_p_child.setAttribute(
                second_child_of_p_child_attribute,
                second_child_of_p_child_attributes[second_child_of_p_child_attribute]
            );
        }
        if (list_data.completed) {
            second_child_of_p_child.setAttribute("checked", true);
        }
        let third_child_of_p_child = document.createElement("span");
        third_child_of_p_child.textContent = String(list_data.completed).charAt(0).toUpperCase() + String(list_data.completed).slice(1, 10);
        let p_child_of_main_div_child_children = [
            first_child_of_p_child,
            second_child_of_p_child,
            third_child_of_p_child
        ]
        for (let child_of_p_child of p_child_of_main_div_child_children) {
            p_child_of_main_div_child.appendChild(child_of_p_child);
        }
        let submit_button_of_div_child = document.createElement("button");
        let submit_button_classes = [
            "btn",
            "bg__yellow",
            "text__light",
            "btn-yellow",
            "pointer",
            "shadow"
        ];
        for (let class_of_submit_btn of submit_button_classes) {
            submit_button_of_div_child.classList.add(class_of_submit_btn);
        }
        submit_button_of_div_child.setAttribute("data-id", list_data.public_id);
        submit_button_of_div_child.textContent = "Update";
        submit_button_of_div_child.onclick = update_todo_list_function;
        let cancel_button_of_div_child = document.createElement("button");
        let cancel_button_classes = [
            "btn",
            "bg__red",
            "text__light",
            "btn-red",
            "pointer",
            "shadow"
        ];
        for (let class_of_cancel_btn of cancel_button_classes) {
            cancel_button_of_div_child.classList.add(class_of_cancel_btn);
        }
        cancel_button_of_div_child.setAttribute("data-id", list_data.public_id);
        cancel_button_of_div_child.textContent = "Cancel";
        cancel_button_of_div_child.onclick = function () {
            let containers = new Containers();
            let parent_element = document.getElementById(list_data.public_id);
            parent_element.innerHTML = ""
            let create_container = containers.create_full_todo_list_container(list_data, parent_element);
        }
        let main_div_child_children = [
            title_input_child_of_main_div_child,
            deadline_input_child_of_main_div_child,
            p_child_of_main_div_child
        ];
        for (let child_of_main_div_child of main_div_child_children) {
            main_div_child_of_container.appendChild(child_of_main_div_child);
        }
        let div_child_children = [
            submit_button_of_div_child,
            cancel_button_of_div_child
        ];
        for (let child_of_div_child of div_child_children) {
            div_child_of_container.appendChild(child_of_div_child);
        }
        let inner_container_children = [
            main_div_child_of_container,
            div_child_of_container
        ];
        for (let child_of_inner_container of inner_container_children) {
            inner_container.appendChild(child_of_inner_container);
        }
        let create_container_children = [
            heading_child_of_container,
            inner_container
        ]
        for (let child_of_container of create_container_children) {
            create_container.appendChild(child_of_container);
        }
        return create_container;
    }
    create_full_todo_container(serverResponse, default_container=null) {
        let BuildURLS = new URLS();
        /* block commented */
        /* Define variables(properties of new list) */
        let todo_data = serverResponse.todo_data || serverResponse;
        let todo_public_id = todo_data.public_id;
        let filter_id = todo_public_id;
        if (todo_public_id.includes("todo-item-")) {
            filter_id = todo_public_id.replaceAll("todo-item-", "");
        }
        let todo_title = todo_data.title;
        let todo_body = todo_data.body;
        let todo_completed = todo_data.completed;
        let string_todo_completed = String(todo_completed);
        let todo_deadline = todo_data.deadline;
        /*** endblock ***/
        let create_container = default_container || document.createElement("li");
        let classes_of_container = [
            "display-flex",
            "justify-content-between",
            "shadow",
            "px-normal",
            "py-normal",
            "section",
            "flex-wrap"
        ];
        for (let class_of_container of classes_of_container) {
            create_container.classList.add(class_of_container);
        }
        create_container.setAttribute("id", `todo-item-${filter_id}`);
        let main_child_of_container = document.createElement("div");
        let heading_child_of_main_child = document.createElement("h1");
        let classes_of_heading_child_of_main_child = [
            "display-4",
            "text__default",
            "py-normal"
        ]
        for (let class_of_heading_child_of_main_child of classes_of_heading_child_of_main_child) {
            heading_child_of_main_child.classList.add(class_of_heading_child_of_main_child);
        }
        heading_child_of_main_child.textContent = todo_title;
        heading_child_of_main_child.setAttribute("id", `todo-item-title-${filter_id}`);
        let first_p_child_of_main_child = document.createElement("p");
        let classes_of_first_p_child = [
            "font-size-md",
            'py-normal',
            'px-normal'
        ]
        for (let class_of_first_p_child of classes_of_first_p_child) {
            first_p_child_of_main_child.classList.add(class_of_first_p_child)
        }
        first_p_child_of_main_child.textContent = todo_body;
        first_p_child_of_main_child.setAttribute("id", `todo-item-body-${filter_id}`);
        let second_p_child_of_main_child = document.createElement("p");
        second_p_child_of_main_child.classList.add("py-normal");
        let first_span_child_of_second_p_child = document.createElement("span");
        first_span_child_of_second_p_child.textContent = "Completed: "
        let second_input_child_of_second_p_child = document.createElement("input");
        second_input_child_of_second_p_child.setAttribute("type", "checkbox");
        if (todo_completed) {
            second_input_child_of_second_p_child.setAttribute("checked", true);
        }
        second_input_child_of_second_p_child.classList.add("completed-checkbox");
        second_input_child_of_second_p_child.classList.add("disabled");
        second_input_child_of_second_p_child.setAttribute("id", `todo-item-completed-${filter_id}`);
        let third_span_child_of_second_p_child = document.createElement("span");
        third_span_child_of_second_p_child.textContent = string_todo_completed.charAt(0).toUpperCase() + string_todo_completed.slice(1, 10);
        let second_p_child_of_main_child_children = [
            first_span_child_of_second_p_child,
            second_input_child_of_second_p_child,
            third_span_child_of_second_p_child
        ]
        for (let second_p_child_of_main_child_child of second_p_child_of_main_child_children) {
            second_p_child_of_main_child.appendChild(second_p_child_of_main_child_child);
        }
        let third_p_child_of_main_child = document.createElement("p");
        let first_span_child_of_third_p_child = document.createElement("span");
        first_span_child_of_third_p_child.textContent = "Deadline: ";
        let second_span_child_of_third_p_child = document.createElement("span");
        second_span_child_of_third_p_child.textContent = todo_deadline;
        second_span_child_of_third_p_child.setAttribute("id", `todo-item-deadline-${filter_id}`);
        let third_p_child_of_main_child_children = [
            first_span_child_of_third_p_child,
            second_span_child_of_third_p_child
        ]
        for (let child_of_third_p_child of third_p_child_of_main_child_children) {
            third_p_child_of_main_child.appendChild(child_of_third_p_child);
        }
        let main_child_of_container_children = [
            heading_child_of_main_child,
            first_p_child_of_main_child,
            second_p_child_of_main_child,
            third_p_child_of_main_child
        ]
        for (let child_of_main_child_of_container of main_child_of_container_children) {
            main_child_of_container.appendChild(child_of_main_child_of_container);
        }
        let second_main_child_of_container = document.createElement("div");
        second_main_child_of_container.classList.add("py-normal");
        let todo_open_updator_button_child_of_second_main_child_of_container = document.createElement("button");
        let todo_open_updator_button_child_classes = [
            "btn",
            "bg__yellow",
            "text__light",
            "btn-yellow",
            "pointer",
            "shadow",
            "todo-item-open-updator-btns"
        ]
        for (let todo_open_updator_btn_class of todo_open_updator_button_child_classes) {
            todo_open_updator_button_child_of_second_main_child_of_container.classList.add(todo_open_updator_btn_class);
        }
        todo_open_updator_button_child_of_second_main_child_of_container.setAttribute("data-id", `todo-item-${filter_id}`);
        todo_open_updator_button_child_of_second_main_child_of_container.onclick = todo_item_open_updator_function;
        todo_open_updator_button_child_of_second_main_child_of_container.textContent = "Update";
        let delete_button_child_of_second_main_child_of_container = document.createElement("button");
        let delete_button_child_classes = [
            "btn",
            "bg__red",
            "text__light",
            "btn-red",
            "pointer",
            "shadow",
            "delete-btns"
        ]
        for (let delete_btn_class of delete_button_child_classes) {
            delete_button_child_of_second_main_child_of_container.classList.add(delete_btn_class);
        }
        delete_button_child_of_second_main_child_of_container.setAttribute("data-id", `todo-item-${filter_id}`);
        delete_button_child_of_second_main_child_of_container.onclick = delete_todo_or_list;
        delete_button_child_of_second_main_child_of_container.textContent = "Delete";
        second_main_child_of_container.appendChild(todo_open_updator_button_child_of_second_main_child_of_container);
        second_main_child_of_container.appendChild(delete_button_child_of_second_main_child_of_container);
        let todos_wrapper_children = [
            main_child_of_container,
            second_main_child_of_container
        ];
        for (let child_of_container of todos_wrapper_children) {
            create_container.appendChild(child_of_container);
        }
        return create_container;
    }
    create_full_update_todo_container(todo_data, update_todo_function) {
        let filter_id;
        if (todo_data.public_id.includes("todo-item-")) {
            filter_id = todo_data.public_id.replaceAll("todo-item-", "");
        }
        let create_container = document.createElement("div");
        create_container.classList.add("py-normal");
        create_container.classList.add("w-100");
        let inner_container = document.createElement("div");
        let classes_of_inner_container = [
            "card-body",
            "w-100"
        ];
        for (let class_of_inner_container of classes_of_inner_container) {
            inner_container.classList.add(class_of_inner_container);
        }
        let heading_child_of_container = document.createElement("h1");
        heading_child_of_container.textContent = "Update Todo: ";
        let main_div_child_of_container = document.createElement("div");
        let div_child_of_container = document.createElement("div");
        div_child_of_container.classList.add("my-normal");
        let todo_title_input_child_of_main_div_child = document.createElement("input");
        let todo_title_input_attributes = {
            "type": "text",
            "id": `update-todo-item-title-${filter_id}`,
            "value": todo_data.title
        };
        for (let todo_title_input_attribute of Object.keys(todo_title_input_attributes)) {
            todo_title_input_child_of_main_div_child.setAttribute(
                todo_title_input_attribute,
                todo_title_input_attributes[todo_title_input_attribute]
            );
        }
        let todo_title_input_child_classes = [
            "display-block",
            "my-normal"
        ];
        for (let todo_title_input_class of todo_title_input_child_classes) {
            todo_title_input_child_of_main_div_child.classList.add(todo_title_input_class);
        }
        let todo_body_child_of_main_div_child = document.createElement("textarea");
        todo_body_child_of_main_div_child.textContent = todo_data.body;
        let todo_body_child_attributes = {
            "type": "text",
            "id": `update-todo-item-body-${filter_id}`,
            "cols": 40,
            "rows": 10
        };
        for (let todo_body_child_attribute of Object.keys(todo_body_child_attributes)) {
            todo_body_child_of_main_div_child.setAttribute(
                todo_body_child_attribute,
                todo_body_child_attributes[todo_body_child_attribute]
            );
        }
        let todo_body_child_classes = [
            "display-block",
            "my-normal"
        ];
        for (let todo_body_child_class of todo_body_child_classes) {
            todo_body_child_of_main_div_child.classList.add(todo_body_child_class);
        }





        let todo_completed_child_of_main_div_child = document.createElement("p");
        todo_completed_child_of_main_div_child.classList.add("py-normal");
        let first_span_child_of_main_div_child = document.createElement("span");
        first_span_child_of_main_div_child.textContent = "Completed: "
        let second_input_child_of_main_div_child = document.createElement("input");
        second_input_child_of_main_div_child.setAttribute("type", "checkbox");
        if (todo_data.completed) {
            second_input_child_of_main_div_child.setAttribute("checked", true);
        }
        second_input_child_of_main_div_child.classList.add("completed-checkbox");
        second_input_child_of_main_div_child.setAttribute("id", `update-todo-item-completed-${filter_id}`);
        let third_span_child_of_main_div_child = document.createElement("span");
        third_span_child_of_main_div_child.textContent = String(todo_data.completed).charAt(0).toUpperCase() + String(todo_data.completed).slice(1, 10);
        let todo_completed_child_of_main_div_child_children = [
            first_span_child_of_main_div_child,
            second_input_child_of_main_div_child,
            third_span_child_of_main_div_child
        ]
        for (let todo_completed_child_of_main_div_child_child of todo_completed_child_of_main_div_child_children) {
            todo_completed_child_of_main_div_child.appendChild(todo_completed_child_of_main_div_child_child);
        }
        todo_completed_child_of_main_div_child.classList.add("my-normal");
        let todo_deadline_child_of_main_div_child = document.createElement("input");
        let todo_deadline_child_attributes = {
            "type": "text",
            "id": `update-todo-item-deadline-${filter_id}`,
            "value": todo_data.deadline
        };
        let todo_deadline_child_classes = [
            "display-block",
            "my-normal"
        ];
        for (let todo_deadline_child_class of todo_deadline_child_classes) {
            todo_deadline_child_of_main_div_child.classList.add(todo_deadline_child_class);
        }
        for (let todo_deadline_child_attribute of Object.keys(todo_deadline_child_attributes)) {
            todo_deadline_child_of_main_div_child.setAttribute(
                todo_deadline_child_attribute,
                todo_deadline_child_attributes[todo_deadline_child_attribute]
            );
        }
        let main_div_child_of_container_children = [
            todo_title_input_child_of_main_div_child,
            todo_body_child_of_main_div_child,
            todo_completed_child_of_main_div_child,
            todo_deadline_child_of_main_div_child
        ];
        for (let main_div_child_of_container_child of main_div_child_of_container_children) {
            main_div_child_of_container.appendChild(main_div_child_of_container_child)
        }
        let update_button_of_div_child = document.createElement("button");
        let update_button_classes = [
            "btn",
            "bg__yellow",
            "text__light",
            "btn-yellow",
            "pointer",
            "shadow"
        ];
        for (let class_of_update_btn of update_button_classes) {
            update_button_of_div_child.classList.add(class_of_update_btn);
        }
        update_button_of_div_child.setAttribute("data-id", todo_data.public_id);
        update_button_of_div_child.textContent = "Update";
        update_button_of_div_child.onclick = update_todo_function;
        let cancel_button_of_div_child = document.createElement("button");
        let cancel_button_classes = [
            "btn",
            "bg__red",
            "text__light",
            "btn-red",
            "pointer",
            "shadow"
        ];
        for (let class_of_cancel_btn of cancel_button_classes) {
            cancel_button_of_div_child.classList.add(class_of_cancel_btn);
        }
        cancel_button_of_div_child.setAttribute("data-id", todo_data.public_id);
        cancel_button_of_div_child.textContent = "Cancel";
        cancel_button_of_div_child.onclick = function () {
            let containers = new Containers();
            let parent_element = document.getElementById(todo_data.public_id);
            parent_element.innerHTML = ""
            let create_container = containers.create_full_todo_container(todo_data, parent_element);
        }
        let div_child_of_container_children = [
            update_button_of_div_child,
            cancel_button_of_div_child
        ];
        for (let div_child_of_container_child of div_child_of_container_children) {
            div_child_of_container.appendChild(div_child_of_container_child);
        }
        let inner_container_children = [
            main_div_child_of_container,
            div_child_of_container
        ];
        for (let child_of_inner_container of inner_container_children) {
            inner_container.appendChild(child_of_inner_container);
        }
        let create_container_children = [
            heading_child_of_container,
            inner_container
        ]
        for (let child_of_container of create_container_children) {
            create_container.appendChild(child_of_container);
        }
        return create_container;
    }
}