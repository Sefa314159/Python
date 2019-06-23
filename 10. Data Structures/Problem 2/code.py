class File():
    def __init__(self):
        with open("file.txt","r",encoding="utf-8")as file:
            file_content            =   file.read()
            words                   =   file_content.split()
            self.only_words         =   list()
            for i in words:
                i   =   i.strip("\n")
                i   =   i.strip(" ")
                i   =   i.strip(".")
                i   =   i.strip(",")
                self.only_words.append(i)
    def word_frequency(self):
        word_dic    =   dict()
        for i in self.only_words:
            if(i in word_dic):
                word_dic[i] +=  1
            else:
                word_dic[i] =   1
        for i,j in word_dic.items():
            print("The Word {} is used {} times".format(i,j))
            print("------------------------------------")
file    =   File()

file.word_frequency()
