

month_data = {1 : "January" , 2 : "February" , 3 : "March", 4 : "April", 5 : "May", 6 : "June" ,
                    7 : "July", 8 : "August", 9 : "September", 10 : "Oktober", 11 : "November", 12 : "Desember"}

selected_year = 2018

year_limits = (1900, 2050)


def text_parser(filename):

    with open('/home/gharzol/PycharmProjects/Budget_app/bank_txt_files/' + filename + '.txt', 'rb') as f:
        strings = f.readlines()

    strings = [i.rstrip() for i in strings]

    strings.pop(0)

    strings_data = []
    for string in strings:
        charred_string = ""
        for i in string:
            charred_string += chr(i)


        temp_string = charred_string.replace(',', '')
        charred_string = temp_string
        temp_data = []
        count = 0
        symb_indices = [0,0,0,0]
        for i in range(0, len(charred_string)):
            if charred_string[i] == ';' and count == 0:
                temp_data.append(charred_string[1:i - 1])
                symb_indices[0] = i
                count += 1
            elif charred_string[i] == ';' and count <= 3:
                temp_data.append(charred_string[symb_indices[count - 1] + 2:i - 1])
                symb_indices[count] = i
                count +=1
            elif count == 4:
                temp_data.append(charred_string[symb_indices[3] + 2:len(charred_string) - 1])
                count += 1
        strings_data.append(tuple(temp_data))
    return tuple(strings_data)