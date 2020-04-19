def sql_parser(filename):
    file = open(filename, 'r')
    sql_commands = file.read().split(';')
    sql_commands.pop()
    return sql_commands
