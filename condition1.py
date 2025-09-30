# Traffic Lights Code

light = input("light: ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("slow down")
elif(light == "green"):
    print("go")
else:
    print("invalid light color")

# Grades of students

marks = int(input("marks : "))
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D")