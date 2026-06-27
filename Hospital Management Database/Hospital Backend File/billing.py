import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR  = os.path.join(BASE_DIR, 'data')
PATIENT_FILE = os.path.join(BASE_DIR, 'data/patient.csv')
BILL_FILE = os.path.join(BASE_DIR, 'data/bills.csv')

HEADER = [
    "bill_id",
    "patient_id",
    "consultation_fee",
    "medicine_charge",
    "lab_charge",
    "total_amount"
]

def create_bill_file():

    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(BILL_FILE):
        with open(BILL_FILE, 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(HEADER)

def patient_exists(patient_id):

    with open(PATIENT_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['patient_id'] == patient_id:
                return True
            
    return False

def generate_bill():

    bill_id = input('Enter Bill_ID: ')

    patient_id = input('Enter Patient_ID: ')
    if not patient_exists(patient_id):
        print('Patient Not Found !')
        return

    consultation_fee = float(input('Enter Consultation Fee: '))

    medicine_charge = float(input('Enter Medicine Charge: '))

    lab_charge = float(input('Enter Lab Charge: '))

    total_amount = (consultation_fee + medicine_charge + lab_charge)

    with open(BILL_FILE, 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([
            bill_id,
            patient_id,
            consultation_fee,
            medicine_charge,
            lab_charge,
            total_amount
        ])
    print('\nBill Generated Successfully.')
    print_bill(
        bill_id,
        patient_id,
        consultation_fee,
        medicine_charge,
        lab_charge,
        total_amount
    )

def print_bill(bill_id,patient_id,consultation_fee,medicine_charge,lab_charge,total_amount):

    print('\n==========BILL==========')

    print(f"Bill ID           : {bill_id}")
    print(f"Patient ID        : {patient_id}")
    print(f"Consultation Fee  : {consultation_fee}")
    print(f"Medicine Charge   : {medicine_charge}")
    print(f"Lab Charge        : {lab_charge}")

    print("---------------------------")

    print(f'Total Amount      : {total_amount}')
    print('============================')

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
