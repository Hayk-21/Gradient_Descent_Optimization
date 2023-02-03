import unittest
import numpy as np
import sys
sys.path.append("../src") #Access to the "src" directory
from optimization import GradientDescentOptimization

class GradientDescentTest(unittest.TestCase):
    # Set up the test case
    def setUp(self):
        # Define the function to be optimized (x0^2 + x1^2)
        def function(x):
            return x[0]**2 + x[1]**2
        
        # Create an instance of the optimization algorithm with the defined function
        optimizer = GradientDescentOptimization(function)
        # Store the optimized solution
        self.solution = optimizer.optimize()

    def test_gradient_descent(self):
        # Assert that the [x0, x1] is equal to [0, 0] and y is equal to 0. 
        #This means that the endpoint is at the center of the graph.
        self.assertListEqual(list(self.solution.x.astype(np.int32)), [0, 0])
        self.assertEqual(self.solution.min_value.astype(np.int32), 0)

# Run the test case if this module is executed as a script
if __name__ == '__main__':
    unittest.main()