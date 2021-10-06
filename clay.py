import sys

file_path = sys.argv[1]
f = open(file_path , "r")

s = f.read()

while s[-1] == '\n':
	s = s[:-1]


parts = s.split("\n\n")

body = '\n'.join(parts[:-1])
main = parts[-1]

print("body :\n" , body)
print("\nmain : \n" , main)
