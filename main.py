import datetime
import os
import time
import pyperclip

os.system('cls')

print("Másolja ki a PGP titkosított üzenetet a vágólapra\nMajd nyomjon ENTERT")
input()

def convert():
    date = datetime.datetime.now()
    content = pyperclip.paste()

    if content != "":
        if content.startswith("-----BEGIN PGP MESSAGE-----"):
            try:
                dirName = f"{date.year}_{date.month}_{date.day}"
                os.mkdir(f"{dirName}")
                fileName = f"{date.year}{date.month}{date.day}_{date.hour}_{date.minute}_{date.second}.asc"
                sv = open(f"{fileName}", "w")
                sv.write(content)
                sv.close()
                print(f"{fileName} fájl létrehozva!")
                os.system(f"move {fileName} {dirName}")

            except FileExistsError:
                content = pyperclip.paste()
                fileName = f"{date.year}{date.month}{date.day}_{date.hour}_{date.minute}_{date.second}.asc"
                sv = open(f"{fileName}", "w")
                sv.write(content)
                sv.close()
                print(f"{fileName} fájl létrehozva!")
                os.system(f"move {fileName} {dirName}")
        else:
            return "NOTPGPMESSAGE"
    else:
        return "NODATA"

def start():
    result = convert()
    
    if result == "NODATA":
        print("A vágólap üres")
    
    elif result == "NOTPGPMESSAGE":
        print("A vágólapon nem PGP titkosított üzenet szerepel")

start()
