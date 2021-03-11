// For full API documentation, including code examples, visit https://wix.to/94BuAAs
import { homeAHP } from 'backend/homeAHP';
import { homeOwnerAHP } from 'backend/homeOwnerAHP';
import {getHomesData} from 'backend/getHomesData';
import wixData from 'wix-data';

$w.onReady(function () {
	//TODO: write your page related code here...

});

export async function submitButton_click(event) {
	//Add your code for this event here:
	let filterArr = [0,1,2,3];
	let priorityArr = [0,1,2,3,4,5];
	filterArr[0] = [$w('#minRent').value,$w('#maxRent').value];
	filterArr[1] = ['Melbourne'];
	filterArr[2] = $w('#petChoice').value;
	filterArr[3] = $w('#smokingChoice').value;

	priorityArr[0]=$w('#smokingRent').value;
	priorityArr[1]=$w('#smokingLocation').value;
	priorityArr[2]=$w('#smokingPet').value;
	priorityArr[3]=$w('#rentLocation').value;
	priorityArr[4]=$w('#rentPet').value;
	priorityArr[5]=$w('#locationPet').value;


	let filterArrOwner = [0,1,2,3,4];
	let priorityArrOwner = [0,1,2,3,4,5];

	filterArrOwner[0] = $w('#overnight').value;
	let genderPref = $w('#genderPref').value;
	switch(genderPref){
		case 0:
			filterArrOwner[1] = 0;
			filterArrOwner[2] = 0;
			break;
		case 1:
			filterArrOwner[1] = 0;
			filterArrOwner[2] = 1;
			break;
		case 2:
			filterArrOwner[1] = 1;
			filterArrOwner[2] = 0;
			break;
		case 3:
			filterArrOwner[1] = 1;
			filterArrOwner[2] = 1;
			break;
	}
	filterArrOwner[3] = $w('#petChoice').value;
	filterArrOwner[4] = $w('#smokePref').value;

	priorityArrOwner[0] = $w('#genderOvernight').value;
	priorityArrOwner[1] = $w('#genderSmoking').value;
	priorityArrOwner[2] = $w('#genderPet').value;
	priorityArrOwner[3] = $w('#overnighSmoking').value;
	priorityArrOwner[4] = $w('#overnightPet').value;
	priorityArrOwner[5] = $w('#petSmoking').value;
	function convertUsable(number){
		let newNumber = 0;
		switch (number) {
			case -5:
				newNumber = 7;
				break;
			case -4:
			case -3:
				newNumber = 5;
				break;
			case -2:
			case -1:
				newNumber = 3;
				break;
			case 0:
				newNumber = 1;
				break;
			case 1:
			case 2:
				newNumber = 1/3;
				break;
			case 3:
			case 4:
				newNumber = 1/5;
				break;
			case 5: 
				newNumber = 1/7;
				break;
			default:
				newNumber = 1;
				break;
		}
		return newNumber;
	}	

	for(let i in priorityArr){
		priorityArr[i] = convertUsable(priorityArr[i]);
	}
	for(let i in priorityArrOwner){
		priorityArrOwner[i] = convertUsable(priorityArrOwner[i]);
	}
	let orderedPriority = [0,1,2,3,4,5];
	orderedPriority[0] =priorityArr[3];
	orderedPriority[1] =priorityArr[4];
	orderedPriority[2] =(1/priorityArr[0]);
	orderedPriority[3] =priorityArr[5];
	orderedPriority[4] =(1/priorityArr[1]);
	orderedPriority[5] =(1/priorityArr[2]);

	let orderedOwner = [0,1,2,3,4,5];
	orderedOwner[0] = (1/priorityArrOwner[0]);
	orderedOwner[1] = priorityArrOwner[4];
	orderedOwner[2] = priorityArrOwner[3];
	orderedOwner[3] = priorityArrOwner[2];
	orderedOwner[4] = priorityArrOwner[1];
	orderedOwner[5] = priorityArrOwner[5];

	let filterJson = {
		"rentRange":filterArr[0],
		"location":filterArr[1],
		"petFilter":filterArr[2],
		"smokingFilter":filterArr[3],
		"priorityArr":orderedPriority
	}
	console.log(filterJson);
	let ahpResult = await homeAHP(filterArr,orderedPriority);
	console.log('----------ahpResult-------------\n',ahpResult);

	let repeatArr = [];
	for(let i in ahpResult){
		repeatArr.push(ahpResult[i][0]);
	}
	let newArr = [];

	let ownerResult = await homeOwnerAHP(filterArrOwner, orderedOwner, repeatArr);
	console.log('----------ownerResult------------\n',ownerResult);

	let ownerArr = [];
	for(let i in ownerResult){
		ownerArr.push(ownerResult[i][0]);
	}
	let newOwnerArr = [];

	let averagedArr = [];
	let homeAvg=0, ownerAvg=0;
	for(let i in ahpResult){
		homeAvg+=ahpResult[i][1];
		ownerAvg+=ownerResult[i][1];
	}
	homeAvg = homeAvg/(ahpResult.length);
	ownerAvg+=ownerAvg/(ownerResult.length);
	for(let i in ahpResult){
		averagedArr.push([]);
		averagedArr[i].push(ahpResult[i][0]);
		let flag = -1;
		for(let j in ahpResult){
			if(ahpResult[i][0]._id == ownerResult[j][0]._id) flag = j;
		}
		averagedArr[i].push((ahpResult[i][1]/homeAvg)+(ownerResult[flag][1]/ownerAvg));
	}
	averagedArr.sort();
	averagedArr.reverse();

	for(let i in repeatArr){
		let newTemplate = {
			_id:'',
			title:'',
			info:{
				city:'',
				block:'',
			},
			bedroomInfo:{
				rent:'',
			},
			flatmatePrefences:{
				pets:'',
				smoking:'',
			}
		}
		newArr.push(newTemplate);
		newArr[i]._id = repeatArr[i]._id;
		console.log(newArr[i]._id, repeatArr[i]._id);
		newArr[i].title = repeatArr[i]._id;
		newArr[i].infoCity = repeatArr[i].info.city;
		newArr[i].infoBlock = repeatArr[i].info.block;
		newArr[i].bedroomInfoRent = repeatArr[i].bedroomInfo.rent;
		newArr[i].flatmatePreferencesPets = repeatArr[i].flatmatePreferences.pets;
		newArr[i].flatmatePreferencesSmoking = repeatArr[i].flatmatePreferences.smoking;
	}
	for(let i in ownerArr){
		let newTemplate = {
			title:'',
			_id:'',
		};
		newOwnerArr.push(newTemplate);
		let o = ownerArr[i];
		newOwnerArr[i].title = o._id;
		newOwnerArr[i]._id = o._id;
		newOwnerArr[i].bedroomInfoOvernight = o.bedroomInfo.overnight;
		newOwnerArr[i].occupantsPets = o.occupantsPets;
		newOwnerArr[i].occupantsSmoking = o.occupants.smoking;
	}

	let finalArr = [];
	for(let i in averagedArr){
		let newTemplate = {
			_id:'',
			title:'',
			info:{
				city:'',
				block:'',
			},
			bedroomInfo:{
				rent:'',
			},
			flatmatePrefences:{
				pets:'',
				smoking:'',
			}
		}
		finalArr.push(newTemplate);
		finalArr[i]._id = averagedArr[i][0]._id;
		finalArr[i].title = averagedArr[i][0]._id;
		finalArr[i].infoCity = averagedArr[i][0].info.city;
		finalArr[i].infoBlock = averagedArr[i][0].info.block;
		finalArr[i].bedroomInfoRent = averagedArr[i][0].bedroomInfo.rent;
		finalArr[i].flatmatePreferencesPets = averagedArr[i][0].flatmatePreferences.pets;
		finalArr[i].flatmatePreferencesSmoking = averagedArr[i][0].flatmatePreferences.smoking;
		finalArr[i].bedroomInfoOvernight = averagedArr[i][0].bedroomInfo.overnight;
		finalArr[i].occupantsPets = averagedArr[i][0].occupants.pets;
		finalArr[i].occupantsSmoking = averagedArr[i][0].occupants.smoking;
		finalArr[i].occupantsGender = averagedArr[i][0].occupants.gender;
	}
	$w('#repeater1').data = finalArr;
	$w('#repeater1').show();
	// $w('#repeater2').data = newOwnerArr;
	// $w('#repeater2').show();

	console.log('----------averagedArr--------------\n',averagedArr);

	console.log('----------finalArr--------------\n',finalArr);
	
}