document.addEventListener("DOMContentLoaded", initialase)

function initialase (){

    initialaseCategories()


    genres = [
            {request: "action", Title:"Action"},
            {request: "adventure", Title:"Adventure"},
            {request: "animation", Title:"Animation"},
            {request: "biography", Title:"Biography"},
            {request: "comedy", Title:"Comedy"},
            {request: "crime", Title:"Crime"},
            {request: "documentary", Title:"Documentary"},
            {request: "family", Title:"Family"},
            {request: "fantasy", Title:"Fantasy"},
            {request: "film-noir", Title:"Film-Noir"},
            {request: "game-show", Title:"Game-Show"},
            {request: "history", Title:"History"},
            {request: "horror", Title:"Horror"},
            {request: "musical", Title:"Musical"},
            {request: "mystery", Title:"Mystery"},
            {request: "news", Title:"News"},
            {request: "reality-tv", Title:"Reality-TV"},
            {request: "romance", Title:"Romance"},
            {request: "sci-fi", Title:"Sci-Fi"},
            {request: "sport", Title:"Sport"},
            {request: "talk-show", Title:"Talk-Show"},
            {request: "thriller", Title:"Thriller"},
            {request: "war", Title:"War"},
            {request: "western", Title:"Western"}
    ]



    for(let e of genres){
        let xhr = new XMLHttpRequest();
        xhr.open('get', 'https://yts.mx/api/v2/list_movies.json?genre='+ e.request+'&limit=6', true); // rajouter un sort by avec tout les chois(dowload count/last addes/...)

        xhr.onload =  show;
        xhr.send()
        document.querySelector("#propositionSection")

    function show (){

        let list_film = ""
        for (let i in JSON.parse(xhr.responseText).data.movies) {
            let a = JSON.parse(xhr.responseText).data.movies[i].torrents[0].url


            list_film += "<div class=\"FilmDefaultProposition\" onclick='popup(\"" + JSON.parse(xhr.responseText).data.movies[i].id+ "\")'>" +
                "<img class=\"FilmDefaultPropositionCoverImage\" src="+ JSON.parse(xhr.responseText).data.movies[i].medium_cover_image +"></div>";
        }
        document.querySelector("#propositionSection").innerHTML +=     "<div class=\"TitleGenre\">"+ e.Title+" :</div><section class=\"linearArrangement\">"  + list_film + "</section>";

    }
    }
}