window.addEventListener('load',()=> {
    let long;
    let lat;
    let temperatureDescription = document.querySelector(".temperature-description");
    let temperatureDegree = document.querySelector(".temperature-degree");
    let locationTimezone = document.querySelector(".location-timezone");
    
    
    
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(position =>{
           long = position.coords.longitude;
           lat = position.coords.latitude;

           const proxy = "https://cors-anywhere.herokuapp.com/";
           const api = `${proxy}https://api.darksky.net/forecast/f2d897bdcdb545d606af052c0ac3662f/${lat},${long}`;
        
           fetch(api)
           .then(response => {
               return response.json();
           })
           .then(data => {
               console.log(data);
               const{temperature, summary } = data.currently;

               temperatureDegree.textContent = temperature;
               temperatureDescription.textContent = summary;
               locationTimezone.textContent = data.timezone;
           });
        });


    }else{
        h1.textContent = "リクエストできませんでした"
    }
});