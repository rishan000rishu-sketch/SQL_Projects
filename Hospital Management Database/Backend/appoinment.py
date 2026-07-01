
from connection import cursor, conn
from patient import patient_exists
from doctor import doctor_exists


def appoinment_exists(appoinment_id):

    query = 'SELECT * FROM appointments WHERE appoinment_id = %s'

    cursor.execute(query, (appoinment_id,))

    result = cursor.fetchone()

    if result:
        return True
            
    return False

def book_appoinment():

    appoinment_id = input('Enter Appoinment_ID: ')

    if appoinment_exists(appoinment_id):
        print('Appoinment_ID Already Exists !')
        return
    
    patient_id = input('Enter Patient_ID: ')

    if not patient_exists(patient_id):
        print('Patient_ID Not Found !')
        return
    
    doctor_id = input('Enter Doctor_ID: ')

    if not doctor_exists(doctor_id):
        print('Doctor_ID Not Found !')
        return
    
    appoinment_date = input('Enter Appoinment Date (yyyy-mm-dd): ')

    query = '''INSERT INTO appointments (appoinment_id, patient_id, doctor_id, appoinment_date)
               VALUES(%s, %s, %s, %s)
            '''
    
    values = (
        appoinment_id,
        patient_id,
        doctor_id,
        appoinment_date
    )

    cursor.execute(query, values)

    conn.commit()

    print('\nAppoinment Booked Successfully.')

def view_appoinments():

    cursor.execute('SELECT * FROM appointments')

    result = cursor.fetchall()

    if result:

        print('\n----------APPOINMENTS-----------\n')

        for row in result:

            print(f'Appointment ID   : {row[0]}'),
            print(f'Patient ID       : {row[1]}'),
            print(f'Doctor ID        : {row[2]}'),
            print(f'Appointment Date : {row[3]}'),
            print('-' *30)

    else:
        print('Appoinments Not Found !')
            
def search_appoinments():

    appoinment_id = input('Enter Appoinment_ID: ')

    query = 'SELECT * FROM appointments WHERE appoinment_id = %s'

    cursor.execute(query, (appoinment_id,))

    row = cursor.fetchone()

    if row:
                
        print(f'\n-------Appointment-------\n')

        print(f'Appointment_ID   : {row[0]}'),
        print(f'Patient_ID       : {row[1]}'),
        print(f'Doctor_ID        : {row[2]}'),
        print(f'Appointment_Date : {row[3]}')
        return
    
    print('Appoinment Not Found !')

def cancel_appoinments():

    appoinment_id = input('Enter Appoinment_ID: ')

    cursor.execute('SELECT * FROM appointments WHERE appoinment_id = %s', (appoinment_id,))

    result = cursor.fetchone()

    if not result:
        print('Appointment Not Found !')
        return
    
    cursor.execute('DELETE FROM appointments WHERE appoinment_id = %s', (appoinment_id,))

    conn.commit()

    print('Appoinment Cancelled Successfully.')
