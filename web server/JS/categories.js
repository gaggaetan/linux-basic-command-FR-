function initialaseCategories(){
    categories = ["Action","Adventure","Animation","Biography","Comedy","Crime","Documentary","Family","Fantasy","Film-Noir","Game-Show","History","horror","Horror","Musical","Mystery","News","Reality-TV","Romance","Sci-Fi","Sport","talk-show","Talk-Show","Thriller","War","Western"]

    htmloption = ""
    for (let el of categories){
        htmloption += "<option value='el' class='categoriesoptions'> " + el + "</option>"
    }
    document.getElementById("categoriesButton").innerHTML += htmloption
}
