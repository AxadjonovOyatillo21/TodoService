# TodoService
## Structure:
```
tapp/
  src/
    - api/
      - status: new
      - __init__.py
      - api_auth.py
    - auth/
      - templates/
        - auth/
          - register.html
          - sign_in.html
      - __init__.py
      - auth_operations.py
    - config/
      - __init__.py
    - database/
      - __init__.py
      - models.py
    - main_manager/
      - templates/
        - main_manager/
          - todo_list_detail.html
      - todo_list_todo_operations.py
    - static/
      - Audiowide/(font)
      - css/
        - helpers.css
        - main.css
      - js/
        - common_functions/
          - color_picker.js(status: new)
          - containers.js
          - delete_todo_list_or_todo.js
          - message.js
          - selector_pattern_builder.js
          - urls.js
          - wrappers.js(status: maybe trash)
        - todo_functions/
          - add_todo.js
          - update_todo.js
        - todo_list_functions/
          - add_todo_list.js
          - update_todo_list.js
        - todo_engine.js
        - todo_list_engine.js
        - update_profile.js
      - Open_Sans/(font)
    - templates/
      - base.html
      - index.html
    - user/
      - templates/
      - __init__.py
      - update_operations.py
    - validators_tools/
      - __init__.py
      - auth_validators.py
      - common_validators.py
      - todo_list_todo_validators.py
    - __init__.py
    - main.py
  - run.py
  - setup.sh
  - setup_environment.py
```

# Running code
## Windows(powershell)
```
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
python ./tapp/run.py
```
## Linux
```
python3 -m venv env
source ./env/bin/activate
pip3 install -r requirements.txt
python3 ./tapp/run.py
```