marks = [99,76,98]
marks.append("shikher") # type: ignore
marks.insert(4,"jain") # type: ignore
print(76 in marks)
for score in marks :
    print(score)
print("lenght will be",len(marks))
i=0
while i<len(marks):
    print(marks[i])
    i+=1
    marks.clear()
    print("Now marks will be",marks)