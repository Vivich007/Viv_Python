age = 20
if age > 18:
    print("You are an adult")
elif age < 18 and age > 12:
    print("You are a teenager")
else:
    print("You are a minor")

# OR

age = 12
status = "adult" if age > 18 else "child"
print(status)