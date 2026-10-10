def greet(name):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, World!"

names = ["AI", "Management", ""]

for n in names:
    print(greet(n))