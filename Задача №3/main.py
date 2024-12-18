# Вариант кода №1 с указание названия папки где содержатся текстовые документы:
import os

# Папка, где находятся файлы, которые нужно объединить
directory = 'txt'  # Заменить на имя папки, если она называется иначе

# Список файлов, которые нужно объединить
files_to_merge = [os.path.join(directory, '1.txt'), 
                  os.path.join(directory, '2.txt'), 
                  os.path.join(directory, '3.txt')]  # Заменить на имена файлов


def create_file_list(files):
    merge_file_list = []  
    
    for file in files:
        if os.path.isfile(file):  
            with open(file, 'r', encoding='utf-8') as temp_file:  
                content = temp_file.readlines()  
                line_count = len(content)  
                merge_file_list.append((file, line_count, content))  
        else:
            print(f'Файл {file} не найден.')  

    return sorted(merge_file_list, key=lambda x: x[1])


def create_merge_file(output_filename, files):
    with open(output_filename, 'w', encoding='utf-8') as merge_file:  
        for file_info in create_file_list(files):
            file_name, line_count, content = file_info
            merge_file.write(f'{file_name}\n')  
            merge_file.write(f'{line_count}\n')  
            merge_file.writelines(content)  
            merge_file.write('\n')    

    print(f'Итоговый файл "{output_filename}" создан.')

create_merge_file('merged_output.txt', files_to_merge)


# Вариант кода №2, работа в текущей директории: 
# import os

# files_to_merge = ['1.txt', '2.txt', '3.txt']  # Заменить на свои имена файлов

# def create_file_list(files):
#     merge_file_list = []  
    
#     for file in files:
#         if os.path.isfile(file):  
#             with open(file, 'r', encoding='utf-8') as temp_file:  
#                 content = temp_file.readlines()  
#                 line_count = len(content)  
#                 merge_file_list.append((file, line_count, content))  
#         else:
#             print(f'Файл {file} не найден.')  

#     return sorted(merge_file_list, key=lambda x: x[1])

# def create_merge_file(output_filename, files):
#     with open(output_filename, 'w', encoding='utf-8') as merge_file:  
#         for file_info in create_file_list(files):
#             file_name, line_count, content = file_info
#             merge_file.write(f'{file_name}\n')  
#             merge_file.write(f'{line_count}\n')  
#             merge_file.writelines(content)  
#             merge_file.write('\n')  

#     print(f'Итоговый файл "{output_filename}" создан.')

# create_merge_file('merged_output.txt', files_to_merge)