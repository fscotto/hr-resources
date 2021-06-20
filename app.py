import itertools
from datetime import date
from typing import List, Dict

from dateutil import relativedelta as period
from flask import Flask

from db.access import fetch_european_departments, \
    fetch_department_employees, \
    fetch_american_departments, \
    fetch_employees, \
    fetch_departments, \
    fetch_canadian_departments
from models.department import Department

app = Flask(__name__)


@app.get("/")
def index():
    return "<h1>Homepage HR Resources</h1>"


@app.errorhandler(404)
@app.errorhandler(500)
def handle_error(error):
    return {
        "status": error.code,
        "description": error.description,
        "name": error.name
    }


@app.get("/employee")
def employees():
    return {"employees": [e.to_json() for e in fetch_employees()]}


def __employees_group_by_seniority(departments: List[Department]) -> Dict[str, dict]:
    result = {}
    for department in departments:
        # Per ogni dipartimento ricerco i suoi impiegati
        employees = fetch_department_employees(department.department_id)

        # Raggruppo gli impiegati per anni di anzianità
        employee_group_by_years = itertools.groupby(employees,
                                                    lambda e: period.relativedelta(date.today(), e.hire_date).years)

        result[department.name] = {year: [e.to_json() for e in employees]
                                   for (year, employees) in employee_group_by_years}

    return result


@app.get("/employee/all-by-seniority")
def employees_by_seniority():
    departments = fetch_departments()
    return __employees_group_by_seniority(departments)


@app.get("/employee/american-by-seniority")
def american_employees_by_seniority():
    american_departments = fetch_american_departments()
    return __employees_group_by_seniority(american_departments)


@app.get("/employee/canadian-by-seniority")
def canadian_employees_by_seniority():
    canadian_departments = fetch_canadian_departments()
    return __employees_group_by_seniority(canadian_departments)


@app.get("/employee/european-by-seniority")
def european_employees_by_seniority():
    european_departments = fetch_european_departments()
    return __employees_group_by_seniority(european_departments)
