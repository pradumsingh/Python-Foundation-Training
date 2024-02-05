# icrime_analysis_service.py

from abc import ABC, abstractmethod
from typing import Collection
from entity.report import Report
from entity.case import Case

class ICrimeAnalysisService(ABC):

    @abstractmethod
    def create_incident(self, incident) -> bool:
        pass

    @abstractmethod
    def update_incident_status(self, status, incident_id) -> bool:
        pass

    @abstractmethod
    def get_incidents_in_date_range(self, start_date, end_date) -> Collection:
        pass

    @abstractmethod
    def search_incidents(self, criteria) -> Collection:
        pass

    @abstractmethod
    def generate_incident_report(self, incident) -> Report:
        pass

    @abstractmethod
    def create_case(self, case_description, incidents) -> Case:
        pass

    @abstractmethod
    def get_case_details(self, case_id) -> Case:
        pass

    @abstractmethod
    def update_case_details(self, case) -> bool:
        pass

    @abstractmethod
    def get_all_cases(self) -> Collection:
        pass

    @abstractmethod
    def search_incidents(self, criteria) -> Collection:
        pass

    @abstractmethod
    def generate_incident_report(self, incident) -> Report:
        pass

    @abstractmethod
    def create_case(self, case_description, incidents) -> Case:
        pass

    @abstractmethod
    def get_case_details(self, case_id) -> Case:
        pass