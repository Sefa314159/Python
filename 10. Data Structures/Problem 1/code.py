class File():
    def __init__(self):
        with open("file.txt","r",encoding="utf-8")as file:
            file_content    =   file.read()
            words   =   file_content.split("\n")
            self.big_letters =   []
            for i in words:
                i   =   i.strip(" ")
                i   =   i.strip("\n")
                for j in i:
                    if(j in i[0]):
                        self.big_letters.append(j)
                    else:
                        continue
            print(self.big_letters)

file    =   File()
