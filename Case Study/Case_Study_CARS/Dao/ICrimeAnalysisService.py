from abc import ABC, abstractmethod
from typing import List, Collection
from Entity.Case import Case


class ICrimeAnalysisService(ABC):

    @abstractmethod
    def create_incident(self, incident) -> bool:
        pass

    @abstractmethod
    def update_incident_status(self, status, incident_id: int) -> bool:
        pass

    @abstractmethod
    def get_incidents_in_date_range(self, start_date: str, end_date: str) -> Collection:
        pass

    @abstractmethod
    def search_incidents(self, criteria) -> Collection:
        pass

    @abstractmethod
    def generate_incident_report(self, incident):
        pass

    @abstractmethod
    def create_case(self, case_description: str, incidents: Collection) -> Case:
        pass

    @abstractmethod
    def get_case_details(self, case_id: int) -> Case:
        pass

    @abstractmethod
    def update_case_details(self, case: Case) -> bool:
        pass

    @abstractmethod
    def get_all_cases(self) -> List[Case]:
        pass
