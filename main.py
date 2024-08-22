from scipy.optimize import fsolve

# Define the total campaign budget formula
def budget_formula(X_i, Z, Y1, Y2, X_others, HOURS):
    # X_others is the sum of all other ads' budgets
    X_total = X_i + X_others
    return X_total + Y1 * X_total + Y2 * (X_total) + HOURS - Z

# Parameters
Z = 10000  # The total campaign budget
Y1 = 0.1  # Agency fee percentage
Y2 = 0.05  # Third-party tool fee percentage
X_others = 3000  # Sum of budgets for all other ads
HOURS = 500  # Fixed cost for agency hours

# Initial guess for X_i
initial_guess = 1000

# Use fsolve to find the value of X_i
X_i_solution, = fsolve(budget_formula, initial_guess, args=(Z, Y1, Y2, X_others, HOURS))

print(f"The optimized budget for the specific ad (X_i) is: {X_i_solution:.2f} euros")
