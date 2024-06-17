import src.stencils.driving_license as driving_license
import src.stencils.id as id
import src.stencils.id_card as id_card
import src.stencils.mail as mail
import src.stencils.name_gender as name_gender
import src.stencils.pesel as pesel
import src.stencils.random_int as random_int
import src.stencils.random_string as random_string
import src.stencils.surname as surname
import src.stencils.telephone as telephone
import src.stencils.work_position as work_position
import src.stencils.address as address
import src.stencils.date as date
import src.stencils.random_boolean as random_boolean
import src.stencils.cost as cost
import src.stencils.car_data as car_data

def unknown_command():
    print("Unknown method. Please try again.")


methods = {
    "driving_license": driving_license.create_driving_lic_number,
    "id": id.integer_generator,
    "id_card": id_card.create_id_number,
    "mail": mail.create_mail,
    "name": name_gender.select_random_person,  # name as first return value
    "gender": name_gender.select_random_person,  # gender as second return value
    "pesel": pesel.create_pesel,  # gender as arg
    "random_int": random_int.generate_random_integer,
    "random_string": random_string.generate_random_string,
    "surname": surname.select_random_surname,  # gender as arg
    "telephone": telephone.create_telephone,
    "work_position": work_position.create_position,
    "town": address.generate_random_address,
    "street": address.generate_random_address,
    "postal_code": address.generate_random_address,
    "coordinates": address.generate_random_address,
    "date": date.generate_random_datetime,
    "random_boolean": random_boolean.generate_random_boolean,
    "cost": cost.generate_random_cost,
    "car_data": car_data.select_random_car
}


def mapper(user_input):
    parts = user_input.split()

    command_name = parts[0]
    args = parts[1:]

    # print(command_name)
    command = methods.get(command_name, unknown_command)

    try:
        if len(args) == 0:
            return command()
        else:
            return command(*args)
    except TypeError as e:
        print(f"Error: {e}")
