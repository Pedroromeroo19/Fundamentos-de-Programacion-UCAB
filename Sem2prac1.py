a=7
b=3
c=0
d=(a+c)//b
c=d-(a-d)
b=a+(b+c)
a=a%(b+d)
d=(b-c)//(a +(c + d))
c=(a + b*d-c) % (a-( c * c ))
b=b // ( a+(c +d + b ) )
a=a + b + c + d
b= (a-c*d)%(b+c*a)
print(a,b,c,d)