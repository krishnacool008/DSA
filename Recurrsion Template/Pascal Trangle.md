# Recursion

### 1. State
`f(i)`
---

---

### 2. English Meaning
`f(i, j) represents jth number in the ith row of the pascal triangle`
---

---

### 3. Choices / Contribution
- Either we can have decision problem where choice matters
- Or we can have contribution of different states to get the result
    #### Choice/Contribution 1: `f(i-1, j-1)`
    #### Choice/Contribution 2: `f(i-1, j)`
---

### 4. Recurrence
`f(i) = f(i-1, j-1) + f(i-1, j)`
---
- We need all the helper state answers to get the answer of the current state
- jth number of ith row of the triangle is the sum of f(i-1, j) and f(i-1, j-1)

---

### 5. Verification
- f(i, j) represents jth number in the ith row of the pascal triangle
- f(i-1, j-1) represents j-1st number in the i-1st row of the pascal triangle
- f(i-1, j) represents jth number in the i-1st row of the pascal triangle

---


### 6. Base Case If Any
`f(i, 0) = 1`
`f(i, i) = 1`
---

---

### 7. Final Answer To Code
`Answer = f(n, r)` according to the state definition
---


