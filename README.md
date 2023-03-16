# sudoku_solver

This is a Python script for solving Sudoku puzzles. It includes functions for generating a new Sudoku puzzle, solving an existing puzzle, and printing the solved puzzle to the console.

## Installation

To use this script, you will need to have Python 3 installed on your system. You can download Python from the official website [here](https://www.python.org/downloads/).

Once you have Python installed, you can download the Sudoku solver script from this repository. You can either clone the repository using Git, or you can download the ZIP file and extract it to a local directory.

## Usage

### Generating a new Sudoku puzzle

To generate a new Sudoku puzzle, use the `generate_sudoku()` function. This function takes no arguments and returns a 9x9 NumPy array containing the initial puzzle.

```python
import sudoku_solver  

# Generate a new puzzle 
puzzle = sudoku_solver.generate_sudoku() 
# Print the puzzle to the console 
sudoku_solver.print_sudoku(puzzle)`
```

### Solving an existing Sudoku puzzle

To solve an existing Sudoku puzzle, use the `solve_sudoku()` function. This function takes a 9x9 NumPy array containing the puzzle as an argument, and returns True if the puzzle was solved successfully, or False if no solution could be found.

```python
import sudoku_solver

# Define the puzzle
puzzle = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Solve the puzzle
solved = sudoku_solver.solve_sudoku(puzzle)

# Print the solved puzzle to the console
if solved:
    sudoku_solver.print_sudoku(puzzle)
else:
    print("No solution exists for this puzzle.")
```

### Printing a Sudoku puzzle

To print a Sudoku puzzle to the console, use the `print_sudoku()` function. This function takes a 9x9 NumPy array containing the puzzle as an argument, and prints it to the console in a user-friendly format.

```python
import sudoku_solver

# Define the puzzle
puzzle = generate_puzzle()

# Print the defined puzzle
print_sudoku(puzzle)
```

Output :

![image](https://user-images.githubusercontent.com/126460064/225750044-51882f1b-e381-431c-9ae6-42fc4c139306.png)

### Requirements

The Sudoku Solver script requires the following packages to be installed:

-   NumPy

You can install the required packages by running the following command:

`pip install -r requirements.txt`

### Contributing

If you find any issues with the script or have any suggestions for improvement, please feel free to submit a pull request or create an issue on this repository.
