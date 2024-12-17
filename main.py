import datetime
import os
import time
import pyperclip

print("Írja be a PGP titkosított üzenetet a PGPMESSAGE.txt fájlba!\nMajd nyomjon ENTERT")
input()

def convert():
    clipboard = pyperclip.paste()
    date = datetime.datetime.now()
    try:
        with open("PGPMESSAGE.txt", "r") as file:
            content = file.read()
        if content == "":
            return "NODATA"
        else:
            dirName = f"{date.year}_{date.month}_{date.day}"
            os.mkdir(f"{dirName}")
            fileName = f"{date.year}{date.month}{date.day}_{date.hour}_{date.minute}_{date.second}.asc"
            sv = open(f"{fileName}", "w")
            sv.write(content)
            sv.close()
            print(f"{fileName} fájl létrehozva!")
            os.system(f"move {fileName} {dirName}")

    except FileExistsError:
        with open("PGPMESSAGE.txt", "r") as file:
            content = file.read()
        if content == "":
            return "NODATA"
        else:
            fileName = f"{date.year}{date.month}{date.day}_{date.hour}_{date.minute}_{date.second}.asc"
            sv = open(f"{fileName}", "w")
            sv.write(content)
            sv.close()
            print(f"{fileName} fájl létrehozva!")
            os.system(f"move {fileName} {dirName}")

def start():
    result = convert()
    if result == "NODATA":
        print("Nincs egy karakter sem a PGPMESSAGE.txt fájlban!")

start()
