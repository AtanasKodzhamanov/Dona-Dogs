let adoptionExpands = document.getElementsByClassName("AdoptionExpand");
console.log(adoptionExpands)
for(let i=0;i<adoptionExpands.length;i++){
    adoptionExpands[i].querySelectorAll("#AdoptionButton")[0].addEventListener("click", function(){
    let cards = adoptionExpands[i].querySelectorAll("#AdoptionCard");
    for (let j = 0; j < cards.length; j++) {
        if (cards[j].style.display === "none") {
            cards[j].style.display = "block";
        } else {
            cards[j].style.display = "none";
        }
    }
    });
}
