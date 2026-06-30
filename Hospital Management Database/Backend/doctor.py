
from connection import conn, cursor
           
def doctor_exists(doctor_id):

    query = 'SELECT * FROM doctors WHERE doctor_id = %s'

    cursor.execute(query, (doctor_id,))

    doctor = cursor.fetchone()

    if doctor:
        return True
    
    return False

def add_doctor():

    doctor_id = input('Enter Doctor_ID: ')

    if doctor_exists(doctor_id):
        print('\nDoctor_ID Already Existed !')
        return
    
    name = input('Enter Doctor Name: ')
    specialisation = input('Enter Specialisation: ')
    phone = int(input('Enter Phone No: '))

    query = '''INSERT INTO doctors (doctor_id, name,specialisation, phone)
               VALUES (%s, %s, %s, %s)
            '''
    
    values = (
        doctor_id,
        name,
        specialisation,
        phone
    )

    cursor.execute(query, values)

    conn.commit()

    print('Doctor Added Successfully.')

def view_doctors():

    cursor.execute('SELECT * FROM doctors')

    doctors = cursor.fetchall()

    if not doctors:
        print('Doctor Not Found !')
        return

    print('\n--------DOCTORS--------')

    for doctor in doctors:

        print(f'Doctor ID      : {doctor[0]}')
        print(f'Name           : {doctor[1]}')
        print(f'Specialisation : {doctor[2]}')
        print(f'Phone          : {doctor[3]}')
        print('-'*30)

def search_doctor():

    doctor_id = input('Enter Doctor_ID: ')

    cursor.execute('SELECT * FROM doctors WHERE doctor_id = %s', (doctor_id,))

    doctor = cursor.fetchone()

    if not doctor:
        print('Doctor Not Found !')
        return
    
    print(f'\nDoctor ID      : {doctor[0]}')
    print(f'Name           : {doctor[1]}')
    print(f'Specialisation : {doctor[2]}')
    print(f'Phone          : {doctor[3]}')

def update_doctor():

    doctor_id = input('Enter Doctor_ID: ')

    rows = []
    found =  False

    with open(DOCTOR_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['doctor_id'] == doctor_id:
                found = True

                row['name'] = input('Enter New Name: ')
                row['specialisation'] = input('Enter New Specialisation: ')
                row['phone'] = input('Enter New Phone: ')

            rows.append(row)

    if not found:
        print('\nDoctor Not Found !')

    with open(DOCTOR_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)

        writer.writeheader()
        writer.writerows(rows)

    print('Doctor Updated Successfully.')

def delete_doctor():

    doctor_id = input('Enter Doctor_ID: ')

    rows = []
    found = False

    with open(DOCTOR_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['doctor_id'] == doctor_id:
                found = True
            else:
                rows.append(row)

    if not found:
        print('\nDoctor Not Found !')

    with open(DOCTOR_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)

        writer.writeheader()
        writer.writerows(rows)

    print('\nDoctor Deleted Successfully !')
