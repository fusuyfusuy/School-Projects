const homesModule = require("./original\ json/homesOriginal.js");
let homes = homesModule.homes;
const fs = require('fs');

function changeString(obje){
    let returnString = obje;
    if(typeof obje == "object"){
        returnString = obje.join(' && ');
    }
    return returnString;
}

let newHomes = [];
for(i in homes){
    let h = homes[i];
    let n = {};
    n=h;

    let fpgender = h.flatmatePreferences.gender;
    if(typeof fpgender == 'object'){
        fpgender = fpgender.join(' && ');
        h.flatmatePreferences.gender=fpgender;
    }

    let fppets = h.flatmatePreferences.pets;
    if(typeof fppets == 'object'){
        fppets = fppets.join(' && ');
        h.flatmatePreferences.pets = fppets;
    }

    h.flatmatePreferences.smoking = changeString(h.flatmatePreferences.smoking);

    h.description.features = changeString(h.description.features);

    h.occupants.interests = changeString(h.occupants.interests);

    h.occupants.gender = changeString(h.occupants.gender);

    h.occupants.age = changeString(h.occupants.age);

    h.occupants.smoking = changeString(h.occupants.smoking);

    h.bedroomInfo.features = changeString(h.bedroomInfo.features);

    h.bedroomInfo.bills = h.bedroomInfo.rent.bills;
    if(h.bedroomInfo.rent.per=='month'){
        h.bedroomInfo.rent.single = h.bedroomInfo.rent.single/4;
    }
    h.bedroomInfo.rent = h.bedroomInfo.rent.single;

    h.flatmatePreferences.agemin = h.flatmatePreferences.age.agemin;
    h.flatmatePreferences.agemax = h.flatmatePreferences.age.agemax;

    delete h.flatmatePreferences.age;

}


fs.writeFile ("stringifiedHomes.json", JSON.stringify(homes), function(err) {
    if (err) throw err;
    console.log('complete');
    }
);