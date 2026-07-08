class Math:
    # Constructor
    def __init__(self, num):
        self.num = num

    # Instance Method
    def addtonum(self, n):
        self.num += n
        print(f"Updated Number: {self.num}")

    # Static Method
    @staticmethod
    def add(a, b):
        return a + b


# -------------------------------
# Static Method Call
# -------------------------------
result = Math.add(1, 3)
print("Addition using Static Method:", result)

# -------------------------------
# Object Creation
# -------------------------------
a = Math(5)

print("Initial Number:", a.num)

# -------------------------------
# Instance Method Call
# -------------------------------
a.addtonum(10)

print("Final Number:", a.num)