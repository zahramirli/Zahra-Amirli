# Zahra-Amirli
Object- Oriented Programming(Coursework project)
Coursework Report
1. Introduction
Goal: Implement a LIFO Stack with additional features using OOP principles and design patterns.

Application: The application provides a stack data structure with logging and size-limiting features.

Run: Execute the script containing the above code. Ensure all necessary class definitions are in place.

Use: Interact with the stack using the push, pop, and peek methods.

2. Body/Analysis
Functional Requirements:

Push Method: Adds an item to the stack.
Pop Method: Removes and returns the last added item.
Peek Method: Returns the last added item without removing it.
Logger (Singleton): Logs stack operations.
StackDecorator: Adds logging functionality.
Implementation:

The script includes the Logger class (Singleton), Stack base class, LimitedStack subclass, and StackDecorator class. The Logger ensures that there is only one instance logging messages, while the StackDecorator adds logging capabilities to the stack operations.

3. Results and Summary
Encapsulation: The stack's internal list is private.
Abstraction: The stack interface hides implementation details.
Inheritance: LimitedStack extends Stack functionality.
Polymorphism: LimitedStack modifies push behavior.
Singleton: Logger ensures a single instance.
Decorator: Adds logging without modifying the stack directly.
Challenges: Ensuring correct implementation of Singleton pattern and seamless integration of decorators.

4. Conclusions
Achievements: Created a stack with additional features demonstrating OOP principles and design patterns.

Future Prospects: Adding thread safety, persistence, or networked stack operations.

References:

"Design Patterns: Elements of Reusable Object-Oriented Software" by Gamma et al.
PEP8 Style Guide for Python Code.
This structure combines all necessary components into a single script while meeting the coursework requirements and demonstrating the principles and patterns effectively.
