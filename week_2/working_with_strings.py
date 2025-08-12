#single quote
name = 'Ada'
#Double quote
greeting = "hello"
print(greeting , name)
# triple quotes (for multi-line strings)
story = '''once upon a time
there was a coder named Ada.'''
# String with numbers and symbols
password = "p@ssword123"


word = "Python"
print(word[0])  # p
print(word[-1]) # n
print(word[-2]) # o
print(word[1])  # y


# slicing 
word = "Python"
print(word[0:4])   #pyth
print(word[2:])    #thon
print(word[:3])    #pyt
print(word[::2])   #pto
print(word[::-1]) 


a = "hello"
b = "world"
print(a + " " + b)  # Hello World


word = " Hi!"
print(word * 3)  # Hi! Hi! Hi!

text = "Python programming"
print("Python" in text)     # true
print("Java" not in text)   # true

text = "Hello World"
print(text.find("o"))     # 4
print(text.rfind("o"))    # 7

text = "Hello World"
print(text.index("World"))

filename = "data.csv"
print(filename.startswith("data"))
print(filename.endswith(".csv"))

name = " Ada Balogun"
print(name.upper())

sentence = "python is amazing"
print(sentence.upper())

text ="   Abuja   "
print(text.strip())

message = "I love Java"
print(message.replace("Java", "Python"))

text = "Hello ABEOKUTA"
print(text.swapcase())

text ="     Nigeria"
print(text.lstrip())

text = "NIgeria       "
print(text.rstrip())

fruits = "mango orange banana"
print(fruits.split())

text = "one,two,three,four"
print(text.rsplit(",",2))

lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())

words = ["I", "love", "Python"]
print(" ".join(words))

text = "Python"
print(text.center(20, "-"))

text = "python"
print(text.ljust(10, "*"))

text = "Python"
print(text.rjust(10, "*"))

num = "42"
print(num.zfill(5))

print("Lagos".isalpha())
print("Lagos123".isalpha())

print("12345".isdigit())
print("123a".isdigit())

print("Python3".isalnum())
print("Python 3".isalnum())