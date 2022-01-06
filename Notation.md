# Notation
```
[Task-Name]

(Datum-Name)

(Datum-Name, Datum-Name, ...)

((Value)) or list form ((Value, value, ...))

--- is a path 
- - - is a path to a web service

| is down path 

> is directional right pointer

< is directional left pointer

^ is directional up pointer

+ is a turn

= terminus
```
# conditional loop
```
[Mark Empty Columns] ---> (rows++) <------------------------------------------------- +
                             + (cols++) <--------------------------------------- +    |
                             |   + (col) <--------------------------------- +    |    |
                             |       + (('', '  ', None)) ---> ((nan)) ---> +    |    |
                             |       + ----------------------------------------> +    |
                             |       + ---------------------------------------------- +
                          (done)
+ <------------------------- + 
```       
