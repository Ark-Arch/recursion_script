# fibonacci code
 
# 0,1,1,2,3,5,8,13,
def fibonacci(base_a, base_b, extent):
    next_fig = base_a + base_b
    if (extent == 1):
        return next_fig
    else:
        base_a = base_b
        base_b = next_fig
        return fibonacci(base_a, base_b, extent-1)


a = int(input('a -> '))
b = int(input('b -> '))
n = int(input('n -> '))
print(fibonacci(a,b,n))