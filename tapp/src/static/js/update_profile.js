let update_form = document.getElementById("update_info");

// Profile settings updater

if (update_form) {
    update_form.onsubmit = function (e) {
        e.preventDefault();
        let message = {
            "messages": [],
            "success": false,
            "code": 400
        };
        let username = document.getElementById("update_username")
        let email = document.getElementById("update_email");
        if (!username.value.trim()) {
            message.messages.push("Empty username!")
        }
        if (!email.value.trim()) {
            message.messages.push("Empty email!")
        }
        if (username.value.trim() && email.value.trim()) {
            fetch("/profile", {
                method: "PATCH",
                body: JSON.stringify({
                    "username": username.value,
                    "email": email.value
                }),
                headers: {
                    "Content-Type": "application/json"
                }
            })
                .then(response => response.json())
                .then(jsonResponse => {
                    if (jsonResponse.messages && jsonResponse.code) {
                        create_message_box(jsonResponse);
                        let username_in_navbar = document.getElementById("username");
                        console.log(username_in_navbar);
                        if (jsonResponse.success) {
                            username_in_navbar.textContent = username.value;
                        } else {
                            username.value = username_in_navbar.textContent;
                            email.value = jsonResponse.email;
                        }
                    }
                })
        } else {
            create_message_box(message);
        }
    }
}