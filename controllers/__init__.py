from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.employees_controller import employee_routes

def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(employee_routes)
