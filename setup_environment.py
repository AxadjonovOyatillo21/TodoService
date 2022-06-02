variables = [
    "FLASK_APP",
    "FLASK_ENV",
    "USERNAME",
    "PASSWORD",
    "SERVER",
    "PORT",
    "DB_NAME"
]

file = open("setup.sh", "a")

for variable in variables:
    inp = input(f"Enter {variable}: ")
    command = f"export {variable}={inp};\n"
    file.write(command)

file.close()

