def get_k_param(param_name, keyword, keywords_param_name):
    if param_name in keywords_param_name[keyword]:
        i = keywords_param_name[keyword].index(param_name)
    else:
        i = 'no maching parameter'
    return i

# add param to the keyword header
def change_fmt_keyword_param(cur_pid, cur_k_to_format, format_template, format_lengths):
    cur_fmt_keyword = cur_k_to_format[0]
    cur_fmt_keyword_w_param = cur_fmt_keyword

    for i in range(len(cur_k_to_format[1])):
        param = cur_k_to_format[1][i]
        if param == 'pid':
            cur_fmt_keyword_w_param += cur_pid
        else:
            cur_fmt_keyword_w_param += param

    format_template[cur_fmt_keyword_w_param] = format_template[cur_fmt_keyword]
    format_lengths[cur_fmt_keyword_w_param] = format_lengths[cur_fmt_keyword]

    return cur_fmt_keyword_w_param, format_template, format_lengths
    
def convert_file(keywords, 
                 keywords_param_name, 
                 k_to_format, 
                 format_template, 
                 format_lengths,
                 format_header,
                 format_separator):

    fmt = {} # fmt means format

    # loop throught the keywords in the k file
    for k in keywords.keys():
        if k in k_to_format:
            cur_fmt_keyword = k_to_format[k][0]
            cur_fmt_keyword_w_param = cur_fmt_keyword
            cur_pid = ''
            pindex = get_k_param('pid', k, keywords_param_name)
            if type(pindex) == int and len(k_to_format[k]) > 1:
                cur_pid = keywords[k][0][pindex]

                # Add pid to the keyword header
                cur_fmt_keyword_w_param, format_template, format_lengths = change_fmt_keyword_param(cur_pid, k_to_format[k],
                                                                                                    format_template, 
                                                                                                    format_lengths)
            fmt[cur_fmt_keyword_w_param] = []

            for l_k in keywords[k]:
                cur_group = []

                pindex = get_k_param('pid', k, keywords_param_name)
                if type(pindex) == int and len(k_to_format[k]) > 1 and cur_pid != l_k[pindex]:
                    cur_pid = l_k[pindex]

                    cur_fmt_keyword_w_param, format_template, format_lengths = change_fmt_keyword_param(cur_pid, k_to_format[k],
                                                                                                    format_template, 
                                                                                                    format_lengths)

                    fmt[cur_fmt_keyword_w_param] = []

                for l_fmt in format_template[cur_fmt_keyword]:
                    cur_line = []

                    for param_fmt in l_fmt:
                        print(param_fmt)
                        index = get_k_param(param_fmt, k, keywords_param_name)

                        if type(index) == int:
                            cur_line.append(l_k[index])
                        else:
                            cur_line.append(param_fmt)

                    cur_group.append(cur_line)
                fmt[cur_fmt_keyword_w_param].append(cur_group)
                        
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
