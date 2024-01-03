'''import random
n=random.randbytes(4)
print(n)

print(random.randrange(1,8))

print(random.randint(100,211))
mylist={"abc","bfr","wer","qaz","edc"}
mylist1={"abc","bfr","wer","qaz","edc"}
print(random.choice(mylist))'''

import string
import random
s =10
ran = ''.join(random.sample(string.ascii_uppercase + string.digits,k = s))
s1=4
ran1=''.join(random.sample(string.digits,k=6))
print(ran1)
