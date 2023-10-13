import glob
import os


def get_paths_to_files():
    '''Возвращает пути к файлам, которые необходимо объединить'''
    path_to_directory = os.getcwd() + '\\divided\\'
    paths_to_files_for_merging = glob.glob(path_to_directory + '*.txt')
    return paths_to_files_for_merging


def merging_files():
    '''Читает файлы и записывает их контент вместе со служебной информацией о файлах в один общий файл'''
    paths_to_files = get_paths_to_files()
    files_content_list = []

    for file in paths_to_files:
        file_name = file.split('\\')[-1]
        
        with open(file, encoding='utf-8') as f:
            text_lines = f.readlines()
            files_content_list.append([len(text_lines), file_name, text_lines])
    
    files_content_list.sort()

    with open('final_file.txt', 'w', encoding='utf-8') as f:
        for file_content in files_content_list:
            f.write(f"{file_content[1]}\n{file_content[0]}\n{''.join(file_content[2])}\n")

merging_files()