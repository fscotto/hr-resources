from datetime import date

from models.department import Department


class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name


class Employee(Person):
    def __init__(self, employee_id: int, first_name: str, last_name: str, email: str, phone_number: str,
                 hire_date: date, department: Department, job_id: int = 0, salary: float = 0, manager_id: int = 0):
        super().__init__(first_name, last_name)
        self.__employee_id = employee_id
        self.__email = email
        self.__phone_number = phone_number
        self.__hire_date = hire_date
        self.__department = department
        self.__job_id = job_id
        self.__salary = salary
        self.__manager_id = manager_id

    @property
    def employee_id(self) -> int:
        return self.__employee_id

    @property
    def email(self) -> str:
        return self.__email

    @property
    def phone_number(self) -> str:
        return self.__phone_number

    @property
    def hire_date(self) -> date:
        return self.__hire_date

    @property
    def department(self) -> Department:
        return self.__department

    @property
    def job_id(self) -> int:
        return self.__job_id

    @property
    def salary(self) -> float:
        return self.__salary

    @property
    def manager_id(self) -> int:
        return self.__manager_id

    def __json__(self):
        return {
            'employee_id': self.__employee_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.__email,
            'hire_date': self.__hire_date,
            'department': self.__department if self.__department is not None else None,
            'job_id': self.__job_id,
            'salary': f"{self.__salary:,.2f}",
            'manager_id': self.__manager_id
        }

    def __str__(self):
        return f"Employee({self.__employee_id}, {self.first_name}, {self.last_name}, " \
               f"{self.__email}, {self.__phone_number}, {self.__hire_date})"
