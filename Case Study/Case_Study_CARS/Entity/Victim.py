class Victim:
    def __init__(self, victim_id: int = None, first_name: str = None, last_name: str = None, date_of_birth: str = None,
                 gender: str = None, contact_information: str = None):
        self.__victim_id = victim_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__contact_information = contact_information

    # Getters
    def get_victim_id(self):
        return self.__victim_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_gender(self):
        return self.__gender

    def get_contact_information(self):
        return self.__contact_information

    # Setters
    def set_victim_id(self, victim_id):
        self.__victim_id = victim_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth







