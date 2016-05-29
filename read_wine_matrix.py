"""
Allows user to read wine vectors from a comma-separated
value matrix into a dictionary and the genres into
a list and then write these to a file
"""

filename = input("Enter a filename to be read: ")

with open(filename) as f:
    contents = f.readlines()
    genres = contents[0].strip("\n").split(",")[1:]
    wine_dict = {}
    for line in contents[1:]:
        line = line.strip("\n").split(",")
        wine_dict[line[0]] = [float(x) for x in line[1:]]
        
with open("data.py", "w") as f2:
    f2.write("genre = ")
    len_list = len(genres)
    f2.write("[\n")
    while len_list > 0:
        row = 5
        while row > 0 and len_list > 0:
            f2.write("'" + genres[len(genres) - len_list]+ "', ")
            row -= 1
            len_list -= 1
        f2.write("\n")
    f2.write("]")
    f2.write("\n")
    f2.write("wine_dict = ")
    f2.write("{\n")
    for key, value in wine_dict.items():
        f2.write("'" + key + "': ")
        f2.write(str(value) + ",\n")
    f2.write("}\n")
    f2.write("\n")


    
    
