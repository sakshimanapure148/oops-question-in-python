"""Photography Contest Manager
OOP practice: encapsulation, composition, properties, validation and sorting.

Run:
    python daily_task_2026_11_22.py
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class PhotoEntry:
    """Represents one photograph submitted by a participant."""

    entry_id: str
    title: str
    category: str
    score: float = 0.0

    def __post_init__(self) -> None:
        self.entry_id = self.entry_id.strip().upper()
        self.title = self.title.strip()
        self.category = self.category.strip().title()

        if not self.entry_id:
            raise ValueError("Entry ID cannot be empty.")
        if not self.title:
            raise ValueError("Photo title cannot be empty.")
        if not self.category:
            raise ValueError("Category cannot be empty.")
        self.score = self._validate_score(self.score)

    @staticmethod
    def _validate_score(value: float) -> float:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Score must be a number.")
        if not 0 <= value <= 100:
            raise ValueError("Score must be between 0 and 100.")
        return float(value)

    def update_score(self, new_score: float) -> None:
        self.score = self._validate_score(new_score)


class Participant:
    """Stores a participant and their submitted photo entries."""

    def __init__(self, participant_id: str, name: str) -> None:
        participant_id = participant_id.strip().upper()
        name = name.strip()

        if not participant_id:
            raise ValueError("Participant ID cannot be empty.")
        if not name:
            raise ValueError("Participant name cannot be empty.")

        self.participant_id = participant_id
        self.name = name.title()
        self._entries: Dict[str, PhotoEntry] = {}

    @property
    def entries(self) -> tuple:
        """Return a read-only snapshot of submitted entries."""
        return tuple(self._entries.values())

    def submit_photo(self, entry: PhotoEntry) -> None:
        if not isinstance(entry, PhotoEntry):
            raise TypeError("Only PhotoEntry objects can be submitted.")
        if entry.entry_id in self._entries:
            raise ValueError("This participant already used that entry ID.")
        self._entries[entry.entry_id] = entry

    def average_score(self) -> float:
        if not self._entries:
            return 0.0
        return sum(item.score for item in self._entries.values()) / len(self._entries)


class PhotographyContest:
    """Coordinates participants, entries and contest results."""

    def __init__(self, contest_name: str) -> None:
        contest_name = contest_name.strip()
        if not contest_name:
            raise ValueError("Contest name cannot be empty.")

        self.contest_name = contest_name
        self._participants: Dict[str, Participant] = {}

    def register_participant(self, participant: Participant) -> None:
        if not isinstance(participant, Participant):
            raise TypeError("Register a valid Participant object.")
        if participant.participant_id in self._participants:
            raise ValueError("Participant ID is already registered.")
        self._participants[participant.participant_id] = participant

    def submit_entry(self, participant_id: str, entry: PhotoEntry) -> None:
        key = participant_id.strip().upper()
        if key not in self._participants:
            raise ValueError("Participant not found.")
        if any(
            entry.entry_id == existing.entry_id
            for person in self._participants.values()
            for existing in person.entries
        ):
            raise ValueError("Entry IDs must be unique across the contest.")
        self._participants[key].submit_photo(entry)

    def find_participant(self, participant_id: str) -> Optional[Participant]:
        """Find a participant using their ID; return None if not found."""
        return self._participants.get(participant_id.strip().upper())

    def category_winners(self) -> Dict[str, tuple]:
        """Return the highest-scoring photo and its owner in each category."""
        winners = {}
        for participant in self._participants.values():
            for entry in participant.entries:
                current = winners.get(entry.category)
                if current is None or entry.score > current[1].score:
                    winners[entry.category] = (participant, entry)
        return winners

    def display_category_winners(self) -> None:
        print("\n===== Category Winners =====")
        winners = self.category_winners()
        if not winners:
            print("No photo entries have been submitted.")
            return

        for category, (participant, entry) in sorted(winners.items()):
            print(
                f"{category}: {entry.title} — {participant.name} "
                f"({entry.score:.1f}/100)"
            )

    def display_participant_report(self, participant_id: str) -> None:
        """Display all submitted photos for one participant."""
        participant = self.find_participant(participant_id)
        if participant is None:
            print("Participant not found.")
            return

        print(f"\n===== Report: {participant.name} =====")
        if not participant.entries:
            print("No photos submitted yet.")
            return

        for entry in participant.entries:
            print(
                f"{entry.entry_id} | {entry.title} | "
                f"{entry.category} | {entry.score:.1f}/100"
            )
        print(f"Average score: {participant.average_score():.1f}/100")

    def leaderboard(self) -> List[Participant]:
        """Return participants ordered by average score, highest first."""
        return sorted(
            self._participants.values(),
            key=lambda person: (person.average_score(), person.name),
            reverse=True,
        )

    def display_results(self) -> None:
        print(f"\n===== {self.contest_name} — Leaderboard =====")
        if not self._participants:
            print("No participants have registered.")
            return

        for position, participant in enumerate(self.leaderboard(), start=1):
            print(
                f"{position}. {participant.name:<18} "
                f"Average: {participant.average_score():.1f}/100 "
                f"| Entries: {len(participant.entries)}"
            )


def main() -> None:
    contest = PhotographyContest("Lens & Light Photography Challenge")

    participants = [
        Participant("P101", "Sakshi Manapure"),
        Participant("P102", "Aarav Sharma"),
        Participant("P103", "Riya Patil"),
    ]

    for participant in participants:
        contest.register_participant(participant)

    contest.submit_entry("P101", PhotoEntry("E101", "Monsoon Streets", "Street", 92))
    contest.submit_entry("P101", PhotoEntry("E102", "Golden Hour", "Nature", 88))
    contest.submit_entry("P102", PhotoEntry("E103", "City Lights", "Street", 85))
    contest.submit_entry("P103", PhotoEntry("E104", "Quiet Morning", "Nature", 96))
    contest.submit_entry("P103", PhotoEntry("E105", "Old Windows", "Architecture", 90))

    contest.display_results()
    contest.display_category_winners()
    contest.display_participant_report("P101")


if __name__ == "__main__":
    main()
