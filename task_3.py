"""Daily OOP Task - 03 November 2026
Project: Music Playlist Manager
Concepts: classes, objects, encapsulation, validation and object interaction.
"""


class Track:
    """Store details about one music track."""

    def __init__(self, title, artist, duration):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title cannot be empty.")
        if not isinstance(artist, str) or not artist.strip():
            raise ValueError("Artist cannot be empty.")
        if isinstance(duration, bool) or not isinstance(duration, int) or duration <= 0:
            raise ValueError("Duration must be a positive whole number of seconds.")

        self.title = title.strip()
        self.artist = artist.strip()
        self.duration = duration

    def display(self):
        minutes, seconds = divmod(self.duration, 60)
        print(f"{self.title} - {self.artist} ({minutes}:{seconds:02d})")


class Playlist:
    """Manage tracks while keeping the internal list private."""

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Playlist name cannot be empty.")
        self.name = name.strip()
        self.__tracks = []

    def add_track(self, track):
        if not isinstance(track, Track):
            raise TypeError("Only Track objects can be added.")

        duplicate = any(
            item.title.casefold() == track.title.casefold()
            and item.artist.casefold() == track.artist.casefold()
            for item in self.__tracks
        )
        if duplicate:
            print(f'"{track.title}" is already in the playlist.')
            return False

        self.__tracks.append(track)
        print(f'Added: "{track.title}"')
        return True

    def remove_track(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Track title cannot be empty.")

        for track in self.__tracks:
            if track.title.casefold() == title.strip().casefold():
                self.__tracks.remove(track)
                print(f'Removed: "{track.title}"')
                return True

        print(f'Track "{title}" was not found.')
        return False

    def total_duration(self):
        return sum(track.duration for track in self.__tracks)

    def show_playlist(self):
        print(f"\n--- {self.name} ---")
        if not self.__tracks:
            print("Playlist is empty.")
            return

        for number, track in enumerate(self.__tracks, start=1):
            print(f"{number}. ", end="")
            track.display()

        minutes, seconds = divmod(self.total_duration(), 60)
        print(f"Total tracks: {len(self.__tracks)}")
        print(f"Total duration: {minutes} min {seconds} sec")


if __name__ == "__main__":
    playlist = Playlist("My Favourites")
    playlist.add_track(Track("Kesariya", "Arijit Singh", 268))
    playlist.add_track(Track("Heeriye", "Jasleen Royal", 194))
    playlist.add_track(Track("Apna Bana Le", "Arijit Singh", 261))
    playlist.add_track(Track("Kesariya", "Arijit Singh", 268))

    playlist.show_playlist()
    playlist.remove_track("Heeriye")
    playlist.show_playlist()
