import os
import fnmatch
import chardet
from PyQt5.QtCore import pyqtSlot, QObject, QThread
import datetime
import ProgressThread


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
        line_counter = 0
        for line in file:
            # print(line)
            line_counter += 1
            # print(line_counter)
            line = universal_decoder(line)
            list_of_file_data.append(line)
            header_data["file"] = file.name
            if "Description" in line:
                header_data["description"] = clean_string(line.split(":")[1])
            if "Version:" in line:
                header_data["version"] = clean_string(line.split(":")[1])
            if "Designer:" in line:
                header_data["designer"] = clean_string(line.split(":")[1])
            if "Developer:" in line:
                header_data["designer"] = clean_string(line.split(":")[1])
                # if "module " in line and "endmodule" not in line and line.lstrip(" ").startswith("m"):
                #     header_data["modules"].append(line.split(" ")[1].split("(")[0])
            if line_counter == 7:
                break
    file.close()
    return header_data


class HdlTasker(QObject):
    now = datetime.datetime.now()
    time = ""
    path = ""
    current_counter = 0  # счетчик для количества обработанных файлов

    @pyqtSlot()
    def find(self, path, extension) -> list:
        result = []
        self.path = path
        for root, dirs, files in os.walk(path):
            for ext in extension:
                for name in fnmatch.filter(files, ext):
                    result.append(os.path.join(root, name))  # в листе сохраняется путь до файла
        # self.dataReady.emit(result)
        return result

    @pyqtSlot()
    def generate_report(self, file_list):
        self.time = self.now.strftime("%d_%m_%Y_%H-%M")
        report_filename = "report_" + str(self.time) + ".html"
        report_file = open(str(report_filename), 'a+', errors="ignore")

        # пишет таблицу с зебромодом
        report_file.write("""<html>
        <head>
        <style>
        table {
            border-spacing: 0;
            width: 100%;
            border: 1px solid #ddd;
        }
        
        th {
            cursor: pointer;
        }
        
        th, td {
            text-align: left;
            padding: 16px;
        }
        
        tr:nth-child(even) {
            background-color: #f2f2f2
        }
                
        .btn-group button {
            background-color: #4CAF50; /* Green background */
            border: 1px solid green; /* Green border */
            color: white; /* White text */
            padding: 10px 24px; /* Some padding */
            cursor: pointer; /* Pointer/hand icon */
            float: left; /* Float the buttons side by side */
        }
        
        .btn-group button:not(:last-child) {
            border-right: none; /* Prevent double borders */
        }
        
        /* Clear floats (clearfix hack) */
        .btn-group:after {
            content: "";
            clear: both;        
            display: table;
        }
        
        /* Add a background color on hover */
        .btn-group button:hover {
            background-color: #3e8e41;
        }
        </style>
        </head>
        <body>""")

        # добавляет таблицу
        report_file.write("""<p><strong>Нажмите на имена колонок для сортировки</strong></p> """)
        report_file.write("""<table border=:'1' id="reportTable">""")
        report_file.write(
            """<caption><b style = "font-size:40px">Version extractor report<br>
            Folder: %s, Timestamp: %s </b></caption>""" % (
                self.path, self.time))
        report_file.write("""<tr>
                <th onClick ="sortTable(0)">File</th>
                <th onClick ="sortTable(1)">Description</th>
                <th onClick ="sortTable(2)">Version</th>
                <th onClick ="sortTable(3)">Designer</th>
                </tr>""")

        self.current_counter = 0
        for file in file_list:
            file_info = file_parser(file)
            self.current_counter += 1
            # TODO тут можно упростить конструкцию
            report_file.write(
                "<tr><td>" + file_info["file"] + "</td><td>" + file_info["description"] + "</td><td>" + file_info[
                    "version"] + "</td><td>" + file_info["designer"] + "</td></tr>")
        report_file.write("</table>")

        # скрипты для сортировки отчета
        report_file.write("""
        <script>
            function sortTable(n) {
                  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
                  table = document.getElementById("reportTable");
                  switching = true;
                  dir = "asc"; 
                  while (switching) {
                    switching = false;
                    rows = table.getElementsByTagName("TR");
                    for (i = 1; i < (rows.length - 1); i++) {
                      shouldSwitch = false;
                      x = rows[i].getElementsByTagName("td")[n];
                      y = rows[i + 1].getElementsByTagName("td")[n];
                      if (dir == "asc") {
                        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                          shouldSwitch= true;
                          break;
                        }
                      } else if (dir == "desc") {
                        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                          shouldSwitch= true;
                          break;
                        }
                      }
                    }
                    if (shouldSwitch) {
                      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                      switching = true;
                      switchcount ++;      
                    } else {
                      if (switchcount == 0 && dir == "asc") {
                        dir = "desc";
                        switching = true;
                      }
                    }
                  }
                }
            </script>           
        """)
        report_file.write("""</body>
        </html>""")
        report_file.close()


if __name__ == "__main__":
    # test_dir_path = 'E:\!VersionExtractorTestFolder\!TEST_FOLDER'
    # test_dir_path = 'E:\!VersionExtractorTestFolder\BurakovTestFolder'
    # test_dir_path = 'E:\!VersionExtractorTestFolder\!NewHeaderTest'
    test_dir_path = "V:\_ВНБО-1\_Разработка ПО"
    # test_dir_path = 'D:\MyFiles\Projects\PyCharmProjects\VersionExtractor\VersionExtractor\!TEST_FOLDER\\v_new'

    tasker = HdlTasker()
    # thread = QThread()
    # tasker.moveToThread(thread)
    # thread.start()
    file_list = tasker.find(test_dir_path, ["*.v", "*.vhd"])
    # print(file_list)

    thread1 = ProgressThread.MyThread(1, file_list)
    thread1.start()
    # tasker.generate_report(file_list)
    # print(file_parser(test_file_with_fuck_coding))
