import os
import fnmatch

test_path = '//MRS//Project_Quartet//КВАРТЕТ//Разработка//Блок 308-051-01 (СЦВМ)//ПО'


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))  # в листе сохраняется путь до файла
                print(name)  # выводит имя файла
    return result


print(find("*.v", test_path))
