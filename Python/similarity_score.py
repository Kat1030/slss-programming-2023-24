# Comparing Similarity Scores
# Author: Katrina Chan
# Date: November 8, 2023

# Calculate the similarity scores between two people

# Create two lists that represent the movies that people like

ubials_favourite_movies = [
    "The Matrix",
    "Avengers: Infinity War",
    "Star Wars; The Empire Strikes Back",
    "Infernal Affairs",
    "Rogue One"
]

bens_favourite_movies = [
    "Thomas and Friends Big World Big Adventure",
    "Infernal Affairs",
    "Rogue One",
    "Spider-Man: Into the Spiderverse",
    "Gaurdians of the Galaxy: Volume 3"
]

# Initialize a similarity score

similarity_score = 0

# Iterate all movies in the first list
for movie in ubials_favourite_movies:
    if movie in bens_favourite_movies:
        similarity_score += 1

# Display the results
print(f"Ubial and Ben have a similarity score of: {similarity_score}")