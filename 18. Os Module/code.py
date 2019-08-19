import os

file1 = open("pdf_dosyaları.txt", "w", encoding = "utf-8")
file2 = open("mp4_dosyaları.txt", "w", encoding = "utf-8")
file3 = open("txt_dosyaları.txt", "w", encoding = "utf-8")

for klasör_yolu, klasör_isimleri, dosya_isimleri in os.walk("C:/Users/user/Desktop"):
    for i in dosya_isimleri:
        if(i.endswith(".pdf")):
            file1.write("{}\n".format(i))
                
        if(i.endswith(".mp4")):
            file2.write("{}\n".format(i))
                
        if(i.endswith(".txt")):
            file3.write("{}\n".format(i))
            
file1.close()            
file2.close()            
file3.close()
