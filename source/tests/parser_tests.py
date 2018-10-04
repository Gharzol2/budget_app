
def text_parser(strings):
    strings_data = []
    for string in strings:
        charred_string = ""
        for i in string:
            charred_string += chr(i)
        temp_data = []
        count = 0
        symb_indices = [0,0,0,0]
        for i in range(0, len(string)):
            if charred_string[i] == ';' and count == 0:
                temp_data.append(charred_string[1:i - 1])
                symb_indices[0] = i
                count += 1
            elif charred_string[i] == ';' and count <= 3:
                temp_data.append(charred_string[symb_indices[count - 1] + 2:i - 1])
                symb_indices[count] = i
                count +=1
            elif count == 4:
                temp_data.append(charred_string[symb_indices[3] + 2:len(string) - 1])
                count += 1
        strings_data.append(tuple(temp_data))
    return tuple(strings_data)


with open('/home/gharzol/PycharmProjects/Budget_app/bank_txt_files/transaksjonliste.txt', 'rb') as f:
    strings = f.readlines()



print(strings[0])
print(strings[1])

strings = [i.rstrip() for i in strings]
strings.pop(0)

print(strings[0])
print(strings[1])

parsed = text_parser(strings)


print("final result: ", parsed[0][0])
print("final result: ", parsed[0][1])
print("final result: ", parsed[0][2])
print("final result: ", parsed[0][3])
print("final result: ", parsed[0][4])

print("final result: ", parsed[14][0])
print("final result: ", parsed[14][1])
print("final result: ", parsed[14][2])
print("final result: ", parsed[14][3])
print("final result: ", parsed[14][4])

print("length: ", len(parsed[0]))
