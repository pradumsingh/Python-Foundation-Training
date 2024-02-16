from Util.Db_Connection import DBConnection
from Entity.Incidents import Incidents
from Entity.Law_Enforcement_agencies import Law_Enforcement_Agencies
from Entity.Officers import Officers
from Entity.Evidence import Evidence
from Entity.Reports import Reports
from Entity.Suspects import Suspects
from Entity.Victims import Victims
from Data_Access_Objects.Crime_analysis_service_impl import crime_analysis_service_impl
from Exception_Handling.Incident_number_not_found import IncidentNumberNotFoundException

try:
    connObj = DBConnection()
    con = connObj.getConnection()

    victimObj = Victims()
    suspectObj = Suspects()

    while True:
        incidentObj = Incidents()
        lawObj = Law_Enforcement_Agencies()
        officerObj = Officers()
        evidenceObj = Evidence()
        reportObj = Reports()
        serviceImplementObj = crime_analysis_service_impl()

        print("Select table to use functionalities")
        print("1.Incidents\n2.Victims\n3.Suspects\n4.Law Enforcement Agencies\n5.Officers\n6.Evidence\n7.Reports\n8.Crime Analysis Service Impl\n9.Exit")
        ch = int(input("enter your choice:"))

        if ch == 1:
            while True:
                print("1.Create Incident\t2.Insert Incident\t3.Update Incident\n4.Delete Incident\t5.Select Incident\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    try:
                        incidentObj.create_table()
                    except IncidentNumberNotFoundException as e:
                        print("Error:", e.msg)
                    except Exception as e:
                        print("An unexpected error occurred:", e)
                elif choice == 2:
                    victim_first_name = input("Enter victim's first name: ")
                    victim_last_name = input("Enter victim's last name: ")
                    suspect_first_name = input("Enter suspect's first name: ")
                    suspect_last_name = input("Enter suspect's last name: ")
                    incidentObj.insert_into(victim_first_name, victim_last_name, suspect_first_name, suspect_last_name)
                elif choice == 3:
                    incidentObj.update_table()
                elif choice == 4:
                    incidentObj.delete_table()
                elif choice == 5:
                    incidentObj.select_table()
                elif choice == 6:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 2:
            while True:
                print("1.Create Victim\t2.Insert Victim\t3.Update Victim\n4.Delete Victim\t5.Select Victim\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    victimObj.create_table()
                elif choice == 2:
                    victimObj.insert_into()
                elif choice == 3:
                    victimObj.update_table()
                elif choice == 4:
                    victimObj.delete_table()
                elif choice == 5:
                    victimObj.select_table()
                elif choice == 6:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 3:
            while True:
                print("1.Create Suspect\t2.Insert Suspect\t3.Update Suspect\n4.Delete Suspect\t5.Select Suspect\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    suspectObj.create_table()
                elif choice == 2:
                    suspectObj.insert_into()
                elif choice == 3:
                    suspectObj.update_table()
                elif choice == 4:
                    suspectObj.delete_table()
                elif choice == 5:
                    suspectObj.select_table()
                elif choice == 6:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 4:
            while True:
                print("1.Create Law Enforcement Agency\t2.Insert Law Enforcement Agency\t3.Update Law Enforcement Agency\n4.Delete Law Enforcement Agency\t5.Select Law Enforcement Agency\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    lawObj.create_table()
                elif choice == 2:
                    lawObj.insert_into()
                elif choice == 3:
                    lawObj.update_table()
                elif choice == 4:
                    lawObj.delete_table()
                elif choice == 5:
                    lawObj.select_table()
                elif choice == 6:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 5:
            while True:
                print("1.Create Officer\t2.Insert Officer\t3.Update Officer\n4.Delete Officer\t5.Select Officer\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    officerObj.create_table()
                elif choice == 2:
                    officerObj.insert_into()
                elif choice == 3:
                    officerObj.update_table()
                elif choice == 4:
                    officerObj.delete_table()
                elif choice == 5:
                    officerObj.select_table()
                elif choice == 6:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 6:
            while True:
                print("1.Create Evidence\t2.Insert Evidence\t3.Update Evidence\n4.Delete Evidence\t5.Select Evidence\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    evidenceObj.create_table()
                elif choice == 2:
                    evidenceObj.insert_into()
                elif choice == 3:
                    evidenceObj.update_table()
                elif choice == 4:
                    evidenceObj.delete_table()
                elif choice == 5:
                    evidenceObj.select_table()
                elif choice == 6:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 7:
            while True:
                print("1.Create Report\t2.Insert Report\t3.Update Report\n4.Delete Report\t5.Select Report\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    reportObj.create_table()
                elif choice == 2:
                    reportObj.insert_into()
                elif choice == 3:
                    reportObj.update_table()
                elif choice == 4:
                    reportObj.delete_table()
                elif choice == 5:
                    reportObj.select_table()
                elif choice == 6:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 8:
            while True:
                print("1.Create Incident\t2.Update Incident Status\t3.Get Incidents in Date Range\n4.Search Incidents\n5.Generate Incident Report\n6.Create Case\n7.Get Case Details\n8.Update Case Details\n9.Get All Cases\n10.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    serviceImplementObj.createIncident()
                elif choice == 2:
                    serviceImplementObj.updateIncidentStatus()
                elif choice == 3:
                    serviceImplementObj.getIncidentsInDateRange()
                elif choice == 4:
                    serviceImplementObj.searchIncidents()
                elif choice == 5:
                    serviceImplementObj.generateIncidentReport()
                elif choice == 6:
                    serviceImplementObj.createCase()
                elif choice == 7:
                    serviceImplementObj.getCaseDetails()
                elif choice == 8:
                    serviceImplementObj.updateCaseDetails()
                elif choice == 9:
                    serviceImplementObj.getAllCases()
                elif choice == 10:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 9:
            print("Exited successfully")
            break

        else:
            print("Wrong choice")

except Exception as e:
    print(f"Unhandled error: {e}")

finally:
    DBConnection.connection.close()
    print("Database connection closed")
