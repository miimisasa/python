notes = list()


def main():
    welcome()
    command = int(input())
    logic(command)


def welcome():
    print("Выберите действие из списка команд и впишите его номер в консоль.\n")
    print("Список команд :\n"
          "1. Добавить заметку\n"
          "2. Изменить заметку\n"
          "3. Просмотреть содержимое заметки\n"
          "4. Удалить заметку\n"
          "5. Поиск заметки по ключевым словам\n")


def addNote():
    print("Введите содержимое новой заметки :")
    note = str(input())
    print("Содержимое вашей заметки :", note)
    notes.append(note)


def deleteNote():
    print("Выберите номер заметки :")
    number = int(input()) - 1

    def inner(number):
        del notes[number]

    checkNumberOfNote(number, inner)


def editNote():
    print("Выберите номер заметки :")
    number = int(input()) - 1

    def inner(number):
        print("Внесите изменения")
        notes[number] = str(input())
        print("Содержимое вашей заметки :", notes[number])

    checkNumberOfNote(number, inner)


def openNote():
    print("Выберите номер заметки :")
    number = int(input()) - 1

    def inner(number):
        print("Содержимое заметки #", number, ":", notes[number])

    checkNumberOfNote(number, inner)


def logic(command):
    if command == 1:
        addNote()
    elif command == 2:
        editNote()
    elif command == 3:
        openNote()
    elif command == 4:
        deleteNote()
    elif command == 5:
        searchInNotes()
    else:
        print("Error")
    chooseAction()


def chooseAction():
    print("Вы хотите сделать что-то еще?")
    choose = str(input())
    if choose == "Да":
        print("Чтобы вы хотели сделать?")
        print("Список команд :\n"
              "1. Добавить заметку\n"
              "2. Изменить заметку\n"
              "3. Просмотреть содержимое заметки\n"
              "4. Удалить заметку\n"
              "5. Поиск заметки по ключевым словам\n")
        command = int(input())
        logic(command)
    elif choose == "Нет":
        print("Шлюхи аргумент. Пока")
    else:
        print("Мата поменьше")


def checkNumberOfNote(number, inner):
    if len(notes) >= number >= 0:
        inner(number)
    else:
        print("Умняшечка ты моя, а ты писал заметку под этим номером чтобы просить ее??")

def searchInNotes():
    print("vv kl slovo")
    word = str(input())
    searchNote = list(filter(lambda x: word in x, notes))
    print("Найденные заметки по запросу", "\tword\t", ":", searchNote)
main()
