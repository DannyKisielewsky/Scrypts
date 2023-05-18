import os
import csv

InventoryList=[]
AnswerList={'Tak', 'tak', 'Nie', 'nie'}
pola = ['Dane użytkownika', 'PC', 'iPad SN', 'Phone SN']

dirname = 'example C:\\Users\\xx\\xx\\xx\\xx\\xx'
filename = input(' Wprowadź nazwe dla swojego swojego pliku ')
filepath = os.path.join(dirname,filename)
Output = (filepath + '.csv')

while os.path.isfile(Output) == True:
    filename=input('Plik juz istnieje, wybierz inna nazwe')
    filepath = os.path.join(dirname,filename)
    Output = (filepath + '.csv')
    os.path.isfile(Output)
    if os.path.isfile(Output) == False:
        print('Mozna stworzyc plik o nazwie', filename)
        break

ID=input('Wprowadz dane uzytkownika: ')
InventoryList.append(ID)
PC=input('Wprowadz nazwe PC: ')
InventoryList.append(PC)
Tablet=input('Wprowadz Serial Number tableta: ')
InventoryList.append(Tablet)
Phone=input('Wprowadz Serial Number telefonu: ')
InventoryList.append(Phone)

def summary():
    print('')
    print('Podsumowanie')
    print('')
    print('1. Dane użytkownika: ', InventoryList[0])
    print('2. Nazwa PC:         ', InventoryList[1])
    print('3. iPad  SN:         ', InventoryList[2])
    print('4. Phone SN:         ', InventoryList[3])
    print('')
def SaveOperation():
    with open (Output, mode='w') as plikCSV:
        writer = csv.writer(plikCSV, delimiter=';')
        writer.writerow(InventoryList)
        print('Twoj plik zostal zapisany', Output)
        input('Wcisnij enter by zamknac program')
summary()        
check=input('Czy dane są poprawne? ')
while check == "nie" or check == "Nie":
    print('Ktora kolumne chcesz edytować?')
    edit = input('1,2,3,4? ')
    if edit == '1':
        InventoryList[0]=str(input('Wprowadz poprawne dane '))
        print(summary())
        print("")
        check = input('Czy teraz dane sa poprawne? ')
        if check == "tak" or check == "Tak":
            SaveOperation()
            break
    elif edit == '2':
        InventoryList[1]=str(input('Wprowadz poprawne dane '))
        print(summary())
        print("")
        check = input('Czy teraz dane sa poprawne? ')
        if check == "tak" or check == "Tak":
            SaveOperation()
            break
    elif edit == '3':
        InventoryList[2]=str(input('Wprowadz poprawne dane '))
        print(summary())
        print("")
        check = input('Czy teraz dane sa poprawne? ')
        if check == "tak" or check == "Tak":
            SaveOperation()
            break
    elif edit == '4':
        InventoryList[3]=str(input('Wprowadz poprawne dane '))
        print(summary())
        print("")
        check = input('Czy teraz dane sa poprawne? ')
        if check == "tak" or check == "Tak":
            SaveOperation()
            break
SaveOperation()
