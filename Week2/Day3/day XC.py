

my_list = [1,5,76,"ff",5,66,"ttt"]

def some_sum(some_list):
    try:
        result = sum(some_list)
    except TypeError:
        print("Error founded")
        raise
    
    else:
        print(result)




some_sum(my_list)
