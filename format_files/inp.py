k_to_format = {"*NODE": "*NODE",
            "*ELEMENT_SHELL": "*ELEMENT, TYPE=S4"}

format_template = {"*NODE": [['nid', 'x', 'y', 'z']],
                "*ELEMENT, TYPE=S4": [['eid', 'n1', 'n2', 'n3', 'n4']]}

format_lengths = {
    "*NODE" : "[8]*1 + [13]*3",
    "*ELEMENT, TYPE=S4" : "[6]*1 + [7]*4"
}

format_header = ''
format_separator = ','
