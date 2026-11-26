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
python study_session_planner.py
```

On Windows:

```bash
py study_session_planner.py
```

Replace the filename with any exercise from the file guide below.

## Complete File Guide

| File | Main classes | What you will practise |
|---|---|---|
| [`laptop_class.py`](laptop_class.py) | `Laptop` | Classes, objects, constructors and object attributes. |
| [`calculator.py`](calculator.py) | `Calculator` | Instance methods, arithmetic, validation and division-by-zero handling. |
| [`employee_annual_salary_calculator.py`](employee_annual_salary_calculator.py) | `Employee` | Employee details, salary validation and annual salary calculation. |
| [`product_price_calculator.py`](product_price_calculator.py) | `Product` | Attributes, price and quantity validation, and total-price calculation. |
| [`vehicle_inheritance_polymorphism.py`](vehicle_inheritance_polymorphism.py) | `Vehicle` and child classes | Inheritance, `super()`, method overriding and polymorphism. |
| [`course_registration_system.py`](course_registration_system.py) | `Student`, `Course` | Object interaction, enrolment, duplicate prevention and capacity validation. |
| [`event_ticket_booking_system.py`](event_ticket_booking_system.py) | `Event`, `TicketBooking` | Ticket booking, availability, total-price calculation and cancellation. |
| [`music_playlist_manager.py`](music_playlist_manager.py) | `Track`, `Playlist` | Playlist management, adding/removing tracks and duration calculation. |
| [`smart_plant_care_tracker.py`](smart_plant_care_tracker.py) | `Plant`, `PlantCareTracker` | Watering records, date validation and care reminders. |
| [`photography_equipment_rental_tracker.py`](photography_equipment_rental_tracker.py) | `Equipment`, `Camera`, `Tripod`, `RentalDesk` | Equipment rental, returns, composition and late fees. |
| [`parcel_delivery_tracking_system.py`](parcel_delivery_tracking_system.py) | `Parcel`, `ExpressParcel`, `FragileParcel`, `DeliveryHub` | Parcel tracking, shipping charges and polymorphism. |
| [`photo_album_organizer.py`](photo_album_organizer.py) | `Photo`, `PhotoAlbum` | Photo organization, tags, searching, formats and storage calculations. |
| [`community_garden_manager.py`](community_garden_manager.py) | `Plant`, `GardenPlot`, `GardenManager` | Garden management, composition and harvest tracking. |
| [`smart_home_energy_monitor_word_puzzle.py`](smart_home_energy_monitor_word_puzzle.py) | `SmartDevice`, `SmartLight`, `SmartFan`, `SmartHome`, `WordPuzzleGame` | Smart-device controls, energy estimates and an interactive word puzzle. |
| [`photo_video_portfolio_manager.py`](photo_video_portfolio_manager.py) | `MediaAsset`, `Photo`, `Video`, `PhotoAlbum`, `PortfolioLibrary` | Abstract classes, inheritance, composition, searching and sorting. |
| [`photography_contest_manager.py`](photography_contest_manager.py) | `PhotoEntry`, `Participant`, `PhotographyContest` | Photo submissions, score validation, category winners and leaderboard. |
| [`art_workshop_registration_manager.py`](art_workshop_registration_manager.py) | `Workshop`, `OnlineWorkshop`, `InPersonWorkshop`, `Participant`, `Registration`, `WorkshopManager` | Workshop registration, capacity, fee calculation and cancellation. |
| [`study_session_planner.py`](study_session_planner.py) | `StudyTopic`, `StudySession`, `StudyPlanner` | Study scheduling, time-conflict detection, session status and progress reports. |
| [`parcel_delivery_tracking_tests.py`](parcel_delivery_tracking_tests.py) | `ParcelTests` | Unit tests for parcel charges, validation, delivery status and duplicate IDs. |

## Daily OOP Projects

### 26 November 2026 — Study Session Planner

**File:** [`study_session_planner.py`](study_session_planner.py)

- Creates and validates study topics.
- Schedules sessions and detects overlapping planned sessions.
- Tracks Planned, Completed and Skipped statuses.
- Stores revision notes and displays a study progress report.

**Concepts:** classes, composition, encapsulation, properties, validation, `datetime`, filtering and sorting.

Run:

```bash
python study_session_planner.py
```

### 24 November 2026 — Art Workshop Registration Manager

**File:** [`art_workshop_registration_manager.py`](art_workshop_registration_manager.py)

- Manages online and in-person workshops with different fee rules.
- Registers participants while checking capacity and duplicate entries.
- Calculates fees through overridden methods.
- Supports cancellation and registration reports.

**Concepts:** inheritance, encapsulation, polymorphism, composition, validation, `Decimal` and exception handling.

Run:

```bash
python art_workshop_registration_manager.py
```

### 22 November 2026 — Photography Contest Manager

**File:** [`photography_contest_manager.py`](photography_contest_manager.py)

- Registers contest participants and photo entries.
- Validates entry details and scores.
- Calculates average scores, category winners and a leaderboard.

**Concepts:** dataclasses, encapsulation, composition, validation, sorting and aggregation.

Run:

```bash
python photography_contest_manager.py
```

### 17 November 2026 — Photo & Video Portfolio Manager

**File:** [`photo_video_portfolio_manager.py`](photo_video_portfolio_manager.py)

Organizes photo and video assets into albums and a portfolio library.

**Concepts:** abstract base classes, inheritance, method overriding, composition, searching and sorting.

### 15 November 2026 — Smart Home Energy Monitor & Word Puzzle

**File:** [`smart_home_energy_monitor_word_puzzle.py`](smart_home_energy_monitor_word_puzzle.py)

Manages smart lights and fans, estimates energy use and includes an interactive word puzzle.

**Concepts:** inheritance, encapsulation, polymorphism, composition and validation.

### Earlier Practice Projects

| Date | Project | File |
|---|---|---|
| 14 Nov 2026 | Community Garden Manager | [`community_garden_manager.py`](community_garden_manager.py) |
| 12 Nov 2026 | Photo Album Organizer | [`photo_album_organizer.py`](photo_album_organizer.py) |
| 9 Nov 2026 | Parcel Delivery Tracking System | [`parcel_delivery_tracking_system.py`](parcel_delivery_tracking_system.py) |
| 8 Nov 2026 | Photography Equipment Rental Tracker | [`photography_equipment_rental_tracker.py`](photography_equipment_rental_tracker.py) |
| 4 Nov 2026 | Smart Plant Care Tracker | [`smart_plant_care_tracker.py`](smart_plant_care_tracker.py) |
| 3 Nov 2026 | Music Playlist Manager | [`music_playlist_manager.py`](music_playlist_manager.py) |

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
2. Practise methods and calculations using `calculator.py`, `employee_annual_salary_calculator.py` and `product_price_calculator.py`.
3. Learn inheritance and polymorphism with `vehicle_inheritance_polymorphism.py`.
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
