
class Album:

    def __init__(self, album_name, group):
        self.album_name = album_name
        self.group = group
        self.track_list = []

    def get_tracks(self):
        for track in self.track_list:
            track.show()

    def add_track(self, track):
        self.track_list.append(track)

    def get_duration(self):
        duration_list = []
        for track in self.track_list:
            duration_list.append(track.duration)
        print(sum(duration_list))


class Track:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def show(self):
        print(self.name + '-' + str(self.duration))


track_1 = Track('Разнообразие', 3)
track_2 = Track('Информация', 4)
track_3 = Track('Животное', 3)

track_4 = Track('Инициализация', 3)
track_5 = Track('Теория', 3)
track_6 = Track('Практика', 2)

album_1 = Album('Первый альбом', 'Мелодичные пряники')
album_1.add_track(track_1)
album_1.add_track(track_2)
album_1.add_track(track_3)
album_1.get_tracks()
album_1.get_duration()

album_2 = Album('Второй альбом', 'Красивые пряники')
album_2.add_track(track_4)
album_2.add_track(track_5)
album_2.add_track(track_6)
album_2.get_tracks()
album_2.get_duration()

