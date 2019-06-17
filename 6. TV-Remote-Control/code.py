import random
import time

class Control():

    def __init__(self,  tv_status="Closed", tv_sound=0, channel_list=["TRT"],   channel="TRT"):
        self.tv_status      =   tv_status
        self.tv_sound       =   tv_sound
        self.channel_list   =   channel_list
        self.channel        =   channel

    def open_tv(self):
        if(self.tv_status   ==  "Open"):
            print("TV is already open")
        else:
            print ("TV is opening...")
            time.sleep(1)
            self.tv_status  =   "Open"

    def close_tv(self):
        if(self.tv_status   ==  "Closed"):
            print ("TV is already closed")
        else:
            print ("TV is closing...")
            time.sleep(1)
            self.tv_status="Closed"

    def sound_settings(self):
        while True:
            response    =   input("Decrease Volume : '<'\nIncrease Volume : '>'\nExit : e\n")
            if(response     ==  "<"):
                if(self.tv_sound    !=  0):
                    self.tv_sound   -=  1
                    print ("Volume :",self.tv_sound)
            elif(response   ==  ">"):
                if(self.tv_sound    !=  31):
                    self.tv_sound   +=  1
                    print ("Volume :",self.tv_sound)
            elif(response   ==  "e"):
                print ("Volume is updated :",self.tv_sound)
                break
            else:
                print("invalid operation")
    def add_channel(self,channel_name):
        print ("Adding channel...")
        time.sleep(1)
        self.channel_list.append(channel_name)
        print ("Channel is added.")

    def random_channel(self):
        rand    =   random.randint(0,len(self.channel_list)-1)
        self.channel    =   self.channel_list[rand]
        print("Channel :",self.channel)

    def __len__(self):
        return len(self.channel_list)

    def __str__(self):
        return "Tv Status : {}\nTv Volume : {}\nChannel List : {}\nCurrent Channel : {}\n".format(self.tv_status,self.tv_sound,self.channel_list,self.channel)

control =   Control()
print("""
TV Remote Control Application
1. Open TV
2. Close TV
3. Volume Settings
4. Add Channel
5. Learn Channel Number
6. Random Channel
7. TV Settings
for closing the application, press 'q'
""")
while True:
    process =   input("\nChoose the option:")
    if(process  ==  "q"):
        print("Program is closing...")
        time.sleep(1)
        break
    elif(process    ==  "1"):
        control.open_tv()
    elif(process    ==  "2"):
        control.close_tv()
    elif(process    ==  "3"):
        control.sound_settings()
    elif(process    ==  "4"):
        channel_names   =   input("Enter channel names separated by ' :")
        channel_list    =   channel_names.split(",")
        for i in channel_list:
            control.add_channel(i)
    elif(process    ==  "5"):
        print("Channel Number :",len(control))
    elif(process    ==  "6"):
        control.random_channel()
    elif(process    ==  "7"):
        print(control)
    else:
        print("invalid operation...")
        time.sleep(1)
