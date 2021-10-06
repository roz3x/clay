import sys

file_path = sys.argv[1]
f = open(file_path , "r")

s = f.read()

while s[len(s)-1] == '\n':
	s = s[:-1]


parts = s.split("\n\n")
for part in parts:
	print(part)
