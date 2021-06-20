import itertools
from datetime import date

from dateutil import relativedelta as datedelta

from db.access import fetch_european_departments, fetch_department_employees

if __name__ == '__main__':
    # Ricerco tutti i dipartimenti europei
    for department in fetch_european_departments():
        print(f"\n####### Department of {department.name} #######\n")
        # Per ogni dipartimento ricerco i suoi impiegati
        employees = [employee for employee in fetch_department_employees(department.department_id)]
        for employee in employees:
            print(f"{employee.last_name} {employee.first_name}")

        print("\n")
        # Raggruppo gli impiegati per anni di anzianità
        calculate_seniority = lambda e: datedelta.relativedelta(date.today(), e.hire_date).years
        employee_group_by_years = itertools.groupby(employees, calculate_seniority)
        # Stampo i risultati dell'aggregazione
        for years_to_employees in employee_group_by_years:
            print(f"Employees with {years_to_employees[0]} years of seniority:")
            for employee in years_to_employees[1]:
                print(employee.last_name, employee.first_name)
            print("\n")
