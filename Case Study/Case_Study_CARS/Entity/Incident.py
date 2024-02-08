class Incident:
    def __init__(self, incident_id: int = None, incident_type: str = None, incident_date: str = None,
                 location: str = None, description: str = None, status: str = None, victim_id: int = None,
                 suspect_id: int = None):
        self.__incident_id = incident_id
        self.__incident_type = incident_type
        self.__incident_date = incident_date
        self.__location = location
        self.__description = description
        self.__status = status
        self.__victim_id = victim_id
        self.__suspect_id = suspect_id

    # Getters
    def get_incident_id(self):
        return self.__incident_id

    def get_incident_type(self):
        return self.__incident_type

    def get_incident_date(self):
        return self.__incident_date

    def get_location(self):
        return self.__location

    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status

    def get_victim_id(self):
        return self.__victim_id



    def get_suspect_id(self):
        return self.__suspect_id

    # Setters
    def set_incident_id(self, incident_id):
        self.__incident_id = incident_id

    def set_incident_type(self, incident_type):
        self.__incident_type = incident_type

    def set_incident_date(self, incident_date):
        self.__incident_date = incident_date

    def set_location(self, location):
        self.__location = location

    def set_description(self, description):
        self.__description = description

    def set_status(self, status):
        self.__status = status

    def set_victim_id(self, victim_id):
        self.__victim_id = victim_id

    def set_suspect_id(self, suspect_id):
        self.__suspect_id = suspect_id