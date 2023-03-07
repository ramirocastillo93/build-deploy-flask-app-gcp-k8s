CREATE DATABASE databesos;

\c databesos

CREATE TABLE usuarios (
  id SERIAL PRIMARY KEY,
  username VARCHAR(100) NOT NULL,
  dateOfBirth DATE NOT NULL
);