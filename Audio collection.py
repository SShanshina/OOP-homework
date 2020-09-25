class track:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def show(self):
        return f'{self.name} - {self.duration}'


track_1 = track('FAKE LOVE', 4)
track_2 = track('The Truth Untold', 4)
track_3 = track('Anpanman', 4)
track_4 = track('Interlude: Shadow', 4)
track_5 = track('Black Swan', 3)
track_6 = track('ON', 4)


class album:

    def __init__(self, group, name, tracks):
        self.group = group
        self.name = name
        self.tracks = tracks

    def get_tracks(self):
        for track in self.tracks:
            print(track.show())

    def add_track(self):
        track_name = input('Введите название трека: ')
        track_duration = int(input('Введите длительность трека: '))
        track_7 = track(track_name, track_duration)
        self.tracks.append(track_7)
        return f'Трек {track_7.name} был успешно добавлен в альбом {self.name}, его длительность составляет {track_7.duration} минуты'

    def get_duration(self):
        duration_list = []
        for track in self.tracks:
            duration_list.append(track.duration)
        return f'Длительность альбома {self.name} составляет {sum(duration_list)} минут'


album_1 = album('BTS', 'Love Yourself: Tear', [track_1, track_2, track_3])
album_2 = album('BTS', 'Map Of The Soul: 7', [track_4, track_5, track_6])

# print(track_1.show())
# print(album_1.add_track())
# print(album_2.add_track())
# print(album_1.get_tracks())
# print(album_2.get_tracks())
print(album_1.get_duration())
print(album_2.get_duration())