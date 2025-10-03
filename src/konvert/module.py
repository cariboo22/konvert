import typer
from typing_extensions import Annotated

from .k_reading import parse_k_file
from .convert_file import convert_file
from .tools import write_file

def konverting(
    file: Annotated[str, typer.Argument(help='The name of the .k file to convert')] = "",
    file_format: Annotated[str, typer.Argument(help='The format to convert .k file to')] = "",
    output_name: Annotated[str, typer.Option(help='Output filename, without extention')] = ""
):

    filename = file.split('.')[0]

    match file_format:
        case 'unv':
            from .format_files import unv as fmt
        case 'inp':
            from .format_files import inp as fmt
        case _:
            print('Not a valid format')
            quit()

    # read the .k file and write each keyword line in a dictionnary
    print('Parsing k file...')
    keywords, keywords_param_name = parse_k_file(filename)
    print("done")

    ###----- convert the file to generic format -----###
    print(f"Converting k to {file_format}...")
    lines = convert_file(keywords, 
                         keywords_param_name, 
                         fmt.k_to_format, 
                         fmt.format_template, 
                         fmt.format_lengths, 
                         fmt.format_header, 
                         fmt.format_separator)
    print("done")

    ###----- write to a text file -----###
    print(f"Writing {file_format} file...")
    if not output_name:
        output_name = filename

    write_file(output_name, lines, file_format)
    print("done")
    print(f"{filename}.k successfully converted to {output_name}.{file_format} !")
