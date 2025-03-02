# 9. Password Validator
# Write a function that checks if a given password is valid. Password validations are:
# •	It should be 6 - 10 (inclusive) characters long
# •	It should consist only of letters and digits
# •	It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"

def password_validator (password):
    checklist = [0, 0, 0]
    # prvo proveravamo duzinu password-a
    if 6 <= len(password) <= 10:
        checklist[0] = 1
    else:
        print("Password must be between 6 and 10 characters")
    # proveravamo da li se password sačinjava samo od brojeva i slova
    for char in password:
        if char.isalpha() or char.isdigit():
            continue
        else:
            print("Password must consist only of letters and digits")
            break
    else:
        checklist[1] = 1
    # proveravamo da li sadrži barem dva broja
    nums = 0
    for char in password:
        if char.isdigit():
            nums += 1
        if nums == 2:
            checklist[2] = 1
            break
    else:
        print("Password must have at least 2 digits")
    if sum(checklist) == 3:
        print("Password is valid")
password_validator(input())