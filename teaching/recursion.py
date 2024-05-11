def recursion(count):
    if count > 0:
        print("-" * count)
        return recursion(count - 1)


# recursion(10)

student = []
# for _ in range(3):
#     student.append(input())

# w = open('student.txt', 'w')
try:
    open('student.txt', 'r')
except FileNotFoundError:
    print("file not found")
else:
    print("file exists!")

# for item in student:
#     w.writelines("{}\n".format(item))
#
# w.close()
