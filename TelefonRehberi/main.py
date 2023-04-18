import pickle
import os


def DisplayMenu()->None:
    print("1. Kayıtları Listele")
    print("2. Kayıt Ara")
    print("3. Kayıt Ekle")
    print("4. Kayıt Sil")
    print("5. Cıkıs")
    print()


def MenuLoop()->str:
    while True:
        DisplayMenu()
        option=input("Secenek (1-5):")
        print("\n")
        if option.isdigit() and 1<= int(option) <=5:
            break
        else:
            print("Geçersiz secenek!\n")
    return option


def MainLoop()->None:
    while True:
        option=MenuLoop()
        if option=="1":
            ListRecord()
        elif option=="2":
            SearchRecord()
        elif option=="3":
            AddRecord()
        elif option=="4":
            DeleteRecord()
        elif option=="5":
            break
        else:
            print("Geçersiz secenek!\n")


def ListRecord() -> None:
    recordsList=ReadFile()
    print(f"number of records: {len(recordsList)}\n")
    print(f"{'Name':^10} {'Surname':^10} {'Telephone':^11}")
    for record in recordsList:
        print(f"{record.get('name',' '):10.10} {record.get('surname',' '):10.10} {record.get('telno',' '):11.11}")
    print()


def SearchRecord() -> None:
    print("Search Record")
    name=input("Name: ")
    surname=input("Surname: ")
    recordList=SearchRecordFromFile(name, surname)

    print("Telephone Number: ",end='')
    for record in recordList:
        print(f"{record.get('telno'):11.11}" ,end='')
    print("\n")


def AddRecord() -> None:
    print("Add New Record")
    name=input("Name: ")
    surname=input("Surname: ")
    telno=input("Phone number: ")
    print(f"Yeni Kayıt: {name} {surname} - {telno}")
    if AreYouSure():
        AddRecordToFile(name, surname, telno)
        print("record added\n")


def DeleteRecord() -> None:
    print("Delete Record")
    name=input("Name: ")
    surname=input("Surname: ")
    recordList=SearchRecordFromFile(name, surname)

    print("Telephone Number: ",end='')
    for record in recordList:
        print(f"{record.get('telno'):11.11}" ,end='')
    print("\n")
    if AreYouSure():
        DeleteRecordFromFile(recordList)
        print("record deleted\n")


def AreYouSure() -> bool:
    while True:
        answer=input("Are you sure? (Y)es / (N)o\n")
        print()
        if answer.upper()=="Y":
            return True
        elif answer.upper()=="N":
            return False
        

def ReadFile() -> list:
    if os.path.isfile("data.bin"):
        with open("data.bin", "rb") as fileObject:
            recordsList = pickle.load(fileObject)
    else:
        recordsList = list()
    return recordsList


def WriteFile(recordListParam : list) -> None:
    with open("data.bin", "wb") as fileObject:
        pickle.dump(recordListParam, fileObject)


def SearchRecordFromFile(nameparam:str, surnameparam:str) -> list:
    recordsList=ReadFile()
    responseList=list()
    for record in recordsList:
        if record.get("name").upper()==nameparam.upper() and record.get("surname").upper()==surnameparam.upper():
            responseList.append(record)
    return responseList


def AddRecordToFile(nameparam:str, surnameparam:str, telnoparam:str) -> None:
    recordsList=ReadFile()
    recordDict = dict(name = nameparam, surname=surnameparam, telno=telnoparam)
    recordsList.append(recordDict)
    WriteFile(recordsList)


def DeleteRecordFromFile(recordListParam : list) -> None:
    recordsList=ReadFile()
    for record in recordsList:
        for recordForDelete in recordListParam:
            if record.get("name").upper()==recordForDelete.get("name").upper() and record.get("surname").upper()==recordForDelete.get("surname").upper():
                recordsList.remove(recordForDelete)
                continue
    WriteFile(recordsList)


MainLoop()