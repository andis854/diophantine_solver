# Diophantine Solver 
Finds all solutions to a linear inhomogeneous diophantine equation. The output is numpy compatible.

Below we describe two ways of installing and using this package; by calling it from a Linux shell or from a Python shell.

##  Download
Use one of the following methods: 
1. Using git clone:
```bash
$ git clone https://github.com/andis854/diophantine-solver.git
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Move the directory _diophantine-solver_  to a directory that is a search\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; path of Python, e.g.
```bash
~/.local/lib/python3.10/site-packages/ # Example of a common path.
```
2. Download the source code: (also works for Windows) 
Download the files in [tar.gz](............) or [zip](.........) form. Extract the directory _diophantine-solver_ and put in a directory that is a search path of Python, e.g.
```bash
~/.local/lib/python3.10/site-packages/ # Example of a common path.
```

To find the available search paths, type the following commands in a Python terminal.
```Python
>>> import sys
>>> sys.path
```

### Usage

In your Python terminal or script type
```Python
>>> import diophantine-solver
```
Now call the function using
```Python
diophantine-solver.solve
```
The syntax is 
```Python
diophantine-solver.solve(coefficients, right-hand-side)
```
For a detailed explanation, type
```Python
>>> help(diophantine-solver)
```
or
```Python
>>> help(diophantine-solver.solve)
```


License
----

MIT License

Copyright (c) 2023 Anders Israelsson, andis854

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
