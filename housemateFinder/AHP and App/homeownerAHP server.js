const homes = require('./original json/homesOriginal.js').homes;
/*
gender
    Female, straight
    Male, straight
    Male, gay/bi
    Female, gay/bi

pet
    "No cat or dog", 
    "Have a cat", 
    "Have a dog",
    "Have a cat and dog"


smoking
    Non-smoker
    Outdoor smoker
    Indoor smoker

overnight
    yes
    no 
*/

function ownerAHP(filterArr, priortyArr){
    console.log(homes[1]);
    
    let overnightFilter = filterArr[0];//0; // 1 for yes, 0 for no
    let genderFilterSex =  filterArr[1];//1; // 1 for male, 2 for female
    let genderFilterAppeal =  filterArr[2];//1; // 1 for straight, 2 for bi/gay
    let petFilter =  filterArr[3];//3; // 0 no pet, 1 dog, 2 cat, 3 okay all
    let smokingFilter =  filterArr[4];//2; // 0 no smoke, 1 outdoor, 2 indoor/all
    //// priorities 

    let priorities = {
        "OG": priortyArr[0],
        "OP": priortyArr[1],
        "OS": priortyArr[2],
        "GP": priortyArr[3],
        "GS": priortyArr[4],
        "PS": priortyArr[5]
    };
    let priorityMatrix = [
        [1, priorities.OG, priorities.OP, priorities.OS], //rent
        [(1 / priorities.OG), 1, priorities.GP, priorities.GS], //location
        [(1 / priorities.OP), (1 / priorities.GP), 1, priorities.PS], //pets
        [(1 / priorities.OS), (1 / priorities.GS), (1 / priorities.PS), 1]               //smoking
    ];

    function goAhp(compareArr, stdAvg) {

        //toplamlari
        let compareArrSums = [];
        for (let i in compareArr) {
            let sum = 0;
            for (let j in compareArr[i]) {
                sum += compareArr[j][i];
            }
            compareArrSums.push(sum);
        }


        // toplama böl
        for (let i in compareArr) {
            for (let j in compareArr[i]) {
                compareArr[i][j] = compareArr[i][j] / compareArrSums[j];
            }
        }

        // row ortalama hesabi
        let compareArrAvg = [];
        for (let i in compareArr) {
            let sum = 0;
            for (let j in compareArr[i]) {
                sum += compareArr[i][j];
            }
            compareArrAvg.push(sum / compareArr.length);
        }

        // ortalamalar x agirlik
        for (let i in compareArrAvg) {
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
    for (let j in priorityMatrix) {
        let i = priorityMatrix[j];
        matrixSum[0] += i[0];
        matrixSum[1] += i[1];
        matrixSum[2] += i[2];
        matrixSum[3] += i[3];
    }

    let standardizeMatrix = [[], [], [], []];
    for (let i in priorityMatrix) {
        for (let j in priorityMatrix[i]) {
            standardizeMatrix[i].push(priorityMatrix[i][j] / matrixSum[j]);
        }
    }

    let stdAverages = [0, 0, 0, 0];
    for (let i in standardizeMatrix) {
        let sum = 0;
        for (let j in standardizeMatrix[i]) {
            sum += standardizeMatrix[i][j];
        }
        stdAverages[i] = sum / 4;
    }

    let lamdaMax = 0;
    for (let i in matrixSum) {
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



    ///////////////////////////////////////////////////
    let filteredArr = homes;
    // let filteredArr = homes.filter(h => h.bedroomInfo.rent.single > 300);
    // filteredArr = filteredArr.filter(h => h.bedroomInfo.rent.single < 310);


    // filteredArr.forEach(i =>{
    //     console.log(i.occupants.gender);
    // })

    //AHP stuff

    // overnight ahp
    let overnightCompare = [];
    for (let i in filteredArr) {
        overnightCompare.push([]);
        for (let j in filteredArr) {
            let leftOvernight = filteredArr[i].bedroomInfo.overnight;
            let topOvernight = filteredArr[j].bedroomInfo.overnight;
            leftOvernight = (leftOvernight == 'yes') ? 1 : 0;
            topOvernight = (topOvernight == 'yes') ? 1 : 0;

            let leftControl = (leftOvernight == overnightFilter);
            let topControl = (topOvernight == overnightFilter);

            let point = -1;
            if (leftControl && topControl) point = 1;
            else if (leftControl && !topControl) point = 3;
            else if (!leftControl && topControl) point = 1 / 3;
            else if (!leftControl && !topControl) point = 1;

            if (i == j) point = 1;
            overnightCompare[i].push(point);
        }
    }

    let overnightCompareAvg = goAhp(overnightCompare, stdAverages[0]);


    //// gender ahp

    let genderCompare = [];
    for (let i in filteredArr) {   
        genderCompare.push([]);
        for (let j in filteredArr) {
            let leftGender = filteredArr[i].occupants.gender;
            let topGender = filteredArr[j].occupants.gender;
            let sex = (genderFilterSex == 1) ? 'Male' : 'Female';
            let appeal = (genderFilterAppeal == 1) ? 'straight' : 'gay/bi';
            let les = (genderFilterAppeal == 1) ? 'straight' : 'lesbian/bi';

            if (typeof leftGender == 'object') {
                let flagArr = [];
                for (k in leftGender) {
                    let flagSex = 0, flagAppeal = 0;
                    if (leftGender[k].split(", ")[0] == sex) flagSex = 1;
                    if (leftGender[k].split(", ")[1] == appeal || leftGender[k].split(", ")[1] == les) flagAppeal = 1;
                    flagArr.push((flagSex + flagAppeal));
                }            
                let index = returnMaxIndex(flagArr);
                leftGender = leftGender[index];            
            }

            if (typeof topGender == 'object') {
                let flagArr = [];
                for (k in topGender) {
                    let flagSex = 0, flagAppeal = 0;
                    if (topGender[k].split(", ")[0] == sex) flagSex = 1;
                    if (topGender[k].split(", ")[1] == appeal || leftGender[k].split(", ")[1] == les) flagAppeal = 1;
                    flagArr.push(flagSex + flagAppeal);
                }
                let index = returnMaxIndex(flagArr);
                topGender = topGender[index];
            }

            let sex1 = leftGender.split(", ")[0];
            let appeal1 = leftGender.split(", ")[1];
            let sex2 = topGender.split(", ")[0];
            let appeal2 = topGender.split(", ")[1];
            
            let sex1Control = (sex1 == sex);
            let appeal1Control = (appeal1 == appeal || appeal1 == les);
            let sex2Control = (sex2 == sex);
            let appeal2Control = (appeal2 == appeal || appeal1 == les);

            let pointSex = 0, pointAppeal = 0;
        
            if (sex1Control && sex2Control) pointSex = 1;
            else if (sex1Control && !sex2Control) pointSex = 4;
            else if (!sex1Control && sex2Control) pointSex = 1/4;
            else pointSex = 1;
        
            if (appeal1Control && appeal2Control) pointAppeal = 1;
            else if (appeal1Control && !appeal2Control) pointAppeal = 3;
            else if (!appeal1Control && appeal2Control) pointAppeal = 1/3;
            else pointAppeal = 1;

            let point=pointSex+pointAppeal/2;        
            genderCompare[i].push(point);
            
        }
    }
    let genderCompareAvg = goAhp(genderCompare, stdAverages[1]);



    ///// pets ahp
    let petCompare = [];
    for (let i in filteredArr) {
        petCompare.push([]);
        for (let j in filteredArr) {
            let leftPet = filteredArr[i].occupants.pets;
            let topPet = filteredArr[j].occupants.pets;

            let filter;
            switch (petFilter) {
                case 0:
                    filter = 'No cat or dog';
                    break;
                case 1:
                    filter = 'Have a dog';
                    break;
                case 2:
                    filter = 'Have a cat';
                    break;
                case 3:
                    filter = 'Have a cat and dog';
                    break;
            }

            let leftControl = (leftPet == filter);
            let topControl = (topPet == filter);

            let point = -1;
            if (leftControl && topControl) point = 1;
            else if (leftControl && !topControl) point = 3;
            else if (!leftControl && topControl) point = 1 / 3;
            else if (!leftControl && !topControl) point = 1;
            if (i == j) point = 1;
            petCompare[i].push(point);
        }
    }
    let petCompareAvg = goAhp(petCompare, stdAverages[2]);


    ///// smoking ahp
    let smokingCompare = [];
    for (let i in filteredArr) {
        smokingCompare.push([]);
        for (let j in filteredArr) {
            let leftSmoking = filteredArr[i].occupants.smoking;
            let topSmoking = filteredArr[j].occupants.smoking;


            if (typeof leftSmoking == 'object') {
                if (leftSmoking.indexOf('Indoor smoker') != -1) leftSmoking = 'Indoor smoker';
                else if (leftSmoking.indexOf('Outdoor smoker' != -1)) leftSmoking = 'Outdoor smoker';
            }

            if (typeof topSmoking == 'object') {
                if (topSmoking.indexOf('Indoor smoker') != -1) topSmoking = 'Indoor smoker';
                else if (topSmoking.indexOf('Outdoor smoker' != -1)) topSmoking = 'Outdoor smoker';
            }

            let smokingControl = '';
            switch (smokingFilter) {
                case 0:
                    smokingControl = 'Non-smoker';
                    break;
                case 1:
                    smokingControl = 'Outdoor smoker';
                    break;
                case 2:
                    smokingControl = 'Indoor smoker';
                    break;
            }

            let leftControl = (leftSmoking == smokingControl);
            let topControl = (topSmoking == smokingControl);

            let point = -1;
            if (leftControl && topControl) point = 1;
            if (leftControl && !topControl) point = 3;
            if (!leftControl && topControl) point = 1 / 3;
            if (!leftControl && !topControl) point = 1;

            if (smokingFilter == 2){
                if(leftSmoking == 'Outdoor smoker' && topSmoking=='Non-smoker') point = 2;
                else if(leftSmoking=='Non-smoker' && topSmoking=='Outdoor smoker') point =1/2;
            }

            if (i == j) point = 1;
            smokingCompare[i].push(point);
        }
    }
    let smokingCompareAvg = goAhp(smokingCompare, stdAverages[3]);



    let resultArr = [];
    for(i in overnightCompareAvg){
        resultArr.push([]);
    }
    for (let i in overnightCompareAvg) {
        resultArr[i].push(overnightCompareAvg[i] + genderCompareAvg[i] + smokingCompareAvg[i] + petCompareAvg[i]);
        resultArr[i].push(i);
    }

    resultArr.sort();
    resultArr.reverse();

    // console.log('\ngirilen degerler:');
    // console.log('overnight:        ', overnightFilter);
    // console.log('gender:           ', genderFilterSex,'appeal:  ', genderFilterAppeal);
    // console.log('pet:              ', petFilter);
    // console.log('smoking:          ', smokingFilter);

    // console.log('///////////////////////////////////////////');
    // console.log('///////////////////////////////////////////');


    // for (let i in resultArr) {
    //     let index = resultArr[i][1];
    //     let f = filteredArr[index];
    //     console.log('point:      ', resultArr[i]);
    //     console.log('overnight   ', f.bedroomInfo.overnight,overnightCompareAvg[index]);    
    //     console.log('gender:     ', f.occupants.gender,genderCompareAvg[index]);
    //     console.log('pets:       ', f.occupants.pets, petCompareAvg[index]);
    //     console.log('smoking:    ', f.occupants.smoking, smokingCompareAvg[index]);
    //     console.log('\n===========================================\n');
    // }

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
ownerAHP();
exports.ownerAHP = ownerAHP;