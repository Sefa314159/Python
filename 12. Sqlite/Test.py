from Library import *

print("""
**************************************
Welcome to the Book-Library Application

Options;

1. Show the Library
2. Find a book from the Library
3. Add a book in the Library
4. Delete a book from the Library
5. Increase book's edition in Library

Press 'q' for exit
**************************************
""")

library = createLibrary()
while True:
        option      =       input("Choose an option :\n")
        if(option == "q"):
            print("Program Exit...")
            time.sleep(2)
            print("Have a good day...")
            break
        else:
            try:
                option = int(option)
                if (option == 1):
                    library.showBooks()
                elif (option == 2):
                    name = input("Which book you want to find ? : \n")
                    print("Searching the book that you wrote...\n")
                    time.sleep(2)
                    library.bookQuery(name)
                elif (option == 3):
                    name = input("Book's Name : ")
                    author = input("Author : ")
                    publisher = input("Publisher : ")
                    genre = input("Genre :")
                    edition = input("Edition : ")
                    newBook = createBook(name, author, publisher, genre, edition)
                    print("Adding...")
                    time.sleep(2)
                    library.addBook(newBook)
                elif (option == 4):
                    name = input("Which book you want to delete ? :")
                    answer = input("Are you sure you want to delete {} ? \n(E/H) : ".format(name))
                    try :
                        if (answer == "E"):
                            print("Deleting...")
                            time.sleep(2)
                            library.deleteBook(name)
                        elif(answer == "H"):
                            print("Deletion is cancelled...")
                        else:
                            print("Invalid Operation")
                    except ValueError:
                        print("Invalid Operation")
                        print("Please try again")

                elif (option == 5):
                    name = input("Which book do you want increase it's edition ? :")
                    print("Increasing edition...")
                    time.sleep(2)
                    library.increaseEdition(name)
            except ValueError:
                print("Invalid Operation...")
                print("Please try again!")
