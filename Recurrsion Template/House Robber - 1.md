# Recursion

### 1. State
`f(i)`
---

---

### 2. English Meaning
`f(i) represents max money robbed starting from ith house till last house`
---

---

### 3. Choices / Contribution
- Either we can have decision problem where choice matters
- Or we can have contribution of different states to get the result
    #### Choice/Contribution 1: `f(i+1)`
    #### Choice/Contribution 2: `f(i+2)`
---

### 4. Recurrence
`f(i) = max ( cost[i] + f(i+2) , f(i+1) )`
---
Both contribution is needed, this is contribution problem

---

### 5. Verification
- f(i)   - represents max money robbed starting from ith house till last house
- f(i+1) - represents max money robbed starting from i+1th house till last house
- f(i+2) - represents max money robbed starting from i+2end house till last house

---


### 6. Base Case If Any
`f(i) = 0 for all i where i > number of houses`
---

---

### 7. Final Answer To Code
`Answer = f(0)` according to line 23
---

