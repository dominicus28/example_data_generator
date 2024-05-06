import json
import src.entity_fabrics.person_fabric as prsfab
import src.entity_fabrics.client_fabric as clntfab
import src.entity_fabrics.employee_fabric as emplfab
import src.sql_generator.insert_generator as insert_gen
import src.sql_generator.create_table_generator as create_gen

def read_config_and_run():

    f = open("../config/config.json")
    data = json.load(f)
    persons = 0

    person = next((item for item in data["tabs"] if item["tab"] == "person" and item["exist"] == True), None)
    if person:
        persons = prsfab.person_fabric(person["rows"], person["name"], person["gender"], person["surname"],
                                       person["telephone"], person["mail"])
        # print(persons)
        person_pk = person["primary_key"].split()[0]
        create_gen.gen(person["tab_name"], person["primary_key"], person["name"], person["gender"],
                       person["surname"], person["telephone"], person["mail"], "PRIMARY KEY ({})".format(person_pk))
        #sql_gen.generate_insert_script(persons)

    employee = next((item for item in data["tabs"] if item["tab"] == "employee" and item["exist"] == True), None)
    if employee:
        employees = emplfab.employee_fabric(employee["rows"], persons, employee["position"])

        # print(employees)
        employee_pk = employee["primary_key"].split()[0]
        empl_per_fk = employee["person_id_fk"].split()[0]
        create_gen.gen(employee["tab_name"], employee["primary_key"], employee["position"],
                       employee["person_id_fk"], "PRIMARY KEY ({})".format(employee_pk),
                       "FOREIGN KEY ({})".format(empl_per_fk)+" REFERENCES {}({})".format(person["tab_name"],
                                                                                          person_pk))
        # sql_gen.generate_insert_script(employees)

    client = next((item for item in data["tabs"] if item["tab"] == "client" and item["exist"] == True), None)
    if client:
        client_pk = client["primary_key"].split()[0]
        clients = clntfab.client_fabric(client["rows"], persons, client_pk,
                                        client["id_card_number"], client["driving_license_number"])

        # print(clients)
        cli_per_fk = client["person_id_fk"].split()[0]
        create_gen.gen(client["tab_name"], client["primary_key"], client["id_card_number"],
                       client["driving_license_number"], employee["person_id_fk"], "PRIMARY KEY ({})".format(client_pk),
                       "FOREIGN KEY ({})".format(cli_per_fk)+" REFERENCES {}({})".format(person["tab_name"],
                                                                                          person_pk))
        # for client in clients:
        #     print(client[1].pesel)
        # sql_gen.generate_insert_script(clients)

    f.close()