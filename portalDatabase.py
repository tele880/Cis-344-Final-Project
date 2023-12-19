import mysql.connector
from mysql.connector import Error

class Database():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="hospital_portal",
                 user='root',
                 password='Tubon@74'):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password)
            
            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)

    def addPatient(self, patient_name, age, admission_date, discharge_date):
        ''' Method to insert a new patient into the patients table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO patients (patient_name, age, admission_date, discharge_date) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (patient_name, age, admission_date, discharge_date))
            self.connection.commit()
            return
    def addDoctor(self, doctor_name, specialization):
        ''' Method to insert a new doctor into the Doctor table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO doctors (doctor_name, specialization) VALUES (%s, %s)"
            self.cursor.execute(query, (doctor_name, specialization))
            self.connection.commit()
            return

    def getAllPatients(self):
        ''' Method to get all patients from the patients table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM patients"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return

    def scheduleAppointment(self, patient_id, doctor_id, appointment_date, appointment_time):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (patient_id, doctor_id, appointment_date, appointment_time))
            self.connection.commit()
    def viewAppointments(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM appointments"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def dischargePatient(self, patient_id):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "UPDATE patients SET discharge_date = CURRENT_DATE WHERE patient_id = %s"
            self.cursor.execute(query, (patient_id,))
            self.connection.commit()
    def createDoctorsTable(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "CREATE TABLE IF NOT EXISTS doctors (doctor_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, doctor_name VARCHAR(45) NOT NULL, specialization VARCHAR(45) NOT NULL)"
            self.cursor.execute(query)
            self.connection.commit()

    def getAllPatients(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM patients"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def getAllDoctors(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM doctors"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def createRecordsView(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "CREATE VIEW IF NOT EXISTS doctor_appointment_patient AS SELECT d.doctor_id, d.doctor_name, d.specialization, a.appointment_id, a.appointment_date, a.appointment_time, p.patient_id, p.patient_name, p.age, p.admission_date, p.discharge_date FROM doctors d JOIN appointments a ON d.doctor_id = a.doctor_id JOIN patients p ON a.patient_id = p.patient_id"
            self.cursor.execute(query)
            self.connection.commit()

    def viewRecords(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM doctor_appointment_patient"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records


