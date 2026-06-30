
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

    cursor.execute('SELECT * FROM bills')

    bills = cursor.fetchall()

    if not bills:
        print('Bills Not Found !')
        return

    print('\n------BILL RECORDS------')

    for bill in bills:

        print(f'Bill ID      : {bill[0]} | ')
        print(f'Patient ID   : {bill[1]} | ')
        print(f'Total Amount : {bill[5]}')
        print('-' * 25)

def search_bill():

    bill_id = input('Enter Bill_ID: ')

    cursor.execute('SELECT * FROM bills WHERE bill_id = %s', (bill_id,))

    bill = cursor.fetchone()

    if bill:

                print('\n========Bill Found========')
                print(f'Bill_ID          : {bill[0]}')
                print(f'Patient_ID       : {bill[1]}')
                print(f'Consultation Fee : {bill[2]}')
                print(f'Medicine Charge  : {bill[3]}')
                print(f'Lab Charge       : {bill[4]}')
                print(f'Total Amount     : {bill[5]}')
                return
            
    print('\nBill Not Found.')
