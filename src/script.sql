CREATE TABLE my_person (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255), gender CHAR(0), surname VARCHAR(255), tel INT, PRIMARY KEY (id));

CREATE TABLE my_employee (id INT NOT NULL AUTO_INCREMENT, position VARCHAR(255), person_id INT, PRIMARY KEY (id), FOREIGN KEY (person_id) REFERENCES my_person(id));

CREATE TABLE my_client (PESEL INT NOT NULL AUTO_INCREMENT, license_num, person_id INT, PRIMARY KEY (PESEL), FOREIGN KEY (person_id) REFERENCES my_person(id));

