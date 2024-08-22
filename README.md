# Dentsu_challenge
This contains the solution to the dentsu backend developer trainee challenge implemented in Python

## Explanation:
budget_formula(X_i, Z, Y1, Y2, X_others, HOURS): This function calculates the difference between the actual budget (Z_actual) calculated from the given X_i and the target budget Z. The goal is to find X_i such that this difference is zero.

## Parameters:

Z: The total campaign budget.
Y1: Agency fee percentage.
Y2: Third-party tool fee percentage.
X_others: The sum of budgets for all other ads.
HOURS: Fixed cost for agency hours.
initial_guess: The initial estimate for the budget of the specific ad (X_i).
fsolve: This function finds the root of the budget_formula function, meaning it finds the value of X_i that makes the formula equal to zero (i.e., the total budget equals Z).

## Running the Script:
Install scipy if you don't have it: pip install scipy.
Run the script in a Python environment.
Output:
The script will print the optimized budget for the specific ad (X_i) that ensures the total campaign budget does not exceed the limit Z.

Feel free to customize the parameters (Z, Y1, Y2, X_others, HOURS, and initial_guess) as per your specific scenario.
