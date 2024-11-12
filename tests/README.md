# Geometry Shapes Unit Tests

This folder contains unit tests for various geometric shapes: circles, rectangles, squares, and triangles. The tests are implemented using Python's `unittest` framework to ensure that the area and perimeter calculations for each shape are accurate.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
- [Test Cases](#test-cases)
  - [Circle Tests](#circle-tests)
  - [Rectangle Tests](#rectangle-tests)
  - [Square Tests](#square-tests)
  - [Triangle Tests](#triangle-tests)

## Requirements

- Python 3.x
- `unittest` module (included in the standard library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Gtollm/geometric_lib
   cd geometric_lib
   ```

2. Ensure you have Python installed on your machine.

## Running the Tests

To run the tests, navigate to the main directory and execute the following command:

```bash

python3 -m unittest discover -s tests

```

This command will automatically discover and run all test cases defined in the repository.

## Test Cases

### Circle Tests

The `CircleTestCase` class tests the following functionalities of the circle module:

- Area calculations for radius values of 0, integers, and floating-point numbers.
- Perimeter calculations for radius values of 0, integers, and floating-point numbers.

### Rectangle Tests

The `RectangleTestCase` class tests the following functionalities of the rectangle module:

- Area calculations for various combinations of width and height, including cases with zero dimensions.
- Perimeter calculations for various combinations of width and height.

### Square Tests

The `SquareTestCase` class tests the following functionalities of the square module:

- Area calculations for square dimensions of 0, integers, and floating-point numbers.
- Perimeter calculations for square dimensions of integers and floating-point numbers.

### Triangle Tests

The `TriangleTestCase` class tests the following functionalities of the triangle module:

- Area calculations for various base and height combinations, including cases with zero dimensions.
- Perimeter calculations for various combinations of the three sides of the triangle.


