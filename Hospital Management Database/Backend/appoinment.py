
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

    print('\n----------APPOINMENTS-----------')

    with open(APPOINMENT_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:

            print(
                f'{row['appoinment_id']} | ',
                f'{row['patient_id']} | ',
                f'{row['doctor_id']} | ',
                f'{row['appoinment_date']}'
            )

def search_appoinments():

    appoinment_id = input('Enter Appoinment_ID: ')

    with open(APPOINMENT_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['appoinment_id'] == appoinment_id:

                print(f'Apponment_ID : {row['appoinment_id']}')
                print(f'Patient_ID   : {row['patient_id']}')
                print(f'Doctor_ID    : {row['doctor_id']}')
                print(f'Date         : {row['appoinment_date']}')
                return
    
    print('Appoinment Not Found !')

def cancel_appoinments():

    appoinment_id = input('Enter Appoinment_ID: ')

    rows = []
    found = False

    with open(APPOINMENT_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['appoinment_id'] == appoinment_id:
                found = True
            else:
                rows.append(row)

    if not found:
        print('Appoinment Not Found !')
        return
    
    with open(APPOINMENT_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)

        writer.writeheader()
        writer.writerows(rows)

    print('Appoinment Cancelled Successfully.')
    