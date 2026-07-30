class playlist:
    def __init__(self, name, genre):

        self.name = name
        self.genre = genre
        self.songs = []

    def add_song(self, song):

        self.songs.append(song)

        print('Your Song {} has been added to {}'.format( song, self.name))

    def remove_song(self, song):

        if song in self.songs:

            self.songs.remove(song)
            print('{} has been removed'.format(song))
        else:
            print('{} not found'.format(song))

    def display(self):

        print(self.name, self.genre)
        if self.songs:

            for i, song in enumerate(self.songs, 1):

                print(i,song)

        else:
            print('No songs yet, please add some')

    def __delete__(self):

        print('Playlist {} has been deleted '.format(self.name))

my_playlist = playlist("Night drive", 'House')

while True:

    print("\n1. Add Song  2. Remove Song  3. View Playlist  4. Delete ")

    choice = input('Enter your choice: ')

    if choice == '1':
        song = input('Enter Song Name: ')
        my_playlist.add_song(song)

    elif choice == '2':
        song = input('Which Song to delete:')
        my_playlist.remove_song(song)

    elif choice == '3':
        my_playlist.display()

    elif choice == '4':

        del my_playlist
        break
    else:
        print('Invalid choice.')