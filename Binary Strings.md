# Recursion

### 1. State
`f(i)`
---

---

### 2. English Meaning
`f(i) represents array of all possible binary strings of length i`
---

---

### 3. Choices / Contribution
- Either we can have decision problem where choice matters
- Or we can have contribution of different states to get the result
    #### Choice/Contribution 1: `f(i-1)`
---

### 4. Recurrence
`f(i) = [append 0 at end of all elements of f(i-1)] and [append 1 at end of all elements of f(i-1)]`
---
- We need all the helper state answers to get answer of the current state
- To get all the binary strings for f(i) we need to append 0 and 1 at the end to all the strings of f(i-1)

---

### 5. Verification
-  f(i) represents array of all possible binary strings of length i
-  f(i-1) represents array of all possible binary strings of length i-1

---


### 6. Base Case If Any
`f(1) = ["0", "1"]`
---

---


