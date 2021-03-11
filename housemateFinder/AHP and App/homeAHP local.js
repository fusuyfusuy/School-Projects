const homes = require('./original json/homesOriginal').homes;

/* 
kullanıcıdan alınacak değişkenler nasıl gelecek?
o değişkenler bi yerde tutulacak. matris değişkenleri olacak ahp ilk tablosu priority şeyleri.
filtre değişkenleri olacak.

rent range - iki değer min max

location - list ?

pet - düz qualitative  (cats dogs or no)
    flatmate: "Without a cat or dog","Dogs okay","Cats okay","Pets okay"
    occupant: "No cat or dog", "Have a cat", "Have a dog","Have a cat and dog"

smoking - düz qualitative (indoor outdoor no)
    FlatmatePreferences: "Non-smokers", "Outdoors okay", "Smokers okay"
    OCCUPANTS: Non-smoker, Outdoor smoker, Indoor smoker



filteredArr onemli. islemler ona gore yapiliyor. olmayacaksa filteredArr = homes yapilir.
    */
////filter
function homeAHP(filterArr, priorityArr){

    for(let i in homes){
        if(homes[i].bedroomInfo.rent.per=='month'){
            homes[i].bedroomInfo.rent.per = 'week';
            homes[i].bedroomInfo.rent.single = homes[i].bedroomInfo.rent.single/4;            
        }
    }

    // let filter = homes.find(h=>{
    //     return h._id=='952574';
    // })
    // console.log(filter);
    

    let rentRange = [350, 500];
    let location = ['Melbourne'];
    let petFilter = 3; // 0 no pet, 1 dog, 2 cat, 3 okay all
    let smokingFilter = 2; // 0 no smoke, 1 outdoor, 2 indoor
    //// priorities 
    // console.log('filters  =   ', rentRange,location,petFilter,smokingFilter);
    
    let priorities = {
        "RL": 3,//priorityArr[0],
        "RP": 5,//priorityArr[1],
        "RS": 7,//priorityArr[2],
        "LP": 3,//priorityArr[3],
        "LS": 5,//priorityArr[4],
        "PS": 3,//priorityArr[5]
    };
    // console.log('priorities  =  ',priorities);
    
    let priorityMatrix = [
        [1, priorities.RL, priorities.RP, priorities.RS], //rent
        [(1 / priorities.RL), 1, priorities.LP, priorities.LS], //location
        [(1 / priorities.RP), (1 / priorities.LP), 1, priorities.PS], //pets
        [(1 / priorities.RS), (1 / priorities.LS), (1 / priorities.PS), 1]               //smoking
    ];

    function goAhp(compareArr, stdAvg) {

        //toplamlari
        let compareArrSums = [];
        for (i in compareArr) {
            let sum = 0;
            for (j in compareArr[i]) {
                sum += compareArr[j][i];
            }
            compareArrSums.push(sum);
        }


        // toplama böl
        for (i in compareArr) {
            for (j in compareArr[i]) {
                compareArr[i][j] = compareArr[i][j] / compareArrSums[j];
            }
        }

        // row ortalama hesabi
        let compareArrAvg = [];
        for (i in compareArr) {
            let sum = 0;
            for (j in compareArr[i]) {
                sum += compareArr[i][j];
            }
            compareArrAvg.push(sum / compareArr.length);
        }

        // ortalamalar x agirlik
        for (i in compareArrAvg) {
            compareArrAvg[i] = compareArrAvg[i] * stdAvg;
        }
        return compareArrAvg;
    }
    function returnMaxIndex(array) {
        let max = 0;
        for (let i = 0; i < array.length; i++) {
            if (array[max] <= array[i]) max = i;
        }
        return max;
    }

    ////////////////////////////


    //consistency check
    let matrixSum = [0, 0, 0, 0];
    for (j in priorityMatrix) {
        let i = priorityMatrix[j];
        matrixSum[0] += i[0];
        matrixSum[1] += i[1];
        matrixSum[2] += i[2];
        matrixSum[3] += i[3];
    }

    let standardizeMatrix = [[], [], [], []];
    for (i in priorityMatrix) {
        for (j in priorityMatrix[i]) {
            standardizeMatrix[i].push(priorityMatrix[i][j] / matrixSum[j]);
        }
    }

    let stdAverages = [0, 0, 0, 0];
    for (i in standardizeMatrix) {
        let sum = 0;
        for (j in standardizeMatrix[i]) {
            sum += standardizeMatrix[i][j];
        }
        stdAverages[i] = sum / 4;
    }

    let lamdaMax = 0;
    for (i in matrixSum) {
        lamdaMax += (matrixSum[i] * stdAverages[i]);
    }
    let CI = (lamdaMax - 4) / 3;
    let CR = CI / 0.9;
    if (CR < 0.1) {
        console.log("CONSISTENT  -  ", CR);
    }
    else {
        console.log("NOT CONSISTENT  -  ", CR);
        return -1;
    }




    ////////////////////////////


    


    //real stuff

    ////////// filter. bu database querysi olarak da yapilabilir. direkt burda da yapilabilir.
    // let filteredArr = homes;
    let filteredArr = homes.filter(h => h.bedroomInfo.rent.single > rentRange[0]);
    filteredArr = filteredArr.filter(h => h.bedroomInfo.rent.single < rentRange[1]);

    
    /// rent icin ahp
    if(typeof rentRange[0] != "number"){
        rentRange[0] = parseInt(rentRange[0]);
        rentRange[1] = parseInt(rentRange[1]);
    }
    let rentConstant = (rentRange[1] - rentRange[0]);
    let rentCompare = [];
    for (i in filteredArr) {
        rentCompare.push([]);
        for (j in filteredArr) {
            let leftHome, topHome;
            if(filteredArr[i].bedroomInfo.rent.per!="week"){
                leftHome = filteredArr[i].bedroomInfo.rent.single/4;                
            }
            else leftHome = filteredArr[i].bedroomInfo.rent.single;
            topHome = (filteredArr[j].bedroomInfo.rent.per != "week")?filteredArr[j].bedroomInfo.rent.single/4:filteredArr[j].bedroomInfo.rent.single;
            let endPoint = 0;
            let diff = leftHome - topHome;
            if (diff <= 0) {
                endPoint = rentConstant / (rentConstant + diff);
            }
            else {
                endPoint = (rentConstant - diff) / rentConstant;
            }
            rentCompare[i].push(endPoint);
        }
    }
    let rentCompareAvg = goAhp(rentCompare, stdAverages[0]);



    
    ///// location ahp 
    let locCompare = [];
    let locConstant = 1.2;
    let locOutlier = Math.pow(locConstant, (location.length * 10));
    // let locOutlier = Math.pow(locConstant,location.length);
    for (i in filteredArr) {
        locCompare.push([]);
        for (j in filteredArr) {
            let leftLoc = filteredArr[i].info.block;
            let topLoc = filteredArr[j].info.block;
            let leftI = location.indexOf(leftLoc);
            let topI = location.indexOf(topLoc);
            if (leftI != -1 && topI != -1) {
                locCompare[i].push(Math.pow(locConstant, topI - leftI));
            }
            else if (leftI != -1 && topI == -1) {
                locCompare[i].push(locOutlier);
            }
            else if (leftI == -1 && topI != -1) {
                locCompare[i].push(1 / locOutlier);
            }
            else if (leftI == -1 && topI == -1) {
                locCompare[i].push(1);
            }
        }
    }
    let locCompareAvg = goAhp(locCompare, stdAverages[1]);




    

    ///// pets ahp
    if(typeof petFilter != "number") petFilter = parseInt(petFilter);
    let petArray = [];
    for (i in filteredArr) {
        let number = 0;
        let pet = filteredArr[i].flatmatePreferences.pets;
        if (typeof pet == "object") {
            for (i in pet) {
                if (pet[i] != 'Without a cat or dog') {
                    number = (pet[i] == 'Dogs okay') ? 1 : 2;
                }
            }
        }
        else {
            switch (pet) {
                case 'Dogs okay':
                    number = 1;
                    break;
                case 'Cats okay':
                    number = 2;
                    break;
                case 'Without a cat or dog':
                    number = 0;
                    break;
                case 'Pets okay':
                    number = 3;
                    break;
                default:
                    number = -1;
                    break;
            }
        }
        petArray.push(number);
    }
    let dogArr = [[1, 1 / 3, 1 / 2, 1 / 3], [3, 1, 2, 1], [2, 1 / 2, 1, 1 / 2], [3, 1, 2, 1]];
    let catArr = [[1, 1 / 2, 1 / 3, 1 / 3], [2, 1, 1 / 2, 1 / 2], [3, 2, 1, 1], [3, 2, 1, 1]];
    let noArr = [[1, 1, 1 / 5, 2], [1, 1, 1 / 5, 2], [5, 5, 1, 5], [1 / 2, 1 / 2, 1 / 5, 1]];
    let yesArr = [[1, 1 / 3, 1 / 3, 1 / 5], [3, 1, 1, 1 / 2], [3, 1, 1, 1 / 2], [5, 2, 2, 1]];
    let petCompare = [];
    for (i in petArray) {
        petCompare.push([]);
        let theArr = [];
        for (j in petArray) {
            let leftPet = petArray[i];
            let topPet = petArray[j];
            let endPoint = 0;
            switch (petFilter) {
                case 0:
                    theArr = noArr;
                    break;
                case 1:
                    theArr = dogArr;
                    break;
                case 2:
                    theArr = catArr;
                    break;
                case 3:
                    theArr = yesArr;
                    break;
                default:
                    console.error("Pet AHP error!");
            }
            petCompare[i].push(theArr[leftPet][topPet]);
        }
    }
    let petCompareAvg = goAhp(petCompare, stdAverages[2]);



    


    ////////// smoking ahp
    if(typeof smokingFilter != "number") smokingFilter = parseInt(smokingFilter);
    let smokingArr = [];
    for (i in filteredArr) {
        let number = 0;
        let smoking = filteredArr[i].flatmatePreferences.smoking;
        if (typeof smoking == 'object') {
            for (i in smoking) {
                if (smoking[i] != 'Non-smokers') {
                    number = (smoking[i] == 'Outdoors okay') ? 1 : 2;
                }
            }
        }
        else {
            switch (smoking) {
                case 'Non-smokers':
                    number = 0;
                    break;
                case 'Outdoors okay':
                    number = 1;
                    break;
                case 'Smokers okay':
                    number = 2;
                    break;
                default:
                    number = -1;
                    break;
            }
        }
        smokingArr.push(number);
    }
    let noSmoke = [[1, 3, 5], [1 / 3, 1, 2], [1 / 5, 1 / 2, 1]];
    let yesSmoke = [[1, 1 / 3, 1 / 5], [3, 1, 2], [5, 2, 1]];
    let outSmoke = [[1, 1 / 2, 2], [2, 1, 3], [1 / 2, 1 / 3, 1]];
    let smokingCompare = [];
    for (i in smokingArr) {
        smokingCompare.push([]);
        let theArr = [];
        for (j in smokingArr) {
            let leftS = smokingArr[i];
            let topS = smokingArr[j];
            switch (smokingFilter) {
                case 0:
                    theArr = noSmoke;
                    break;
                case 1:
                    theArr = outSmoke;
                    break;
                case 2:
                    theArr = yesSmoke;
                    break;
                default:
                    console.error('Smoking AHP error!')
            }
            smokingCompare[i].push(theArr[leftS][topS]);
        }
    }
    let smokingCompareAvg = goAhp(smokingCompare, stdAverages[3]);

    
    let resultArr = [];
    for(i in rentCompareAvg){
        resultArr.push([]);
    }
    for (i in rentCompareAvg) {
        resultArr[i].push(rentCompareAvg[i] + locCompareAvg[i] + smokingCompareAvg[i] + petCompareAvg[i]);
        resultArr[i].push(i);
    }
    
    resultArr.sort();
    resultArr.reverse();
    console.log(filteredArr.length);
    
    // for(i in filteredArr){
    //     if(filteredArr[i].info.block=='Melbourne')
    //         console.log("FOUND");   
    // }


    // console.log('girilen degerler:');
    // console.log('rent:        ', rentRange);
    // console.log('location:    ', location);
    // console.log('pet:         ', petFilter);
    // console.log('smoking:     ', smokingFilter);
    // console.log('----------------------------------------------------');
    
    // // console.log(filteredArr.length);
    
    for (i in resultArr) {
        let f = filteredArr[resultArr[i][1]];
        console.log('point:   ', resultArr[i]);
        console.log('id:      ',f._id);
        // console.log('rent:    ', f.bedroomInfo.rent);
        // console.log('rent point:    ',rentCompareAvg[resultArr[i][1]]);
        // console.log('block:   ', f.info.block);
        // console.log('block point:   ',locCompareAvg[resultArr[i][1]]);
        // console.log('pets:    ', f.flatmatePreferences.pets);
        // console.log('pets point:    ',petCompareAvg[i]);
        // console.log('smoking: ', f.flatmatePreferences.smoking);
        // console.log('smoking point: ',smokingCompareAvg[i]);
        console.log('\n=================================================\n');
    }
    

    let returnArr = [];
    for(i in resultArr){
        returnArr.push([]);
    }
    for(i in resultArr){
        returnArr[i].push(filteredArr[resultArr[i][1]]);
        returnArr[i].push(resultArr[i][0]);
    }

    let returnLength = returnArr.length;
    let finalArr = [];
    if(returnLength<20) return returnArr;
    else{
        for(let i = 0; i<20; i++){
            finalArr.push(returnArr[i]);
        }
        return finalArr;
    }
    
}
homeAHP();
exports.homeAHP = homeAHP;