

def extended_euclidean(x,y):
    if(y>x):
        x,y = y,x

    a = x
    b = y
    c = 1
    d = 0
    e = 0
    f = 1

    iteration = 1
    while(b>0):
        print("iteration: {}\n".format(iteration))
        iteration += 1

        q = a//b
        r = a - q * b
        print("q = {} / {} = {}".format(a,b,q))
        print("r = {} - {} * {} = {}".format(a,q,b,r))
        a = b
        b = r
        print("a = {}\nb = {}\n".format(a,b))

        m = c - q * d
        print("m = {} - {} * {} = {}".format(c,q,d,m))
        c = d
        d = m
        print("c = {}\nd = {}\n".format(c,d))

        n = e - q * f 
        print("n = {} - {} * {} = {}".format(e,q,f,n))
        e = f
        f = n
        print("e = {}\nf = {}".format(e,f))
        print("-"*30)

    print("\ngcd({},{}) = {}, m = {}, n = {}\n".format(x,y,a,c,e))
    return a,c,e

def euclidean(x,y):
    if(y>x):
        x,y = y,x
    
    a = x
    b = y
    iteration = 1
    while(b>0):
        print("iteration: {}\n".format(iteration))
        iteration += 1

        q = a//b
        r = a - q * b
        print("q = {} / {} = {}".format(a,b,q))
        print("r = {} - {} * {} = {}".format(a,q,b,r))

        a = b
        b = r
        print("a = {}\nb = {}".format(a,b))
        print("-"*30)
    
    print("\ngcd({},{}) = {}\n".format(x,y,a))
    return a

# euclidean(2740,1760)
extended_euclidean(400,60)




