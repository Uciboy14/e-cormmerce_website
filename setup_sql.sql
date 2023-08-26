-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS ecormmerce_db;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'adminpass';
GRANT ALL PRIVILEGES ON `mouau_db`.* TO 'admin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
