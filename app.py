from bottle import Bottle
from config import Config
from models.db import db

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()
        db.init_db() # Inicializa o banco de dados

    def setup_routes(self):
        from controllers import init_controllers

        print('🚀 Inicializa rotas!')
        init_controllers(self.bottle)

    def run(self):
        self.setup_routes()
        self.bottle.run(
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )


def create_app():
    return App()
