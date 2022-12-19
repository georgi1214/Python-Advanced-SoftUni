def add_songs(*info):
    final_print = ''
    args_as_dict = {}
    for el in info:
        song_title = el[0]
        lyrics = el[1]
        if song_title not in args_as_dict:
            args_as_dict[song_title] = []
            args_as_dict[song_title].extend(lyrics)
        else:
            args_as_dict[song_title].extend(lyrics)

    for songs, lyrics in args_as_dict.items():
        final_print += f'- {songs}\n'
        for el in lyrics:
            final_print += f'{el}\n'
    return final_print