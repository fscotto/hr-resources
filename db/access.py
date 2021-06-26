from typing import List

from psycopg2 import connect, extras as dbopts

from models.department import Department
from models.employee import Employee
from models.location import Location

db_url: str = 'postgresql://postgres:@localhost:5432/postgres'


def __create_department(row):
    return Department(
        department_id=row["department_id"],
        name=row["department_name"],
        location=Location(
            location_id=row["location_id"],
            postal_code=row["postal_code"],
            street_address=row["street_address"],
            state_province=row["state_province"],
            country_id=row["country_id"],
            city=row["city"]
        ))


def fetch_departments() -> List[Department]:
    """
    Ricerca tutti i dipartimenti attivi
    :return: elenco dei dipartimenti
    """
    with connect(db_url) as connection:
        with connection.cursor(cursor_factory=dbopts.DictCursor) as cursor:
            cursor.execute(
                """
                select
                    d.department_id,
                    d.department_name,
                    d.location_id,
                    l.postal_code,
                    l.street_address,
                    l.city,
                    l.state_province,
                    l.country_id 
                from
                    hr.departments d
                left join hr.locations l on
                    d.location_id = l.location_id
                """
            )

            departments = [__create_department(row) for row in cursor.fetchall()]

    return departments


def fetch_american_departments() -> List[Department]:
    """
    Ricerca tutti i dipartimenti presenti negli USA.
    :return: elenco dei dipartimenti USA
    """
    with connect(db_url) as connection:
        with connection.cursor(cursor_factory=dbopts.DictCursor) as cursor:
            cursor.execute(
                """
                select
                    d.department_id,
                    d.department_name,
                    d.location_id,
                    l.postal_code,
                    l.street_address,
                    l.city,
                    l.state_province,
                    l.country_id 
                from
                    hr.departments d
                left join hr.locations l on
                    d.location_id = l.location_id
                where
                    l.country_id = 'US'
                """
            )

            departments = [__create_department(row) for row in cursor.fetchall()]

    return departments


def fetch_canadian_departments() -> List[Department]:
    """
    Ricerca tutti i dipartimenti presenti in Canada.
    :return: elenco dei dipartimenti canadesi
    """
    with connect(db_url) as connection:
        with connection.cursor(cursor_factory=dbopts.DictCursor) as cursor:
            cursor.execute(
                """
                select
                    d.department_id,
                    d.department_name,
                    d.location_id,
                    l.postal_code,
                    l.street_address,
                    l.city,
                    l.state_province,
                    l.country_id 
                from
                    hr.departments d
                left join hr.locations l on
                    d.location_id = l.location_id
                where
                    l.country_id = 'CA'
                """
            )

            departments = [__create_department(row) for row in cursor.fetchall()]

    return departments


def fetch_european_departments() -> List[Department]:
    """
    Ricerca tutti i dipartimenti dei paesi europei dove sono presenti
    dei dipartimenti.
    :return: elenco dei dipartimenti europei
    """
    with connect(db_url) as connection:
        with connection.cursor(cursor_factory=dbopts.DictCursor) as cursor:
            cursor.execute(
                """
                select
                    d.department_id,
                    d.department_name,
                    d.location_id,
                    l.postal_code,
                    l.street_address,
                    l.city,
                    l.state_province,
                    l.country_id 
                from
                    hr.departments d
                left join hr.locations l on
                    d.location_id = l.location_id
                where
                    l.country_id in ('UK', 'DE')
                """
            )

            # Prendo dal DB tutti i dipartimenti presenti nel Regno Unito e Germania
            departments = [__create_department(row) for row in cursor.fetchall()]

    return departments


def fetch_department_employees(department_id: int) -> List[Employee]:
    """
    Ricerca tutti i dipendenti di un dipartimento
    :param department_id: dipartimento da ricercare
    :return: elenco dei dipendenti
    """
    employees = []
    with connect(db_url) as connection:
        with connection.cursor(cursor_factory=dbopts.DictCursor) as cursor:
            cursor.execute(
                f"""
                select
                    e.employee_id,
                    e.first_name,
                    e.last_name,
                    e.email,
                    e.phone_number,
                    e.hire_date,
                    e.job_id,
                    e.salary,
                    e.manager_id,
                    e.department_id,
                    d.department_name,
                    l.location_id,
                    l.city,
                    l.postal_code,
                    l.state_province,
                    l.street_address,
                    l.country_id
                from
                    hr.employees e
                left join hr.departments d on
                    e.department_id = d.department_id
                left join hr.locations l on
                    d.location_id = l.location_id
                where
                    e.department_id = %s
                """,
                (department_id,)
            )

            # Prendo dal DB tutti i dipendenti di un dipartimento
            for row in cursor.fetchall():
                employees.append(Employee(
                    employee_id=row["employee_id"],
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    email=row["email"],
                    phone_number=row["phone_number"],
                    hire_date=row["hire_date"],
                    job_id=row["job_id"],
                    salary=row["salary"],
                    manager_id=row["manager_id"],
                    department=__create_department(row)
                ))

    return employees


def fetch_employees() -> List[Employee]:
    """
    Ricerca tutti i dipendenti dell'azienda
    :return: elenco dei dipendenti
    """
    employees = []
    with connect(db_url) as connection:
        with connection.cursor(cursor_factory=dbopts.DictCursor) as cursor:
            cursor.execute(
                f"""
                select
                    e.employee_id,
                    e.first_name,
                    e.last_name,
                    e.email,
                    e.phone_number,
                    e.hire_date,
                    e.job_id,
                    e.salary,
                    e.manager_id,
                    e.department_id,
                    d.department_name,
                    l.location_id,
                    l.city,
                    l.postal_code,
                    l.state_province,
                    l.street_address,
                    l.country_id
                from
                    hr.employees e
                left join hr.departments d on
                    e.department_id = d.department_id
                left join hr.locations l on
                    d.location_id = l.location_id
                """
            )

            # Prendo dal DB tutti i dipendenti di un dipartimento
            for row in cursor.fetchall():
                employees.append(Employee(
                    employee_id=row["employee_id"],
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    email=row["email"],
                    phone_number=row["phone_number"],
                    hire_date=row["hire_date"],
                    job_id=row["job_id"],
                    salary=row["salary"],
                    manager_id=row["manager_id"],
                    department=__create_department(row)
                ))

    return employees
