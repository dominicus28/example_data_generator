def generate(table, *args):
    text1 = 'INSERT INTO {} VALUES ({});'
    text2 = '{}' + (', {}' * (len(args) - 1))
    # print(*args)
    #
    # print(text2)
    text3 = text2.format(*args)
    final = text1.format(table, text3)

    with open('script.sql', 'a', encoding="utf-8") as f:
        f.write(final+"\n\n")

    f.close()