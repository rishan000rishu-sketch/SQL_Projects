from connection import cursor, conn

def patient_exists(patient_id):

    query = 'SELECT * FROM patients WHERE patient_id = %s'

    cursor.execute(query, (patient_id,))

    result = cursor.fetchone()

    if result:
        return True
    
    return False

def add_patient():
    patient_id  = input('Enter Patient_ID: ')

    if patient_exists(patient_id):
        print('Patient Already Exists !')
        return
    
    name = input('Enter Patient Name: ')
    age = int(input('Enter Patient Age: '))
    gender  = input('Enter Gender (male/female/other): ')
    phone = int(input('Enter Phone No: '))

    query =  '''INSERT INTO patients (patient_id, name, age, gender, phone)
                VALUES (%s, %s, %s, %s, %s)
                '''
    values = (
        patient_id,
        name,
        age,
        gender,
        phone
    )

    cursor.execute(query, values)

    conn.commit()

    print('Patient Added Successfully.')

def view_patients():

    query = 'SELECT * FROM patients'

    cursor.execute(query)

    patients = cursor.fetchall()

    if not patients:
        print('Patients Not Found !')
        return

    print('\n------PATIENT LIST------\n')

    for patient in patients:
            
        print(f"Patient ID : {patient[0]}")
        print(f"Name       : {patient[1]}")
        print(f"Age        : {patient[2]}")
        print(f"Gender     : {patient[3]}")
        print(f"Phone      : {patient[4]}")
        print("-" * 35)

def search_patients():

    patient_id = input('Enter Patient_ID: ')

    query = '''
            SELECT * FROM patients
            WHERE patient_id = %s
            '''
    
    cursor.execute(query, (patient_id,))

    patient = cursor.fetchone()

    if patient:

        print("\n===== Patient Found =====\n")
        print(f"Patient ID : {patient[0]}")
        print(f"Name       : {patient[1]}")
        print(f"Age        : {patient[2]}")
        print(f"Gender     : {patient[3]}")
        print(f"Phone      : {patient[4]}")

    else:
        print("Patient Not Found!")

def delete_patients():

    patient_id  = input('Enter Patient_ID: ')

    cursor.execute(
        'SELECT * FROM patients WHERE patient_id = %s',
        (patient_id,)
    )

    patient = cursor.fetchone()

    if not patient:
        print('Patient Not Found !')
        return
    
    cursor.execute(
        'DELETE FROM patients WHERE patient_id = %s',
        (patient_id,)
    )

    conn.commit()

    print('\nPatient Deleted Successfully !')

def update_patients():

    patient_id = input('Enter Patient_ID: ')

    rows = []
    found = False

    with open(PATIENT_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['patient_id'] == patient_id:
                found = True

                row['name'] = input('Enter New Name: ')
                row['age'] = int(input('Enter New Age: '))
                row['gender'] = input('Enter New Gender: ')
                row['phone'] = int(input('Enter New phone: '))

            rows.append(row)

    if not found:
        print('\nPatient Not Found !')
        return
    
    with open(PATIENT_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)

        writer.writeheader()
        writer.writerows(rows)

    print('\nPatient Updated Successfully.')
