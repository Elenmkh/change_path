#!/usr/bin/env python3

def change_path(path):
    path = path.replace("\\", "/")
    path = path.replace('"', "")
    if path.startswith("T:"):
        path = path.replace("\\", "/")
        path = path.replace("T:", "/mnt/t")
    elif path.startswith(("mnt/t", "/mnt/t")):
        path = path.replace("/mnt/t", "T:")
        path = path.replace("/", "\\")
    else:
        return path
    return path

ask = '1'
while ask != '0':
    if ask == '1':
        print("Введите путь для изменения:")
        path = input()
    else:
        path = ask
    print(change_path(path))
    print("Что делать дальше?\nДля новой замены - введи путь, для выхода - нажми (0)")
    ask = input()


