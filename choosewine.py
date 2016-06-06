import math
import data
import requests

class TVProgram:

    def __init__(self):
        self.title, self.json = TVProgram.get_program()
        self.genres = self.json["Genre"].split(", ")
        self.plot = self.json["Plot"]

    def get_program():
        title = input("Enter a movie or TV show title for wine pairing: ")
        response = requests.get("http://www.omdbapi.com/?t=" + title + "&y=&plot=short+r=json")
        if response.json()["Response"] == 'True':
            return title, response.json()
        else:
            print("Something went wrong. Try again.")


class WinePairer:

    def __init__(self, genres_list, wine_vectors, program):
        self.genres = genres_list
        self.wine_vectors = wine_vectors
        self.program = program
        self.program_vector = self.initialize_vector()
        
        
    def initialize_vector(self):
        program_vector = [0] * len(self.genres)
        for genre in program.genres:
            program_vector[self.genres.index(genre)] = 1
        return program_vector

    def cosine_similarity(v1,v2):
        "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(v1)):
            x = v1[i]; y = v2[i]
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
        return sumxy/math.sqrt(sumxx*sumyy)

    def calculate_top_wine(self):
        top_wine = ["", 0]
        for entry in self.wine_vectors.items():
            if WinePairer.cosine_similarity(entry[1], self.program_vector) > top_wine[1]:
                top_wine[0] = entry[0]
                top_wine[1] = WinePairer.cosine_similarity(entry[1], self.program_vector)
        return top_wine[0]

if __name__ == "__main__":
    program = TVProgram()
    wp = WinePairer(data.genres, data.wine_dict, program)
    print(program.title + " pairs best with " + wp.calculate_top_wine() + ".")

