<!-- # Python coding task

Your task is to implement [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) algorithm. For your convinence there are class structures inside the `src` directory. Feel free to change anything if find it useful or use any external libraries if needed.

Implement as it is a production code, use correct code style, variables/function namings, well-designed and optimized code with unit tests.

## Hints

There are many approaches to solve the problem. Some of them are below. 

- You can use a function as a python function with pre-defined derivative
- You can use some python libraries to compute the derivative either in symbolic form or numerically, such as [sympy](https://www.sympy.org/en/index.html) or [scipy](https://scipy.org/)
 -->

## Modifications and overall code structure
In dto.py I have added the "tails" list to keep track of the points obtained from the optimization.
This means that the optimization function returns the value: x(x0, x1), min_value(last value), tails(all tracking points).

## How to start
If you do not have those libraries that are written to requirements.txt then run the command:
- pip install -r requirements.txt

Launch Notebook for a visual preview plot.py from the ./notebooks directory

To test, go to the ./test directory and run the command:
- python -m unittest .\gradient_descent_test.py