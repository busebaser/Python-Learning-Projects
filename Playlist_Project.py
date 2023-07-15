import sqlite3
import time
import random
class Song():
    def __init__(self,title,singer,album,production_company,duration):
        self.title = title
        self.singer = singer
        self.album = album
        self.production_company = production_company
        self.duration = duration

    def __str__(self):
        return "Song title: {}\n Singer {}\n The Album: {}\n Production Company: {}\n Song Duration:{}\n".format(self.title,self.singer,self.album,self.production_company,self.duration)

class Playlist():
    def __init__(self):
        self.to_connect()
        self.playlist = []
    def to_connect(self):
        self.connection = sqlite3.connect("playlist.db")
        self.cursor = self.connection.cursor()
        a = "CREATE TABLE IF NOT EXISTS songs(Title TEXT,Singer TEXT,Album TEXT,Production_Company TEXT,Duration INT)"
        self.cursor.execute(a)
        self.connection.commit()
    def to_disconnect(self):
        self.connection.close()
    def show_the_songs(self):
        a = "Select * From songs"
        self.cursor.execute(a)
        songs = self.cursor.fetchall()
        if len(songs) == 0:
            print("There are no songs in your playlist.")
        else:
            b = Song(songs[0][0],songs[0][1],songs[0][2],songs[0][3],songs[0][4])
            print(b)
    def search_for_song(self,title):
        a = "Select * from songs where title=?"
        self.cursor.execute(a,(title,))
        songs = self.cursor.fetchall()
        if len(songs) == 0:
            print("This song does not exist.")
        else:
            b = Song(songs[0][0],songs[0][1],songs[0][2],songs[0][3],songs[0][4])
            print(b)
    def add_new_song(self,new_song):
        a = "Insert into songs Values(?,?,?,?,?)"
        self.cursor.execute(a,(new_song.title,new_song.singer,new_song.album,new_song.production_company,new_song.duration))
        self.connection.commit()
    def delete_the_song(self,title):
        a = "Delete from songs where title=?"
        self.cursor.execute(a,(title,))
        self.connection.commit()
    def search_for_production_company(self,production_company):
        self.cursor.execute("Select * From where production_company=?",(production_company,))
        music = self.cursor.fetchall()
        if len(music) == 0:
            print("This company does not exist.")
        else:
            c = Song(music[0][0],music[0][1],music[0][2],music[0][3],music[0][4])
            print(c)
    def calculate_total_songduration(self):
        query = "SELECT SUM(duration) FROM songs"
        self.cursor.execute(query)
        total = self.cursor.fetchone()[0]
        self.cursor.close()
        self.connection.close()
        return total

    def currently_playing_song(self):
        a = "Select * From songs"
        self.cursor.execute(a)
        songs = self.cursor.fetchall()
        songs_list = []
        songs_list.extend(songs)
        print("The currently playing song: {}".format(random.choice(songs_list)))


playlist = Playlist()

print("""
***********************************
Welcome to the Your Playlist Programme
Actions:
1. Show the Songs
2. Search for a Song
3. Add a New Song
4. Delete the Song
5. Search for the Production Company
6. Calculate the total song duration in the Database
7. Show the Currently Playing Song
To exit, press 'q'
***********************************""")


while True:
    action = input("Please write the number corresponding to the action you would like to perform.")
    if action == "q":
        print("The program is being terminated...")
        break
    elif action == "1":
        playlist.show_the_songs()
    elif action == "2":
        title = input("Which song do you want to search for?")
        print("Searching for...")
        time.sleep(2)
        playlist.search_for_song(title)
    elif action == "3":
        title = input("Song Title:")
        singer = input("Singer:")
        album = input("Album:")
        production_company = input("Production Company:")
        duration = (input("Song duration: (For example, enter '3.24' to represent 3 minutes and 24 seconds."))
        new_song = Song(title,singer,album,production_company,duration)
        print("The new song is adding...")
        time.sleep(2)
        playlist.add_new_song(new_song)
    elif action == "4":
        title = input("Which song do you want to delete?")
        playlist.delete_the_song(title)
        print("The song is deleted.")
    elif action == "5":
        production_company = input("Which production company do you want to search for?")
        print("Searching for...")
        time.sleep(2)
        playlist.search_for_production_company(production_company)
    elif action == "6":
        print("The programme is calculating...")
        time.sleep(2)
        total = playlist.calculate_total_songduration()
        print("Total : ",total)
    elif action == "7":
        playlist.currently_playing_song()
    else:
        print("Invalid action")









