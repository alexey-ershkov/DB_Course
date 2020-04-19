def sql_parser(filename):
    file = open(filename, 'r')
    sql_commands = file.read().split(';')
    return sql_commands
