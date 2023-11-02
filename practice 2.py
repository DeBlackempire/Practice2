

def text(a, c):
    ans = a + c
    print(ans)
    return ans


text(23, 5)

def student(name='James', age=30):
    # text(23, 5)
    print('Name:', name)
    print('Age:', age)


student('Prince', 40)
student()


# abitrary argument
def myfun(*child):
    print('the youngest child is', child[2])

    # using for loop to iterate the sequence
    for i in child:
        # print(i, end='  ')
        # to print/display vertically
        print(i)


myfun('Henry', 'Hillary', 'Janet', 'Obi', 'Caleb', 'Moses', 'James')


# key word argument 'comment'
def myfunct(child1, child2, child3, child4):
    print('The eldest child is', child1)
    print('the youngest child is', child4)


myfunct(child1='James', child2='Peter', child3='Caleb', child4='Hillary')


# arbitrary keyword argument
def funct(**kids):
    print(kids['kid1'], 'is the first child')


funct(kid2='dave', kid1='Moses', kid3='larry')

# lambda function
x = lambda a: a + 20
print(x(30))


def fun(s):
    return lambda b: b * s


doubler = fun(2)
print(doubler(22))

ok = fun(3)
print(ok(22))
