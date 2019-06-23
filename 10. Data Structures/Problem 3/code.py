def word_frequency(word):
    word_dic    =   dict()
    for i in word:
        if(i in word_dic):
            word_dic[i] +=  1
        else:
            word_dic[i] =   1
    for i,j in word_dic.items():
        print("{} : {}".format(i,j))

s   =   "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
word_frequency(s)
