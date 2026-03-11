# Pattern N
n = 5
print("Pattern N")
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Pattern Z
print("\nPattern Z")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i + j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Pattern H
print("\nPattern H")
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Pattern I
print("\nPattern I")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()