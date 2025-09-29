def get_k_param(param_name, keyword, keywords_param_name):
    if param_name in keywords_param_name[keyword]:
        # print(param_name)
        i = keywords_param_name[keyword].index(param_name)
    else:
        i = 'no maching parameter'
    return i
    
def convert_file(keywords, 
                 keywords_param_name, 
                 k_to_format, 
                 format_template, 
                 format_lengths,
                 format_header,
                 format_separator):
    unv = {}

    for k in keywords.keys():
        if k in k_to_format:
            cur_unv_keyword = k_to_format[k]
            unv[cur_unv_keyword] = []

            for l_k in keywords[k]:
                cur_group = []
                for l_unv in format_template[cur_unv_keyword]:
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

    return make_file(unv, format_lengths, format_header, format_separator)


def make_file(unv, format_lengths, format_header, format_separator):

    lines = []

    for k in unv.keys():
        lines.append(format_header.rjust(6) + "\n")
        lines.append(k.rjust(6) + "\n")
        for l in unv[k]:
            j = 0
            for ll in l:
                for i in range(len(ll)):

                    if i < len(ll) - 1:
                        ll[i] = ll[i].rjust(eval(format_lengths[k])[j]) + format_separator
                    else:
                        ll[i] = ll[i].rjust(eval(format_lengths[k])[j])

                    j += 1
            
                ll = ''.join(ll) + "\n"

                lines.append(ll)
        lines.append(format_header.rjust(6) + "\n")

    # print(lines)

    return lines
