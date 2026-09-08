# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](https://github.com/mkssaltorio-stack/9siliconcs3/blob/main/q1/MyOOPseedSystem/classObjectUml.md)
## Design Revision
- No major changes were needed from my original design.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| color | String | private | Prevents the color from being changed directly. |
| length | Integer | private | Keeps the pencil's length protected from direct changes. |
| brand | String | private | Keeps the pencil's brand information protected. |
| isSharpened | Boolean | private | Keeps track of whether the pencil is sharpened. |
## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
- 
### Which method changes the state of your object?
- 
### How did your two objects demonstrate that instances are independent?
- 
### What is the difference between your class diagram and your object diagram?
- 