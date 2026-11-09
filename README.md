# Python OOP Practice

A growing collection of beginner-friendly Python Object-Oriented Programming exercises and practical mini-projects by **Sakshi Manapure**.

This repository is a daily learning space to practise writing clean, reusable Python code and understand how OOP concepts are used in real-world applications.

## Learning Goals

- Understand classes, objects, constructors and instance methods.
- Practise encapsulation, inheritance and polymorphism.
- Use properties and validation to protect object data.
- Build small projects that combine multiple OOP concepts.
- Improve problem-solving skills through regular coding practice.

## Repository Structure

| File | Project / Concepts |
|---|---|
| `opp.py` | OOP fundamentals, inheritance, method overriding and polymorphism |
| `laptop_class.py` | Classes, objects, constructors and attributes |
| `calculator_methods.py` | Instance methods and arithmetic operations |
| `employee_salary.py` | Methods, validation and salary calculations |
| `product_class.py` | Properties, quantity validation and total price |
| `event_ticket_booking.py` | Object interaction, booking and cancellation |
| `course_registration_system.py` | Student and course objects, enrollment and capacity validation |
| `daily_task_2026_11_03.py` | Playlist manager, encapsulation and duplicate prevention |
| `daily_task_2026_11_04.py` | Plant-care tracker, properties and date handling |
| `daily_task_2026_11_08.py` | Photography equipment rental, inheritance and late-fee calculation |
| `daily_task_2026_11_09.py` | Parcel delivery tracking, inheritance, encapsulation and polymorphism |

## Latest Daily Task — 09 November 2026

### Parcel Delivery Tracking System

**Problem statement:** Create a parcel tracking application that registers different parcel types, tracks delivery progress and calculates shipping charges.

### OOP Design

- **`Parcel`** — Base class containing the tracking ID, receiver, weight and private delivery status.
- **`ExpressParcel`** — Child class that overrides the shipping-cost method to include an express surcharge.
- **`FragileParcel`** — Child class that overrides the shipping-cost method to include a special-handling surcharge.
- **`DeliveryHub`** — Manages parcel registration, tracking and the total shipping collection.

### Features

1. Register regular, express and fragile parcels.
2. Validate tracking IDs, receiver names and parcel weights.
3. Prevent duplicate tracking IDs.
4. Keep delivery status private and expose it through a read-only property.
5. Validate delivery status updates and prevent moving to an earlier status.
6. Find and display parcel details using a tracking ID.
7. Calculate different shipping charges through method overriding.
8. Calculate the total shipping collection.
9. Verify important results with assertions.

### Concepts Practised

`class`, `object`, `__init__()`, inheritance, `super()`, encapsulation, private attributes, `@property`, method overriding, polymorphism, dictionaries, exception handling and assertions.

### Sample Output

```text
NGP101 registered.
NGP102 registered.
NGP103 registered.

--- Nagpur Central Hub: Parcel List ---
NGP101 | Aarav | 2.5 kg
Status: Booked | Shipping: Rs. 90.00
-----------------------------------
NGP102 | Meera | 1.2 kg
Status: Booked | Shipping: Rs. 139.00
-----------------------------------
NGP103 | Kabir | 3.0 kg
Status: Booked | Shipping: Rs. 150.00
-----------------------------------

Updated status: Out for Delivery
Total shipping collection: Rs. 379.00
All checks passed successfully.
```

### Run the Latest Task

Make sure Python 3.9 or later is installed. No external packages are required.

```bash
python daily_task_2026_11_09.py
```

On Windows, you can also run:

```bash
py daily_task_2026_11_09.py
```

## How to Run Any Exercise

1. Clone or download this repository.
2. Open the project folder in VS Code or a terminal.
3. Choose the Python file you want to practise.
4. Run it using `python filename.py` or `py filename.py` on Windows.

## OOP Topics Covered in This Repository

- Classes, objects, attributes and methods
- Constructors and the `self` keyword
- Encapsulation and private attributes
- Inheritance and `super()`
- Method overriding and polymorphism
- Properties and data validation
- Object interaction and composition
- Dictionaries for managing objects
- Exception handling and assertions
- Date handling and calculations

## Ideas for Further Practice

- Add a new parcel type with its own shipping rule.
- Add a method to list only parcels that are still in transit.
- Add a delivery hub feature to mark parcels as delivered.
- Write additional tests for invalid input and duplicate IDs.
- Extend an existing mini-project with another OOP concept.

## Author

**Sakshi Manapure**

[GitHub Profile](https://github.com/sakshimanapure148)
