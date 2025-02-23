# Write a function that receives a grade between 2.00 and 6.00 and print the corresponding grade in words.
# 2.00 – 2.99 - "Fail"
# 3.00 – 3.49 - "Poor"
# 3.50 – 4.49 - "Good"
# 4.50 – 5.49 - "Very Good"
# 5.50 – 6.00 - "Excellent"

# Verzija 1 - pomocu funkcije koja stampa

def grades (grade):
    if 2.00 <= grade <= 2.99:
        print("Fail")
    elif 3.00 <= grade <= 3.49:
        print("Poor")
    elif 3.50 <= grade <= 4.49:
        print("Good")
    elif 4.50 <= grade <= 5.49:
        print("Very Good")
    elif 5.50 <= grade <= 6.00:
        print("Excellent")

grade = float(input())
grades(grade)

# Verzija 1 - pomocu funkcije koja vraca vrednost

# def grades (grade):
#     if 2.00 <= grade <= 2.99:
#         return "Fail"
#     elif 3.00 <= grade <= 3.49:
#         return "Poor"
#     elif 3.50 <= grade <= 4.49:
#         return "Good"
#     elif 4.50 <= grade <= 5.49:
#         return "Very Good"
#     elif 5.50 <= grade <= 6.00:
#         return "Excellent"
#
# grade = float(input())
# print(grades(grade))

# Verzija 3

# while True:
#     try:
#         grade = float(input())
#         if 2.00 <= grade <= 6.00:
#             break
#         else:
#             print("Uneta ocena nije u opsegu od 2.00 do 6.00. Unesite ponovo.")
#     except ValueError:
#         print("Unos je nepravilan. Unesite broj u opsegu od 2.00 do 6.00.")
# if 2.00 <= grade <= 2.99:
#     print("Fail")
# elif 3.00 <= grade <= 3.49:
#     print("Poor")
# elif 3.50 <= grade <= 4.49:
#     print("Good")
# elif 4.50 <= grade <= 5.49:
#     print("Very Good")
# elif 5.50 <= grade <= 6.00:
#     print("Excellent")