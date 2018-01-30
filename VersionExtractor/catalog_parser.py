import os
import fnmatch
import chardet
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, QThread
import datetime


# декодирует строку исходя из определенной кодировки
def universal_decoder(line):
    if chardet.detect(line)['encoding'] == 'ascii':
        return line.decode("ascii", "ignore")
    if chardet.detect(line)['encoding'] == 'windows-1251':
        return line.decode("windows-1251", errors="ignore")
    if chardet.detect(line)['encoding'] == 'MacCyrillic':
        return line.decode("MacCyrillic", errors="ignore")
    if chardet.detect(line)['encoding'] == 'utf-8':
        return line.decode("utf-8", "ignore")
    return ""


# функция для очистки строки от \n  и лишних пробелов
def clean_string(dirty_string):
    clean = str(dirty_string).strip()
    clean = str(clean).replace('\n', '')
    return clean


# функция парсит шапку файла:
# описание файла(description),
# версию(version) ....
# так же выводит список модулей в данном файле
def file_parser(filepath):
    list_of_file_data = []  # построчный лист с содержимым файла
    # header_data = {"modules": []}
    header_data = {"file": "имя файла", "description": "описание не определено", "version": "версия не определена",
                   "designer": "разработчик не определен"}
    with open(filepath, "rb") as file:  # открываем файл
        for line in file:
            # print(line)
            line = universal_decoder(line)
            list_of_file_data.append(line)
            header_data["file"] = file.name
            if "Description" in line:
                header_data["description"] = clean_string(line.split(":")[1])
            if "Version:" in line:
                header_data["version"] = clean_string(line.split(":")[1])
            if "Designer:" in line:
                header_data["designer"] = clean_string(line.split(":")[1])
                # if "module " in line and "endmodule" not in line and line.lstrip(" ").startswith("m"):
                #     header_data["modules"].append(line.split(" ")[1].split("(")[0])
    file.close()
    return header_data


class HdlTasker(QObject):
    finished = pyqtSignal()
    dataReady = pyqtSignal(list)
    now = datetime.datetime.now()

    @pyqtSlot()
    def find(self, path, extension) -> list:
        result = []
        for root, dirs, files in os.walk(path):
            for ext in extension:
                for name in fnmatch.filter(files, ext):
                    result.append(os.path.join(root, name))  # в листе сохраняется путь до файла
        # self.dataReady.emit(result)
        return result

    @pyqtSlot()
    def generate_report(self, file_list):
        time = self.now.strftime("%d_%m_%Y_%H-%M")
        report_filename = "report_" + str(time) + ".html"
        report_file = open(str(report_filename), 'a+', errors="ignore")
        report_file.write("""<html>
        <head></head>
        <body>""")
        report_file.write("<table border=:'1'>")
        report_file.write("<caption>Version extractor report</caption>")
        report_file.write("""<tr>
                <th>File</th>
                <th>Description</th>
                <th>Version</th>
                <th>Designer</th>
                </tr>""")
        for file in file_list:
            file_info = file_parser(file)
            report_file.write(
                "<tr><td>" + file_info["file"] + "</td><td>" + file_info["description"] + "</td><td>" + file_info[
                    "version"] + "</td><td>" + file_info["designer"] + "</td></tr>")

        report_file.write("""</body>
        </html>""")
        report_file.close()


if __name__ == "__main__":
    # test_dir_path = 'E:\!TEST_FOLDER'
    test_dir_path = 'E:\!test'
    # test_dir_path = "V:\_ВНБО-1\_Разработка ПО"
    # test_dir_path = 'D:\MyFiles\Projects\PyCharmProjects\VersionExtractor\VersionExtractor\!TEST_FOLDER\\v_new'
    test_file_with_fuck_coding = "E:\!test\dc_fifo_16_16.v"

    tasker = HdlTasker()
    thread = QThread()
    tasker.moveToThread(thread)
    thread.start()
    file_list = tasker.find(test_dir_path, ["*.v", "*.vhd"])
    print(file_list)
    tasker.generate_report(file_list)
    # print(file_parser(test_file_with_fuck_coding))
