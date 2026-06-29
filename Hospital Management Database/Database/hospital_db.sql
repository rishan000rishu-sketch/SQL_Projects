-- ================DATA BASE===============

CREATE DATABASE hospital_management;

-- =============TABLES================

-- PATIENT

CREATE TABLE patients(
    patient_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(20),
    age INT,
    gender VARCHAR(20),
    phone VARCHAR(20)
);

-- DOCTORS

CREATE TABLE doctors(
    doctor_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(50),
    specilisation VARCHAR(50),
    phone VARCHAR(15)
);

-- BILLS

CREATE TABLE bills(
    bill_id VARCHAR(50) PRIMARY KEY,
    patient_id VARCHAR(50),
    consultation_fee DECIMAL(10,2),
    medicine_charge DECIMAL(10,2),
    lab_charge DECIMAL(10,2),
    total_amount DECIMAL(10,2)
);

-- APPOINTMENTS

CREATE TABLE appointments(
    appoinment_id VARCHAR(50) PRIMARY KEY,
    patient_id VARCHAR(50),
    doctor_id VARCHAR(50),
    appoinment_date DATETIME 
);
