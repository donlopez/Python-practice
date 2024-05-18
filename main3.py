import first

def fct_a(number):
    return number ** 2

def fct_b(number):
    return number * 1

def fct_c(number):
    return fct_a(number) - fct_b(number)

print(fct_c(9))
print(first.fct_c(9))
print(first.fct_d(9))