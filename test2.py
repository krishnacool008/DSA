def permutation(nums):
    result = []

    def backtrack(path):
        # 1. Base Case
        if len(path) == len(nums):
            result.append(path[:])
            # Got the result we can end this branch
            return
        
        # Condition can be added outside for also
        # But this condition will run after 1st one
        # Here we are deciding we want to make/explore this node
        # Note -> we use this condition to check if this node is valid or not
        
        #2. Choise for each element
        # Creating node for each element 
        for num in nums:
            #3. Constraints (Condition 1st)
            # Here we are diciding we want to make/explore child node
            # Note -> This condition we use when we are making the node 
            # and while making we want to test it's validity
            if num in path:
                continue
            path.append(num) # This is where we create the node
            backtrack(path)
            # 4. Backtracking Step
            path.pop()

    backtrack([])
    return result

k = [1,2,3]
print(permutation(k))