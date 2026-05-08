dataList = [10, "Kanha", 20.5, "Madhur"]

print(dataList)      # Print 1: Initial list
print(dataList[1])   # Print 2: Index 1 ("Kanha")
print(dataList[2])   # Print 3: Index 2 (20.5)
print(dataList[-3])  # Print 4: Negative index -3 ("Kanha")

dataList[1] = "Rahul" # MODIFICATION: Changes the element at index 1

print(dataList)      # Print 5: Modified list
print(type(dataList)) # Print 6: Data type
