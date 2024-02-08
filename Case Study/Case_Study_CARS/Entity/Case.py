class Case:
    def __init__(self, case_id: int = None, case_description: str = None, incidents: list = None):
        self.__case_id = case_id
        self.__case_description = case_description
        self.__incidents = incidents

    # Getters
    def get_case_id(self):
        return self.__case_id

    def get_case_description(self):
        return self.__case_description

    def get_incidents(self):
        return self.__incidents

    # Setters
    def set_case_id(self, case_id):
        self.__case_id = case_id

    def set_case_description(self, case_description):
        self.__case_description = case_description

    def set_incidents(self, incidents):
        self.__incidents = incidents