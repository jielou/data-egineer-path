from sys import intern

a_string = "I am here haha. How are doingssssssss?"
b_string = "I am here haha. How are doingssssssss?"

print(a_string is b_string)
print(id(a_string))
print(id(b_string))
b_string +="new"
a_string +="new"
print(id(a_string))
print(id(b_string))
print(a_string is b_string)

# make b string and a string share the same memory
a_string = intern(b_string)
b_string = intern(a_string)

print(a_string is b_string)
print(a_string)
print(b_string)
