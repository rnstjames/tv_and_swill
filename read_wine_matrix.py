filename = "/Users/Ryan/Desktop/wine_matrix.csv"

with open(filename) as f:
    contents = f.readlines()
    genres = contents[0].strip("\n").split(",")[1:]
    wine_dict = {}
    for line in contents[1:]:
        line = line.strip("\n").split(",")
        wine_dict[line[0]] = [float(x) for x in line[1:]]
print(genres)
print(wine_dict)

        

    
    
