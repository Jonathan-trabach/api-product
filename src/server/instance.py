from flask import Flask
from flask_restx import Api

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version="1.0",
            title="Api de Produtos",
            description="Api de Produtos",
            doc="/docs",
            prefix="/api"
        )

    def run(self, ):
        self.app.run(
            port=8085,
            debug=True,
        )

server = Server()