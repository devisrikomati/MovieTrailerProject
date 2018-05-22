import webbrowser


class Movie():
    def __init__(j, movie_title, poster_image, trailer_youtube):
        j.title = movie_title
        j.poster_image_url = poster_image
        j.trailer_youtube_url = trailer_youtube


def show_trailer(j):
        webbrowswer.open(j.trailer_youtube_url)


