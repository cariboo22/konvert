import argparse

from k_reading import parse_k_file
from convert_file import convert_file
from tools import write_file

parser = argparse.ArgumentParser(prog='konvert',
                                 description='Convert LS-PrePost .k mesh to :\n - I-DEAS Universal Format .unv (only for 2D mesh for now)\n - CalculiX ?inp (also only for 2D quad mesh)',
                                 epilog='...')

parser.add_argument('filename', help='The name of the .k file to convert')
parser.add_argument('output_format', help='The format to convert .k file to')
parser.add_argument('-on', '--output_name', help='Output filename, without extention')

args = parser.parse_args()

file = args.filename
filename = file.split('.')[0]
file_format = args.output_format

match file_format:
    case 'unv':
        from unv import *
    case 'inp':
        from inp import *
    case _:
        print('Not a valid format')
        quit()

# read the .k file and write each keyword line in a dictionnary
print('Parsing k file...')
keywords, keywords_param_name = parse_k_file(filename)
print("done")

###----- convert the file to generic format -----###
print(f"Converting k to {file_format}...")
lines = convert_file(keywords, keywords_param_name, k_to_format, format_template, format_lengths, format_header, format_separator)
print("done")

###----- write to a text file -----###
print(f"Writing {file_format} file...")
out_filename = filename
if args.output_name:
    out_filename = args.output_name

write_file(out_filename, lines)
print("done")
print(f"{filename}.k successfully converted to {out_filename}.{file_format} !")
