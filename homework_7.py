import sqlite3

connect = sqlite3.connect('library.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS library(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL)""")

def addbook():
  title = input("Введите название книги: ")
  author = input("Введите имя автора: ")
  year  = int(input("Введите год выпуска: "))
  cursor.execute("""INSERT INTO library(title,author,year)
                  VALUES (?,?,?)""",(title,author,year))
  connect.commit()
# addbook()        

def find_book_by_title():
  title = input("Введите название книги для поиска: ")
  cursor.execute("""SELECT * FROM library WHERE title = ? """,(title,))
  find_title = cursor.fetchone()
  print(find_title)
# find_book_by_title()


def update_book_title(cursor, connect):
    title = input("Введите title книги: ")
    new_year = int(input("Введите новый год: "))
    cursor.execute("UPDATE library SET year = ? WHERE title = ?", (new_year, title))
    connect.commit()
    print(f"Год выпуска изменен на {new_year} для книги '{title}'.")

# update_book_title(cursor, connect)
def delete_book(): 
    title = input("Введите название книги для удаления: ")
    cursor.execute("DELETE FROM library WHERE title = ?", (title,)) 
    connect.commit() 
    print("удаленац")

# delete_book()
while True:
   print("1 - добавить книгу\n2 - найти книгу\n3 - обновить книгу\n4 - удалить книгу\n5 - выйти из прораммы")
   book = int(input("Введите номер для выбора действия:"))
   if book == 1:
      addbook()
   elif book == 2:
      find_book_by_title()
   elif book == 3:
      update_book_title()
   elif book == 4:
      delete_book()
   elif book == 5:
      break
   print("Вы вышли из программы")