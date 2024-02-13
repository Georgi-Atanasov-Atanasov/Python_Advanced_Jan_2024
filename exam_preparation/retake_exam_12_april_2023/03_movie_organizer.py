def movie_organizer(*args):
    movie_data = {}
    genres = {}
    output = []
    for data in args:
        movie_name = data[0]
        genre = data[1]
        movie_data[movie_name] = genre

        if genre not in genres:
            genres[genre] = 1
        else:
            genres[genre] += 1
    data = sorted(genres.items(), key=lambda x: (-x[1], x[0]))
    movies = sorted(movie_data.items(), key=lambda x: (x[1], x[0]))

    for current_genre, number in data:
        output.append(f"{current_genre} - {number}")
        for movie, genre in movies:
            if current_genre == genre:
                output.append(f"* {movie}")
    return "\n".join(output)


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))


