import os
import fnmatch
import chardet


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
    list_of_file_data = []  # построчный лист с содержимым файла
    header_data = {"modules": []}
    with open(filepath, "rb") as file:  # открываем файл maccyrillic
        print("filename: " + file.name)
        for line in file:
            # print(line)
            line = universal_decoder(line)
            list_of_file_data.append(line)
            if "Description" in line:
                header_data["description"] = clean_string(line.split(":")[1])

            if "Version:" in line:
                header_data["version"] = clean_string(line.split(":")[1])

            if "Designer:" in line:
                header_data["designer"] = clean_string(line.split(":")[1])

            # if "module " in line and "endmodule" not in line and line.lstrip(" ").startswith("m"):
            #     header_data["modules"].append(line.split(" ")[1].split("(")[0])

    # TODO добавить "автор не указан","версия не указана" если соответствующее поле пустое
    print(header_data)
    return header_data


# декодирует строку исходя из определенной кодировки
def universal_decoder(line):
    if chardet.detect(line)['encoding'] == 'ascii':
        return line.decode("ascii")
    if chardet.detect(line)['encoding'] == 'windows-1251':
        return line.decode("windows-1251", "replace")
    if chardet.detect(line)['encoding'] == 'MacCyrillic':
        return line.decode("MacCyrillic")
    if chardet.detect(line)['encoding'] == 'utf-8':
        return line.decode("utf-8")
    return ""


# функция для очистки строки от \n  и лишних пробелов
def clean_string(dirty_string):
    clean = str(dirty_string).strip()
    clean = str(clean).replace('\n', '')
    return clean


if __name__ == "__main__":
    # test_dir_path = 'E:\!TEST_FOLDER\\v_new'
    test_dir_path = 'E:\!TEST_FOLDER'
    # test_dir_path = 'E:\!test'
    # test_dir_path = 'D:\MyFiles\Projects\PyCharmProjects\VersionExtractor\VersionExtractor\!TEST_FOLDER\\v_new'
    # test_file_path = 'E:/addr_cntr.v'
    # test_file_path = 'D:/addr_cntr.v'
    # test_file_path = 'D:/many_modules.v'
    file_list = find("*.v", test_dir_path)
    for f in file_list:
        file_parser(f)
        print('\n')
