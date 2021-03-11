const personsModule = require("./original\ json/personsOriginal.js");
let persons = personsModule.persons;
const fs = require('fs');

function changeString(obje){
    let returnString = obje;
    if(typeof obje == "object"){
        returnString = obje.join(' && ');
    }
    return returnString;
}

let newpersons = [];
for(i in persons){
    let p = persons[i];

    p.info.interests = changeString(p.info.interests);

    p.info.smoking = changeString(p.info.smoking);

    p.search.home.homeSizes = changeString(p.search.home.homeSizes);
    if(p.search.home.rent.per == 'month') p.search.home.rent = p.search.home.rent.single/4;
    else if(p.search.home.rent.per=='week') p.search.home.rent = p.search.home.rent.single;
    p.search.home.bedroomSizes = changeString(p.search.home.bedroomSizes);
    p.search.location = changeString(p.search.location);
    p.search.flatmate.gender = changeString(p.search.flatmate.gender);
    p.search.flatmate.pets = changeString(p.search.flatmate.pets);
    p.search.flatmate.smoking = changeString(p.search.flatmate.smoking)

    let regexp = /(\d\d) to (\d\d) yrs/g;
    let regexp2 = /(\d\d)/;
    let result = regexp.exec(p.search.flatmate.ageGroup);
    if(result == null) result = regexp2.exec(p.search.flatmate.ageGroup);
    
    p.search.flatmate.agemin = result[1];
    if(result.length == 2) p.search.flatmate.agemax = -1
    else p.search.flatmate.agemax = result[2];

    delete p.search.flatmate.ageGroup;

    p.info.employment = changeString(p.info.employment);
}


fs.writeFile ("stringifiedPersons.json", JSON.stringify(persons), function(err) {
    if (err) throw err;
    console.log('complete');
    }
);