# Konvert

Konvert is a utility script written in Python for converting LS-Dyna keyword files to other FEA format (unv or inp for example). The goal is to use LS-PrePost as a meshing tool (the best free meshing tool in my opinion) and any other software for simulation.

## Installation

<!Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.>

For now, to use the package, you have to clone the github repo. The goal would be to use pipx to install it.

## Usage

```bash
python3 main.py <filename> <output_format>
```
The filename is the keyword file (.k) to convert.

The output_format that are currently supported are .unv and .inp.

## Project status

This project is in a very early stage of developpement. Only quadrangular shell elements can be converted.

## Contributing

During the early developpement phase, I wont take any pull request, but feel free to open issues or give me advice, this is my first public project on github.

## License

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
