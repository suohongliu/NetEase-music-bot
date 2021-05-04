import requests
import json

#prefix = 'http://music.163.com/'
prefix = 'http://127.0.0.1:8000/'


#return list => all songs' name by (playlist_id)
def get_songs_name(id):
    #store songs' name in playlist
    songs_name = []

    songs_id = get_songs_id(id)

    id_str = ''
    for s in range(len(songs_id)):
        id_str += str(songs_id[s])
        if s != len(songs_id) - 1:
            id_str += ','

    res = requests.get(prefix + 'api/song/detail?id=' + id_str)
    data = json.loads(res.text)
    songs = data['songs']

    for s in songs:
        songs_name.append(s['name'])

    return songs_name


#return list => all songs' id by playlist's id
def get_songs_id(id):
    res = requests.get(prefix + 'api/playlist/detail?id=' + str(id))
    data = json.loads(res.text)

    playlist = data['playlist']
    songs = playlist['trackIds']
    #store songs' id in playlist
    songs_id = []

    for s in songs:
        songs_id.append(s['id'])

    return songs_id


#return song's name by id
def get_song_name(id):
    res = requests.get(prefix + 'api/song/detail?id=' + str(id))
    data = json.loads(res.text)
    song = data['songs'][0]
    return song['name']


"""
a = get_songs_name(5452173199)
print(len(a))
print(a)"""
