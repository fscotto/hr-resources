class Location:
    def __init__(self, location_id: int, street_address: str, postal_code: str,
                 city: str, state_province: str, country_id: int):
        self.__location_id = location_id
        self.__street_address = street_address
        self.__postal_code = postal_code
        self.__city = city
        self.__state_province = state_province
        self.__country_id = country_id

    @property
    def location_id(self) -> int:
        return self.__location_id

    @property
    def street_address(self) -> str:
        return self.__street_address

    @property
    def postal_code(self) -> str:
        return self.__postal_code

    @property
    def city(self) -> str:
        return self.__city

    @property
    def state_province(self) -> str:
        return self.__state_province

    @property
    def country_id(self) -> int:
        return self.__country_id

    def __json__(self):
        return {
            'location_id': self.__location_id,
            'street_address': self.__street_address,
            'postal_code': self.__postal_code,
            'city': self.__city,
            'state_province': self.__state_province,
            'country_id': self.__country_id
        }

    def __str__(self):
        return f"Location({self.__location_id}, {self.__postal_code}, " \
               f"{self.__street_address}, {self.__city}, {self.__state_province}) "
