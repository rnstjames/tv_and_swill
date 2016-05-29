"""
Allows user to read wine vectors from a comma-separated
value matrix into a dictionary and the genres into
a list and then write these to a file
"""


filename = input("Enter a filename to be read: ") #/Users/Ryan/Desktop/wine_matrix.csv

with open(filename) as f:
    contents = f.readlines()
    genres = contents[0].strip("\n").split(",")[1:] # removes line breaks and initial formatting column
    wine_dict = {}
    for line in contents[1:]:
        line = line.strip("\n").split(",")
        wine_dict[line[0]] = [float(x) for x in line[1:]]
        
write = input("Enter a filename to write to: ")

with open(write, "w") as f2:
    f2.write("genre = ")
    f2.write("\n")
    f2.write("wine_dict = ")
    f2.write(str(wine_dict))
    f2.write("\n")


    
    
