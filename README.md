# Python OOP Practice & Mini-Projects

A hands-on collection of Python Object-Oriented Programming exercises and mini-projects by **Sakshi Manapure**. This repository documents consistent practice, from beginner-level classes and objects to practical systems using inheritance, encapsulation, polymorphism, composition and testing.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Focus](https://img.shields.io/badge/Focus-Python%20OOP-green)
![Projects](https://img.shields.io/badge/Projects-Ongoing-orange)

## Repository Highlights

- Beginner-friendly exercises for classes, objects, constructors and methods.
- Practical mini-projects with validation and exception handling.
- OOP design using inheritance, encapsulation, polymorphism and composition.
- A growing collection of daily coding exercises.
- Automated tests using Python's built-in `unittest` framework.

All projects are built with the Python standard library. No third-party packages are required.

## Quick Start

Clone the repository:

```bash
git clone https://github.com/sakshimanapure148/oops-question-in-python.git
cd oops-question-in-python
```

Check that Python is installed:

```bash
python --version
```

On Windows, `py --version` can be used. Python 3.9 or later is recommended.

Run an exercise:

```bash
python task_13.py
```

On Windows:

```bash
py task_13.py
```

Replace the filename with any exercise from the file guide below.

## Complete File Guide

| File | Main classes | What you will practise |
|---|---|---|
| [`task_16.py`](task_16.py) | `Laptop` | Classes, objects, constructors and object attributes. |
| [`task_1.py`](task_1.py) | `Calculator` | Instance methods, arithmetic, validation and division-by-zero handling. |
| [`task_14.py`](task_14.py) | `Employee` | Employee details, salary validation and annual salary calculation. |
| [`task_18.py`](task_18.py) | `Product` | Attributes, price and quantity validation, and total-price calculation. |
| [`task_17.py`](task_17.py) | `Vehicle` and child classes | Inheritance, `super()`, method overriding and polymorphism. |
| [`task_2.py`](task_2.py) | `Student`, `Course` | Object interaction, enrolment, duplicate prevention and capacity validation. |
| [`task_15.py`](task_15.py) | `Event`, `TicketBooking` | Ticket booking, availability, total-price calculation and cancellation. |
| [`task_3.py`](task_3.py) | `Track`, `Playlist` | Playlist management, adding/removing tracks and duration calculation. |
| [`task_4.py`](task_4.py) | `Plant`, `PlantCareTracker` | Watering records, date validation and care reminders. |
| [`task_5.py`](task_5.py) | `Equipment`, `Camera`, `Tripod`, `RentalDesk` | Equipment rental, returns, composition and late fees. |
| [`task_6.py`](task_6.py) | `Parcel`, `ExpressParcel`, `FragileParcel`, `DeliveryHub` | Parcel tracking, shipping charges and polymorphism. |
| [`task_7.py`](task_7.py) | `Photo`, `PhotoAlbum` | Photo organization, tags, searching, formats and storage calculations. |
| [`task_8.py`](task_8.py) | `Plant`, `GardenPlot`, `GardenManager` | Garden management, composition and harvest tracking. |
| [`task_9.py`](task_9.py) | `SmartDevice`, `SmartLight`, `SmartFan`, `SmartHome`, `WordPuzzleGame` | Smart-device controls, energy estimates and an interactive word puzzle. |
| [`task_10.py`](task_10.py) | `MediaAsset`, `Photo`, `Video`, `PhotoAlbum`, `PortfolioLibrary` | Abstract classes, inheritance, composition, searching and sorting. |
| [`task_11.py`](task_11.py) | `PhotoEntry`, `Participant`, `PhotographyContest` | Photo submissions, score validation, category winners and leaderboard. |
| [`task_12.py`](task_12.py) | `Workshop`, `OnlineWorkshop`, `InPersonWorkshop`, `Participant`, `Registration`, `WorkshopManager` | Workshop registration, capacity, fee calculation and cancellation. |
| [`task_13.py`](task_13.py) | `StudyTopic`, `StudySession`, `StudyPlanner` | Study scheduling, time-conflict detection, session status and progress reports. |
| [`task_19.py`](task_19.py) | `ParcelTests` | Unit tests for parcel charges, validation, delivery status and duplicate IDs. |

## Daily OOP Projects

### 26 November 2026 — Study Session Planner

**File:** [`task_13.py`](task_13.py)

- Creates and validates study topics.
- Schedules sessions and detects overlapping planned sessions.
- Tracks Planned, Completed and Skipped statuses.
- Stores revision notes and displays a study progress report.

**Concepts:** classes, composition, encapsulation, properties, validation, `datetime`, filtering and sorting.

Run:

```bash
python task_13.py
```

### 24 November 2026 — Art Workshop Registration Manager

**File:** [`task_12.py`](task_12.py)

- Manages online and in-person workshops with different fee rules.
- Registers participants while checking capacity and duplicate entries.
- Calculates fees through overridden methods.
- Supports cancellation and registration reports.

**Concepts:** inheritance, encapsulation, polymorphism, composition, validation, `Decimal` and exception handling.

Run:

```bash
python task_12.py
```

### 22 November 2026 — Photography Contest Manager

**File:** [`task_11.py`](task_11.py)

- Registers contest participants and photo entries.
- Validates entry details and scores.
- Calculates average scores, category winners and a leaderboard.

**Concepts:** dataclasses, encapsulation, composition, validation, sorting and aggregation.

Run:

```bash
python task_11.py
```

### 17 November 2026 — Photo & Video Portfolio Manager

**File:** [`task_10.py`](task_10.py)

Organizes photo and video assets into albums and a portfolio library.

**Concepts:** abstract base classes, inheritance, method overriding, composition, searching and sorting.

### 15 November 2026 — Smart Home Energy Monitor & Word Puzzle

**File:** [`task_9.py`](task_9.py)

Manages smart lights and fans, estimates energy use and includes an interactive word puzzle.

**Concepts:** inheritance, encapsulation, polymorphism, composition and validation.

### Earlier Practice Projects

| Date | Project | File |
|---|---|---|
| 14 Nov 2026 | Community Garden Manager | [`task_8.py`](task_8.py) |
| 12 Nov 2026 | Photo Album Organizer | [`task_7.py`](task_7.py) |
| 9 Nov 2026 | Parcel Delivery Tracking System | [`task_6.py`](task_6.py) |
| 8 Nov 2026 | Photography Equipment Rental Tracker | [`task_5.py`](task_5.py) |
| 4 Nov 2026 | Smart Plant Care Tracker | [`task_4.py`](task_4.py) |
| 3 Nov 2026 | Music Playlist Manager | [`task_3.py`](task_3.py) |

## Run Automated Tests

The repository currently includes a `unittest` test file for parcel tracking.

Run the test suite from the repository directory:

```bash
python -m unittest -v
```

On Windows:

```bash
py -m unittest -v
```

The parcel tests cover shipping charges, invalid weights, delivery-status rules, duplicate tracking IDs and collection totals.

## OOP Concepts Practised

| Concept | Meaning |
|---|---|
| Class and object | A class is a blueprint; an object is an instance of that class. |
| Constructor | `__init__()` initializes object data. |
| Instance method | A method that works with an object's data. |
| Encapsulation | Controls access to an object's internal state. |
| Inheritance | Lets a child class reuse and extend a parent class. |
| `super()` | Accesses methods or constructors from a parent class. |
| Method overriding | Lets a child class provide its own implementation. |
| Polymorphism | The same method call can behave differently for different objects. |
| Composition | Builds a larger object using other objects. |
| Property | Provides controlled access to attributes. |
| Validation | Checks values before accepting them. |
| Exception handling | Handles invalid operations with clear errors. |
| Unit testing | Checks expected program behaviour automatically. |

## Suggested Learning Roadmap

1. Start with `task_16.py` to understand classes, objects and constructors.
2. Practise methods and calculations using `task_1.py`, `task_14.py` and `task_18.py`.
3. Learn inheritance and polymorphism with `task_17.py`.
4. Practise object interaction with the course and ticket projects.
5. Explore encapsulation and composition in the daily mini-projects.
6. Run the tests and add new test cases as you learn.

## How to Add a New Exercise

1. Create a separate, clearly named `.py` file.
2. Use meaningful class, method and variable names.
3. Validate inputs and handle expected errors.
4. Include a runnable example under `if __name__ == "__main__":`.
5. Add the file and its purpose to the **Complete File Guide**.
6. Add tests for important behaviour where appropriate.

## About the Author

**Sakshi Manapure**  
BCA Student | Aspiring Python Full Stack Developer

Interested in building projects with Python, Django, JavaScript and SQL.

- GitHub: [@sakshimanapure148](https://github.com/sakshimanapure148)
- Repository: [oops-question-in-python](https://github.com/sakshimanapure148/oops-question-in-python)

---

*Learning OOP one class, one object and one project at a time.*
