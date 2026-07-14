# Recursion

### 1. State
`f(i)`
---

---

### 2. English Meaning
`f(i) represents max coins we have after robbing ith house`
---

---

### 3. Choices / Contribution
- Either we can have decision problem where choice matters
- Or we can have contribution of different states to get the result
    #### Choice/Contribution 1: `f(i-1)`
        Come from i-1
    #### Choice/Contribution 1: `f(i-2)`
        Come from i-2
---

### 4. Recurrence
`f(i) = max(f(i-1), f(i-2) + cost[i])`
---
- If we are skipping current house then money stays same as `f(i-1)` money collected from till i-1st house
- If we are robbing current house then we will have money we had at i-2end house `f(i-2)`

---

### 5. Verification
- f(i) represents max coins we have after robbing ith house
- f(i-1) represents max coins we have after robbing i-1th house
- f(i-2) represents max coins we have after robbing i-2th house

---


### 6. Base Case If Any
`f(0) = coint[0]`
`f(1) = max( coin[0], coin[1] )`
---

---

### 7. Final Answer To Code
`Answer = f(len(cost) - 1)` according to line 25
---

