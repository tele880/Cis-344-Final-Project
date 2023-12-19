from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep
from portalDatabase import Database
import cgi
import os

class HospitalPortalHandler(BaseHTTPRequestHandler):

    def __init__(self, *args):
        try:
            self.database = Database(port=3306) 
        except Error as e:
            print("Error while connecting to MySQL:", e)
            self.database = None
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_GET(self):
        try:
            if self.path == '/':
                data = []
                records = self.database.getAllPatients()
                print(records)
                data = records
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h2>All Patients</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Patient ID </th>\
                                        <th> Patient Name</th>\
                                        <th> Age </th>\
                                        <th> Admission Date </th>\
                                        <th> Discharge Date </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return

            if self.path == '/addPatient':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h2>Add New Patient</h2>")

                self.wfile.write(b"<form action='/addPatient' method='post'>")
                self.wfile.write(b"<form action='/addPatient' method='post'>"
                  b"<label for='patient_name'>Patient Name:</label>"
                  b"<input type='text' id='patient_name' name='patient_name'/><br><br>"
                  b"<label for='patient_age'>Age:</label>"
                  b"<input type='number' id='patient_age' name='patient_age'><br><br>"
                  b"<label for='admission_date'>Admission Date:</label>"
                  b"<input type='date' id='admission_date' name='admission_date'><br><br>"
                  b"<label for='discharge_date'>Discharge Date:</label>"
                  b"<input type='date' id='discharge_date' name='discharge_date'><br><br>"
                  b"<input type='submit' value='Submit'>"
                  b"</form>")


                self.wfile.write(b"</center></body></html>")
                return
            if self.path == '/addDoctor':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h2>Add New Doctor</h2>")

                self.wfile.write(b"<form action='/addDoctor' method='post'>")
                self.wfile.write(b"<form action='/addDoctor' method='post'>"
                  b"<label for='doctor_name'>Doctor's Name:</label>"
                  b"<input type='text' id='doctor_name' name='doctor_name'/><br><br>"
                  b"<label for='specialization'>Doctor's Specialization:</label>"
                  b"<input type='text' id='specialization' name='specialization'/><br><br>"
                  b"<input type='submit' value='Submit'>"
                  b"</form>")


                self.wfile.write(b"</center></body></html>")
                return

            if self.path == '/scheduleAppointment':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h2>Schedule Appointment</h2>")

                self.wfile.write(b"<form action='/scheduleAppointment' method='post'>"
                  b"<label for='patient_id'>Patient ID:</label>"
                  b"<input type='number' id='patient_id' name='patient_id'><br><br>"
                  b"<label for='doctor_id'>Doctor ID:</label>"
                  b"<input type='number' id='doctor_id' name='doctor_id'><br><br>"
                  b"<label for='appointment_date'>Appointment Date:</label>"
                  b"<input type='date' id='appointment_date' name='appointment_date'><br><br>"
                  b"<label for='appointment_time'>Appointment Time:</label>"
                  b"<input type='time' id='appointment_time' name='appointment_time'><br><br>"
                  b"<input type='submit' value='Submit'>"
                  b"</form>")


                self.wfile.write(b"</center></body></html>")
                return

            if self.path == '/viewAppointments':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                records = self.database.viewAppointments()

                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h2>View Appointments</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Appointment ID </th>\
                                        <th> Patient ID</th>\
                                        <th> Doctor ID </th>\
                                        <th> Appointment Date </th>\
                                        <th> Appointment Time </th></tr>")
                for row in records:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return

            if self.path == '/dischargePatient':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h2>Discharge Patient</h2>")

                self.wfile.write(b"<form action='/dischargePatient' method='post'>"
                  b"<label for='patient_id'>Patient ID:</label>"
                  b"<input type='number' id='patient_id' name='patient_id'><br><br>"
                  b"<input type='submit' value='Submit'>"
                  b"</form>")


                self.wfile.write(b"</center></body></html>")
                return
            if self.path == '/viewPatient':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                records = self.database.getAllPatients()
                print(records)

                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h2>View Patient</h2>")
                self.wfile.write(b"<table border=2> \
                    <tr><th> Patient ID </th>\
                    <th> Patient</th>\
                    <th> Patient Age</th>\
                    <th> Admission Date </th>\
                    <th> Discharge Date</th></tr>")

                for row in records:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())  
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())  
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return


            if self.path == '/viewDoctors':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                records = self.database.getAllDoctors()

                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h2>View Doctors</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Doctor ID </th>\
                                        <th> Doctor Name</th>\
                                        <th> Specialization </th></tr>")
                for row in records:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return

            if self.path == '/viewRecords':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                records = self.database.viewRecords()

                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h2>View Records</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Doctor ID </th>\
                                        <th> Doctor Name</th>\
                                        <th> Specialization </th>\
                                        <th> Appointment ID </th>\
                                        <th> Appointment Date </th>\
                                        <th> Appointment Time </th>\
                                        <th> Patient ID </th>\
                                        <th> Patient Name </th>\
                                        <th> Age </th>\
                                        <th> Admission Date </th>\
                                        <th> Discharge Date </th></tr>")


                for row in records:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[5]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[6]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[7]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[8]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[9]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[10]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

        return

    def do_POST(self):
        try:
            if self.path == '/addPatient':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                patient_name = form.getvalue("patient_name")
                age = int(form.getvalue("patient_age"))
                admission_date = form.getvalue("admission_date")
                discharge_date = form.getvalue("discharge_date")
                
                self.database.addPatient(patient_name, age, admission_date, discharge_date)

                print("Patient added:", patient_name, age, admission_date, discharge_date)

                self.wfile.write(b"<html><head><title> Hospital Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewPatients'>View Patients</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h3>Patient has been added</h3>")
                self.wfile.write(b"<div><a href='/addPatient'>Add Another Patient</a></div>")
                self.wfile.write(b"</center></body></html>")
            if self.path == '/addDoctor':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                doctor_name = form.getvalue("doctor_name")
                specialization = form.getvalue("specialization")
                
                self.database.addDoctor(doctor_name, specialization)

                print("Doctor added:", doctor_name, specialization)

                self.wfile.write(b"<html><head><title> Hospital Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h3>Doctor has been added</h3>")
                self.wfile.write(b"<div><a href='/addDoctor'>Add Another Doctor</a></div>")
                self.wfile.write(b"</center></body></html>")

            if self.path == '/scheduleAppointment':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                patient_id = int(form.getvalue("patient_id"))
                doctor_id = int(form.getvalue("doctor_id"))
                appointment_date = form.getvalue("appointment_date")
                appointment_time = form.getvalue("appointment_time")

                self.database.scheduleAppointment(patient_id, doctor_id, appointment_date, appointment_time)

                print("Appointment scheduled for Patient ID:", patient_id, "with Doctor ID:", doctor_id,
                      "on", appointment_date, "at", appointment_time)

                self.wfile.write(b"<html><head><title> Hospital Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h3>Appointment scheduled</h3>")
                self.wfile.write(b"<div><a href='/scheduleAppointment'>Schedule Another Appointment</a></div>")
                self.wfile.write(b"</center></body></html>")


            if self.path == '/viewAppointments':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                records = self.database.viewAppointments()

                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h2>View Appointments</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Appointment ID </th>\
                                        <th> Patient ID</th>\
                                        <th> Doctor ID </th>\
                                        <th> Appointment Date </th>\
                                        <th> Appointment Time </th></tr>")
                for row in records:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return

            if self.path == '/dischargePatient':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h2>Discharge Patient</h2>")

                self.wfile.write(b"<form action='/dischargePatient' method='post'>"
                  b"<label for='patient_id'>Patient ID:</label>"
                  b"<input type='number' id='patient_id' name='patient_id'><br><br>"
                  b"<input type='submit' value='Submit'>"
                  b"</form>")


                self.wfile.write(b"</center></body></html>")
                return
            if self.path == '/viewPatient':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                records = self.database.getAllPatients()

                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h2>View Patient</h2>")
                self.wfile.write(b"<table border=2> \
                    <tr><th> Patient ID </th>\
                    <th> Patient</th>\
                    <th> Patient Age</th>\
                    <th> Admission Date </th>\
                    <th> Discharge Date</th></tr>")

                for row in records:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())  
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())  
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return


            if self.path == '/viewDoctors':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                records = self.database.getAllDoctors()

                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h2>View Doctors</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Doctor ID </th>\
                                        <th> Doctor Name</th>\
                                        <th> Specialization </th></tr>")
                for row in records:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return

            if self.path == '/viewRecords':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                records = self.database.viewRecords()

                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h2>View Records</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Doctor ID </th>\
                                        <th> Doctor Name</th>\
                                        <th> Specialization </th>\
                                        <th> Appointment ID </th>\
                                        <th> Appointment Date </th>\
                                        <th> Appointment Time </th>\
                                        <th> Patient ID </th>\
                                        <th> Patient Name </th>\
                                        <th> Age </th>\
                                        <th> Admission Date </th>\
                                        <th> Discharge Date </th></tr>")

                for row in records:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[5]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[6]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[7]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[8]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[9]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[10]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return

            if self.path == '/dischargePatient':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                patient_id = int(form.getvalue("patient_id"))

                self.database.dischargePatient(patient_id)

                print("Patient with ID:", patient_id, "has been discharged.")

                self.wfile.write(b"<html><head><title> Hospital Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                 <a href='/addDoctor'>Add Doctor</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>|\
                                  <a href='/viewPatient'>View Patient</a>|\
                                  <a href='/viewDoctors'>View Doctors</a>|\
                                  <a href='/viewRecords'>View Records</a></div>")
                self.wfile.write(b"<hr><h3>Patient has been discharged</h3>")
                self.wfile.write(b"<div><a href='/dischargePatient'>Discharge Another Patient</a></div>")
                self.wfile.write(b"</center></body></html>")

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

        return


def run():
    port = 8000
    print('Starting server on port', port)

    server_address = ('', port)
    httpd = HTTPServer(server_address, HospitalPortalHandler)
    print('Server running...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()



