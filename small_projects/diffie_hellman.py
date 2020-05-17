# private keys
x = 91
y = 71

# public keys
g = 13
n = 27


my_public = pow(g,x,n)
your_public = pow(g,y,n)

my_key = pow(your_public,x,n)
your_key = pow(my_public, y,n)


print(my_key, your_key)
