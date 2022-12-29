variables = [
    "FLASK_APP",
    "FLASK_ENV",
    "DB",
    "USERNAME",
    "PASSWORD",
    "SERVER",
    "PORT",
    "DB_NAME"
]

file = open("setup.sh", "a")
if file:
    inp = input("File is not empty. Do you want to clear file?(y/n)")
    if inp == "y":
        file.close()
        file = open("setup.sh", "w")
    
for variable in variables:
    inp = input(f"Enter {variable}: ")
    if inp:
        command = f"export {variable}={inp};\n"
        file.write(command)
    else:
        continue
file.close()

