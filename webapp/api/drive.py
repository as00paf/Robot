from webapp.api import bp
from flask import request
from webapp.api.auth import token_auth


@bp.route('/drive', methods=['POST'])
@token_auth.login_required
def drive():
    data = request.get_json() or {}
    key = data["key"]
    is_down = data["is_down"]
    return "Well received : " + str(data)

