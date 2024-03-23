a,n,b = input().split()
a = int(a)
b = int(b)
num_dict = {str(i):i for i in range(11)}
rev_dict = {i:str(i) for i in range(11)}
for char in list(map(chr, range(97, 123))):
    num_dict[char] = 10 + ord(char) - ord('a')
    rev_dict[10+ord(char)-ord('a')] = char
# into 10진법

rev = n[::-1]
num = sum([(a**i)*num_dict[rev[i]] for i in range(len(rev))])


ret = ""
while(num > 0):
    num,na = divmod(num,b)
    ret += rev_dict[na]

    if num < b:
        ret += rev_dict[num]
        break
print(ret[::-1])