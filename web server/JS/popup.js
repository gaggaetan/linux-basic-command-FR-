function popup(filmId){
    document.getElementById("propositionSection").style.opacity = 0.5
    document.getElementById("popup1").style.visibility = "visible"
    document.getElementById("popup1").style.opacity = 1



    allcateg = ["popupTitle", "popupExit", "popupAffiche", "popupAnnee","popupCategorie", "popupResume", "popupDuree","popupEtoiles", "popupTorrens", "popupProposition"]

    for (let el of allcateg){
        document.getElementById(el).innerHTML = ""
    }

    let xhr = new XMLHttpRequest()
    xhr.open('get', 'https://yts.mx/api/v2/movie_details.json?movie_id=' +filmId)
    xhr.onload = addInfosPopup
    xhr.send()

    function addInfosPopup (){
        movieInfos = JSON.parse(xhr.responseText).data.movie
        console.log(movieInfos)

        document.getElementById("popupTitle").innerText = movieInfos.title
        if (movieInfos.title.length > 30 && movieInfos.title.length <= 40){
            document.getElementById("popupTitle").style.fontSize = "2em"

        }else if (movieInfos.title.length > 40){
            document.getElementById("popupTitle").style.fontSize = "1.5em"
            document.getElementById("popupTitle").innerText = movieInfos.title.substring(0, 80)
        }

        document.getElementById("popupAffiche").style.backgroundImage = "url(" + movieInfos.medium_cover_image + ")"
        document.getElementById("popupAnnee").innerText = movieInfos.year
        genresText = ""
        for (let el of movieInfos.genres){
            genresText += el + ", "
        }
        document.getElementById("popupCategorie").innerText = genresText.substring(0,genresText.length -2)

        if (movieInfos.description_intro.length == 0){
            document.getElementById("popupResume").innerText = "no summery"
        }else{
            document.getElementById("popupResume").innerText = movieInfos.description_intro;
        }
        if (movieInfos.runtime == 0){
            document.getElementById("popupDuree").innerText = "?h??"
        }else{
            document.getElementById("popupDuree").innerText = Math.floor(movieInfos.runtime/60) + "h" + movieInfos.runtime % 60
        }

        document.getElementById("popupEtoiles").innerHTML = stars(movieInfos.rating)

        document.getElementById("popupTorrens").innerHTML = ""
        for (let el of movieInfos.torrents){
            document.getElementById("popupTorrens").style.gridTemplateColumns +=  " 2.5em";
            document.getElementById("popupTorrens").innerHTML += "<div class='torrentlink'><img class='torrentlinkImg' src='/IMG/imagen-futorrent-0ori.jpg' onclick='download(\"" + el.url + "\")'>" + el.quality+"</div>"
        }
        if(movieInfos.torrents.length > 5){
            document.getElementById("popupTorrens").style.scale = "0.6";
            document.getElementById("popupTorrens").style.translate = "-25%";
        }else{
            document.getElementById("popupTorrens").style.scale = "1";
            document.getElementById("popupTorrens").style.translate = "0";
        }
        popupproposition(filmId)

    }
}

function stars(rating){
    let star1,star2,star3,star4,star5

    if (0 <= rating){star1 = "style=\"color: #fda401;\""}else{star1 = "style=\"color: #178582;\""}
    if (2 <= rating){star2 = "style=\"color: #fda401;\""}else{star2 = "style=\"color: #178582;\""}
    if (4 <= rating){star3 = "style=\"color: #fda401;\""}else{star3 = "style=\"color: #178582;\""}
    if (6 <= rating){star4 = "style=\"color: #fda401;\""}else{star4 = "style=\"color: #178582;\""}
    if (8 <= rating ){star5 = "style=\"color: #fda401;\""}else{star5 = "style=\"color: #178582;\""}


    return "<div>\n" +
        "  <i class=\"star \" "+star1+">★</i>\n" +
        "  <i class=\"star \" "+star2+" >★</i>\n" +
        "  <i class=\"star \" "+star3+" >★</i>\n" +
        "  <i class=\"star \" "+star4+" >★</i>\n" +
        "  <i class=\"star \" "+star5+" >★</i>\n " +
        rating +"/10</div>";
}

function popupproposition (filmId){
    let hxr = new XMLHttpRequest()
    hxr.open("get", "https://yts.mx/api/v2/movie_suggestions.json?movie_id=" + filmId,'yes')
    hxr.onload = popuppropositionload
    hxr.send()

    function popuppropositionload (){
        result = ""
        for(let el of JSON.parse(hxr.responseText).data.movies){
            result += "<img class='popupPropositionImg' src='" + el.medium_cover_image + "')>"
        }

        let hxr2 = new XMLHttpRequest()
        hxr2.open("get", "https://yts.mx/api/v2/movie_suggestions.json?movie_id=" + JSON.parse(hxr.responseText).data.movies[0].id,'yes')
        hxr2.onload = popuppropositionload2
        hxr2.send()

        function popuppropositionload2 (){
            for(let i=0; i < 2;i++ ){
                result += "<img class='popupPropositionImg' src='" + JSON.parse(hxr2.responseText).data.movies[i].medium_cover_image + "' onclick='popup(" + JSON.parse(hxr2.responseText).data.movies[i].id+")'>"
            }
            document.getElementById("popupProposition").innerHTML = result
        }






    }
}


function popupExit (){
    document.getElementById("popup1").style.visibility = "hidden"
    document.getElementById("popup1").style.opacity = 0
    document.getElementById("propositionSection").style.opacity = 1
}

function download (magnet_Link){
    console.log(magnet_Link)

    window.open(magnet_Link, "_blank");

}