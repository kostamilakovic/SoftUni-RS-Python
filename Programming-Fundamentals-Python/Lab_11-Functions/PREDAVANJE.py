# Funkcija poziva drugu funkciju

def print_hi(name):
    print(f"Hi {name}")
    print_how_are_you(name)

def print_how_are_you(ime):
    print(f"How are you {ime}")

print_hi("SoftUni")

# RECURSION (rekurzija)
# Funkcija poziva samu sebe

def factorial(n):
    if n == 1:  # ukoliko je n == 1 vracamo broj 1 i zavrsavamo izvrsavanje funkcije
        return 1    # konkretno u ovom primeru return 1 je kao break u while True petlji
    else:   # doke god je n != 1 pozivacemo opet funkciju sa novom vrednoscu n
        return n * factorial(n - 1) # konkretno u ovom primeru return je kao continu u while True petlji
print(factorial(5))

# DODELJIVANJE VREDNOSTI PARAMETRIMA

def povrsina(a, b):
    print(a*b)
povrsina(5, 5)
povrsina(a=5, b=7) # direktno dodeljujemo vrednost odredjenom parametru putem odgovarajucih argumenata
povrsina(b=7, a=5) # direktno dodeljujemo vrednost odredjenom parametru putem odgovarajucih argumenata

# Zelimo da svaki element u listi pomnozimo sa dva
numbers_list = [1,2,3,4,5]
new_numbers_list = list(map(lambda x: x*2, numbers_list))