from patient import *
from doctor import *
from appoinment import *
from billing import *

def patient_menu():

    while True:
        print('\n==============PATIENT MENU===============')

        print('''
1. Add Patients
2. View Patients
3. Search Patients
4. Update Patients
5. Delete Patients
6. Back
              ''')
        
        choice = input('Enter Your Choice: ')

        if choice == '1':
            add_patient()

        elif choice == '2':
            view_patients()

        elif choice == '3':
            search_patients()

        elif choice == '4':
            view_patients()

        elif choice == '5':
            delete_patients()

        elif choice == '6':
            break

        else:
            print('Invalid Choice !')

def doctor_menu():

      while True:
        print('\n==============PATIENT MENU===============')

        print('''
1. Add Doctors
2. View Doctors
3. Search Doctors
4. Update Doctors
5. Delete Doctors
6. Back
              ''')
        
        choice = input('Enter Your Choice: ')

        if choice == "1":
            add_doctor()

        elif choice == "2":
            view_doctors()

        elif choice == "3":
            search_doctor()

        elif choice == "4":
            update_doctor()

        elif choice == "5":
            delete_doctor()

        elif choice == "6":
            break

        else:
            print("Invalid choice.")

def appoinment_menu():

     while True:

        print("\n====== APPOINTMENT MENU ======")

        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Search Appointment")
        print("4. Cancel Appointment")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            book_appoinment()

        elif choice == "2":
            view_appoinments()

        elif choice == "3":
            search_appoinments()

        elif choice == "4":
            cancel_appoinments()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")

def billing_menu():

    while True:

        print("\n========== BILLING MENU ==========")

        print("1. Generate Bill")
        print("2. View Bills")
        print("3. Search Bill")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            generate_bill()

        elif choice == "2":
            view_bills()

        elif choice == "3":
            search_bill()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")

def main():

    while True:

        print("\n")
        print("=" * 45)
        print("     HOSPITAL MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Appointment Management")
        print("4. Billing Management")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            patient_menu()

        elif choice == "2":
            doctor_menu()

        elif choice == "3":
            appoinment_menu()

        elif choice == "4":
            billing_menu()

        elif choice == "5":

            print("\nThank you for using HMS.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
