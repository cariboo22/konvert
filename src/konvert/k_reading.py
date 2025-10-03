
interesting_keys = {
    "*ELEMENT_SHELL": "[8]*8",
    "*NODE": "[8]+[16]*3+[8]*2"
}

###----- read and parse the .k file -----###
def parse_k_file(filename):

    keys = {}

    # read the .k file and write each keyword line in a dictionnary
    with open(filename + ".k") as f:

        current_key = ""
        for l in f:
            l = l.strip('\n')
            # print(l)

            if l[0] == "*":
                if l in interesting_keys:
                    keys[l] = []
                    current_key = l
                else:
                    current_key = ""
            elif not current_key == "":
                keys[current_key].append(l)
        
        # print(keys)

    keywords = {}
    keywords_param_name = {}

    # parse the lines to put them in an array inside a dictionnary
    for k in keys.keys():
        keywords[k] = []
        i = 0
        for l in keys[k]:
            parsed_data = parse(interesting_keys[k], l)
            if i == 0:
                keywords_param_name[k] = parsed_data
            else:
                keywords[k].append(parsed_data)
            i+=1

    # print(keywords)
    # print(keywords_param_name)

    return keywords, keywords_param_name

# separate a line of text by following the pattern given in text_pattern
def parse(text_pattern, string_to_parse):
    parsed = []
    i = 0

    for n in eval(text_pattern):
        parsed.append(string_to_parse[i:i+n].strip(' $#'))
        i += n
    return parsed
