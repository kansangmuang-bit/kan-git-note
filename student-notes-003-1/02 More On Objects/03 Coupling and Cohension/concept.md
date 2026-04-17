

# Coupling and Cohesion

A unit is any reasonable self-contained component
Ex: a class, a function, a file, a folder, and so on

Coupling

    - The linking of two separate units
    - The idea of making a unit dependent on another
    - Loosely coupled units are not very dependent on each other
    - Tightly coupled are very dependent on each other
    - Goal is loosely coupled units for the purposes of maintenance.

Cohesion

    - refers to the number of and diversity of tasks that a single unit is responsible for
    - Ex: The random library handles randomness and only randomness, thus it is cohesive
    - High Cohesion means a unit is responsible for one (type of) task
    - Low Cohesion means a unit is responsible for a wide variety of tasks
    - Goal is for highly cohesive units
