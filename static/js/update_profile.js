let update_form = document.getElementById("update_info");

// Profile settings updater

if (update_form) {
    update_form.onsubmit = function (e) {
        e.preventDefault();
        let username = document.getElementById("update_username");
        let email = document.getElementById("update_email");
        fetch("/profile", {
            method: "POST",
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
                }
            })
    }
}