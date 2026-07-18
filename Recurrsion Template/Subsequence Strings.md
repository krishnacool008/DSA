# Recursion

### 1. State
`f(i)`
---

---

### 2. English Meaning
`f(i) represents array of all possible subsequence for the substring s[0:i+1]`
---

---

### 3. Choices / Contribution
- Either we can have decision problem where choice matters
- Or we can have contribution of different states to get the result
    #### Choice/Contribution 1: `f(i-1)`
---

### 4. Recurrence
`f(i) = [append s[i] to all the elements of f(i-1)] and [all elements of f(i-1)]`
---
- We need all the helper state answers to get answer of the current state
- To get all possible subsequences we need to append ith element to all the substring from i-ith state and also add all the subsequence from i-1st state

---

### 5. Verification
-  f(i) represents array of all possible subsequence for the substring s[0:i+1]
-  f(i-1) represents array of all possible subsequence for the substring s[0:i]

---


### 6. Base Case If Any
`f(0) = [""]`
---

---

### 7. Final Answer To Code
`Answer = f(len(s) - 1)` according to the state definition
---


