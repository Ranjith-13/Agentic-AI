### Test Plan

#### Function: divide
- **Test Case 1:** Divide two positive numbers.
- **Test Case 2:** Divide a positive number by a negative number.
- **Test Case 3:** Divide a negative number by a positive number.
- **Test Case 4:** Divide two negative numbers.
- **Test Case 5:** Divide by zero (should raise ZeroDivisionError).

#### Function: is_valid_age
- **Test Case 1:** Check with age equal to 18 (boundary condition).
- **Test Case 2:** Check with age greater than 18.
- **Test Case 3:** Check with age less than 18.

#### Function: greet
- **Test Case 1:** Provide a valid name and expect a greeting.
- **Test Case 2:** Provide an empty string and expect ValueError.
- **Test Case 3:** Provide None as name and expect ValueError.