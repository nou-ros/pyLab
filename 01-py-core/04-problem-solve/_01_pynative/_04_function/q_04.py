'''
Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 9000
'''
def showEmployee(name, salary=9000):
    return f"Employee {name} salary is : {salary}"

res1 = showEmployee("Ben", 8500)
res2 = showEmployee("Gin")

print(res1)
print(res2)