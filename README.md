# Diophantine Solver 
Finds all solutions to a linear inhomogeneous diophantine equation. The output is numpy compatible.

##  Download
Use one of the following methods: 
1. Using git clone:
```bash
$ git clone https://github.com/andis854/diophantine_solver.git
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Move the directory _diophantine_solver_  to a directory that is a search\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; path of Python, e.g.
```bash
~/.local/lib/python3.10/site-packages/ # Example of a common path.
```
2. Download the source code: (also works for Windows) 
Download the files in [zip](https://github.com/andis854/diophantine_solver/archive/refs/heads/main.zip) form. Extract the directory _diophantine_solver-main_ and put in a directory that is a search path of Python, e.g.
```bash
~/.local/lib/python3.10/site-packages/ # Example of a common path.
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Rename the directory _diophantine_solver_.

To find the available search paths, type the following commands in a Python terminal.
```Python
>>> import sys
>>> sys.path
```

### Usage

In your Python terminal or script type
```Python
>>> import diophantine_solver
```
Now call the function using
```Python
diophantine_solver.solve
```
The syntax is 
```Python
diophantine_solver.solve(coefficients, right-hand-side)
```
For a detailed explanation, type
```Python
>>> help(diophantine_solver.solve)
```


License
----

MIT License

Copyright (c) 2023, andis854

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
