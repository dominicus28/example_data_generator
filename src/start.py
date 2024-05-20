import json
import itertools
import src.row_generator as gen

def read_config_and_run():
    f = open("../config/config.json")
    data = json.load(f)
    tab_order = []
    rows_quantity = []
    columns = []

    tab_cycle = itertools.cycle(data["tabs"])

    while True:
        tab = next(tab_cycle)
        columns_tmp = []
        if (tab["name"] not in tab_order):
            if not next((column for column in tab["columns"] if "foreign_key" in column), None):
                tab_order.append(tab["name"])
                rows_quantity.append(tab["rows"])
                # columns.append([column["stencil"] for column in tab["columns"] if "stencil" in column])
                for column in tab["columns"]:
                    if "primary_key" in column:
                        columns_tmp.append("pk." + column["name"] + "." + column["stencil"])
                    else:
                        columns_tmp.append(column["stencil"])
                columns.append(columns_tmp)
                columns_tmp = []
            else:
                for column in tab["columns"]:
                    if "foreign_key" in column:
                        if column["reference"].split(".")[0] in tab_order:
                            tab_order.append(tab["name"])
                            rows_quantity.append(tab["rows"])
                            for column in tab["columns"]:
                                if "foreign_key" in column:
                                    columns_tmp.append("ref."+column["reference"])
                                else:
                                    columns_tmp.append(column["stencil"])
                            columns.append(columns_tmp)
                            columns_tmp = []


        if len(tab_order) == len(data["tabs"]):
            break
    print(tab_order)
    print(rows_quantity)
    print(columns)

    for i in range(len(tab_order)):
        gen.generate_row(tab_order[i], rows_quantity[i], columns[i])
