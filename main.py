import datetime
import os
import time

print("Írja be a PGP titkosított üzenetet a PGPMESSAGE.txt fájlba!\nMajd nyomjon ENTERT")
input()

def convert():
    date = datetime.datetime.now()
    try:
        dirName = f"{date.year}_{date.month}_{date.day}"
        os.mkdir(f"{dirName}")
        file = open("PGPMESSAGE.txt", "r")
        fileName = f"{date.year}{date.month}{date.day}_{date.hour}_{date.minute}_{date.second}.asc"
        sv = open(f"{fileName}", "w")
        sv.write(file.read())
        sv.close()
        os.system(f"move {fileName} {dirName}")
        print(f"{fileName} fájl létrehozva!")
    except FileExistsError:
        file = open("PGPMESSAGE.txt", "r")
        fileName = f"{date.year}{date.month}{date.day}_{date.hour}_{date.minute}_{date.second}.asc"
        sv = open(f"{fileName}", "w")
        sv.write(file.read())
        sv.close()
        print(f"{fileName} fájl létrehozva!")
        os.system(f"move {fileName} {dirName}")

convert()

