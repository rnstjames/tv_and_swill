# TV and Swill

TV and Swill is an app that will recommend wines to go along with various TV shows and movies that the user enters and will proffer places that that wine could be purchased. Currently, it utilizes the OMDB API (www.omdbapi.com) and the Snooth API (http://api.snooth.com).

TV and Swill uses the magic of linear algebra and vector representations to pair your favorite wines with the movies and TV shows that you watch. Currently, it supports nine grape varieties of wines:
- Syrah
- Malbec
- White Zinfandel
- Pinot Noir
- Chardonnay
- Sauvignon Blanc
- Pinot Grigio
- Riesling
- Vinho Verde
- Cabernet Sauvignon

Each wine is encoded as a 26-dimension vector in a wine/genre matrix, where each dimension reflects an IMDB genre of movie or television show. Each wine gets assigned a probability that it pairs best with that genre. These probabilities were assigned heuristically based on my own pairing intuitions, with the hope to eventually use polls of users and user suggestions to tweak these values.

By accessing the OMDB API, each television show or movie is assigned one to three genres. A new (proto) 26-dimension wine vector is created where each of these genres is given a probability of one (and the rest, zero). Using cosine similarity, this wine vector is compared to the wine varieties, and the wine with the highest cosine similarity is then paired. 

Stay tuned for future updates!
