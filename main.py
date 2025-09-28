
import argparse

from k_reading import parse_k_file
from unv_writing import make_unv
from tools import write_file

parser = argparse.ArgumentParser(prog='konvert',
                                 description='Convert LS-PrePost .k mesh to I-DEAS Universal Format .unv (only for 2D mesh for now)',
                                 epilog='...')

parser.add_argument('filename', help='The name of the .k file to convert')
parser.add_argument('-o', '--output', help='Output unv filename, without .unv')

args = parser.parse_args()

file = args.filename
filename = file.split('.')[0]

# read the .k file and write each keyword line in a dictionnary
print('Parsing k file...')
keywords, keywords_param_name = parse_k_file(filename)
print("done")

###----- write the .unv file -----###
print("Converting k to unv...")
lines = make_unv(keywords, keywords_param_name)
print("done")

print("Writing unv file...")
out_filename = filename
if args.output:
    out_filename = args.output

write_file(out_filename, lines)
print("done")
print(f"{filename}.k successfully converted to {out_filename}.unv !")
