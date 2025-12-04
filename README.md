# 📉 Python False Position Method Solver

A custom **Numerical Root Finder** implemented in Python. This program finds the root of a non-linear equation using the **False Position Method** (also known as *Regula Falsi*). This method is similar to the Bisection method but typically converges faster by using linear interpolation to estimate the root position.

## 🚀 Features

* **Algorithm:** Uses linear interpolation between two points to find the root ($c = \frac{a \cdot f(a) - b \cdot f(b)}{f(a) - f(b)}$).
* **Target Function:** Currently configured to solve $f(x) = e^x - \sin(x)$.
* **Convergence Validation:** Verifies the Intermediate Value Theorem ($f(a)$ and $f(b)$ must have opposite signs) before starting.
* **Precision Control:** Iterates until the value is within a strict tolerance of `1e-7`.
* **Safety Mechanisms:**
    * Detects if no root exists in the selected interval.
    * Includes a maximum iteration counter (`n=100`) to prevent infinite loops.

## 🛠️ Algorithm Specifications

The solver relies on the following logic defined in the script:

| Category | Logic / Formula |
| :--- | :--- |
| **Formula** | $c = \frac{a \cdot f(a) - b \cdot f(b)}{f(a) - f(b)}$ |
| **Target Function** | `np.exp(x) - np.sin(x)` |
| **Tolerance** | `1e-7` |
| **Stop Condition** | When `abs(f(c)) < tol` |

## 📂 Project Structure

The project consists of a single Python script:

1.  **`False-Position-Method.py`**: Contains the function definition, the Regula Falsi logic loop, and user input handling.

## 💻 How to Run

### 1. Install Dependencies
This project requires **NumPy**. If you don't have it, install it via pip:

```bash
pip install numpy
```
### 2. Run
Execute the python file in your terminal:
```bash
False-Position-Method.py
```

### 3. Input
The program will ask for two numbers (Num1 and Num2) that define the start and end of the interval.
```text
Enter Num1: -4
Enter Num2: -2
```

## 📝 Example Usage
**Scenario:** Finding the root for $e^x - \sin(x)$ between -4 and -2.
#### Console Input:
```text
Enter Num1: -4
Enter Num2: -2
```
#### Generated Output:
Root found at **`x = -3.183063032598762`** after **`4 iterations`**

**Note:** The False Position method often requires fewer iterations than Bisection for well-behaved functions.

## ⚠️ Requirements
* **Python 3.x**
* **NumPy Library** (import numpy)
