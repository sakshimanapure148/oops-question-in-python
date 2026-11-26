"""Study Session Planner
OOP practice: composition, encapsulation, properties, datetime validation,
status management, filtering and summary reports.

Run:
    python study_session_planner.py
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List, Optional


@dataclass
class StudyTopic:
    """A subject or topic that the learner wants to study."""

    topic_id: str
    name: str
    subject: str
    estimated_minutes: int

    def __post_init__(self) -> None:
        self.topic_id = self.topic_id.strip().upper()
        self.name = self.name.strip()
        self.subject = self.subject.strip().title()

        if not self.topic_id or not self.name or not self.subject:
            raise ValueError("Topic ID, name and subject are required.")
        if (
            isinstance(self.estimated_minutes, bool)
            or not isinstance(self.estimated_minutes, int)
            or self.estimated_minutes <= 0
        ):
            raise ValueError("Estimated minutes must be a positive whole number.")


class StudySession:
    """Represents one scheduled study session for a topic."""

    VALID_STATUSES = {"Planned", "Completed", "Skipped"}

    def __init__(
        self,
        session_id: str,
        topic: StudyTopic,
        start_time: datetime,
        duration_minutes: int,
    ) -> None:
        session_id = session_id.strip().upper()
        if not session_id:
            raise ValueError("Session ID cannot be empty.")
        if not isinstance(topic, StudyTopic):
            raise TypeError("A valid StudyTopic object is required.")
        if not isinstance(start_time, datetime):
            raise TypeError("Start time must be a datetime object.")
        if (
            isinstance(duration_minutes, bool)
            or not isinstance(duration_minutes, int)
            or duration_minutes <= 0
        ):
            raise ValueError("Duration must be a positive whole number.")

        self.session_id = session_id
        self.topic = topic
        self.start_time = start_time
        self.duration_minutes = duration_minutes
        self._status = "Planned"
        self._notes = ""

    @property
    def end_time(self) -> datetime:
        return self.start_time + timedelta(minutes=self.duration_minutes)

    @property
    def status(self) -> str:
        return self._status

    @property
    def notes(self) -> str:
        return self._notes

    def update_status(self, new_status: str) -> None:
        normalized = new_status.strip().title()
        if normalized not in self.VALID_STATUSES:
            raise ValueError("Status must be Planned, Completed or Skipped.")
        self._status = normalized

    def add_notes(self, notes: str) -> None:
        if not isinstance(notes, str):
            raise TypeError("Notes must be text.")
        self._notes = notes.strip()

    def overlaps(self, other: "StudySession") -> bool:
        if not isinstance(other, StudySession):
            raise TypeError("Compare with another StudySession object.")
        return self.start_time < other.end_time and other.start_time < self.end_time

    def summary(self) -> str:
        return (
            f"{self.session_id} | {self.topic.subject}: {self.topic.name} | "
            f"{self.start_time:%d %b %Y, %I:%M %p} | "
            f"{self.duration_minutes} min | {self.status}"
        )


class StudyPlanner:
    """Stores topics and sessions and produces a study progress report."""

    def __init__(self, learner_name: str) -> None:
        learner_name = learner_name.strip()
        if not learner_name:
            raise ValueError("Learner name cannot be empty.")
        self.learner_name = learner_name.title()
        self._topics: Dict[str, StudyTopic] = {}
        self._sessions: Dict[str, StudySession] = {}

    @property
    def topics(self) -> tuple:
        return tuple(self._topics.values())

    @property
    def sessions(self) -> tuple:
        return tuple(self._sessions.values())

    def add_topic(self, topic: StudyTopic) -> None:
        if not isinstance(topic, StudyTopic):
            raise TypeError("Only StudyTopic objects can be added.")
        if topic.topic_id in self._topics:
            raise ValueError("Topic ID already exists.")
        self._topics[topic.topic_id] = topic

    def schedule_session(
        self,
        session_id: str,
        topic_id: str,
        start_time: datetime,
        duration_minutes: int,
    ) -> StudySession:
        session_key = session_id.strip().upper()
        topic_key = topic_id.strip().upper()

        if not session_key:
            raise ValueError("Session ID cannot be empty.")
        if session_key in self._sessions:
            raise ValueError("Session ID already exists.")
        if topic_key not in self._topics:
            raise ValueError("Topic not found.")

        session = StudySession(
            session_key, self._topics[topic_key], start_time, duration_minutes
        )

        for existing in self._sessions.values():
            if existing.status == "Planned" and session.overlaps(existing):
                raise ValueError(
                    f"Time conflict with session {existing.session_id}."
                )

        self._sessions[session_key] = session
        return session

    def find_session(self, session_id: str) -> Optional[StudySession]:
        return self._sessions.get(session_id.strip().upper())

    def update_session_status(self, session_id: str, status: str) -> None:
        session = self.find_session(session_id)
        if session is None:
            raise ValueError("Session not found.")
        session.update_status(status)

    def sessions_by_status(self, status: str) -> List[StudySession]:
        normalized = status.strip().title()
        if normalized not in StudySession.VALID_STATUSES:
            raise ValueError("Choose Planned, Completed or Skipped.")
        return [
            session for session in self._sessions.values()
            if session.status == normalized
        ]

    def total_study_minutes(self, status: Optional[str] = None) -> int:
        selected = self.sessions
        if status is not None:
            selected = tuple(self.sessions_by_status(status))
        return sum(
            session.duration_minutes
            for session in selected
            if session.status == "Completed"
        )

    def display_schedule(self) -> None:
        print(f"\n===== {self.learner_name}'s Study Schedule =====")
        ordered = sorted(self._sessions.values(), key=lambda item: item.start_time)
        if not ordered:
            print("No sessions scheduled.")
            return
        for session in ordered:
            print(session.summary())
            if session.notes:
                print(f"   Notes: {session.notes}")

    def display_report(self) -> None:
        completed = self.sessions_by_status("Completed")
        planned = self.sessions_by_status("Planned")
        skipped = self.sessions_by_status("Skipped")
        print("\n===== Study Progress Report =====")
        print(f"Completed sessions: {len(completed)}")
        print(f"Planned sessions:   {len(planned)}")
        print(f"Skipped sessions:   {len(skipped)}")
        print(f"Focused study time: {self.total_study_minutes()} minutes")


def main() -> None:
    planner = StudyPlanner("Sakshi Manapure")

    python_topic = StudyTopic("T101", "OOP revision", "Python", 60)
    sql_topic = StudyTopic("T102", "Joins practice", "SQL", 45)
    planner.add_topic(python_topic)
    planner.add_topic(sql_topic)

    first = planner.schedule_session(
        "S101", "T101", datetime(2026, 11, 27, 9, 0), 60
    )
    second = planner.schedule_session(
        "S102", "T102", datetime(2026, 11, 27, 10, 30), 45
    )

    first.update_status("Completed")
    first.add_notes("Revised inheritance and method overriding.")
    second.add_notes("Practise INNER JOIN and LEFT JOIN queries.")

    planner.display_schedule()
    planner.display_report()


if __name__ == "__main__":
    main()
