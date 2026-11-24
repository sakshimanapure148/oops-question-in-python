# Python OOP Practice & Mini-Projects

A collection of beginner-to-intermediate Python Object-Oriented Programming exercises and mini-projects by **Sakshi Manapure**.

The repository builds OOP skills step by step: classes, objects, constructors, methods, encapsulation, inheritance, polymorphism, composition, validation, exception handling and unit testing.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Focus](https://img.shields.io/badge/Focus-Python%20OOP-green)
![Tests](https://img.shields.io/badge/Tests-unittest-orange)

---

## Table of Contents

- [Repository Overview](#repository-overview)
- [Getting Started](#getting-started)
- [Complete File Guide](#complete-file-guide)
- [Daily OOP Projects](#daily-oop-projects)
- [Run Automated Tests](#run-automated-tests)
- [OOP Concepts Practised](#oop-concepts-practised)
- [Suggested Learning Roadmap](#suggested-learning-roadmap)
- [About the Author](#about-the-author)

## Repository Overview

| Section | What it contains |
|---|---|
| Beginner exercises | Small examples for classes, objects, attributes and methods |
| OOP fundamentals | Encapsulation, inheritance, overriding and polymorphism |
| Mini-projects | Registration, booking, tracking, portfolio and management systems |
| Code quality | Input validation, clear exceptions and readable code |
| Testing | Automated tests using Python's built-in `unittest` module |

All current exercises use Python's standard library; no third-party packages are required.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sakshimanapure148/oops-question-in-python.git
cd oops-question-in-python
```

### 2. Check your Python version

```bash
python --version
```

On Windows, you can use `py --version`. Python 3.9 or later is recommended.

### 3. Run any exercise

```bash
python laptop_class.py
```

On Windows:

```bash
py laptop_class.py
```

Replace the filename with the exercise you want to run. Each project is designed to run independently.

## Complete File Guide

This table lists every Python file currently present in the repository.

| File | Main classes | Purpose and concepts |
|---|---|---|
| [`laptop_class.py`](laptop_class.py) | `Laptop` | Beginner exercise for constructors, object attributes and displaying object details. |
| [`calculator_methods.py`](calculator_methods.py) | `Calculator` | Basic arithmetic instance methods, numeric validation and division-by-zero handling. |
| [`employee_salary.py`](employee_salary.py) | `Employee` | Store employee details, validate monthly salary and calculate annual salary. |
| [`product_class.py`](product_class.py) | `Product` | Product attributes, price and quantity validation, and total-price calculation. |
| [`opp.py`](opp.py) | `Vehicle` and child classes | Inheritance, `super()`, method overriding and polymorphism with vehicle examples. |
| [`course_registration_system.py`](course_registration_system.py) | `Student`, `Course` | Object interaction, course enrolment, duplicate prevention and capacity validation. |
| [`event_ticket_booking.py`](event_ticket_booking.py) | `Event`, `TicketBooking` | Event ticket booking, total-price calculation, ticket availability and cancellation. |
| [`daily_task_2026_11_03.py`](daily_task_2026_11_03.py) | `Track`, `Playlist` | Music playlist manager: add/remove tracks, prevent duplicates and calculate duration. |
| [`daily_task_2026_11_04.py`](daily_task_2026_11_04.py) | `Plant`, `PlantCareTracker` | Plant watering records, date validation, properties and care reminders. |
| [`daily_task_2026_11_08.py`](daily_task_2026_11_08.py) | `Equipment`, `Camera`, `Tripod`, `RentalDesk` | Photography equipment rental and returns, inheritance, composition and late-fee calculations. |
| [`daily_task_2026_11_09.py`](daily_task_2026_11_09.py) | `Parcel`, `ExpressParcel`, `FragileParcel`, `DeliveryHub` | Parcel registration, delivery-status tracking and shipping-cost polymorphism. |
| [`daily_task_2026_11_12.py`](daily_task_2026_11_12.py) | `Photo`, `PhotoAlbum` | Photo organizer with tags, searching, supported file formats and storage calculations. |
| [`daily_task_2026_11_14.py`](daily_task_2026_11_14.py) | `Plant`, `GardenPlot`, `GardenManager` | Community garden manager using composition, harvest tracking, properties and validation. |
| [`daily_task_2026_11_15.py`](daily_task_2026_11_15.py) | `SmartDevice`, `SmartLight`, `SmartFan`, `SmartHome`, `WordPuzzleGame` | Smart-home device controls and energy estimates, plus an interactive word puzzle. Practises inheritance, encapsulation and polymorphism. |
| [`daily_task_2026_11_17.py`](daily_task_2026_11_17.py) | `MediaAsset`, `Photo`, `Video`, `PhotoAlbum`, `PortfolioLibrary` | Photo and video portfolio manager using abstract classes, inheritance, composition, searching and sorting. |
| [`daily_task_2026_11_22.py`](daily_task_2026_11_22.py) | `PhotoEntry`, `Participant`, `PhotographyContest` | Photography contest with validated submissions, average scores and a leaderboard. |
| [`daily_task_2026_11_24.py`](daily_task_2026_11_24.py) | `Workshop`, `OnlineWorkshop`, `InPersonWorkshop`, `Participant`, `Registration`, `WorkshopManager` | Art workshop registration, capacity checks, fee calculation, cancellation and reports. |
| [`test_parcel_tracking.py`](test_parcel_tracking.py) | `ParcelTests` | Unit tests for parcel charges, validation, delivery status, duplicate IDs and collection totals. |

## Daily OOP Projects

### 24 November 2026 — Art Workshop Registration Manager

**File:** [`daily_task_2026_11_24.py`](daily_task_2026_11_24.py)

- Creates online and in-person workshops with different fee rules.
- Registers participants and checks available capacity.
- Prevents duplicate registrations.
- Calculates fees using overridden methods.
- Cancels registrations and updates available seats.
- Displays workshop and registration information.

**Concepts:** inheritance, encapsulation, polymorphism, composition, validation, `Decimal` calculations and exception handling.

Run:

```bash
python daily_task_2026_11_24.py
```

### 22 November 2026 — Photography Contest Manager

**File:** [`daily_task_2026_11_22.py`](daily_task_2026_11_22.py)

- Registers participants and their photo entries.
- Validates entry details and scores.
- Calculates average scores and displays a leaderboard.

**Concepts:** dataclasses, encapsulation, composition, validation, sorting and aggregation.

Run:

```bash
python daily_task_2026_11_22.py
```

### 17 November 2026 — Photo & Video Portfolio Manager

**File:** [`daily_task_2026_11_17.py`](daily_task_2026_11_17.py)

- Models photos and videos as media assets.
- Organizes assets into albums and a portfolio library.
- Demonstrates abstract base classes, overriding, searching and sorting.

Run:

```bash
python daily_task_2026_11_17.py
```

### 15 November 2026 — Smart Home Energy Monitor & Word Puzzle

**File:** [`daily_task_2026_11_15.py`](daily_task_2026_11_15.py)

- Manages smart lights and fans.
- Controls device settings and estimates energy usage.
- Includes a small interactive word puzzle game.

**Concepts:** inheritance, encapsulation, polymorphism, composition, validation and assertions.

Run:

```bash
python daily_task_2026_11_15.py
```

### 14 November 2026 — Community Garden Manager

**File:** [`daily_task_2026_11_14.py`](daily_task_2026_11_14.py)

Manages garden plots and plants, tracks harvest status and creates garden summaries.

Run:

```bash
python daily_task_2026_11_14.py
```

### 12 November 2026 — Photo Album Organizer

**File:** [`daily_task_2026_11_12.py`](daily_task_2026_11_12.py)

Organizes photos, manages tags, searches by tag and calculates storage use.

Run:

```bash
python daily_task_2026_11_12.py
```

### 9 November 2026 — Parcel Delivery Tracking System

**File:** [`daily_task_2026_11_09.py`](daily_task_2026_11_09.py)

Registers regular, express and fragile parcels, tracks delivery progress and calculates shipping charges.

Run:

```bash
python daily_task_2026_11_09.py
```

### 8 November 2026 — Photography Equipment Rental Tracker

**File:** [`daily_task_2026_11_08.py`](daily_task_2026_11_08.py)

Manages camera and tripod inventory, rentals, returns and late fees.

Run:

```bash
python daily_task_2026_11_08.py
```

### 4 November 2026 — Smart Plant Care Tracker

**File:** [`daily_task_2026_11_04.py`](daily_task_2026_11_04.py)

Stores plant details, records watering dates and calculates care reminders.

Run:

```bash
python daily_task_2026_11_04.py
```

### 3 November 2026 — Music Playlist Manager

**File:** [`daily_task_2026_11_03.py`](daily_task_2026_11_03.py)

Creates playlists, adds and removes tracks, prevents duplicates and calculates total duration.

Run:

```bash
python daily_task_2026_11_03.py
```

## Run Automated Tests

The parcel tracking project includes tests using Python's built-in `unittest` framework.

Run all tests from the repository folder:

```bash
python -m unittest -v
```

On Windows:

```bash
py -m unittest -v
```

The test suite checks parcel shipping costs, invalid weights, delivery-status rules, duplicate tracking IDs and collection totals. The tests import parcel classes from `daily_task_2026_11_09.py`.

## OOP Concepts Practised

| Concept | Meaning |
|---|---|
| Class and object | A class is a blueprint; an object is an instance of that class. |
| Constructor | `__init__()` initializes object data. |
| Instance method | A method that works with an object's data. |
| Encapsulation | Protects internal state and controls how it is changed. |
| Inheritance | Allows a child class to reuse and extend a parent class. |
| `super()` | Calls methods or constructors from the parent class. |
| Method overriding | A child class provides its own version of a parent method. |
| Polymorphism | The same method call can behave differently for different objects. |
| Composition | Builds a larger object using other objects. |
| Property | Provides controlled access to attributes. |
| Validation | Checks values before accepting them. |
| Exception handling | Handles invalid operations with clear errors. |
| Unit testing | Checks expected program behaviour automatically. |

## Suggested Learning Roadmap

1. Start with `laptop_class.py` for classes, objects and constructors.
2. Practise methods and calculations with `calculator_methods.py`, `employee_salary.py` and `product_class.py`.
3. Learn inheritance and polymorphism with `opp.py`.
4. Practise object interaction with `course_registration_system.py` and `event_ticket_booking.py`.
5. Explore encapsulation and composition in the dated mini-projects.
6. Run `python -m unittest -v` and try adding more tests.

Try changing sample values and adding one small feature after understanding each program.

## How to Add a New Exercise

1. Create a separate, clearly named `.py` file.
2. Use meaningful class, method and variable names.
3. Validate input and handle expected errors.
4. Include a runnable example under `if __name__ == "__main__":`.
5. Add the file and its purpose to the **Complete File Guide**.
6. Add tests when the program has behaviour that should be checked automatically.

## About the Author

**Sakshi Manapure**  
Python Full Stack Developer — learning and building with Python, Django, JavaScript and SQL.

- GitHub: [@sakshimanapure148](https://github.com/sakshimanapure148)
- Repository: [oops-question-in-python](https://github.com/sakshimanapure148/oops-question-in-python)

---

*Learning OOP one class, one object and one project at a time.*
