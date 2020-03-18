// This script will roll through the images that are kept in the pulsar directory on
// the webserver
// So something like:
// for pulsar in pulsars
//      print a h1 heading = pulsar
//      for plots in pulsar:
//          print a p1 soft heading
//          put down the image 
//
// Pretty much just that, maybe add some interface stuff later - learn javascript

import { readdir } from 'fs';
const dir = '~/pulsars/';

//Reads the amount of pulsars in the directory
readdir(dir, (err, pulsars) => {
    //Defines a length for the pulsar directory
    let totalPulsars = pulsars.length; 
});

// Loop through all the pulsars 
var i,
    img;

for (i=0; i < totalPulsars; i++) {
    document.writeln(pulsars)

    //Need a nested for loop in here to pull out the individual observations
    const dir2 = '~/pulsars'+pulsars
    readdir(dir2, (err, obs) => {
    //Defines a length of the number of plots for the pulsar... I hope
        let pulsarPlots = obs.length;
    
    // This should pull out the images and put them in the site
    //for (var i=0; i < pulsarPlots; i++) {
    //    document.writeln(obs)
    //    var image = document.createElement("img")
    //    image.setAttribute("src", `${dir2}/${i}`)

    //Below this line is an attempt with a different method than above
        for (var i =0; i <= pulsarPlots; i++) {
            img = new Image();
            img.src = dir2+'/'+obs;
            parent.appendChild(img)
        }
    })
    //}
}

 