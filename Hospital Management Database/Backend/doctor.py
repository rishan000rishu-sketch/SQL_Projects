
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

    with open(DOCTOR_FILE, 'r') as file:
        reader = csv.DictReader(file)

        print('\n--------DOCTORS--------')

        for row in reader:

            print(
                f'{row['doctor_id']} | '
                f'{row['name']} | '
                f'{row['specialisation']} | '
                f'{row['phone']} | '
            )

def search_doctor():

    doctor_id = input('Enter Doctor_ID: ')

    with open(DOCTOR_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['doctor_id'] == doctor_id:
                
                print(
                f'{row['doctor_id']} | '
                f'{row['name']} | '
                f'{row['specialisation']} | '
                f'{row['phone']} | '
            )
                
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
