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

    result = next((item for item in data["tabs"] if item["tab"] == "person" and item["exist"] == True), None)
    if result:
        persons = prsfab.person_fabric(result["rows"], result["name"], result["gender"], result["surname"],
                                       result["telephone"], result["mail"])
        # print(persons)
        person_pk = result["primary_key"].split()[0]
        create_gen.gen(result["tab_name"], result["primary_key"], result["name"], result["gender"],
                       result["surname"], result["telephone"], result["mail"], "PRIMARY KEY ({})".format(person_pk))
        #sql_gen.generate_insert_script(persons)

    result = next((item for item in data["tabs"] if item["tab"] == "employee" and item["exist"] == True), None)
    if result:
        employees = emplfab.employee_fabric(result["rows"], persons, result["position"])
        # print(employees)
        create_gen.gen(result["tab_name"], result["primary_key"], result["position"], result["person_id"])
        # sql_gen.generate_insert_script(employees)

    result = next((item for item in data["tabs"] if item["tab"] == "client" and item["exist"] == True), None)
    if result:
        clients = clntfab.client_fabric(result["rows"], persons, result["PSESEL_number"],
                                        result["id_card_number"], result["driving_license_number"])
        # print(clients)
        create_gen.gen(result["tab_name"], result["primary_key"], result["name"], result["gender"],
                       result["surname"], result["telephone"], result["mail"])
        # for client in clients:
        #     print(client[1].pesel)
        # sql_gen.generate_insert_script(clients)

    f.close()