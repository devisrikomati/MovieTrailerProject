import media
import fresh_tomatoes
import webbrowser
print("Content-type:text/html \n")
chalo = media.Movie("Chalo",
                   "https://i2.wp.com/southreel.com/wp-content/uploads/2017/11/chalo-movie-new-lookChalo-Movie-teaserNaga-Shourya-New-Movie-Title-ChaloNaga-Shourya-New-MovieIRA-CreationsNaga-ShouryaRashmika-MandannaTelugu-New-Movieslatest-telugu-movies.jpg?fit=800%2C445",
                   "https://www.youtube.com/embed/B3W4mQTyN2E")

gokula = media.Movie("Gokula Krishnudu",
                     "https://i.ytimg.com/vi/Hwgyw2L_VH4/maxresdefault.jpg",
                     "https://www.youtube.com/embed/N63I3-RiiS8")
ninnu = media.Movie("Ninnu Kori",
                    "http://andhraboxoffice.com/uploads/films/DDsoihFU0AENxiR-jul6.jpg",
                     "https://www.youtube.com/embed/Ia6EXfqKiV4")
jindhagi = media.Movie("Vunnadi Okkate Jindagi",
                       "https://igmedia.blob.core.windows.net/igmedia/telugu/news/unnadiokkatejindagi050817_1.jpg",
                         "https://www.youtube.com/embed/z678PtuCIHo")
movies = [chalo,gokula,ninnu,jindhagi]
fresh_tomatoes.open_page(movies)

