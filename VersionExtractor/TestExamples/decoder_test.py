import chardet


def universal_decoder(line):
    print(chardet.detect(line)['encoding'])
    if chardet.detect(line)['encoding'] == 'ascii':
        return line.decode("ascii", "ignore")
    if chardet.detect(line)['encoding'] == 'windows-1251':
        return line.decode("windows-1251", errors="ignore")
    if chardet.detect(line)['encoding'] == 'MacCyrillic':
        return line.decode("windows-1251", errors="ignore")
    if chardet.detect(line)['encoding'] == 'utf-8':
        return line.decode("utf-8", "ignore")
    return ""


def file_parser(filepath):
    list_of_file_data = []  # построчный лист с содержимым файла
    # header_data = {"modules": []}
    header_data = {"file": "имя файла", "description": "описание не определено", "version": "версия не определена",
                   "designer": "разработчик не определен"}
    with open(filepath, "rb") as file:  # открываем файл
        line_counter = 0
        for line in file:
            print(line)
            line_counter += 1
            # print(line_counter)
            line = universal_decoder(line)
            list_of_file_data.append(line)
            header_data["file"] = file.name
            if "Description" in line:
                # print(line)
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


def clean_string(dirty_string):
    clean = str(dirty_string).strip()
    clean = str(clean).replace('\n', '')
    return clean


if __name__ == "__main__":
    filepath = "E:\!VersionExtractorTestFolder\\noCorrectFirstSYmbol\\p_buffer_sw.v"
    print("header data: ")
    print(file_parser(filepath=filepath))
