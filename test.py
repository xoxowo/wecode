def some_even(x) :
    if 1<= x <=50 :
        results = [ i for i in range(x+1) if i % 2 == 0]
        return results[1:]

print(some_even(50))
