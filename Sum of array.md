# Recursion

### 1. State
`f(i)`
---

---

### 2. English Meaning
`f(i) represents sum of array till ith index including ith item`
---

---

### 3. Choices / Contribution
- Either we can have decision problem where choice matters
- Or we can have contribution of different states to get the result
    #### Choice/Contribution 1: `f(i-1)`
---

### 4. Recurrence
`f(i) = f(i-1) + arr[i]`
---
- We need all the helper state answer to get the answer of the current state
- We add current number to sum of array till i-1st index

---

### 5. Verification
- f(i) represents sum of array till ith index including ith item
- f(i-1) represents sum of array till i-1st index including i-1st item

---


### 6. Base Case If Any
`f(0) = arr[0]`
---

---


