
first = 'first'

def first_func() :
    # global first
    first = "aaaaa"

    def first_child_func() :
        nonlocal first
        first = "bbb"
        print("first : " + first)

    first_child_func()
    print(first)

first_func()
print(first)