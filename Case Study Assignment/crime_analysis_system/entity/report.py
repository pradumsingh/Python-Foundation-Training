# entity/report.py

class Report:
    def __init__(self, report_id, incident_id, reporting_officer, report_date, report_details, status):
        self.report_id = report_id
        self.incident_id = incident_id
        self.reporting_officer = reporting_officer
        self.report_date = report_date
        self.report_details = report_details
        self.status = status

    def __str__(self):
        return f"ReportID: {self.report_id}, IncidentID: {self.incident_id}, ReportingOfficer: {self.reporting_officer}, ReportDate: {self.report_date}, Status: {self.status}"
'''
# Generate instances for testing
if __name__ == "__main__":
    # Create multiple instances of Report for testing
    report1 = Report(report_id=1, incident_id=1, reporting_officer="John Doe", report_date="2024-02-10", report_details="Initial report", status="Draft")
    report2 = Report(report_id=2, incident_id=2, reporting_officer="Jane Smith", report_date="2024-02-11", report_details="Finalized report", status="Finalized")

    # Display report details
    print(report1)
    print(report2)
'''