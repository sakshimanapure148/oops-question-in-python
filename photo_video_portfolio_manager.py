"""
Photo & Video Portfolio Manager
================================
Daily OOP practice project — 17 November 2026.

Concepts demonstrated:
- Abstract classes and inheritance
- Encapsulation and properties
- Method overriding and polymorphism
- Composition (library contains albums; albums contain assets)
- Input validation, exceptions, searching and sorting

Run:
    python photo_video_portfolio_manager.py
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class MediaAsset(ABC):
    """Common base class for media items in a portfolio."""

    def __init__(self, asset_id: str, title: str, file_size_mb: float) -> None:
        if not isinstance(asset_id, str) or not asset_id.strip():
            raise ValueError("Asset ID cannot be empty.")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title cannot be empty.")
        if isinstance(file_size_mb, bool) or not isinstance(file_size_mb, (int, float)):
            raise TypeError("File size must be a number.")
        if file_size_mb <= 0:
            raise ValueError("File size must be greater than zero.")

        self.asset_id = asset_id.strip().upper()
        self.title = title.strip().title()
        self.__file_size_mb = float(file_size_mb)

    @property
    def file_size_mb(self) -> float:
        """Read-only access to the stored file size."""
        return self.__file_size_mb

    @abstractmethod
    def media_type(self) -> str:
        """Return the type of media."""

    @abstractmethod
    def details(self) -> str:
        """Return formatted information about this asset."""


class Photo(MediaAsset):
    """A photograph with pixel dimensions and a camera label."""

    def __init__(
        self,
        asset_id: str,
        title: str,
        file_size_mb: float,
        width: int,
        height: int,
        camera: str,
    ) -> None:
        super().__init__(asset_id, title, file_size_mb)

        for label, value in (("Width", width), ("Height", height)):
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError(f"{label} must be an integer.")
            if value <= 0:
                raise ValueError(f"{label} must be greater than zero.")

        if not isinstance(camera, str) or not camera.strip():
            raise ValueError("Camera name cannot be empty.")

        self.width = width
        self.height = height
        self.camera = camera.strip()

    def media_type(self) -> str:
        return "Photo"

    def details(self) -> str:
        return (
            f"[{self.media_type()}] {self.asset_id} | {self.title} | "
            f"{self.width}x{self.height} px | {self.camera} | "
            f"{self.file_size_mb:.2f} MB"
        )


class Video(MediaAsset):
    """A video with duration and resolution information."""

    def __init__(
        self,
        asset_id: str,
        title: str,
        file_size_mb: float,
        duration_seconds: int,
        resolution: str,
    ) -> None:
        super().__init__(asset_id, title, file_size_mb)

        if isinstance(duration_seconds, bool) or not isinstance(duration_seconds, int):
            raise TypeError("Duration must be an integer number of seconds.")
        if duration_seconds <= 0:
            raise ValueError("Duration must be greater than zero.")
        if not isinstance(resolution, str) or not resolution.strip():
            raise ValueError("Resolution cannot be empty.")

        self.duration_seconds = duration_seconds
        self.resolution = resolution.strip().upper()

    def media_type(self) -> str:
        return "Video"

    def details(self) -> str:
        minutes, seconds = divmod(self.duration_seconds, 60)
        return (
            f"[{self.media_type()}] {self.asset_id} | {self.title} | "
            f"{minutes:02d}:{seconds:02d} | {self.resolution} | "
            f"{self.file_size_mb:.2f} MB"
        )


class PhotoAlbum:
    """An album that owns and organizes multiple media assets."""

    def __init__(self, album_name: str) -> None:
        if not isinstance(album_name, str) or not album_name.strip():
            raise ValueError("Album name cannot be empty.")

        self.album_name = album_name.strip().title()
        self.__assets: Dict[str, MediaAsset] = {}

    def add_asset(self, asset: MediaAsset) -> None:
        if not isinstance(asset, MediaAsset):
            raise TypeError("Only Photo or Video objects can be added.")
        if asset.asset_id in self.__assets:
            raise ValueError(f"Asset ID '{asset.asset_id}' already exists.")
        self.__assets[asset.asset_id] = asset

    def remove_asset(self, asset_id: str) -> MediaAsset:
        key = asset_id.strip().upper() if isinstance(asset_id, str) else ""
        if not key:
            raise ValueError("Asset ID cannot be empty.")
        if key not in self.__assets:
            raise LookupError(f"Asset '{key}' was not found.")
        return self.__assets.pop(key)

    def find_asset(self, asset_id: str) -> Optional[MediaAsset]:
        if not isinstance(asset_id, str) or not asset_id.strip():
            raise ValueError("Asset ID cannot be empty.")
        return self.__assets.get(asset_id.strip().upper())

    @property
    def asset_count(self) -> int:
        return len(self.__assets)

    @property
    def total_size_mb(self) -> float:
        return sum(asset.file_size_mb for asset in self.__assets.values())

    def list_assets(self) -> List[MediaAsset]:
        return sorted(self.__assets.values(), key=lambda asset: asset.title.lower())


class PortfolioLibrary:
    """Manage multiple albums using composition."""

    def __init__(self, owner: str) -> None:
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Owner name cannot be empty.")
        self.owner = owner.strip().title()
        self.__albums: Dict[str, PhotoAlbum] = {}

    def create_album(self, album: PhotoAlbum) -> None:
        if not isinstance(album, PhotoAlbum):
            raise TypeError("Expected a PhotoAlbum object.")
        key = album.album_name.casefold()
        if key in self.__albums:
            raise ValueError(f"Album '{album.album_name}' already exists.")
        self.__albums[key] = album

    def get_album(self, album_name: str) -> Optional[PhotoAlbum]:
        if not isinstance(album_name, str) or not album_name.strip():
            raise ValueError("Album name cannot be empty.")
        return self.__albums.get(album_name.strip().casefold())

    def search_assets(self, keyword: str) -> List[MediaAsset]:
        if not isinstance(keyword, str) or not keyword.strip():
            raise ValueError("Search keyword cannot be empty.")

        term = keyword.strip().casefold()
        matches: List[MediaAsset] = []
        for album in self.__albums.values():
            matches.extend(
                asset for asset in album.list_assets()
                if term in asset.title.casefold()
                or term in asset.media_type().casefold()
            )
        return matches

    def display_report(self) -> None:
        print(f"\n{' PORTFOLIO LIBRARY ':=^72}")
        print(f"Owner: {self.owner}")
        print("-" * 72)

        total_assets = 0
        total_size = 0.0

        for album in self.__albums.values():
            print(f"\nAlbum: {album.album_name}")
            for asset in album.list_assets():
                # Polymorphism: Photo and Video provide their own details().
                print(f"  {asset.details()}")
            print(f"  Assets: {album.asset_count} | Storage: {album.total_size_mb:.2f} MB")
            total_assets += album.asset_count
            total_size += album.total_size_mb

        print("-" * 72)
        print(f"Total albums: {len(self.__albums)}")
        print(f"Total assets: {total_assets}")
        print(f"Total storage: {total_size:.2f} MB")
        print("=" * 72)


def run_demo() -> None:
    """Create a sample portfolio and verify important behaviours."""
    library = PortfolioLibrary("Sakshi")

    travel_album = PhotoAlbum("Travel Memories")
    travel_album.add_asset(
        Photo("P101", "Mountain View", 4.5, 4000, 3000, "Mirrorless Camera")
    )
    travel_album.add_asset(
        Photo("P102", "City Lights", 3.2, 3000, 2000, "Mobile Camera")
    )
    travel_album.add_asset(
        Video("V201", "Sunset Walk", 28.0, 95, "1080p")
    )

    event_album = PhotoAlbum("College Events")
    event_album.add_asset(
        Photo("P103", "Stage Moments", 5.1, 4200, 2800, "DSLR")
    )

    library.create_album(travel_album)
    library.create_album(event_album)
    library.display_report()

    print("\nSearch results for 'video':")
    for result in library.search_assets("video"):
        print(" ", result.details())

    # Basic checks make the example easier to verify.
    assert library.get_album("travel memories") is travel_album
    assert travel_album.find_asset("p101").media_type() == "Photo"
    assert travel_album.asset_count == 3
    assert round(travel_album.total_size_mb, 2) == 35.70
    assert len(library.search_assets("video")) == 1

    try:
        travel_album.add_asset(Photo("P101", "Duplicate", 1.0, 100, 100, "Test"))
    except ValueError as error:
        print(f"\n[PASS] Duplicate validation: {error}")
    else:
        raise AssertionError("Duplicate asset IDs must be rejected.")

    try:
        travel_album.remove_asset("UNKNOWN")
    except LookupError as error:
        print(f"[PASS] Missing asset validation: {error}")
    else:
        raise AssertionError("Removing an unknown asset must raise LookupError.")

    print("\n[PASS] All portfolio checks completed successfully.")


if __name__ == "__main__":
    run_demo()
