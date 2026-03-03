""" #occupied space
    def occupy(x,y,t):
    found = 0
    for i in range(x):
        if(y[i] == "c" and t[i] == "c"):
            found += 1
    print(found)
            
occupy(5, "ccc.c","..ccc") """
""" 
""" #language
""" lines = input("How much lines? ")
def text(x):    
    f = 0
    e = 0
    for i in x: 
        if i == "s" or i == "S":
            f = f + 1
        elif i == "t" or i == "T":
            e = e + 1
    if f > e:
        print("French")
    else:
        print("English")
print(lines)
text("This is a test")  """
# Magnus
word = input("give me word").upper()
x=0
c = 1
d = 2
e = 3
h=0
for i in word: 
    if i == "H":
        x=1
    if x == c:
        if i == "O":
            c=2
    if c == d:
        if i == "N":
            d=3
    if d == e:
        if i == "I":
            h += 1
            x=0
            c = 1
            d = 2
            e = 3
            
print(h)