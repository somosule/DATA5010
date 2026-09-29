# DATA 5010: Vending Machine Project

**Course:** DATA 5010 – Intro to Data Science Programming (BGSU, Fall 2026)  
**Instructor:** Dr Arijit Khan  
**Activity:** Class Participation Activity 1

## Project Overview
This project provides an object-oriented Python implementation of a single-product `VendingMachine` class designed as an Abstract Data Type (ADT) to manage stock lifecycle operations, enforce strict state validation, and demonstrate foundational OOP concepts. Structurally, the `VendingMachine` class acts as a factory object that instantiates individual machine objects, establishing a clear distinction between shared class attributes (such as `DEFAULT_INVENTORY`) and isolated instance attributes (`inventory`, `product_name`, `total_purchased`, and `total_restocked`) unique to each machine. Instance methods—including public interface operations like `purchase()` and `restock()`, as well as internal helper functions like `_has_enough_stock()`—receive `self` to safely mutate and query an individual machine's state while protecting internal data integrity. Furthermore, the class customizes built-in Python behaviors through special methods, utilizing `__init__` as the constructor, `__str__()` for human-readable string representation, and `__eq__()` for value-based equality comparison. Finally, the implementation is verified by a robust `unittest` suite that checks edge cases, such as invalid or negative inputs, while ensuring complete state isolation across multiple machine instances.

## 1. Repository Contents

- `vending_machine.py` — Main class implementation and interactive CLI runner.
- `test_vending_machine.py` — Unit testing suite built with Python's standard `unittest` framework.
- `README.md` — Project documentation and setup guide.

---

## 2. Architecture & OOP Concepts

```text
                  +-----------------------------------+
                  |          VendingMachine           |
                  +-----------------------------------+
                  | CLASS ATTRIBUTE:                  |
                  |   DEFAULT_INVENTORY = 20          |
                  |                                   |
                  | INSTANCE ATTRIBUTES:              |
                  |   self.inventory                  |
                  |   self.product_name               |
                  |   self.total_purchased            |
                  |   self.total_restocked            |
                  +-----------------------------------+
                  | PUBLIC INTERFACE:                 |
                  |   + purchase(amount)              |
                  |   + restock(amount)               |
                  |   + report_inventory()            |
                  |                                   |
                  | INTERNAL HELPER:                  |
                  |   - _has_enough_stock(amount)     |
                  |                                   |
                  | SPECIAL METHODS:                  |
                  |   + __str__()                     |
                  |   + __eq__(other)                 |
                  +-----------------------------------+

```

## 3. Usage & Testing

#### Environment Setup
Verify your Python environment:
```bash
python3 --version
```
#### Running the Application
To execute the interactive program:
```bash
python3 vending_machine.py
```
#### Base Case Example Run
*(Inputs: `5`, `2`, `7`)*
```text
Enter amount to purchase: 5
Enter amount to restock: 2
Enter amount to purchase again: 7
Inventory: 10 bottles
```
#### Running Unit Tests
To run the automated test suite and confirm class behavior:
```bash
python3 test_vending_machine.py
```
#### Expected Output
```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```
