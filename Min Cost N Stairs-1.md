# Recursion

### 1. State
`f(i)`
---

---

### 2. English Meaning
`f(i) represents Min cost to reach ith stair and use ith stair`
---

---

### 3. Choices / Contribution
- Either we can have decision problem where choice matters
- Or we can have contribution of different states to get the result
    #### Choice/Contribution 1: `f(i-1)`
        Come from i-1
    #### Choice/Contribution 1: `f(i-2)`
        Come from i-1
---

### 4. Recurrence
`f(i) = min(f(i-1), f(i-2)) + cost[i]`
---
- We can come from i-1 or i-2 stair plus the current cost to use ith stair

---

### 5. Verification
- f(i) = minimum cost required to reach and use stair i
- f(i-1) = minimum cost required to reach and use stair i-1
- f(i-2) = minimum cost required to reach and use stair i-2

---


### 6. Base Case If Any
`f(0) = cost(0)`
`f(1) = cost(1)`
---

---

### 7. Final Answer To Code
`Answer = f(n-1)` according to the state definition
---


