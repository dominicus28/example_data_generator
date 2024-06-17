import src.mapper.stencil_mapper as map
import src.sql_generator.insert_generator as gen
import src.stencils.id as id
import src.references as ref
import random

def generate_row(tab, rows_quantity, columns):
    car_stencils = ["VIN", "brand", "model", "version", "production_year", "engine", "color"]

    has_id = any(column.split('.')[-1] == 'id' for column in columns)
    has_gender = any(column.split('.')[-1] == 'gender' for column in columns)
    has_name = any(column.split('.')[-1] == 'name' for column in columns)
    has_surname = any(column.split('.')[-1] == 'surname' for column in columns)
    has_date_range = any(column.split('.')[-1] == 'date_from' for column in columns) and \
                    any(column.split('.')[-1] == 'date_to' for column in columns)
    has_car_stencil = any(column.split('.')[-1] in car_stencils for column in columns)



    if has_id:
        iterator = id.integer_generator()

    for _ in range(rows_quantity):
        if has_gender or has_name or has_surname:
            tmp = map.mapper("gender")

        if has_date_range:
            tmp_date = map.mapper("date")

        if has_car_stencil:
            tmp_car = map.mapper("car_data")


        values = []
        for column in columns:
            if not column.split(".")[0] == "ref":
                if column.split(".")[-1] == "id":
                    result = next(iterator)+1
                elif column.split(".")[-1] == "name":
                    result = tmp[0]
                elif column.split(".")[-1] == "gender":
                    result = tmp[1]
                elif column.split(".")[-1] == "surname":
                    arg = column.split(".")[-1] + " " + tmp[1]
                    result = map.mapper(arg)
                elif column.split(".")[-1] == "pesel" and tmp:
                    arg = column.split(".")[-1] + " " + tmp[1]
                    result = map.mapper(arg)
                elif column.split(".")[-1] == "date_from" and tmp_date:
                    result = tmp_date[0]
                elif column.split(".")[-1] == "date_to" and tmp_date:
                    result = tmp_date[1]
                elif "date" in column.split(".")[-1] and not tmp_date:
                    result = map.mapper(column.split(".")[-1])[0]
                elif column.split(".")[-1] == "town":
                    arg = column.split(".")[-1] + " " + "town"
                    result = map.mapper(arg)
                elif column.split(".")[-1] == "street":
                    arg = column.split(".")[-1] + " " + "street"
                    result = map.mapper(arg)
                elif column.split(".")[-1] == "postal_code":
                    arg = column.split(".")[-1] + " " + "postal_code"
                    result = map.mapper(arg)
                elif column.split(".")[-1] == "coordinates":
                    arg = column.split(".")[-1] + " " + "coordinates"
                    result = map.mapper(arg)
                elif column.split(".")[-1] == "VIN":
                    result = tmp_car[0]
                elif column.split(".")[-1] == "brand":
                    result = tmp_car[1]
                elif column.split(".")[-1] == "model":
                    result = tmp_car[2]
                elif column.split(".")[-1] == "version":
                    result = tmp_car[3]
                elif column.split(".")[-1] == "production_year":
                    result = tmp_car[4]
                elif column.split(".")[-1] == "engine":
                    result = tmp_car[5]
                elif column.split(".")[-1] == "color":
                    result = tmp_car[6]
                else:
                    result = map.mapper(column.split(".")[-1])
            else:
                random_reference = ref.reference_dict.get(column.split(".")[1])
                chosen_element = random.choice(random_reference)
                # random_reference.remove(chosen_element)
                result = chosen_element

            if column.split(".")[0] == "pk":
                ref.add_reference(tab, [result])

            # print(column.split(".")[-1])
            values.append(result)

        gen.generate(tab, *values)