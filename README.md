# Python OOP Practice

A collection of beginner-friendly Python Object-Oriented Programming (OOP) exercises and practical mini-projects by **Sakshi Manapure**.

The goal of this repository is to strengthen Python fundamentals through small, readable programs with real-world examples.

## Repository Structure

| File | Topic / Concepts |
|---|---|
| `opp.py` | OOP fundamentals, inheritance, overriding and polymorphism |
| `laptop_class.py` | Classes, objects, constructors and attributes |
| `calculator_methods.py` | Instance methods and arithmetic operations |
| `employee_salary.py` | Methods, validation and salary calculations |
| `product_class.py` | Properties, quantity validation and total price |
| `event_ticket_booking.py` | Object interaction, booking and cancellation |
| `daily_task_2026_11_03.py` | Playlist manager, encapsulation and duplicate prevention |
| `daily_task_2026_11_04.py` | Plant-care tracker, properties and date handling |
| `daily_task_2026_11_08.py` | Photography equipment rental, inheritance and late-fee calculation |
| `daily_task_2026_11_09.py` | Parcel delivery tracking, inheritance, encapsulation and polymorphism |
| `course_registration_system.py` | Student/course objects, enrollment and capacity validation |

## Latest Task — 08 November 2026

### Photography Equipment Rental Tracker

**Problem statement:** Build a small rental system that manages photography equipment such as cameras and tripods. A customer can rent available equipment for a selected number of days and return it later.

**OOP design:**

- `Equipment`: Base class containing equipment ID, name, daily rate and rental availability.
- `Camera`: Child class that adds sensor information.
- `Tripod`: Child class that adds maximum height information.
- `RentalDesk`: Manages the inventory, rental process, returns and late fees.

**Features implemented:**

1. Add equipment to the inventory.
2. Prevent duplicate equipment IDs.
3. Display equipment details and availability.
4. Rent equipment and calculate the rental amount.
5. Prevent an already-rented item from being rented again.
6. Return rented equipment and calculate late fees.
7. Validate IDs, names, rates, rental periods and dates.
8. Use fixed sample dates and assertions for predictable demonstrations.

**Concepts practised:** Classes and objects, constructors, inheritance, `super()`, method overriding, encapsulation, properties, composition, validation and date calculations.


| `daily_task_2026_11_09.py` | Parcel delivery tracking, inheritance, encapsulation and polymorphism |

## Latest Task — 09 November 2026

### Parcel Delivery Tracking System

**Problem statement:** Create a parcel tracking system that registers parcels, tracks delivery progress and calculates shipping charges.

**OOP design:**
- `Parcel`: Base class with tracking ID, receiver, weight and private delivery status.
- `ExpressParcel`: Adds an express delivery surcharge by overriding the shipping method.
- `FragileParcel`: Adds a special-handling surcharge through method overriding.
- `DeliveryHub`: Registers parcels, prevents duplicate tracking IDs and tracks shipments.

**Features implemented:**
1. Register regular, express and fragile parcels.
2. Validate tracking IDs, receiver names and parcel weights.
3. Prevent duplicate tracking IDs.
4. Keep delivery status encapsulated with a read-only property.
5. Prevent delivery statuses from moving backwards.
6. Track a parcel using its tracking ID.
7. Calculate shipping charges using polymorphism.
8. Run assertion checks for expected costs and status updates.

**Concepts practised:** Classes, objects, inheritance, `super()`, encapsulation, properties, method overriding, polymorphism, dictionaries, validation and assertions.

**Run the task:**
```bash
python daily_task_2026_11_09.py
```


## How to Run

**Requirements:** Python 3.9 or later. No external packages are needed.

1. Clone or download this repository.
2. Open the project folder in VS Code or a terminal.
3. Run the task file:

```bash
python daily_task_2026_11_08.py
```

On Windows, you can also use:

```bash
py daily_task_2026_11_08.py
```

To run another exercise, replace the filename with the file you want to practise.

## Other OOP Concepts Covered

- Classes, objects, attributes and methods
- The `__init__()` constructor
- Encapsulation and private attributes
- Inheritance and `super()`
- Method overriding and polymorphism
- Properties and data validation
- Managing multiple objects with dictionaries
- Working with dates and calculating amounts

## Practice Suggestions

- Add another equipment type, such as a camera lens.
- Try renting an item that is already rented.
- Test a return made after the due date.
- Add more validation for user input.
- Create your own mini-project using the same OOP concepts.

## Author

**Sakshi Manapure**

[GitHub Profile](https://github.com/sakshimanapure148)
