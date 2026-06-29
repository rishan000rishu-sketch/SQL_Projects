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

    with open(PATIENT_FILE, 'r',) as file:
        reader = csv.DictReader(file)

        print('\n------PATIENTS------')

        for row in reader:
            
            print(
                f'{row['patient_id']} | '
                f'{row['name']} | '
                f'{row['age']} | '
                f'{row['phone']} | '
                f'{row['phone']} | '
            )

def search_patients():

    patient_id = input('Enter Patient_ID: ')

    with open(PATIENT_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['patient_id'] == patient_id:

                print('\nPatient Found !')
                print(row)


def delete_patients():

    patient_id  = input('Enter Patient_ID: ')

    rows = []
    found = False

    with open(PATIENT_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['patient_id'] == patient_id:
                found = True
            else:
                rows.append(row)

    if not found:
        print('Patient Not Found !')
        return
    
    with open(PATIENT_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)

        writer.writeheader()
        writer.writerows(rows)

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
