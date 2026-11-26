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
python daily_task_2026_11_26.py
```

On Windows:

```bash
py daily_task_2026_11_26.py
```

Replace the filename with any exercise from the file guide below.

## Complete File Guide

| File | Main classes | What you will practise |
|---|---|---|
| [`laptop_class.py`](laptop_class.py) | `Laptop` | Classes, objects, constructors and object attributes. |
| [`calculator_methods.py`](calculator_methods.py) | `Calculator` | Instance methods, arithmetic, validation and division-by-zero handling. |
| [`employee_salary.py`](employee_salary.py) | `Employee` | Employee details, salary validation and annual salary calculation. |
| [`product_class.py`](product_class.py) | `Product` | Attributes, price and quantity validation, and total-price calculation. |
| [`opp.py`](opp.py) | `Vehicle` and child classes | Inheritance, `super()`, method overriding and polymorphism. |
| [`course_registration_system.py`](course_registration_system.py) | `Student`, `Course` | Object interaction, enrolment, duplicate prevention and capacity validation. |
| [`event_ticket_booking.py`](event_ticket_booking.py) | `Event`, `TicketBooking` | Ticket booking, availability, total-price calculation and cancellation. |
| [`daily_task_2026_11_03.py`](daily_task_2026_11_03.py) | `Track`, `Playlist` | Playlist management, adding/removing tracks and duration calculation. |
| [`daily_task_2026_11_04.py`](daily_task_2026_11_04.py) | `Plant`, `PlantCareTracker` | Watering records, date validation and care reminders. |
| [`daily_task_2026_11_08.py`](daily_task_2026_11_08.py) | `Equipment`, `Camera`, `Tripod`, `RentalDesk` | Equipment rental, returns, composition and late fees. |
| [`daily_task_2026_11_09.py`](daily_task_2026_11_09.py) | `Parcel`, `ExpressParcel`, `FragileParcel`, `DeliveryHub` | Parcel tracking, shipping charges and polymorphism. |
| [`daily_task_2026_11_12.py`](daily_task_2026_11_12.py) | `Photo`, `PhotoAlbum` | Photo organization, tags, searching, formats and storage calculations. |
| [`daily_task_2026_11_14.py`](daily_task_2026_11_14.py) | `Plant`, `GardenPlot`, `GardenManager` | Garden management, composition and harvest tracking. |
| [`daily_task_2026_11_15.py`](daily_task_2026_11_15.py) | `SmartDevice`, `SmartLight`, `SmartFan`, `SmartHome`, `WordPuzzleGame` | Smart-device controls, energy estimates and an interactive word puzzle. |
| [`daily_task_2026_11_17.py`](daily_task_2026_11_17.py) | `MediaAsset`, `Photo`, `Video`, `PhotoAlbum`, `PortfolioLibrary` | Abstract classes, inheritance, composition, searching and sorting. |
| [`daily_task_2026_11_22.py`](daily_task_2026_11_22.py) | `PhotoEntry`, `Participant`, `PhotographyContest` | Photo submissions, score validation, category winners and leaderboard. |
| [`daily_task_2026_11_24.py`](daily_task_2026_11_24.py) | `Workshop`, `OnlineWorkshop`, `InPersonWorkshop`, `Participant`, `Registration`, `WorkshopManager` | Workshop registration, capacity, fee calculation and cancellation. |
| [`daily_task_2026_11_26.py`](daily_task_2026_11_26.py) | `StudyTopic`, `StudySession`, `StudyPlanner` | Study scheduling, time-conflict detection, session status and progress reports. |
| [`test_parcel_tracking.py`](test_parcel_tracking.py) | `ParcelTests` | Unit tests for parcel charges, validation, delivery status and duplicate IDs. |

## Daily OOP Projects

### 26 November 2026 — Study Session Planner

**File:** [`daily_task_2026_11_26.py`](daily_task_2026_11_26.py)

- Creates and validates study topics.
- Schedules sessions and detects overlapping planned sessions.
- Tracks Planned, Completed and Skipped statuses.
- Stores revision notes and displays a study progress report.

**Concepts:** classes, composition, encapsulation, properties, validation, `datetime`, filtering and sorting.

Run:

```bash
python daily_task_2026_11_26.py
```

### 24 November 2026 — Art Workshop Registration Manager

**File:** [`daily_task_2026_11_24.py`](daily_task_2026_11_24.py)

- Manages online and in-person workshops with different fee rules.
- Registers participants while checking capacity and duplicate entries.
- Calculates fees through overridden methods.
- Supports cancellation and registration reports.

**Concepts:** inheritance, encapsulation, polymorphism, composition, validation, `Decimal` and exception handling.

Run:

```bash
python daily_task_2026_11_24.py
```

### 22 November 2026 — Photography Contest Manager

**File:** [`daily_task_2026_11_22.py`](daily_task_2026_11_22.py)

- Registers contest participants and photo entries.
- Validates entry details and scores.
- Calculates average scores, category winners and a leaderboard.

**Concepts:** dataclasses, encapsulation, composition, validation, sorting and aggregation.

Run:

```bash
python daily_task_2026_11_22.py
```

### 17 November 2026 — Photo & Video Portfolio Manager

**File:** [`daily_task_2026_11_17.py`](daily_task_2026_11_17.py)

Organizes photo and video assets into albums and a portfolio library.

**Concepts:** abstract base classes, inheritance, method overriding, composition, searching and sorting.

### 15 November 2026 — Smart Home Energy Monitor & Word Puzzle

**File:** [`daily_task_2026_11_15.py`](daily_task_2026_11_15.py)

Manages smart lights and fans, estimates energy use and includes an interactive word puzzle.

**Concepts:** inheritance, encapsulation, polymorphism, composition and validation.

### Earlier Practice Projects

| Date | Project | File |
|---|---|---|
| 14 Nov 2026 | Community Garden Manager | [`daily_task_2026_11_14.py`](daily_task_2026_11_14.py) |
| 12 Nov 2026 | Photo Album Organizer | [`daily_task_2026_11_12.py`](daily_task_2026_11_12.py) |
| 9 Nov 2026 | Parcel Delivery Tracking System | [`daily_task_2026_11_09.py`](daily_task_2026_11_09.py) |
| 8 Nov 2026 | Photography Equipment Rental Tracker | [`daily_task_2026_11_08.py`](daily_task_2026_11_08.py) |
| 4 Nov 2026 | Smart Plant Care Tracker | [`daily_task_2026_11_04.py`](daily_task_2026_11_04.py) |
| 3 Nov 2026 | Music Playlist Manager | [`daily_task_2026_11_03.py`](daily_task_2026_11_03.py) |

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

1. Start with `laptop_class.py` to understand classes, objects and constructors.
2. Practise methods and calculations using `calculator_methods.py`, `employee_salary.py` and `product_class.py`.
3. Learn inheritance and polymorphism with `opp.py`.
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
