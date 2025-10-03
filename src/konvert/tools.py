
def write_file(filename, lines, fmt):
    f = open(filename + f".{fmt}", "w")
    f.writelines(lines)
    f.close()
