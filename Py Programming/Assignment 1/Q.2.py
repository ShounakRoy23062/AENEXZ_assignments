marks =[78, 35, 92, 40, 61]

marks_tuple = tuple(marks)

print("List:", marks)
print("Type of list:", type(marks))
print("Tuple:", marks_tuple)
print("Type of tuple:", type(marks_tuple))
print("Highest Marks:", max(marks))
print("Lowest Marks:",min(marks))
print("Students scoring at least 40:", len(marks)- marks.count(35))

valid_range = min(marks) >= 0 and max(marks) <= 100
print("Are all marks within 0 to 100?", valid_range)

marks[0] = 85
print("Modified List:", marks)

'''marks_tuple[0] = 85
print("Modified Tuple:", marks_tuple)'''   #tuples are immutable
