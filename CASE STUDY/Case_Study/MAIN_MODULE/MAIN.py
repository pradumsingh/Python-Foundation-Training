from UTIL.DB_Connection import DBConnection
from Entity.Incidents import Incidents
from Entity.Victims import Victims
from Entity.Suspects import Suspects
from Entity.Law_Enforcement_Agencies import Law_Enforcement_Agencies
from Entity.Officers import Officers
from Entity.Evidence import Evidence
from Entity.Reports import Reports
from Data_Access_Objects_Service.Crime_Analysis_Service_Impl import CrimeAnalysisService
from Exception.ExceptionHandling import IncidentNumberNotFoundException

try:
    connObj = DBConnection()
    con = connObj.getConnection()

    while True:
        incidentObj = Incidents()
        victimObj = Victims()
        suspectObj = Suspects()
        lawObj = Law_Enforcement_Agencies()
        officerObj = Officers()
        evidenceObj = Evidence()
        reportObj = Reports()
        serviceImplementObj = CrimeAnalysisService()

        print("Select table to use functionalities")
        print("1.Incidents\n2.Victims\n3.Suspects\n4.Law Enforcement Agencies\n5.Officers\n6.Evidence\n7.Reports\n8.crime analysis service impl\n9.exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            while True:
                print("1.Create Incidents\t2.Insert Incidents\t3.Update Incidents\n4.Delete Incidents\t5.Select Incidents\n6.Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    incidentObj.create_table()
                elif choice == 2:
                    incidentObj.insert_into()
                elif choice == 3:
                    try:
                        incidentObj.update_table()
                    except IncidentNumberNotFoundException as e:
                        print(e)
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
                print("1.create victims\t2.insert victims\t3.update victims\n4.delete victims\t5.select victims\n6.Exit")
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
                print("1.create suspects\t2.insert suspects\t3.update suspects\n4.delete suspects\t5.select suspects\n6.Exit")
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
                    (suspectObj.select_table())
                elif choice == 6:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 4:
            while True:
                print("1.create law agencies\t2.insert law agencies\t3.update law agencies\n4.delete law agencies\t5.select law agencies\n6.Exit")
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
                print("1.create officers\t2.insert officers\t3.update officers\n4.delete officers\t5.select officers\n6.Exit")
                choice = int(input("enter your choice"))
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
                print("1.create evidence\t2.insert evidence\t3.update evidence\n4.delete evidence\t5.select evidence\n6.Exit")
                choice = int(input("enter your choice"))
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
                print("1.create reports\t2.insert reports\t3.update reports\n4.delete reports\t5.select reports\n6.Exit")
                choice = int(input("enter your choice"))
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
                print("1.create Incident\t2.update incident status\t3.get incidents in date range officers\n4.search incidents\t5.generate incident report\n6.create case\t7.get case details\t8.update case details\t9.get all cases\t10.exit")
                choice = int(input("enter your choice"))
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
