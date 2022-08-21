#center
string = "Hello World"

new_string = string.center(len(string)+4, '*')

print(new_string)

#join
string = ["Hello", "World", "With", "Python"]

# join elements of text with space
print(' '.join(string))

# make trans
dict = {"a": "123", "b": "456", "c": "789"}
string = "abc"
# convert to unicode
print(string.maketrans(dict))

#zfill
string = "Hello World"
print(string.zfill(len(string)+5))

#title
string = "hello world"
print(string.title())


