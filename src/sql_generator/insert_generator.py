def generate(table, *args):
    text1 = 'INSERT INTO {} VALUES ({});'
    text2 = '{}' + (', {}' * (len(args) - 1))
    # print(*args)
    #
    # print(text2)
    formatted_args = [
        f'"{arg}"' if 'Point' not in str(arg) else str(arg)
        for arg in args
    ]

    text3 = text2.format(*formatted_args)
    final = text1.format(table, text3)

    with open('script.sql', 'a', encoding="utf-8") as f:
        f.write(final+"\n\n")

    f.close()