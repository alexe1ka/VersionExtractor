import os
import fnmatch
import chardet
import json2html


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))  # в листе сохраняется путь до файла
                # print("pattern: " + pattern)
                # print(name)  # выводит имя файла
    return result


def generate_report(parsed_data_from_file):
    report_file = open('report.html', 'w')
    message = """<html>
    <head></head>
    <body>"""
    for file_info in parsed_data_from_file:
        message += file_info
    message += """</body>
    </html>"""
    report_file.write(message)
    report_file.close()
    return 1


# функция парсит шапку файла:
# описание файла(description),
# версию(version) ....
# так же выводит список модулей в данном файле
def file_parser(filepath):
    list_of_file_data = []  # построчный лист с содержимым файла
    # header_data = {"modules": []}
    header_data = {"File": "имя файла", "description": "описание не определено", "version": "версия не определена",
                   "designer": "дизайнер не определен"}
    with open(filepath, "rb") as file:  # открываем файл maccyrillic
        # print("filename: " + file.name)
        for line in file:
            # print(line)
            line = universal_decoder(line)
            list_of_file_data.append(line)
            header_data["File"] = file.name
            if "Description" in line:
                header_data["description"] = clean_string(line.split(":")[1])
            if "Version:" in line:
                header_data["version"] = clean_string(line.split(":")[1])
            if "Designer:" in line:
                header_data["designer"] = clean_string(line.split(":")[1])

                # if "module " in line and "endmodule" not in line and line.lstrip(" ").startswith("m"):
                #     header_data["modules"].append(line.split(" ")[1].split("(")[0])

    # TODO добавить "автор не указан","версия не указана" если соответствующее поле пустое
    # print(header_data)
    return header_data


# декодирует строку исходя из определенной кодировки
def universal_decoder(line):
    if chardet.detect(line)['encoding'] == 'ascii':
        return line.decode("ascii")
    if chardet.detect(line)['encoding'] == 'windows-1251':
        return line.decode("windows-1251", "ignore")
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
    # test_dir_path = 'E:\!TEST_FOLDER'
    test_dir_path = 'E:\!test'
    # test_dir_path = 'D:\MyFiles\Projects\PyCharmProjects\VersionExtractor\VersionExtractor\!TEST_FOLDER\\v_new'
    # test_file_path = 'E:/addr_cntr.v'
    # test_file_path = 'D:/addr_cntr.v'
    # test_file_path = 'D:/many_modules.v'
    file_list = find("*.v", test_dir_path)
    hdl_report_list = []
    for f in file_list:
        hdl_report_list.append(file_parser(f))
        print(json2html.json2html.convert(hdl_report_list))
        generate_report(json2html.json2html.convert(hdl_report_list))
        print('\n')
