import random
import time
class TV_remote():
    def __init__(self,tv = "Off",tv_volume = 0,channel_list = ["Trt","Tv8"],resent_channel = "Trt",resent_wifi = "Off"):
        self.tv = tv
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.resent_channel = resent_channel
        self.resent_wifi = resent_wifi
    def internet_connection(self):
        if (self.resent_wifi == "On"):
            print("Your wifi is already connected")
        else:
            print("The internet is connecting..")
            self.resent_wifi = "On"
            TV_remote.internet()
    def internet(self):
        print("TurkTelekom123 \nVodafone1\nTTNet")
        users_respond = input("Please enter the name of the Wi-Fi network you want to connect to.")
        if users_respond == "TurkTelekom123" or "Vodafone1" or "TTNet" :
            sys_password = 123
            password = int(input("Password:"))
            if password == sys_password:
                print("Your connection is succeed.")
    def turn_on_tv(self):
        if (self.tv == "On"):
            print("The television is already on...")
        else:
            print("The television is turning on..")
            self.tv = "On"
    def turn_off_tv(self):
        if self.tv == "Off":
            print("The television is already off.")
        else:
            print("The television is turning off...")
            self.tv = "Off"
    def sound_settings(self):
        while True:
            respond = input("Lower the volume:'<' \nIncrease the volume:'>' \nExit: 'exit'")
            if respond == "<":
                if self.tv_volume != 0 :
                    self.tv_volume -= 1
                    print("The Volume:",self.tv_volume)
            elif respond == ">" :
                if self.tv_volume != 30 :
                    self.tv_volume += 1
                    print("Ses",self.tv_volume)
            else:
                print("The volume is updated.:",self.tv_volume)
                break
    def add_new_channel(self,channel_name):
        print("A channel is adding...")
        time.sleep(1)
        self.channel_list.append(channel_name)
        print("The channel is added.")
    def random_channel(self):
        random1 = random.randint(0,len(self.channel_list)-1)
        self.channel = self.channel_list[random]
        print("The resent channel:",self.channel)
    def remove_channel(self):
        print(self.channel_list)
        to_be_removed = input("Please enter the name of the channel you want to remove to:")
        self.channel_list.remove(to_be_removed)
        print("The channel is removed.",self.channel_list)
    def __len__(self):
        return len(self.channel_list)
    def __str__(self):
        return "Tv :{}\nTv Volume:{} \nChannel List: {}\n The Resent Channel:{}\n Internet Connection: {} \n".format(self.tv,self.tv_volume,self.channel_list, self.resent_channel,self.resent_wifi)
TV_remote = TV_remote()
print(""" 
Television 
1. Turn on the TV
2. Turn off the TV
3. Adjust the sound settings
4. Add a New Channel
5. Remove the Channel
6. How many channels are there?
7. Random Channel
8. Connect your television to Wi-Fi
9. Access Youtube,Netflix,Disney+ and more
10. Television Settings
To exit, press 'q'
""")

while True:
    operation = input("Please select the television operation you would like to perform:")
    if operation == "q":
        print("Program is being terminated..")
        break
    elif operation == "1" :
        TV_remote.turn_on_tv()
    elif operation == "2" :
        TV_remote.turn_off_tv()
    elif operation== "3":
        TV_remote.sound_settings()
    elif operation == "4" :
        channel_name = input("Please enter the channel names separated by commas(,):")
        channel_list = channel_name.split(",")
        for adding_ones in channel_list:
            TV_remote.add_new_channel(adding_ones)
    elif operation == "5" :
        TV_remote.remove_channel()
    elif (operation== "6") :
        print("Channel Count:",len(TV_remote))
    elif(operation == "7"):
        TV_remote.random_channel()
    elif(operation == "8"):
            TV_remote.internet_connection()
    elif operation == "9" :
        if TV_remote.resent_wifi == "Off":
            print("Firstly you have to turn on the Wifi")
        else:
            print("Youtube\nNetflix\nDisney+\nAmazonPrime\nExxen\nSpotify")
            users_selection = input("Please choose the program you want to access to:")
            if users_selection == "Youtube" or "Netflix" or "Disney+" or "AmazonPrime" or "Exxen" or "Spotify" :
                print("Program is starting...")
                time.sleep(1)
                print("Have a good time!")
    elif operation == "10" :
        print(TV_remote)
    else:
        print("Invalid operation")




