from models.db import db
from models.employee import Employee

class EmployeeService():
    def __init__(self):
        self.db = db

    def get_all(self):
        session = self.db.get_session()
        employees = session.query(Employee).all()
        session.close()
        
        return employees
