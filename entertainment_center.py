import media
import fresh_tomatoes
import webbrowser
print("Content-type:text/html \n")
chalo = media.Movie("Chalo",
                    "https://bit.ly/2J07Vfe",
                    "https://www.youtube.com/embed/B3W4mQTyN2E")
gokula = media.Movie("Gokula Krishnudu",
                     "https://i.ytimg.com/vi/Hwgyw2L_VH4/maxresdefault.jpg",
                     "https://www.youtube.com/embed/N63I3-RiiS8")
ninnu = media.Movie("Ninnu Kori",
                    "https://bit.ly/2IE4FqI",
                    "https://www.youtube.com/embed/Ia6EXfqKiV4")
jindhagi = media.Movie("Vunnadi Okkate Jindagi",
                       "https://bit.ly/2rZT1Mo",
                       "https://www.youtube.com/embed/z678PtuCIHo")
movies = [chalo, gokula, ninnu, jindhagi]
fresh_tomatoes.open_page(movies)


