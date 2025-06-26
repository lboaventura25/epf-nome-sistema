from bottle import Bottle, request
from .base_controller import BaseController
from services.employee_service import EmployeeService

class EmployeeController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.employee_service = EmployeeService()


    # Rotas User
    def setup_routes(self):
        self.app.route('/employees', method='GET', callback=self.list_employees)
    

    def list_employees(self):
        employees = self.employee_service.get_all()
        return self.render('employees', employees=employees)


employee_routes = Bottle()
employee_controller = EmployeeController(employee_routes)
