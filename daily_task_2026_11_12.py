"""Daily OOP Task - 12 November 2026: Photo Album Organizer.

Organize photo records into albums, search by tags, and calculate storage.
Concepts: encapsulation, composition, properties, static methods and validation.
"""

from datetime import date
import math


class Photo:
    """Store details about one photo while protecting its tag collection."""

    SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".webp")

    def __init__(self, title, filename, file_size_mb, captured_on, tags=None):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Photo title cannot be empty.")
        if not isinstance(filename, str) or not filename.strip():
            raise ValueError("Filename cannot be empty.")

        filename = filename.strip()
        if not self.is_supported_format(filename):
            raise ValueError("Use a JPG, JPEG, PNG or WEBP photo.")

        if (
            isinstance(file_size_mb, bool)
            or not isinstance(file_size_mb, (int, float))
        ):
            raise TypeError("File size must be a number.")
        if not math.isfinite(file_size_mb) or file_size_mb <= 0:
            raise ValueError("File size must be finite and greater than zero.")

        try:
            date.fromisoformat(captured_on)
        except (TypeError, ValueError):
            raise ValueError("Date must use YYYY-MM-DD format.") from None

        self.title = title.strip()
        self.filename = filename
        self.file_size_mb = float(file_size_mb)
        self.captured_on = captured_on
        self.__tags = set()

        for tag in tags or []:
            self.add_tag(tag)

    @staticmethod
    def is_supported_format(filename):
        """Return whether a filename has a supported image extension."""
        if not isinstance(filename, str):
            return False
        return filename.lower().endswith(Photo.SUPPORTED_FORMATS)

    @property
    def tags(self):
        """Expose tags as a sorted tuple so callers cannot change the set."""
        return tuple(sorted(self.__tags))

    def add_tag(self, tag):
        if not isinstance(tag, str) or not tag.strip():
            raise ValueError("Tag cannot be empty.")
        self.__tags.add(tag.strip().lower())

    def remove_tag(self, tag):
        if not isinstance(tag, str) or not tag.strip():
            raise ValueError("Tag cannot be empty.")
        self.__tags.discard(tag.strip().lower())

    def matches_tag(self, tag):
        return tag.strip().lower() in self.__tags

    def display(self):
        tag_text = ", ".join(self.tags) if self.tags else "No tags"
        print(
            f"{self.title} | {self.filename} | {self.file_size_mb:.2f} MB "
            f"| {self.captured_on} | Tags: {tag_text}"
        )


class PhotoAlbum:
    """Manage Photo objects using composition."""

    def __init__(self, album_name):
        if not isinstance(album_name, str) or not album_name.strip():
            raise ValueError("Album name cannot be empty.")
        self.album_name = album_name.strip()
        self.__photos = {}

    def add_photo(self, photo):
        if not isinstance(photo, Photo):
            raise TypeError("Only Photo objects can be added.")
        key = photo.filename.lower()
        if key in self.__photos:
            raise ValueError("This photo filename already exists in the album.")
        self.__photos[key] = photo

    def remove_photo(self, filename):
        if not isinstance(filename, str) or not filename.strip():
            raise ValueError("Filename cannot be empty.")
        return self.__photos.pop(filename.strip().lower(), None)

    def find_by_tag(self, tag):
        if not isinstance(tag, str) or not tag.strip():
            raise ValueError("Search tag cannot be empty.")
        return [
            photo for photo in self.__photos.values()
            if photo.matches_tag(tag)
        ]

    @property
    def total_photos(self):
        return len(self.__photos)

    @property
    def total_storage_mb(self):
        return sum(photo.file_size_mb for photo in self.__photos.values())

    def show_gallery(self):
        print(f"\n--- {self.album_name} ---")
        if not self.__photos:
            print("The album is empty.")
            return
        for photo in self.__photos.values():
            photo.display()
        print(f"Photos: {self.total_photos}")
        print(f"Storage used: {self.total_storage_mb:.2f} MB")


def main():
    album = PhotoAlbum("Travel Memories")

    photos = [
        Photo("Sunset View", "sunset.jpg", 3.4, "2026-10-18",
              ["travel", "sunset", "nature"]),
        Photo("Mountain Morning", "mountain.png", 4.2, "2026-10-19",
              ["travel", "mountains"]),
        Photo("City Lights", "city.webp", 2.1, "2026-10-20",
              ["city", "night"]),
    ]

    for photo in photos:
        album.add_photo(photo)

    # Add and remove tags without exposing the private tag set.
    photos[0].add_tag("golden-hour")
    photos[2].remove_tag("night")

    album.show_gallery()

    print("\nPhotos tagged 'travel':")
    for photo in album.find_by_tag("travel"):
        print("-", photo.title)

    print("\nTotal photo count:", album.total_photos)
    print(f"Total storage: {album.total_storage_mb:.2f} MB")

    # Check duplicate protection and invalid input handling.
    try:
        album.add_photo(
            Photo("Duplicate", "SUNSET.JPG", 1.0, "2026-10-21")
        )
    except ValueError as error:
        print("Duplicate check passed:", error)

    try:
        Photo("Invalid Photo", "document.pdf", 1.0, "2026-10-21")
    except ValueError as error:
        print("Format validation passed:", error)

    removed = album.remove_photo("city.webp")
    assert removed is not None
    assert album.total_photos == 2
    assert len(album.find_by_tag("travel")) == 2
    assert not Photo.is_supported_format("notes.txt")
    print("\nAll photo album checks passed successfully.")


if __name__ == "__main__":
    main()
