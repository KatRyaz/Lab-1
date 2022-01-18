import re

pokemon_file = open('D:\CAT\Downloads\lab1-main\pokemon_full.json')
description_len = 0
max_descrip_len = 0
max_num_spaces = 0
name = ''
max_name = ''
max_abilities = ''
in_abilities = False
for line in pokemon_file:
    if (line.find('"name"') > 0):
        name = line
    if (line.find('"abilities"') > 0):
        in_abilities = True
    if in_abilities:
        space = line.count(' ') #кол-во пробелов + 1 = кол-во слов в "abilities"
        for j in range(0,(len(line)-1)):
            if (line[j] == ' ' and line[j+1] == '"'):
                space -=1
        if space >= max_num_spaces:
            max_num_spaces = space
            max_abilities = line

    if (line.find('description') > -1):
        description_len = len(line) #определяет длину описания покемона
        if description_len > max_descrip_len: #находит макс, запоминает имя
            max_descrip_len = description_len
            max_name = name


    if (line.find(']') > -1)  : #поиск макс "abilities", пока не встечена "]"
        in_abilities = False


pokemon_file.seek(0)
full_file = pokemon_file.read()
pokemon_file.close()

file_no_punct_marks = re.sub('[\w]', '', full_file)  #файл без знаков препинания

print(f'Количество элементов в файле: ', len(full_file))
print(f'Количество символов без знаков препинания в файле: ', len(full_file) - len(file_no_punct_marks))
print(f'Наиболее длинное описание у покемона: {max_name[12:-2]}')
print(f'Наиболее длинное умение: {max_abilities[6:]}')

