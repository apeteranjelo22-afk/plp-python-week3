count = 1
total = 0

# BUG: The loop stopped before processing 5, so < 5 was changed to <= 5.
# BUG: The while statement was missing a colon.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The program tried to concatenate a string with an integer.
print(f"Sum of 1 to 5 is: {total}")