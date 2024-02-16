from Util.Db_Connection import DBConnection

class Victims(DBConnection):
    def __init__(self, victim_id=None, first_name=None, last_name=None, dob=None, gender=None, address=None, phone_num=None):
        self.victim_id = victim_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender
        self.address = address
        self.phone_num = phone_num

    def create_table(self):
        create_query = '''
            CREATE TABLE IF NOT EXISTS Victims(
            victim_id INT auto_increment primary key,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            dob DATE,
            gender CHAR,
            address VARCHAR(30),
            phone_num VARCHAR(20))
            '''
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(create_query)
        print("Victims table created successfully")

    def insert_into(self):
        # Don't ask for victim_id input since it's auto-incremented
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        self.dob = input("Enter the date of birth: ")
        self.gender = input("Enter the gender: ")
        self.address = input("Enter the address: ")
        self.phone_num = input("Enter the phone number: ")

        insert_query = 'INSERT INTO Victims (first_name, last_name, dob, gender, address, phone_num) VALUES (%s, %s, %s, %s, %s, %s)'
        data = (self.first_name, self.last_name, self.dob, self.gender, self.address, self.phone_num)
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(insert_query, data)
        DBConnection.connection.commit()
        print("Values inserted successfully")


    def update_table(self):
        try:
            self.victim_id = int(input("Enter the victim id to update the values: "))
            self.first_name = input("Enter the first name: ")
            self.last_name = input("Enter the last name: ")
            self.dob = input("Enter the date of birth: ")
            self.gender = input("Enter the gender: ")
            self.address = input("Enter the address: ")
            self.phone_num = input("Enter the phone number: ")

            update_query = 'update Victims set first_name=%s, last_name=%s, dob=%s, gender=%s, address=%s, phone_num=%s where victim_id=%s'
            data = (
            self.first_name, self.last_name, self.dob, self.gender, self.address, self.phone_num, self.victim_id)
            DBConnection.getConnection()
            stmt = DBConnection.connection.cursor()
            stmt.execute(update_query, data)
            DBConnection.connection.commit()
            print("Values updated successfully")
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_table(self):
        self.victim_id = int(input("Enter the victim id to delete values: "))
        delete_query = f'delete from Victims where victim_id={self.victim_id}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(delete_query)
        DBConnection.connection.commit()
        print("Values deleted successfully")

    def select_table(self):
        select_query = 'select * from Victims'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(select_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Values displayed successfully")

