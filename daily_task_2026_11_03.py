# Daily OOP Task - 03 November 2026
# Project: Music Playlist Manager
# Concepts: classes, objects, constructors, encapsulation, methods and object interaction.

class Track:
    """Store details about one music track."""

    def __init__(self, title, artist, duration):
        if not title.strip() or not artist.strip():
            raise ValueError("Title and artist cannot be empty.")
        if duration <= 0:
            raise ValueError("Duration must be greater than zero.")

        self.title = title.strip()
        self.artist = artist.strip()
        self.duration = duration  # duration in seconds

    def display(self):
        minutes, seconds = divmod(self.duration, 60)
        print(f"{self.title} - {self.artist} ({minutes}:{seconds:02d})")


class Playlist:
    """Manage tracks while keeping the track list encapsulated."""

    def __init__(self, name):
        if not name.strip():
            raise ValueError("Playlist name cannot be empty.")

        self.name = name.strip()
        self.__tracks = []

    def add_track(self, track):
        if not isinstance(track, Track):
            print("Error: only Track objects can be added.")
            return

        for existing_track in self.__tracks:
            if (existing_track.title.lower() == track.title.lower()
                    and existing_track.artist.lower() == track.artist.lower()):
                print(f'"{track.title}" is already in the playlist.')
                return

        self.__tracks.append(track)
        print(f'Added: "{track.title}"')

    def remove_track(self, title):
        for track in self.__tracks:
            if track.title.lower() == title.lower():
                self.__tracks.remove(track)
                print(f'Removed: "{track.title}"')
                return

        print(f'Track "{title}" was not found.')

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
    # Create Track objects
    track1 = Track("Kesariya", "Arijit Singh", 268)
    track2 = Track("Heeriye", "Jasleen Royal", 194)
    track3 = Track("Apna Bana Le", "Arijit Singh", 261)

    # Create a Playlist object and manage its tracks
    my_playlist = Playlist("My Favourites")
    my_playlist.add_track(track1)
    my_playlist.add_track(track2)
    my_playlist.add_track(track3)
    my_playlist.add_track(track1)  # duplicate check

    my_playlist.show_playlist()

    my_playlist.remove_track("Heeriye")
    my_playlist.remove_track("Unknown Song")  # not-found handling

    my_playlist.show_playlist()
