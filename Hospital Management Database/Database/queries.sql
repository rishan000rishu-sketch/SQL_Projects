USE hospital_db;

-- 1. View All Doctors

SELECT * FROM doctors;

-- 2. View All Patients

SELECT * FROM patients;

-- 3. View All Appointments

SELECT * FROM appointments;

-- 4. Find a Patient by ID

SELECT *
FROM patients
WHERE patient_id = 1;

-- 5. Find a Doctor by Specialization

SELECT *
FROM doctors
WHERE specialization = 'Cardiology';

-- 6. Show Appointments with Patient and Doctor Names

SELECT
    a.appointment_id,
    p.patient_name,
    d.doctor_name,
    d.specialization,
    a.appointment_date,
    a.appointment_time,
    a.status
FROM appointments a
JOIN patients p
ON a.patient_id = p.patient_id
JOIN doctors d
ON a.doctor_id = d.doctor_id;

-- 7. Count Total Patients

SELECT COUNT(*) AS total_patients
FROM patients;

-- 8. Count Total Doctors

SELECT COUNT(*) AS total_doctors
FROM doctors;

-- 9. Count Appointments per Doctor

SELECT
    d.doctor_name,
    COUNT(a.appointment_id) AS total_appointments
FROM doctors d
LEFT JOIN appointments a
ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_name;

-- 10. Total Billing Amount

SELECT SUM(amount) AS total_income
FROM billing;

-- 11. Average Patient Age

SELECT AVG(age) AS average_age
FROM patients;

-- 12. Delete a Patient

DELETE FROM patients
WHERE patient_id = P003;

-- 13. Show Highest Bill

SELECT *
FROM billing
ORDER BY amount DESC
LIMIT 1;

-- 14. Show Lowest Bill

SELECT *
FROM billing
ORDER BY amount ASC
LIMIT 1;

-- 15. Search Patient by Name

SELECT *
FROM patients
WHERE patient_name LIKE '%Rahul%';

-- 16. Doctors Sorted Alphabetically

SELECT *
FROM doctors
ORDER BY doctor_name ASC;

-- 17. Patients Older Than 40

SELECT *
FROM patients
WHERE age > 40;
