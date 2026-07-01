USE hospital_db;

-- Doctors --

INSERT INTO doctors
(doctor_id, doctor_name, specialization, phone)

VALUES
('D001','Dr. Anil Kumar','Cardiology','9876543210'),
('D002','Dr. Meera Nair','Neurology','9876543211'),
('D003','Dr. Rahul Menon','Orthopedics','9876543212'),
('D004','Dr. Priya Joseph','Pediatrics','9876543213'),
('D005','Dr. Arjun Das','Dermatology','9876543214'),
('D006','Dr. Neha Sharma','Gynecology','9876543215'),
('D007','Dr. Vivek Nair','Ophthalmology','9876543216'),
('D008','Dr. Sanjay Kumar','ENT','9876543217'),
('D009','Dr. Asha Menon','Psychiatry','9876543218'),
('D010','Dr. Deepak Raj','General Medicine','9876543219');

-- Patients --

INSERT INTO patients
(patient_name, age, gender, phone)

VALUES
('P001', 'Rishan', 21,'Male', '9000000001'),
('P002', 'Shadil', 22, 'Female', '9000000002'),
('P003', 'Akhil', 23, 'Male', '9000000003'),
('P004', 'Anu', 24, 'Female', '9000000004'),
('P005', 'Meera', 25, 'Male', '9000000005'),
('P006', 'Rahul', 26, 'Female', '9000000006'),
('P007', 'Sneha', 27, 'Male', '9000000007'),
('P008', 'Arjun', 28, 'Female','9000000008'),
('P009', 'Nisha', 29, 'Male','9000000009'),
('P010', 'Vivek', 30, 'Female','9000000010');

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
