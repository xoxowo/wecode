def some_even(x) :
    if 1 <= x <= 50 :
        if x % 2 == 0 :
            return x
        else: 
            return False

print(some_even(3))