# Recursion

### 1. State
`f(i)`
---

---

### 2. English Meaning
`f(i) represents Min cost to reach the top from ith stair`
---

---

### 3. Choices / Contribution
- Either we can have decision problem where choice matters
- Or we can have contribution of different states to get the result
    #### Choice/Contribution 1: `f(i+1)`
        Come from i-1
    #### Choice/Contribution 1: `f(i+2)`
        Come from i-1
---

### 4. Recurrence
`f(i) = cost[i] + min( f(i+1), f(i+2) ) `
---
- We can come from i-1 or i-2 stair plus the current cost to use ith stair

---

### 5. Verification
- f(i) = Min cost to reach top from ith stair
- f(i+1) = Min cost to reach top from i+1st stair
- f(i+2) = Min cost to reach top from i+2end stair

---


### 6. Base Case If Any
- Last stair in n, it is outside array index and we don't use last stair, just reach it
`f(n) = 0`
`f(n-1) = cost(n-1)`

- Most correct base case
  `f(n) = 0 where for all n > i` 
---

### 7. Final Answer To Code
`Answer = f(0)` according to the state definition
---

### 8. Example and Thinking

```python
cost = [1,100,1]
f(0) = cost[2] + min(f(1), f(2))
f(1) = cost[2] + min(f(2), f(3)) 

# Either we can hard code f(n-1) in our base case and directly get f(2) if we don't 
# have f(4) Defined
# Or we can use optimal base case and return 0 for f(i) where i > n so f(4) = 0
f(2) = cost[2] + min( f(3), f(4) ) or f(2) = cost[2] 

f(3) = 0
```

---


