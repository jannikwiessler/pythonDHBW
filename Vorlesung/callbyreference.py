a = 1
my_list = [1,2,3]

def my_int_function(x: int):
    x = 2

def my_list_function(y: []):
    y[0] = 0

my_int_function(x=a)
print(a)
my_list_function(y=my_list)
print(my_list)
