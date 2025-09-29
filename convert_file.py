def get_k_param(param_name, keyword, keywords_param_name):
    if param_name in keywords_param_name[keyword]:
        # print(param_name)
        i = keywords_param_name[keyword].index(param_name)
    else:
        i = 'no maching parameter'
    return i
    
def convert_file(keywords, keywords_param_name, k_to_file, file_template, file_lengths):
    unv = {}

    for k in keywords.keys():
        if k in k_to_file:
            cur_unv_keyword = k_to_file[k]
            unv[cur_unv_keyword] = []

            for l_k in keywords[k]:
                cur_group = []
                for l_unv in file_template[cur_unv_keyword]:
                    cur_line = []

                    for param_unv in l_unv:
                        index = get_k_param(param_unv, k, keywords_param_name)
                        # print(index)

                        if type(index) == int:
                            cur_line.append(l_k[index])
                        else:
                            cur_line.append(param_unv)

                    cur_group.append(cur_line)
                unv[cur_unv_keyword].append(cur_group)
                        
    # print(unv)

    return make_file(unv, file_lengths)


def make_file(unv, file_lengths):

    lines = []

    for k in unv.keys():
        lines.append('-1'.rjust(6) + "\n")
        lines.append(k.rjust(6) + "\n")
        for l in unv[k]:
            j = 0
            for ll in l:
                for i in range(len(ll)):
                    ll[i] = ll[i].rjust(eval(file_lengths[k])[j])

                    j += 1
            
                ll = ''.join(ll) + "\n"

                lines.append(ll)
        lines.append('-1'.rjust(6) + "\n")

    # print(lines)

    return lines
