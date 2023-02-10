def solution(genres, plays):
    genre_plays = {}
    genre_songs = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre_plays.get(genre):
            genre_plays[genre] += play
            genre_songs[genre] += [idx]
        else:
            genre_plays[genre] = play
            genre_songs[genre] = [idx]

    genres = tuple(sorted(genre_plays.keys(), key=lambda genre: genre_plays[genre], reverse=True))
    genre_songs[genre].sort()
    for genre in genres:
        genre_songs[genre] = sorted(genre_songs[genre], key=lambda song: plays[song], reverse=True)

    answer = []
    for genre in genres:
        if len(genre_songs[genre]) > 1:
            answer.extend(genre_songs[genre][:2])

    return answer
