#Exercise 1
import re
with open("/Users/damirsapar/Desktop/Python/Lab5/row.txt", "r", encoding="utf-8") as f:
    text=f.read()
pat=r"a[b]*"
sos=re.findall(pat, text)
print(sos)



#Exercise 2
import re
with open("/Users/damirsapar/Desktop/Python/Lab5/row.txt", "r", encoding="utf-8") as f:
    text=f.read()
pat=r"a[b]{2,3}"
sos=re.findall(pat, text)
print(sos)



#Exercise 3
import re
with open("/Users/damirsapar/Desktop/Python/Lab5/row.txt", "r", encoding="utf-8") as f:
    text=f.read()
pat=r"[a-z]+(?:_[a-z]+)+"
sos=re.findall(pat, text)
print(sos)



#Exercise 4
import re
with open("/Users/damirsapar/Desktop/Python/Lab5/row.txt", "r", encoding="utf-8") as f:
    text=f.read()
pat=r"[A-Z][a-z]+"
sos=re.findall(pat, text)
print(sos)



#Exercise 5
import re
with open("/Users/damirsapar/Desktop/Python/Lab5/row.txt", "r", encoding="utf-8") as f:
    text=f.read()
pat=r"a.*b$"
sos=re.findall(pat, text)
print(sos)



#Exercise 6
import re
with open("/Users/damirsapar/Desktop/Python/Lab5/row.txt", "r", encoding="utf-8") as f:
    text=f.read()
sos=re.sub(r"[ .,]", ":", text)
print(sos)



#Exercise 7
import re
with open("/Users/damirsapar/Desktop/Python/Lab5/row.txt", "r", encoding="utf-8") as f:
    text=f.read()
sos=re.sub(r'_([a-z])', lambda m: m.group(1).upper(), text)
print(sos)



#Exercise 8
import re
with open("/Users/damirsapar/Desktop/Python/Lab5/row.txt", "r", encoding="utf-8") as f:
    text=f.read()
sos=re.split(r'(?=[A-Z])', text)
print(sos)



#Exercise 9
import re
with open("/Users/damirsapar/Desktop/Python/Lab5/row.txt", "r", encoding="utf-8") as f:
    text=f.read()
sos=re.sub(r'(?=[A-Z])', ' ', text)
print(sos)



#Exercise 10
import re

def c_to_s(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
def process_file(fil):
    with open(fil, 'r', encoding='utf-8') as file:
        c = file.read()
    con = c_to_s(c)
    print(con)

f = '/Users/damirsapar/Desktop/Python/Lab5/row.txt' 
process_file(f)