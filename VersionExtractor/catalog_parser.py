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


# функция парсит шапку файла:
# описание файла(description),
# версию(version) ....
# так же выводит список модулей в данном файле
def file_parser(filepath):
    file_list = []  # построчный лист с содержимым файла
    header_data = {"modules": []}
    with open(filepath, "r") as file:  # открываем файл
        print("filename: " + file.name)
        for line in file:
            file_list.append(line)
            if "Description" in line:
                header_data["description"] = clean_string(line.split(":")[1])

            if "Version:" in line:
                header_data["version"] = clean_string(line.split(":")[1])

            if "Designer" in line:
                header_data["designer"] = clean_string(line.split(":")[1])

            if "module" in line and "endmodule" not in line:
                # header_data["modules"] = line.split(" ")[1].split("(")[0]
                header_data["modules"].append(line.split(" ")[1].split("(")[0])

    print(header_data)
    return header_data


# функция для очистки строки от \n  и лишних пробелов
def clean_string(dirty_string):
    clean = str(dirty_string).strip()
    clean = str(clean).replace('\n', '')
    return clean


if __name__ == "__main__":
    test_dir_path = '//MRS//Project_Quartet//КВАРТЕТ//Разработка//Блок 308-051-01 (СЦВМ)//ПО'
    # test_file_path = 'E:/addr_cntr.v'
    test_file_path = 'D:/addr_cntr.v'
    # test_file_path = 'D:/many_modules.v'
    file_parser(test_file_path)
    # print(find("*.v", test_dir_path))
