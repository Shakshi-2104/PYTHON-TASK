#open file in read mode
file = open(r"C:\Users\shakshi kanojiya\Documents\data file.txt", "r")
#read the contents of the file
str = file.read()
#display the content on the screen
print("Contents of data file.txt are as follows:",str)
#close the file
file.close()
