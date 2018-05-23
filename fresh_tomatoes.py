import re
import os
import webbrowser
print("Content-type:text/html \n")
main_head = '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<style>
        .modal {
            display: none;
            position: fixed;
            z-index: 1;
            padding-top: 100px;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgb(0, 0, 0);
            background-color: rgba(0, 0, 0, 0.4);
    }

         .modal-content {
            background-color: #fefefe;
            margin: auto;
            padding: 20px;
            border: 1px solid #888;
            width: 40%;
        }
        .close {
            color: #aaaaaa;
            float: right;
            font-size: 20px;
            font-weight: bold;
        }

        .close:hover,
        .close:focus {
            background-color: red;
            text-decoration: none;
            cursor: pointer;
        }
     h1 {
            color: blue;
            text-align: center;
            background: burlywood;
        }

        body{
            background-color: bisque;
        }
        .img1,
        .img2,
        .img3,
        .img4 {
            float: left;
            width: 300px;
            height: 400px;
            margin-left: 200px;
            padding: 50px;
            }

        img {
            width: 300px;
            height: 400px;
        }

        .img1:hover {
            background-color: aqua;

        }

        .img2:hover {
            background-color: aqua;
        }

        .img3:hover {
            background-color: aqua;

        }

        .img4:hover {
            background-color: aqua;
            cursor: pointer;
        }

        img {
            width: 100%;
            cursor: pointer;
        }

    </style>

    <title>movies</title>
    <div id="myModal" class="modal">
         <div class="modal-content">
            <span class="close">&times;</span>
            <iframe width="100%" height="250" src="" frameborder="0"
             {movie_tiles} allow = "autoplay; encrypted-media"
             allowfullscreen></iframe>
         </div>
</div>
      <script>
         var modal=document.getElementById('myModal');
         var span=document.getElementsByClassName("close")[0];
         onc=function (c){
             modal.style.display="block";
             document.getElementsByTagName("iframe")[0].setAttribute("src",
             'https://www.youtube.com/embed/'+c);
         }
         span.onclick=function(){
         modal.style.display="none";
         document.getElementsByTagName("iframe")[0].setAttribute("src",
             '');
         }
         window.onclick=function(event){
         if(event.target==modal){
         modal.style.display="none";document.getElementsByTagName("iframe")[0].setAttribute("src",
             '');
         }
         }
      </script>

</head>
    '''
main_content = '''
<body>
    <h1>movie trailer</h1>

    <div class="img1" onclick="onc('B3W4mQTyN2E')">
        <img  src="https://bit.ly/2J07Vfe"
            alt="chalo">
        <p style="text-align: center; color: bisque;  font-size: 25px">
        challo</p>

    </div>
    <div class="img2" onclick="onc('N63I3-RiiS8')">
    <img src="https://i.ytimg.com/vi/Hwgyw2L_VH4/maxresdefault.jpg"
        alt="gokula krishnudu">
       <p style="text-align: center; color: bisque; font-size: 25px">
       gokula krishudu</p>
    </div>
    <div class="img3" onclick="onc('Ia6EXfqKiV4')">
        <img src="https://bit.ly/2IE4FqI" alt="Ninnu kori">
        <p style="text-align: center; color: bisque; font-size: 25px">
        Ninnu kori</p>
    </div>
    <div class="img4" onclick="onc('z678PtuCIHo')">
        <img src="https://bit.ly/2rZT1Mo" alt="unnadhi okate gindhagi">
        <p style="text-align: center; color: bisque;  font-size: 25px">"
        "vunnadhi okate gindhagi</p>
    </div>
    <div id="myMoadal" class="modal">
        <div class="modal-content">
            <button type="button" data-dismiss="modal">&times;</button>
        </div>
    </div>
        <div id="myModal" class="modal">
           <div class="modal-content">
            <span class="close">&times;</span>
            <iframe width="560" height="315"
            src="https://www.youtube.com/embed"
            frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
            </iframe>
        </div>
    </div>

</body>
</html>
'''
movie_title_content = '''
<div class="col-md-6 col-lg-4 movie-title text-center" data-trailer-yutube-
id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}"width="220" height="342">
    <h2 style="color:white;">{movie_title}</h2>
</div>
'''


def create_movie(movies):
    content = ''
    for i in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', i.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', i.trailer_youtube_url)
        trailer_youtube_url = (youtube_id_match.group(0) if youtube_id_match
                               else None)

        content += movie_title_content.format(
                   movie_title=i.title,
                   poster_image_url=i.poster_image_url,
                   trailer_youtube_id=trailer_youtube_url
        )
    return content


def open_page(movies):
    output_file = open('fresh_tomatoes.html', 'w')
    rendered_content = main_content.format(
        movie_tiles=create_movie(movies))
    output_file.write(main_head + rendered_content)
    output_file.close()

    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)


