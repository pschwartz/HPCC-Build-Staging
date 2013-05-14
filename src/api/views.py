
from api import api
from api.utils import Registry
from flask import jsonify
from flask.views import MethodView


class BaseAPI(MethodView):
    def get(self, base_id):
        if base_id is None:
            return jsonify({"message": "test"})
        else:
            return jsonify({"message": base_id})

Registry.register_get(api, BaseAPI, 'base_api', '/api/base/', pk='base_id', pk_type='string')
print Registry.build_url('/api/base', [('string','base_id')])
