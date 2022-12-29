export default class Wrappers {
	update_todo_list_wrapper(list) {
		`
		<div>
		    <input type="text" id="update-todo-list-title-${list.public_id}" placeholder="Title" value="${list.title}">
		    <input type="text" id="update-todo-list-deadline-${list.public_id}" placeholder="Deadline: dd/mm/yyyy" value="${list.deadline}">
		    <input type="submit" value="Update Todo List" class="bg__default__hover">
		</div>
		<div>
		<button class="
				btn bg__yellow text__light btn-yellow
				pointer shadow update-btns" data-id="todo-list-${ list.public_id }">
			Update              
		</button>
		<button class="
				btn bg__yellow text__light btn-yellow
				pointer shadow cancel-btns" data-id="todo-list-${ list.public_id }">
			Cancel              
		</button>
		</div>  
		`
	}
}