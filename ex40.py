class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

lyrics_bday = "Happy birthday to you \nI don't want to get sued \nSoI'll stop right there"
happy_bday = Song([lyrics_bday])

lyrics_bulls = "They rally around tha family \nWith pockets full of shells"
bulls_on_parade = Song([lyrics_bulls])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()