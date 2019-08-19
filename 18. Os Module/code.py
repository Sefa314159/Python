import os

file1 = open("pdf_dosyaları.txt", "w", encoding = "utf-8")
file2 = open("mp4_dosyaları.txt", "w", encoding = "utf-8")
file3 = open("txt_dosyaları.txt", "w", encoding = "utf-8")

for folder_path, folder_name, file_name in os.walk("C:/Users/Sefa3/Desktop"):
    for i in file_name:
        if(i.endswith(".pdf")):
            file1.write("{}\n".format(i))
                
        if(i.endswith(".mp4")):
            file2.write("{}\n".format(i))
                
        if(i.endswith(".txt")):
            file3.write("{}\n".format(i))
            
file1.close()            
file2.close()            
file3.close()
