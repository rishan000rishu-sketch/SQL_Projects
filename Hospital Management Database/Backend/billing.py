
from connection import conn, cursor
from patient import patient_exists

def bill_exists(bill_id):

    query = 'SELECT * FROM bills WHERE bill_id = %s'

    cursor.execute(query, (bill_id,))

    result = cursor.fetchone()

    if result:
        return True
    
    return False

def generate_bill():

    bill_id = input('Enter Bill_ID: ')

    if bill_exists(bill_id):
        print('Bill ID Already Taken !')
        return

    patient_id = input('Enter Patient_ID: ')
    if not patient_exists(patient_id):
        print('Patient Not Found !')
        return

    consultation_fee = float(input('Enter Consultation Fee: '))

    medicine_charge = float(input('Enter Medicine Charge: '))

    lab_charge = float(input('Enter Lab Charge: '))

    total_amount = (consultation_fee + medicine_charge + lab_charge)

    query = '''INSERT INTO bills (bill_id, patient_id, consultation_fee, medicine_charge, lab_charge, total_amount)
               VALUES(%s, %s, %s, %s, %s, %s) 
                '''

    values =(
            bill_id,
            patient_id,
            consultation_fee,
            medicine_charge,
            lab_charge,
            total_amount
        )
    
    cursor.execute(query, values)

    conn.commit()

    print_bill(bill_id)

    print('\nBill Generated Successfully.')

def print_bill(bill_id):

    cursor.execute('SELECT * FROM bills WHERE bill_id = %s',(bill_id,))

    bill = cursor.fetchone()

    if not bill:
        print('Bill Not Found !')
        return

    print('\n==========BILL==========')

    print(f"Bill ID           : {bill[0]}")
    print(f"Patient ID        : {bill[1]}")
    print(f"Consultation Fee  : {bill[2]}")
    print(f"Medicine Charge   : {bill[3]}")
    print(f"Lab Charge        : {bill[4]}")

    print("---------------------------")

    print(f'Total Amount      : {bill[5]}')
    print('============================')

    conn.commit()

def view_bills():

    print('\n------BILL RECORDS------')

    with open(BILL_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            
            print(f'{row['bill_id']} | ')
            print(f'{row['patient_id']} | ')
            print(f'{row['total_amount']}')

def search_bill():

    bill_id = input('Enter Bill_ID: ')

    with open(BILL_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['bill_id'] == bill_id:
                print('\nBill found.\n')

                print(f'Bill_ID          : {row['bill_id']}')
                print(f'Patient_ID       : {row['patient_id']}')
                print(f'Consultation Fee : {row['consultation_fee']}')
                print(f'Medicine Charge  : {row['medicine_charge']}')
                print(f'Lab Charge       : {row['lab_charge']}')
                print(f'Total Amount     : {row['total_amount']}')
                return
            
    print('\nBill Not Found.')
