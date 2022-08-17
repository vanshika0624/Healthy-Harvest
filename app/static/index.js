$("#predict-crop-btn").click(function(){
  var temperature = document.getElementById('temperature').value
  var humidity =  document.getElementById('humidity').value
  var pH = document.getElementById('pH').value;
  var rainfall = document.getElementById('rainfall').value
  $.ajax(
  {
    type:"GET",
    url: "/predictcrop",
    data:{
          'temperature':temperature,
          'humidity':humidity,
          'pH':pH,
          'rainfall':rainfall,
       },
       success: function( data )
       {
         if(data == "0"){
           document.getElementById('predicted-crop').innerHTML = "** Your conditons are not a good fit for any crop right now. **"
         } else {
            document.getElementById('predicted-crop').innerHTML = "You can grow <b>" + data + "</b> right now."
         }


       }
     })
})



$("#video-demo-btn").click(function(){

  $.ajax(
  {
    type:"GET",
    url: "/videoleaf",
    data:{
       },
       success: function( data )
       {
       }
     })

})






$("#explore-btn").click(function(){
  gsap.to(".container",{transform:"translateX(-100%)"})
})
$("#take-demo-button").click(function(){
  gsap.to(".container",{transform:"translateX(-200%)"})
})



$(".back-btn").click(function(e){
  var btn_id = "#"+$(this).attr('id')
  var slide_number = parseInt(btn_id[5])
  console.log(slide_number)
  var amount_translate = "translateX("+String((slide_number-2)*100*-1)+"%)";
  console.log(amount_translate)
  gsap.to(".container",{transform:amount_translate})
})



$(".next-btn").click(function(e){
  var btn_id = "#"+$(this).attr('id')
  var slide_number = parseInt(btn_id[5])
  console.log(slide_number)
  var amount_translate = "translateX("+String((slide_number)*100*-1)+"%)";
  console.log(amount_translate)
  gsap.to(".container",{transform:amount_translate})
})
