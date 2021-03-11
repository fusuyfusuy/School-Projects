// For full API documentation, including code examples, visit https://wix.to/94BuAAs
import {personAHP} from 'backend/personAHP';
$w.onReady(function () {
	//TODO: write your page related code here...

});

export async function button6_click(event) {




	let filterArrOwner = [0,1,2,3,4];
	let priorityArrOwner = [0,1,2,3,4,5];

	filterArrOwner[0] = $w('#overnight').value;
	let genderPref = $w('#gender').value;
	switch(genderPref){
		case 0:
			filterArrOwner[1] = 1;
			filterArrOwner[2] = 1;
			break;
		case 1:
			filterArrOwner[1] = 1;
			filterArrOwner[2] = 2;
			break;
		case 2:
			filterArrOwner[1] = 2;
			filterArrOwner[2] = 1;
			break;
		case 3:
			filterArrOwner[1] = 2;
			filterArrOwner[2] = 2;
			break;
	}
	filterArrOwner[3] = $w('#pet').value;
	filterArrOwner[4] = $w('#smoking').value;

	priorityArrOwner[0] = $w('#genderOvernight').value;
	priorityArrOwner[1] = $w('#genderSmoking').value;
	priorityArrOwner[2] = $w('#genderPet').value;
	priorityArrOwner[3] = $w('#overnightSmoking').value;
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

	
	let orderedOwner = [0,1,2,3,4,5];
	orderedOwner[0] = (1/priorityArrOwner[0]);
	orderedOwner[1] = priorityArrOwner[4];
	orderedOwner[2] = priorityArrOwner[3];
	orderedOwner[3] = priorityArrOwner[2];
	orderedOwner[4] = priorityArrOwner[1];
	orderedOwner[5] = priorityArrOwner[5];

	let ownerResult = await personAHP(filterArrOwner, orderedOwner);
	console.log('----------personResult------------\n',ownerResult);

	let ownerArr = [];
	for(let i in ownerResult){
		ownerArr.push(ownerResult[i][0]);
	}
	let newArr = [];

	for(let i in ownerArr){
		let newTemplate = {
			title: '',
			_id: '',
			info: {
				interests: '',
				name: '',
				pets: '',
				smoking: '',
				availableDate: '',
				gender: '',
				age: '',
				employment: '',
				overnight: ''
			},
			search: {
				home: {
					bedroomType: '',
					bathroomFacilities: '',
					homeSizes: '',
					rent: '',
					bedroomFurniture: '',
					parkingFacilities: '',
					bedroomSizes: '',
				overnight: ''
				},
				location: '',
				flatmate: {
					gender: '',
					pets: '',
					ageGroup: '',
				smoking: ''
					}
				}
			}
		
		newArr.push(newTemplate);
		newArr[i]._id = ownerArr[i]._id;
		newArr[i].title = ownerArr[i]._id;
		newArr[i].infoName = ownerArr[i].info.name;
		newArr[i].infoGender = ownerArr[i].info.gender;
		newArr[i].infoPets = ownerArr[i].info.pets;
		newArr[i].infoSmoking = ownerArr[i].info.smoking;
		newArr[i].infoOvernight = ownerArr[i].info.overnight;
	}

	$w('#repeater1').data = newArr;
	$w('#repeater1').show();
}