from models.location import Location


class Department:
    def __init__(self, department_id: int, name: str, location: Location):
        self.__department_id = department_id
        self.__name = name
        self.__location = location

    @property
    def department_id(self) -> int:
        return self.__department_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def location_id(self) -> Location:
        return self.__location

    def to_json(self):
        return {
            'department_id': self.__department_id,
            'name': self.__name,
            'location': self.__location.to_json() if self.__location is not None else None
        }

    def __str__(self):
        return f"Department({self.__department_id}, {self.__name}, {self.__location})"
