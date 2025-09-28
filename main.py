
###----- read and parse the .k file -----###

intersting_keys = {
    "*ELEMENT_SHELL" : "[8]*8",
    "*NODE" : "[8]+[16]*3+[8]*2"
}

keys = {}

# read the .k file and write each keyword line in a dictionnary
with open("frame_mesh_full_full.k") as f:

    current_key = ""
    for l in f:
        l = l.strip('\n')
        # print(l)

        if l[0] == "*":
            if l in intersting_keys:
                keys[l] = []
                current_key = l
            else:
                current_key = ""
        elif not current_key == "":
            keys[current_key].append(l)
    
    # print(keys)


# separate a line of text by following the pattern given in text_pattern
def parse(text_pattern, string_to_parse):
    parsed = []
    i = 0

    for n in eval(text_pattern):
        parsed.append(string_to_parse[i:i+n].strip(' $#'))
        i += n
    return parsed


keywords = {}
keywords_param_name = {}

# parse the lines to put them in an array inside a dictionnary
for k in keys.keys():
    keywords[k] = []
    i = 0
    for l in keys[k]:
        parsed_data = parse(intersting_keys[k], l)
        if i == 0:
            keywords_param_name[k] = parsed_data
        else:
            keywords[k].append(parsed_data)
        i+=1

# print(keywords)
# print(keywords_param_name)


###----- write the .unv file -----###

k_to_unv = {"*NODE": "2411",
            "*ELEMENT_SHELL": "2412"}

unv_template = {"2411": [['nid', '1', '1', '11'], ['x', 'y', 'z']],
                "2412": [['eid', '94', 'pid', '0', '7', '4'], ['n1', 'n2', 'n3', 'n4']]}

unv_lengths = {
    "2411" : "[10]*4 + [25]*3",
    "2412" : "[10]*6 + [10]*4"
}

unv = {}

def get_k_param(param_name, keyword):
    if param_name in keywords_param_name[keyword]:
        # print(param_name)
        i = keywords_param_name[keyword].index(param_name)
    else:
        i = 'no maching parameter'
    return i
    

for k in keywords.keys():
    if k in k_to_unv:
        cur_unv_keyword = k_to_unv[k]
        unv[cur_unv_keyword] = []

        for l_k in keywords[k]:
            cur_group = []
            for l_unv in unv_template[cur_unv_keyword]:
                cur_line = []

                for param_unv in l_unv:
                    index = get_k_param(param_unv, k)
                    # print(index)

                    if type(index) == int:
                        cur_line.append(l_k[index])
                    else:
                        cur_line.append(param_unv)

                cur_group.append(cur_line)
            unv[cur_unv_keyword].append(cur_group)
                        
# print(unv)

lines = []

for k in unv.keys():
    lines.append('-1'.rjust(6) + "\n")
    lines.append(k.rjust(6) + "\n")
    for l in unv[k]:
        j = 0
        for ll in l:
            for i in range(len(ll)):
                ll[i] = ll[i].rjust(eval(unv_lengths[k])[j])

                j += 1
        
            ll = ''.join(ll) + "\n"

            lines.append(ll)
    lines.append('-1'.rjust(6) + "\n")

# print(lines)


f = open("frame_mesh_full_full.unv", "w")
f.writelines(lines)
f.close()
