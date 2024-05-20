import src.mapper.stencil_mapper as map
import src.sql_generator.insert_generator as gen
import src.stencils.id as id
import src.references as ref
import random

def generate_row(tab, rows_quantity, columns):
    has_id = any(column.split('.')[-1] == 'id' for column in columns)
    has_gender = any(column.split('.')[-1] == 'gender' for column in columns)
    has_name = any(column.split('.')[-1] == 'name' for column in columns)
    has_surname = any(column.split('.')[-1] == 'surname' for column in columns)
    if has_id:
        iterator = id.integer_generator()

    for _ in range(rows_quantity):
        if has_gender or has_name or has_surname:
            tmp = map.mapper("gender")

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
                else:
                    result = map.mapper(column.split(".")[-1])
            else:
                random_reference = ref.reference_dict.get(column.split(".")[1])
                chosen_element = random.choice(random_reference)
                random_reference.remove(chosen_element)
                result = chosen_element

            if column.split(".")[0] == "pk":
                ref.add_reference(tab, [result])

            # print(column.split(".")[-1])
            values.append(result)

        gen.generate(tab, *values)