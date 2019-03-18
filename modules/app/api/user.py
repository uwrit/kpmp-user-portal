import os
from flask import request, jsonify, g
from modules.app import mongo
from modules.app.api import api
import modules.logger as logger

LOG = logger.get_root_logger(__name__)


@api.route('/api/user', methods=['GET'])
def get_users():
    query = request.args
    users = [u for u in mongo.db.users.find(query)]
    return jsonify(users), 200


@api.route('/api/user/<string:eppn>', methods=['GET'])
def get_user(eppn):
    user = mongo.db.users.find_one({'eppn': eppn})
    if not user:
        return jsonify(), 404
    return jsonify(user), 200
