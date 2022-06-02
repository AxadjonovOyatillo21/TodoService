function create_message_box(serverResponse) {
	let messages_container = document.querySelector(".messages-container");
	let message_box = document.createElement("div");
	let classes_of_message_box = [
		"card-body",
		"font-size-md",
		"message-body",
		"shadow",
		"mx-auto",
		"px-normal",
		"py-normal",
		"section"
	];
	for (let class_of_message_box of classes_of_message_box) {
		message_box.classList.add(class_of_message_box);
	}
	let first_span_child_of_message = document.createElement("span");
	first_span_child_of_message.classList.add("text__default");
	first_span_child_of_message.textContent = "Messages: ";
	let code_status_code = document.createElement("code");
	code_status_code.innerHTML = `Status code: ${serverResponse.code}`;
	let close_button_of_message_box = document.createElement("button");
	close_button_of_message_box.classList.add("close");
	close_button_of_message_box.onclick = close;
	close_button_of_message_box.innerHTML = "&cross;"
	let messages_container_for_messages_from_server = document.createElement("div");
	messages_container_for_messages_from_server.classList.add("px-normal");
	messages_container_for_messages_from_server.classList.add("py-normal");
	for (message of serverResponse.messages) {
		let p_child = document.createElement("p");
		p_child.innerHTML = message;
		messages_container_for_messages_from_server.appendChild(p_child);
	}
	let message_box_children = [
		first_span_child_of_message,
		messages_container_for_messages_from_server,
		close_button_of_message_box,
		code_status_code
	];

	for (let child_of_message_box of message_box_children) {
		message_box.appendChild(child_of_message_box);
	}
	messages_container.appendChild(message_box);
	setInterval(function (){
		message_box.classList.add("opacity-animation");
		setInterval(function () {
			message_box.remove();
		}, 200);
	}, 3000)
} 

let close_msg;
if (document.querySelectorAll(".close")) {
    close_msg = document.querySelectorAll(".close");
}

if (close_msg) {
    // Connectiong close function to buttons
    for (btn of close_msg) {
        btn.onclick = close;
    }
}

function close(e) {
    let item = e.target.parentElement;
	item.classList.add("opacity-animation");
    setTimeout(function () {
		item.remove();
	}, 150);
}