# Recursion

### 1. State
`f(i)`
---

---

### 2. English Meaning
`f(i) represents number of ways to reach ith stair from the ground`
---

---

### 3. Choices / Contribution
- Either we can have decision problem where choice matters
- Or we can have contribution of different states to get the result
    #### Contribution 1: `f(i-1)`
    Reach stair (i-1) and take 1 step
    #### Contribution 2: `f(i-2)`
    Reach stair (i-2) and take 2 step
---

### 4. Recurrence
`f(i) = f(i-1) + f(i-2)`
---
Both contribution is needed, this is contribution problem

---

### 5. Verification
- f(i-1) = number of ways to reach stair (i-1) from the ground, After taking 1 step we reach i
- f(i-2) = number of ways to reach stair (i-2) from the ground, After taking 2 step we reach i
- In both case we can reach i so we have or situation (+)
---


### 6. Base Case
`f(0) = 1 (stay on ground do nothing)`
`f(1) = 1`
`f(2) = 2`
---

---

### 7. Final Answer To Code
`Answer = f(n)` according to the state definition
---


