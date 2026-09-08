# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](https://github.com/mkssaltorio-stack/9siliconcs3/blob/main/q1/MyOOPseedSystem/classObjectUml.md)
## Design Revision
- No major changes were needed from my original design.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| color | String | public | The color can be accessed and changed when needed. |
| length | Integer | public | The length can be accessed to know how long the pencil is. |
| brand | String | public | The brand can be accessed to identify the pencil. |
| isSharpened | Boolean | private | It should be protected so it can only be changed through the appropriate method. |
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
