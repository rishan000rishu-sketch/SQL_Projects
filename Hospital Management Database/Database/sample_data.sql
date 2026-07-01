USE hospital_db;

-- Doctors --

INSERT INTO doctors
(doctor_name, specialization, phone)

VALUES
('Dr. John', 'Cardiology', '9876543210'),
('Dr. Alice', 'Neurology', '9876543211'),
('Dr. David', 'Orthopedics', '9876543212');

-- Patients --

INSERT INTO patients
(patient_name, age, gender, phone)

VALUES
('Rahul', 25, 'Male', '9991112222'),
('Anu', 30, 'Female', '9991113333'),
('Arjun', 42, 'Male', '9991114444');

-- Appointments --

INSERT INTO appointments
(appoinment_id, patient_id, doctor_id, appointment_date)

VALUES
('A001', 'P001', 'D001', 2026-06-30),
('A002', 'P002', 'D002', 2026-07-01),
('A003', 'P003', 'D003', 2026-07-02);

-- Billing --

INSERT INTO billing
(bill_id, patient_id, consultation_fee, medicine_charge, lab_charge, total_amount)

VALUES
('B001', 'P001', 350.00, 230.00, 120.00, 700.00),
('B002', 'P002', 450.00, 23.00, 120.00, 593.00),
('B003', 'P003', 245.00, 560.00, 230.00, 1035.00);
