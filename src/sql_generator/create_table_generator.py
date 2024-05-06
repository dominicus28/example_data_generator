def gen(table, *args):
    text1 = 'CREATE TABLE {} ({});'
    arguments = [arg for arg in args if arg is not None]
    text2 = '{}' + (', {}' * (len(arguments) - 1))
    text3 = text2.format(*arguments)
    final = text1.format(table, text3)

    with open('script.sql', 'a') as f:
        f.write(final)

    f.close()