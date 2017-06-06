def read_text():
    quotes = open("/home/air-walk/workspaces/udacity-programming-foundations-with-python/lesson-5/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_text()
