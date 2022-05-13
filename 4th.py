import string
alf = string.ascii_lowercase
n = int(input())
a = [ [0] * n for i in range(n) ]
for i in range(n):
    for j in range(n):
        k = min( abs(i-j), abs(i+j-n+1) )
        a[i][j] = alf[k%26]
for row in a:
    s1 = "".join(filter(str.isalpha, str(row)))
    print(s1)
        

