USE hospital_management;

-- Patient View 

CREATE VIEW patient_view AS
SELECT patient_id, name, age, gender, phone
FROM patients;

-- Doctor View

CREATE VIEW doctor_view AS
SELECT doctor_id, name, specialization, phone
FROM doctors;

--Appoinment Details View

CREATE VIEW appointment_details AS
SELECT
    a.appointment_id,
    p.name AS patient_name,
    d.name AS doctor_name,
    a.appointment_date
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN doctors d ON a.doctor_id = d.doctor_id;

-- Billing View

CREATE VIEW billing_view AS
SELECT
    bill_id,
    patient_id,
    total_amount,
    bill_date
FROM bills;

-- Patient Bill Details 

CREATE VIEW patient_bill_details AS
SELECT
    b.bill_id,
    p.name AS patient_name,
    b.total_amount,
    b.bill_date
FROM bills b
JOIN patients p
ON b.patient_id = p.patient_id;

-- Doctor Appointment Count

CREATE VIEW doctor_appointments AS
SELECT
    doctor_id,
    COUNT(*) AS total_appointments
FROM appointments
GROUP BY doctor_id;