import sys

file_path = sys.argv[1]
f = open(file_path , "r")

s = f.read()

while s[-1] == '\n':
	s = s[:-1]


parts = s.rsplit("\n\n",1)

body = parts[0]
main = parts[-1]


main_function = "int main(){\n\t%s\n\treturn 0;\n}\n" % main


print(main_function)
