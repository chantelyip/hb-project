"use strict";

{var buttons = document.querySelectorAll('.save-recipe')

buttons.forEach((button)=> {button.addEventListener('click', (evt) => {
  const btn = evt.target;
  const savedRecipes = {
    'link_to_recipe': evt.toElement.previousSibling.previousElementSibling.previousElementSibling.href,
    'recipe_name': $(`.${evt.target.id}.recipe-name`).html(),
    'recipe_id': btn.id
  };  
        console.log(evt.srcElement.parentNode)
        console.log(evt)
        console.log(evt.target) 
        console.log(evt.target.id) 
        console.log(savedRecipes)
        console.log(btn.classList)
        console.log(evt.toElement.previousSibling.previousElementSibling.previousElementSibling.href) 


if (btn.innerHTML === 'Save recipe') {
    $.post('/saved_recipes', savedRecipes, (response) => { 
        console.log(response)
        btn.innerHTML = 'Unsave recipe'
        btn.classList.add("button-saverecipe-class")

})
}
else if (btn.innerHTML === 'Unsave recipe') {
    $.post('/unsave_recipe', savedRecipes, (response)=> {
        console.log(response)
        btn.innerHTML = 'Save recipe'
        btn.classList.remove("button-saverecipe-class")
})};
});
})
}

{
const textButtons = document.querySelectorAll('.text-recipe')

textButtons.forEach((button)=> {button.addEventListener('click', (evt) => {
    const btn = evt.target;
    const recipeText = {
        'link_to_recipe': btn.parentNode.children[0].href,
        'recipe_name': $(`.${evt.target.id}, .recipe-name`).html(),
};
    console.log(evt.srcElement.parentNode)
    console.log(evt)
    console.log(evt.target) 
    console.log(evt.target.id) 
    console.log(recipeText)
if (btn.innerHTML === 'Text recipe link to phone') {
    $.post('/recipe_texted', recipeText, (response) => { 
        console.log(response)
        btn.innerHTML = 'Recipe texted!' 
        btn.classList.add("button-saverecipe-class")
})
}
else if (btn.innerHTML === 'Recipe texted!') {
    $.post('/recipe_texted', recipeText, (response) => {
        console.log(response)
        btn.innerHTML = 'Text recipe link to phone'
        btn.classList.add("button-saverecipe-class")
})};
});
})
}
 
function func() {
    document.getElementById('toggle').value  = 'Searching for recipes!';
}





















function initGeocoder() { 
    $('#location-button').on('click', (evt) => {
     navigator.geolocation.getCurrentPosition((res) => {
        console.log(res);
    const geocoder = new google.maps.Geocoder();
    const latlng = {lat: res.coords.latitude, lng: res.coords.longitude}
    geocoder.geocode({'location':latlng}, (res, status) => {
    const userLocation = res[3].formatted_address
        console.log(userLocation)
        console.log(latlng)
    const locationInput = document.querySelector('#location')
    const locationButton = document.querySelector('#location-button') 
        locationInput.value = userLocation;
        console.log(locationInput)
    })
     })
    })
}

 
 
