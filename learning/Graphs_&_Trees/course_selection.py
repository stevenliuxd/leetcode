numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

def findOrder(numCourses, prerequisites):
    prereq = { c:[] for c in range(numCourses)} # Create initial empty list of prereqs
    for crs, pre in prerequisites:
        prereq[crs].append(pre)
    print(prereq)
    # 3 Possible States:
    # visited
    # visiting
    # unvisited
    output = []

    # Allow us to know if a course has been visited 
    # OR currently along given path
    visit, cycle = set(), set()
    
    def dfs(crs): # Pass in the course number currently visiting
        print(visit)
        if crs in cycle: # Determine if there is a cycle
            return False # Return empty list
        if crs in visit:
            return True # Don't need to visit this course twice
        cycle.add(crs) # Add cycle for future detection of cycles
        for pre in prereq[crs]: # Go through every prereq for this course
            if dfs(pre) == False:
                return False # Detected cycle
        cycle.remove(crs) # Remove because no longer along the path
        visit.add(crs)
        output.append(crs)
        return True
    
    for c in range(numCourses): # 0, 1, 2, 3, etc
        if dfs(c) == False: # Only if dfs detected a cycle, so return empty list
            return []
        

a = findOrder(numCourses, prerequisites)
#print(a)
