var slides=document.querySelector(".slider-items").children;
var nextSlide=document.querySelector(".right-slide");
var prevSlide=document.querySelector(".left-slide");
var numSlides=slides.length;
var index=0;

nextSlide.onclick=function() {
    next("next");
}
prevSlide.onclick=function() {
    next("prev");
}

function next(direction){
    //handle when user clicks next slide 
    if (direction=="next"){
        index++;
        if (index==numSlides){    //handle when you reach end of slideshow
            index=0;        //loop to beginning of slides 
        }
    }
    //handle when user clicks previous slide
    else {
        if (index==0){      //handle when you reach the beginning of slideshow
            index=numSlides-1;        //loop to end of slides
        }
        else{
            index--;
        }
    }
    //update active tag if slide is being shown to user
    for(i=0; i<slides.length; i++){
        slides[i].classList.remove("active");
    }
    slides[index].classList.add("active");
    console.log("function works")
}