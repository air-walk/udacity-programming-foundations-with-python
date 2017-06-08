import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# print(avatar.storyline)
# avatar.show_trailer()

office_space = media.Movie("Office Space",
                           "An inspirational saga from the corporate world",
                           "https://upload.wikimedia.org/wikipedia/en/8/8e/Office_space_poster.jpg",
                           "https://www.youtube.com/watch?v=dMIrlP61Z9s")
print(office_space.storyline)
office_space.show_trailer()