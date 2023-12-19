function search(form){
    let xhr = new XMLHttpRequest();
    if (form.querySelector("#searchValue").value.length == 0){
        clearPropositionContainer()
    }else{
        xhr.open('get', 'https://yts.mx/api/v2/list_movies.json?limit=6&query_term=' + form.querySelector("#searchValue").value, true);
        xhr.onload =  show;
        xhr.send()
    }


    function show (){


        let list_film = ""
        for (let i in JSON.parse(xhr.responseText).data.movies) {
            let a = JSON.parse(xhr.responseText).data.movies[i].torrents[0].url
            console.log(JSON.parse(xhr.responseText).data.movies[i])
            let rating = JSON.parse(xhr.responseText).data.movies[i].rating
            let star1,star2,star3,star4,star5

            if (0 <= rating){star1 = "style=\"color: #fda401;\""}
            if (2 <= rating){star2 = "style=\"color: #fda401;\""}
            if (4 <= rating){star3 = "style=\"color: #fda401;\""}
            if (6 <= rating){star4 = "style=\"color: #fda401;\""}
            if (8 <= rating ){star5 = "style=\"color: #fda401;\""}

            list_film += "<div class=\"proposition\" onclick='popup("+ JSON.parse(xhr.responseText).data.movies[i].id+")'>" +
                "<img class=\"research_medium_cover_image\" src="+ JSON.parse(xhr.responseText).data.movies[i].medium_cover_image +">" +
                "<div id='part2'><div class='titleProposition'>" + JSON.parse(xhr.responseText).data.movies[i].title + "</div> <p id='stars'>\n" +
                "  <i class=\"star \" "+star1+">★</i>\n" +
                "  <i class=\"star \" "+star2+" >★</i>\n" +
                "  <i class=\"star \" "+star3+" >★</i>\n" +
                "  <i class=\"star \" "+star4+" >★</i>\n" +
                "  <i class=\"star \" "+star5+" >★</i>\n " +
                 rating +"/10</p></div></div>";
        }
        document.querySelector("#propositionContainer").innerHTML = list_film;
    }
}



function clearPropositionContainer() {
    setTimeout(function(){
        document.querySelector("#propositionContainer").innerHTML = "";
        document.querySelector("#searchValue").value = ""
    }, 100);


}