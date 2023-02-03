from dto import Solution
import numpy as np

class GradientDescentOptimization:
    def __init__(self, function, learning_rate=1e-2, eps=1e-3, max_iter=1000):
        """
        Initialize the gradient descent optimization algorithm with the given function, learning rate,
        optimal value of function accuracy, and maximum number of iterations.
        
        Args:
            function: The function to be optimized
            learning_rate: Learning rate
            eps: The optimal value of function accuracy
            max_iter: Maximum iterations for the algorithm
        """
        self.function = function
        self.learning_rate = learning_rate
        self.eps = eps
        self.max_iter = max_iter
        self.tails = []
        self.h = 1e-6 #0.000001

    # Generate initial random points
    def _initial_points(self):
        # Returns a float list of random digits from -6 to 6. In size 2.
        # For example [-2, 3]
        rng = np.random.default_rng()
        return rng.integers(low=-6, high=6, size=2).astype(np.float32) 
    
    # Calculate the gradient at a given point
    def _gradient(self, x):
        #The gradient is calculated by the formula: f(x+h) - f(x)/h
        gradient = np.zeros(x.shape)

        for i in range(x.shape[0]):
            x_plus_h = x.copy()
            x_plus_h[i] += self.h
            gradient[i] = (self.function(x_plus_h) - self.function(x)) / self.h

        return gradient

    # Perform one step of gradient descent  
    def _gradient_descent_step(self, x):
        return x - self.learning_rate * self._gradient(x)

    # Optimize the function
    def optimize(self) -> Solution:
        x = self._initial_points()

        #Function value at starting point
        current_cost = self.function(x)
        #Adding a starting point to the "tails" list to track it on the plot
        self.tails.append(np.hstack((x, current_cost)))

        for i in range(self.max_iter):
            #The new value of x
            x = self._gradient_descent_step(x)   
            #The new value of function
            new_cost = self.function(x)

            #We check if the accuracy is good enough then stops the optimization
            if abs(current_cost - new_cost) < self.eps:
                print(f"Optimization is stopped!\nIteration:{i}")
                break
            
            #Update the current value of a function
            current_cost = new_cost
            #Adding new tracking values
            self.tails.append(np.hstack((x, current_cost)))

        #Returning the end value of x0, x1, y and "tails" to track on the plot
        return Solution(x, current_cost, self.tails)