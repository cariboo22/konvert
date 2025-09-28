
import argparse

from k_reading import parse_k_file
from unv_writing import make_unv
from tools import write_file

parser = argparse.ArgumentParser(prog='Program Name',
                                 description='What the program does',
                                 epilog='Text at the bottom of help')

parser.add_argument('filename')

args = parser.parse_args()

file = args.filename
filename = file.split('.')[0]

# read the .k file and write each keyword line in a dictionnary
keywords, keywords_param_name = parse_k_file(filename)

###----- write the .unv file -----###
lines = make_unv(keywords, keywords_param_name)

write_file(filename, lines)
