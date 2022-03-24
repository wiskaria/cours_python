def is_odd(x):
    try:
        return x % 2 == 1
    except:
        return False


print(is_odd(2))
print(is_odd(3))
print(is_odd(3.1))
print(is_odd("a"))
print(is_odd(4549041))
print(is_odd(25648))
print(is_odd(141))
print(is_odd(0))
print(is_odd(-55))
