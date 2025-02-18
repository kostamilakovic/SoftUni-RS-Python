# 3. List Statistics
# On the first line, you will receive a number n.
# On the following n lines, you will receive integers.

# You should create and print two lists:
# One with all the positive (including 0) numbers
# One with all the negative numbers

# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"

# Verzija 1 - stampamo svaki red putem nove print()

n = int(input())
positive = []
negative = []
for i in range(n):
    broj = int(input())
    if broj >= 0:
        positive.append(broj)
    else:
        negative.append(broj)
print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")

# Verzija 2 - stampamo svaki red putem jedne print() koristeci /n

# n = int(input())
# positive = []
# negative = []
# for i in range(n):
#     broj = int(input())
#     if broj >= 0:
#         positive.append(broj)
#     else:
#         negative.append(broj)
# print(f"{positive}\n{negative}\nCount of positives: {len(positive)}\nSum of negatives: {sum(negative)}")