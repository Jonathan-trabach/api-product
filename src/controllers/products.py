from flask_restx import Resource
from src.server.instance import server
from src.listener.producer import send
from src.db.db import *

app, api = server.app, server.api

@api.route('/produtos')
class ProductsList(Resource):

    def get(self,):
        response = load()
        return response

    def post(self,):
        payload = api.payload
        save(payload)
        send(payload)
        return payload, 200

