def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    '''
    while playlist.count(song) > 3:
        playlist.remove(song)

playlist = ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
song = 'Lola'
cap_song_repetition(playlist, song)
print(playlist)



def cap_song_repetition1(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    '''
    while playlist.count(song) > 3:
        playlist.remove(playlist.index(song))

playlist = ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
song = 'Lola'
#cap_song_repetition1(playlist, song)
#print(playlist)



def cap_song_repetition2(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    '''
    while playlist.count(song) >= 3:
        playlist.remove(song)

playlist = ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
song = 'Lola'
cap_song_repetition2(playlist, song)
print(playlist)


def cap_song_repetition3(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    '''
    while playlist.count(song) > 3:
         playlist.pop(playlist.index(song))

playlist = ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
song = 'Lola'
cap_song_repetition3(playlist, song)
print(playlist)

def cap_song_repetition4(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    '''
    while playlist.count(song) > 3:
         playlist.pop(song)

playlist = ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
song = 'Lola'
cap_song_repetition4(playlist, song)
print(playlist)
