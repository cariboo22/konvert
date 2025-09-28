
def write_file(filename, lines):
    f = open(filename + ".unv", "w")
    f.writelines(lines)
    f.close()
