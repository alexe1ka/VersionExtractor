import os
import fnmatch
import re


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))  # в листе сохраняется путь до файла
                # print("pattern: " + pattern)
                # print(name)  # выводит имя файла
    return result


def generate_report(hdl_file_list):
    return 1


def file_parser(filepath):
    file_list = []
    header_data = {}

    with open(filepath, "r") as file:  # открываем файл
        print("filename: " + file.name)
        for line in file:
            file_list.append(line)
            if "Description" in line:
                header_data["description"] = line.split(":")[1]

    print(header_data)
    return file_list


if __name__ == "__main__":
    test_dir_path = '//MRS//Project_Quartet//КВАРТЕТ//Разработка//Блок 308-051-01 (СЦВМ)//ПО'
    test_file_path = 'E:/addr_cntr.v'
    file_parser(test_file_path)
    # print(find("*.v", test_dir_path))
