1. Encapsulation
A Product class can store name, price, and stock together with methods like addStock() and sellProduct(). This protects the data and prevents incorrect changes.

2. Abstraction
Methods like sellProduct() can hide the details of updating stock and calculating prices. This makes the inventory system easier to use and understand.

3. Inheritance
A general Product class can be inherited by classes such as FoodProduct and HouseholdProduct. This allows them to share common properties while having their own features.

4. Polymorphism
Different product classes can have the same method, such as getDescription(), but implement it differently. This allows the system to handle different products using the same method.

Reflection
I think encapsulation is the most useful pillar for the inventory system. It protects important data like prices and stock quantities. It also makes the program more organized and reliable.