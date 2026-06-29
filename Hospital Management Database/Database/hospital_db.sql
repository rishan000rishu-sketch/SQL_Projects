-- ================DATA BASE===============

CREATE DATABASE hospital_management;

-- =============TABLES================

-- PATIENT

CREATE TABLE patients(
    patient_id VARCHAR(20),
    name VARCHAR(20),
    age INT,
    gender VARCHAR(20),
    phone VARCHAR(20)
);
