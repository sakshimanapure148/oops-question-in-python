# Python OOP Practice & Mini-Projects

A structured collection of Python Object-Oriented Programming (OOP) exercises and practical mini-projects by **Sakshi Manapure**.

This repository is designed to build OOP skills step by step—from creating classes and objects to using encapsulation, inheritance, polymorphism, composition, validation, exception handling and automated tests.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Learning](https://img.shields.io/badge/Focus-Python%20OOP-green)](#learning-roadmap)
[![Tests](https://img.shields.io/badge/Tests-unittest-orange)](#automated-tests)

---

## Table of Contents

- [Repository Overview](#repository-overview)
- [Getting Started](#getting-started)
- [Complete File Guide](#complete-file-guide)
- [Daily OOP Projects](#daily-oop-projects)
- [Automated Tests](#automated-tests)
- [OOP Concepts Practised](#oop-concepts-practised)
- [Suggested Learning Roadmap](#learning-roadmap)
- [How to Contribute](#how-to-contribute)
- [About the Author](#about-the-author)

## Repository Overview

| Area | Description |
|---|---|
| Beginner practice | Small, focused exercises for classes, objects, attributes and methods |
| OOP fundamentals | Inheritance, encapsulation, method overriding and polymorphism |
| Mini-projects | Practical systems such as booking, registration, tracking and management |
| Code quality | Input validation, meaningful exceptions and readable structure |
| Testing | A built-in `unittest` test suite for parcel tracking |

All projects are written in Python. The repository's examples use Python's standard library; no third-party package is needed for the current exercises.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sakshimanapure148/oops-question-in-python.git
cd oops-question-in-python
```

### 2. Check Python

```bash
python --version
```

On Windows, you can use:

```bash
py --version
```

Python 3.9 or later is recommended.

### 3. Run a Python file

Choose any exercise and run it from the repository folder:

```bash
python laptop_class.py
```

On Windows:

```bash
py laptop_class.py
```

Replace `laptop_class.py` with the file you want to practise. Each exercise can be run independently unless it is a test file.

## Complete File Guide

The table below documents **every Python file currently in this repository**.

| File | Main classes | What you will practise |
|---|---|---|
| [`laptop_class.py`](laptop_class.py) | `Laptop` | Create objects, use a constructor, store attributes and display object details. |
| [`calculator_methods.py`](calculator_methods.py) | `Calculator` | Write instance methods for addition, subtraction, multiplication and division; validate numeric inputs and handle division by zero. |
| [`employee_salary.py`](employee_salary.py) | `Employee` | Store employee information, validate salary data and calculate annual salary. |
| [`product_class.py`](product_class.py) | `Product` | Work with object attributes, validate price and quantity, and calculate a total price. |
| [`opp.py`](opp.py) | `Vehicle`, `Car`, `Bicycle` | Learn inheritance, `super()`, method overriding and polymorphism through different vehicle types. |
| [`course_registration_system.py`](course_registration_system.py) | `Student`, `Course` | Connect objects, enrol and remove students, prevent duplicate enrolments and enforce course capacity. |
| [`event_ticket_booking.py`](event_ticket_booking.py) | `Event`, `TicketBooking` | Model event bookings, calculate totals and discounts, cancel bookings and restore ticket availability. Uses `Decimal` for ticket-price calculations. |
| [`daily_task_2026_11_03.py`](daily_task_2026_11_03.py) | `Track`, `Playlist` | Build a playlist, add and remove tracks, prevent duplicates and calculate total duration. |
| [`daily_task_2026_11_04.py`](daily_task_2026_11_04.py) | `Plant`, `PlantCareTracker` | Track watering records, use read-only properties, validate dates and display plant-care reminders. |
| [`daily_task_2026_11_08.py`](daily_task_2026_11_08.py) | `Equipment`, `Camera`, `Tripod`, `RentalDesk` | Practise inheritance and method overriding while managing equipment rentals, due dates and late-return charges. |
| [`daily_task_2026_11_09.py`](daily_task_2026_11_09.py) | `Parcel`, `ExpressParcel`, `FragileParcel`, `DeliveryHub` | Manage parcel registration and delivery status; calculate different shipping charges using inheritance and polymorphism. |
| [`daily_task_2026_11_12.py`](daily_task_2026_11_12.py) | `Photo`, `PhotoAlbum` | Organize photo records, manage private tags, search by tag, validate file formats and calculate storage. |
| [`daily_task_2026_11_14.py`](daily_task_2026_11_14.py) | `Plant`, `GardenPlot`, `GardenManager` | Use composition to manage garden plots and plants, track harvests, validate records and generate summaries. |
| [`test_parcel_tracking.py`](test_parcel_tracking.py) | `ParcelTests` | Run automated tests for parcel shipping costs, validation, delivery-status rules, duplicate IDs and collection totals. |

## Daily OOP Projects

### 14 November 2026 — Community Garden Manager

**File:** [`daily_task_2026_11_14.py`](daily_task_2026_11_14.py)

Manage a community garden containing multiple plots and plants.

- `Plant` stores plant details, planting date and private harvest status.
- `GardenPlot` manages plant objects, prevents duplicate plant IDs and calculates growing/harvested totals.
- `GardenManager` manages multiple plots and prints a garden-wide report.

**Key concepts:** composition, encapsulation, read-only properties, dictionaries, date handling, validation and exception handling.

Run it:

```bash
python daily_task_2026_11_14.py
```

### 12 November 2026 — Photo Album Organizer

**File:** [`daily_task_2026_11_12.py`](daily_task_2026_11_12.py)

Organize photos into an album, manage tags, search by tag and calculate storage use.

**Key concepts:** composition, encapsulation, private attributes, properties, static methods, sets, validation and assertions.

Run it:

```bash
python daily_task_2026_11_12.py
```

### 9 November 2026 — Parcel Delivery Tracking System

**File:** [`daily_task_2026_11_09.py`](daily_task_2026_11_09.py)

Register and track regular, express and fragile parcels, update delivery progress and calculate shipping charges.

**Key concepts:** inheritance, `super()`, encapsulation, properties, method overriding, polymorphism and validation.

Run it:

```bash
python daily_task_2026_11_09.py
```

### 8 November 2026 — Photography Equipment Rental Tracker

**File:** [`daily_task_2026_11_08.py`](daily_task_2026_11_08.py)

Manage camera and tripod inventory, process rentals and returns, and calculate late fees.

**Key concepts:** inheritance, method overriding, encapsulation, date calculations and object management.

Run it:

```bash
python daily_task_2026_11_08.py
```

### 4 November 2026 — Smart Plant Care Tracker

**File:** [`daily_task_2026_11_04.py`](daily_task_2026_11_04.py)

Register plants, record watering dates and calculate when a plant needs attention.

**Key concepts:** encapsulation, properties, date validation, methods and object interaction.

Run it:

```bash
python daily_task_2026_11_04.py
```

### 3 November 2026 — Music Playlist Manager

**File:** [`daily_task_2026_11_03.py`](daily_task_2026_11_03.py)

Create a playlist, add or remove tracks, prevent duplicate entries and calculate the playlist duration.

**Key concepts:** classes, objects, encapsulation, lists, validation and object interaction.

Run it:

```bash
python daily_task_2026_11_03.py
```

## Automated Tests

The parcel tracking project includes a test suite built with Python's standard `unittest` module.

Run all available tests from the repository folder:

```bash
python -m unittest -v
```

On Windows:

```bash
py -m unittest -v
```

The current test file checks:

- Regular, express and fragile parcel shipping-cost calculations.
- Rejection of invalid parcel weight.
- Prevention of delivery-status changes that move backwards.
- Duplicate tracking-ID validation.
- Total shipping collection.

The tests import the parcel classes from `daily_task_2026_11_09.py`. If you add new features, consider adding matching tests to keep behaviour reliable.

## OOP Concepts Practised

| Concept | Meaning in this repository |
|---|---|
| Class and object | Create reusable blueprints and individual instances. |
| Constructor | Initialize object data using `__init__()`. |
| Instance method | Define behaviour that works with object data. |
| Encapsulation | Keep internal state private and control how it changes. |
| Inheritance | Reuse and extend behaviour from a parent class. |
| `super()` | Call parent-class behaviour from a child class. |
| Method overriding | Give a child class its own implementation of a method. |
| Polymorphism | Use a common method call with different object behaviours. |
| Composition | Build a larger object by managing other objects. |
| Property | Provide controlled, readable access to object data. |
| Validation | Reject invalid values before they enter an object. |
| Exception handling | Handle invalid operations with clear errors. |
| Unit testing | Check expected behaviour with repeatable tests. |

## Suggested Learning Roadmap

1. Start with `laptop_class.py` to understand classes, objects and constructors.
2. Practise methods and calculations with `calculator_methods.py`, `employee_salary.py` and `product_class.py`.
3. Learn inheritance and polymorphism with `opp.py`.
4. Practise object interaction with `course_registration_system.py` and `event_ticket_booking.py`.
5. Explore encapsulation and composition in the daily mini-projects.
6. Run `test_parcel_tracking.py` through the `unittest` command and try writing additional tests.

Try to understand the logic, modify the sample values, and add one small feature after completing each exercise.

## How to Contribute

This is a learning repository. To add a new exercise:

1. Create a separate, clearly named `.py` file.
2. Give classes and methods meaningful names.
3. Add input validation and handle expected errors.
4. Include a small example under `if __name__ == "__main__":`.
5. Update this README with the new file, its purpose, concepts and run command.
6. Add tests when the project has behaviour that should be checked automatically.

Keep each exercise focused and avoid mixing unrelated tasks into an existing file.

## About the Author

**Sakshi Manapure**  
Python Full Stack Developer — Learning and building with Python, Django, JavaScript and SQL.

- GitHub: [@sakshimanapure148](https://github.com/sakshimanapure148)
- Repository: [oops-question-in-python](https://github.com/sakshimanapure148/oops-question-in-python)

---

*Learning OOP one class, one object and one project at a time.*
