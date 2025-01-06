'''
Writing two files.
We need a variable that represents the file
The keyword open is used to open a file.
'''

# this is will do one of two things, if these if there is no file named ' file_name.ext', it will create a new file with that name. If one already exists,
#    it will overwrite the existing file



my_file = open('Names.txt', 'w') # r is for reading and w is for writing



my_file.write('Matt Priem 38\n')
my_file.write('Ashley Mc Call 37\n')
my_file.write('Dexter\t Priem 7\n')
my_file.write('Eugene\t Priem 5\n')