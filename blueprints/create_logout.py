from flask import Blueprint, session, redirect


def create_logout_blueprint():
    logout_blueprint = Blueprint('logout', __name__, template_folder='templates')

    @logout_blueprint.route('/logout', methods=['GET'])
    def logout():
        session.pop('role', None)
        session.pop('name', None)
        session.pop('surname', None)
        return redirect('/login')

    return logout_blueprint
