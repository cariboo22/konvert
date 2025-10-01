def get_k_param(param_name, keyword, keywords_param_name):
    if param_name in keywords_param_name[keyword]:
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

    fmt = {} # fmt means format

    for k in keywords.keys():
        if k in k_to_format:
            cur_fmt_keyword = k_to_format[k]
            fmt[cur_fmt_keyword] = []

            for l_k in keywords[k]:
                cur_group = []
                for l_fmt in format_template[cur_fmt_keyword]:
                    cur_line = []

                    for param_fmt in l_fmt:
                        index = get_k_param(param_fmt, k, keywords_param_name)

                        if type(index) == int:
                            cur_line.append(l_k[index])
                        else:
                            cur_line.append(param_fmt)

                    cur_group.append(cur_line)
                fmt[cur_fmt_keyword].append(cur_group)
                        
    return make_file(fmt, format_lengths, format_header, format_separator)


def make_file(fmt, format_lengths, format_header, format_separator):

    lines = []

    for k in fmt.keys():
        lines.append(format_header.rjust(6) + "\n")
        lines.append(k.rjust(6) + "\n")
        for l in fmt[k]:
            j = 0
            for ll in l:
                for i in range(len(ll)):

                    # formatting the different lines with the good lengths
                    if i < len(ll) - 1:
                        ll[i] = ll[i].rjust(eval(format_lengths[k])[j]) + format_separator
                    else:
                        ll[i] = ll[i].rjust(eval(format_lengths[k])[j])

                    j += 1
            
                ll = ''.join(ll) + "\n"

                lines.append(ll)
        lines.append(format_header.rjust(6) + "\n")

    return lines
