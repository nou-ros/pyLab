#File Objects

##The Basics:
# f = open("test.txt", "r")
# f = open("test.txt", "w")
# f = open("test.txt", "a")
# f = open("test.txt", "r+")
# print(f.name)
# print(f.mode)
# f.close()

##Reading Files:
with open("test.txt", "r") as f:
	# pass

	#Small Files:
	# f_contents = f.read()
	# print(f_contents)

	##Big Files:
	# f_contents = f.readlines()
	# print(f_contents)

    ###With the extra lines:
	# f_contents = f.readline()
	# print(f_contents)
	# f_contents = f.readline()
	# print(f_contents)

	###Without the extra lines:
	# f_contents = f.readline()
	# print(f_contents, end = '')
	# f_contents = f.readline()
	# print(f_contents, end = '')

	###Iterating through the file:
	# for line in f:
	# 	print(line, end = '')

	###Going Back....:
	# f_contents = f.read()
	# print(f_contents, end = '')

	###Printing by characters:
	# f_contents = f.read(100)
	# print(f_contents, end = '')
	# f_contents = f.read(100)
	# print(f_contents, end = '')
	# f_contents = f.read(100)
	# print(f_contents, end = '')

	###Iterating through small chunks:
	#size_to_read = 100
	#f_contents = f.read(size_to_read)
	#while len(f_contents) > 0:
		#print(f_contents)
		#f_contents = f.read(size_to_read)

	###Iterating through small chunks, with 10 characters:
	size_to_read = 100
	#f_contents = f.read(size_to_read)
	#print(f_contents, end = '')
	# f.seek(0)
	# f_contents = f.read(size_to_read)
	# print(f_contents, end = '')
	# print(f.tell())
	#while len(f_contents) > 0:
		#print(f_contents, end = '*')
		#f_contents = f.read(size_to_read)
#print(f.mode)
#print(f.closed)
#print(f.read())


##Writing Files:
###The Error: