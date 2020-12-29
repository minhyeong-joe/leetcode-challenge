from collections import defaultdict, Counter


def favoriteGenres(userSongs, songGenres):
    result = defaultdict(list)
    songGenreMap = dict()
    # create a map 1-to-1 map from song to genre
    for genre, songs in songGenres.items():
        for song in songs:
            songGenreMap[song] = genre
    # print(songGenreMap)
    # init result dict with names and genres
    for user, songs in userSongs.items():
        for song in songs:
            if song in songGenreMap:
                result[user].append(songGenreMap[song])
    # print(result)
    # keep the most genres
    for user, genres in result.items():
        counter = Counter(genres)
        maxCount = max(counter.values())
        result[user] = [genre for genre in counter if counter[genre] == maxCount]
    # print(result)
    return result


userSongs = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma":  ["song5", "song6", "song7"]
}
songGenres = {
    "Rock":    ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno":  ["song2", "song4"],
    "Pop":     ["song5", "song6"],
    "Jazz":    ["song8", "song9"]
}
print(favoriteGenres(userSongs, songGenres))
userSongs = {
    "David": ["song1", "song2"],
    "Emma":  ["song3", "song4"]
}
songGenres = {}

print(favoriteGenres(userSongs, songGenres))
