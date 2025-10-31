#count occurance of chars
s="hello i am python i am programming language"
print(s.count("a"))
print(s.count("o"))

#count characters
from collections import Counter
s="hello i am python i am programming language"
count=Counter (s)
print(count)
