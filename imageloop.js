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

import fs from 'fs';

const dir = '~/pulsars/';

fs.readdir(dir, (err, files) => {console.log(files.length);
});

var i;
for (i=0; )
 