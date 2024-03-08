def solution(genres, plays):
    genres_dict = {}
    genres_play = {}
    genres_set = set()
    ans = []
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in genres_dict:
            genres_dict[genre].append((play, i))
            genres_play[genre] += play
            genres_set.add(genre)
        else:
            genres_dict[genre] = [(play, i)]
            genres_play[genre] = play
    genres_play = sorted(genres_play.items(), key=lambda x: -x[1])
    for genre, _ in genres_play:
        genres_dict[genre].sort(key=lambda x: (x[0], -x[1]))
        for _ in range(1+(genre in genres_set)):
            ans.append(genres_dict[genre].pop()[1])
    return ans