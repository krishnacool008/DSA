# Recursion

### 1. State
`f(i)`
---

---

### 2. English Meaning
`f(i) represents x to power i`
---

---

### 3. Choices / Contribution
- Either we can have decision problem where choice matters
- Or we can have contribution of different states to get the result
    #### Choice/Contribution 1: `f(i-1)`
---

### 4. Recurrence
`f(i) = f(i-1) * x`
---
- We need all the helper state answer to get the answer of the current state
- f(i) = x to power i-1 multiply by x

---

### 5. Verification
- f(i) represent x to power i
- f(i-1) represent x to the power i-1

---


### 6. Base Case If Any
`f(0) = 1`
---

---

### 6. Negative power
    If the power is negative treat that as different porblem where only negative power is allowed
    and create the recurrence according to that
    have switch to start which solution +ve one or -ve one


