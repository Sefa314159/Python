import sqlite3
import time

class createBook():

    def __init__(self,bookname,author,publisher,genre,edition):
        self.bookname       =       bookname
        self.author         =       author
        self.publisher      =       publisher
        self.genre          =       genre
        self.edition        =       edition

    def __str__(self):
        return "Book name : {}\nAuthor : {}\nPublisher : {}\nGenre : {}\nEdition : {}\n".format(self.bookname,self.author,self.publisher,self.genre,self.edition)

class createLibrary():

    def __init__(self):
        self.createConnection()

    def createConnection(self):
        self.connection =       sqlite3.connect("Library.db")
        self.cursor     =       self.connection.cursor()
        query           =       "Create Table if not exists Books(name TEXT,author TEXT,publisher TEXT,genre TEXT,edition INT)"
        self.cursor.execute(query)
        self.connection.commit()

    def cutConnection(self):
        self.connection.close()

    def showBooks(self):
        query           =       "Select * From Books"
        self.cursor.execute(query)
        books           =       self.cursor.fetchall()
        if(len(books) == 0):
            print("There are no books in the library...")
        else:
            for bookTuples in books:
                book    =       createBook(bookTuples[0],bookTuples[1],bookTuples[2],bookTuples[3],bookTuples[4])
                print(book)

    def bookQuery(self,name):
        query           =       "Select * From  Books where name = ?"
        self.cursor.execute(query,(name,))
        books           =       self.cursor.fetchall()
        if(len(books) == 0):
            print("There are no books in the library...")
        else:
            for bookTuples in books:
                book    =       createBook(bookTuples[0], bookTuples[1], bookTuples[2], bookTuples[3],bookTuples[4])
                print(book)

    def addBook(self,classBook):
        query            =       "Select * From Books where name = ?"
        self.cursor.execute(query,(classBook.bookname,))
        books           =       self.cursor.fetchall()
        if(len(books) == 0):
            query2 = "Insert into Books Values(?,?,?,?,?)"
            self.cursor.execute(query2, (classBook.bookname, classBook.author, classBook.publisher, classBook.genre, classBook.edition))
            self.connection.commit()
            print("Book is added...")
        else:
            print("Library already contains the book you wrote...")

    def deleteBook(self,bookName):
        query            =       "Select * From Books where name = ?"
        self.cursor.execute(query,(bookName,))
        books           =       self.cursor.fetchall()
        if(len(books) == 0):
            print("There are no books in the library that you can delete please try again...")
        else:
            query2 = "Delete From Books where name = ?"
            self.cursor.execute(query2, (bookName,))
            self.connection.commit()

    def increaseEdition(self,bookName):
        query           =       "Select * From Books where name = ?"
        self.cursor.execute(query,(bookName,))
        books           =       self.cursor.fetchall()
        if(len(books) == 0):
            print("There are no books in the library...")
        else:
            edition     =       books[0][4]
            edition     +=      1
            query2      =       "Update Books set edition = ? where name = ?"
            self.cursor.execute(query2,(edition,bookName))
            self.connection.commit()
