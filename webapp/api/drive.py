from webapp.api import bp
from flask import request, current_app
from webapp.api.auth import token_auth
from pynput.keyboard import KeyCode


@bp.route('/drive', methods=['POST'])
@token_auth.login_required
def drive():
    try:
        data = request.get_json() or {}
        key = KeyCode.from_char(data["key"])
        is_down = data["is_down"]
        
        if is_down == True:
            current_app.control_service.on_key_pressed(key)
        else:
            current_app.control_service.on_key_released(key)
            
        return "Well received : " + str(data)
    except Exception as e:
        return "An error occured: " + str(e) + "\nFrom data: " + str(data)

