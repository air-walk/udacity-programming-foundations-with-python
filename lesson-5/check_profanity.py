import urllib

def read_text():
    quotes = open("/home/air-walk/workspaces/udacity-programming-foundations-with-python/lesson-5/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    check_profanity(contents_of_file)
    quotes.close()

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output     = connection.read()
    print(output)
    connection.close()

    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Couldn't scan the document properly :(")

read_text()
