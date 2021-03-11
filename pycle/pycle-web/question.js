
function updateTable(changedCell){
    left = changedCell.cellIndex
    right = changedCell.parentNode.rowIndex
    me = parseFloat(changedCell.querySelector("input").value)
    document.getElementById("priorityTable").rows[left].cells[right].querySelector("input").value = (1/me).toPrecision(2)
}
function matrixify(array){
    let matrix
    if(array.length==10){
        matrix = [
        [1,           array[0],    array[1],   array[2],   array[3]],
        [1/array[0], 1,            array[4],   array[5],   array[6]],
        [1/array[1], 1/array[4],  1,           array[7],   array[8]],
        [1/array[2], 1/array[5],  1/array[7], 1,           array[9]],
        [1/array[3], 1/array[6],  1/array[8], 1/array[9], 1]
        ]
    }
    else if(array.length==3){
        matrix = [
        [1,           array[0],   array[1]],
        [1/array[0], 1,           array[2]],
        [1/array[1], 1/array[2], 1]
        ]
    }
    else {
        console.log("matrixify error ---",array)
        console.log("matrixify error ---", array.length)
        return false
    }
    return matrix
}
function consistencyCheck(matrix){
    let l = matrix.length
    let matrixSums = []
    for(let i = 0; i<l; i++){
        let sum = 0
        for(let j =0; j<l;j++){
            sum += matrix[j][i]
        }
        matrixSums.push(sum)
    }
    let standardizedMatrix = []
    for(let i = 0; i<l; i++){
        standardizedMatrix.push([])
        for(let j = 0; j<l; j++){
            standardizedMatrix[i].push(matrix[i][j]/matrixSums[j])
        }
    }

    let averages = []
    for(let i = 0; i<l; i++){
        let sum = 0
        for(let j = 0; j<l; j++){
            sum+=standardizedMatrix[i][j]
        }
        averages.push(sum/l)
    }

    ax = []
    for(let i = 0; i<l;i++){
        let sum = 0
        for(let j = 0; j<l;j++){
            sum += matrix[i][j] * averages[j]
        }
        ax.push(sum)
    }
    let lambdaMax = 0
    let lambdaSum = 0
    for(let i = 0; i<l; i++){
        lambdaSum += ax[i]/averages[i]
    }
    lambdaMax = lambdaSum/l
    let CI = (lambdaMax-l)/(l-1)
    if(CI<0.1) return true
    else return false
}
function getInputs(){
    inputMaxPrice = parseFloat(document.getElementById("inputPriceMax").value)
    inputMinPrice = parseFloat(document.getElementById("inputPriceMin").value)
    if(isNaN(inputMaxPrice) || isNaN(inputMinPrice)){
        alert("Prices must be a number!")
        return false
    }
    else if(inputMaxPrice < 1 || inputMinPrice < 1){
        alert("Prices cannot be lower than 1!")
        return false
    }
    else if(inputMinPrice >= inputMaxPrice){
        alert("Maximum price must be bigger than minimum price!")
        return false
    }


    inputHeight = parseFloat(document.getElementById("inputHeight").value)
    if(isNaN(inputHeight)){
        alert("Height must be a number!")
        return false
    }
    else if(inputHeight < 1){
        alert("Height cannot be lower than 1!")
        return false
    }



    Q1 = document.getElementsByName("qTerrain")
    Q2 = document.getElementsByName("qRides")
    Q3 = document.getElementsByName("qExperience")
    A1 = -1
    A2 = -1
    A3 = -1
    check1 = 0
    check2 = 0
    check3 = 0
    for(let i = 0, l = Q1.length; i < l; i++){
        if(Q1[i].checked){
            A1 = i
            check1++
        }
        if(Q2[i].checked){
            A2 = i
            check2++
        }
        if(Q3[i].checked){
            A3 = i
            check3++
        }
    }
    if(check1==0 || check2==0 || check3==0){
        alert("Please answer all the questions!")
        return false
    }

    // mountain, hybrid, road
    inputTypeWeights = [5, 5, 5]
    switch(A1){
        case 0:
            inputTypeWeights[0] += 2
            inputTypeWeights[2] -= 1
            break;
        case 1:
            inputTypeWeights[1] +=1
            inputTypeWeights[2] +=2
            break;
        case 2:
            inputTypeWeights[0] += 1
            inputTypeWeights[1] += 2
            break;
    }
    switch(A2){
        case 0:
            inputTypeWeights[2] += 3
            break;
        case 1:
            inputTypeWeights[2] += 1
            break;
        case 2:
            break;
    }
    switch(A3){
        case 0:
            break;
        case 1:
            inputTypeWeights[2] -= 1
            break;
        case 2:
            inputTypeWeights[2] -= 2
            break;
    }

    // climb/transmisson. speed/brake. rough/suspension
    // sirasi = brake, transmission, suspension
    //'brakeTransmission': speedClimb,
    //'brakeSuspension': speedRough,
    //'transmissionSuspension': climbRough

    techPriorities = [0, 0, 0]
    climbSpeed = document.getElementById("climbSpeed").value
    roughSpeed = document.getElementById("roughSpeed").value
    climbRough = document.getElementById("climbRough").value
    function sliderToPriority(number){
        check = number - 9
        if(check < 0){
            return Math.abs(check)+1
        }
        else if(check == 0) return 1
        else return 1/(check+1)
    }
    techPriorities[0] = 1/sliderToPriority(climbSpeed)
    techPriorities[1] = 1/sliderToPriority(roughSpeed)
    techPriorities[2] = sliderToPriority(climbRough)

    techMatrix = matrixify(techPriorities)
    if(!techMatrix) {
        alert("Matrixify techMatrix wrong!")
        return false
    }
    techCheck = consistencyCheck(techMatrix)
    if(!techCheck){
        alert("Sliders are not consistent!")
        return false
    }
    priorityMatrix = []
    priorityTable = document.getElementById("priorityTable")
    let isnancheck = 0
    let ninecheck = 0
    let elevencheck = 0
    for(let i = 1, length = priorityTable.rows.length; i<length; i++){
        for(let j = 1; j<length; j++){
            if(priorityTable.rows[i].cells[j].querySelector("input").value == ''){
                alert("Comparison scores must be numbers")
                return false
            }
            else if(parseFloat(priorityTable.rows[i].cells[j].querySelector("input").value)>9){
                alert("Comparison scores cannot be larger than 9")
                return false
            }
            else if(parseFloat(priorityTable.rows[i].cells[j].querySelector("input").value)<0.11){
                alert("Comparison scores cannot be smaller than 1/9 (0.111111)")
                return false
            }
        }
    }

    for(let i = 1, length = priorityTable.rows.length; i<length; i++){
        for(let j = i+1, length2 = priorityTable.rows.length; j<length2; j++){
            priorityMatrix.push(parseFloat(priorityTable.rows[i].cells[j].querySelector("input").value))
        }
    }
    if(priorityMatrix.length != 10){
        console.log("ERROR PRIORITY MATRIX INPUT CALCULATION")
        return
    }
    priorityMatrix2 = matrixify(priorityMatrix)
    if(!priorityMatrix2){
        alert("Matrixify priorityMatrix wrong!")
        return false
    }
    priorityCheck = consistencyCheck(priorityMatrix2)
    if(!priorityCheck){
        alert("Comparison scores are not consistent!")
        return false
    }

    returnJson = {
        "inputPriceMin": inputMinPrice, 
        "inputPriceMax": inputMaxPrice, 
        "inputHeight": inputHeight, 
        "inputTypeWeights": inputTypeWeights, 
        "inputPriorities": priorityMatrix, 
        "inputTechPriorities" : techPriorities
    }
    return returnJson
}
function run(){
    toSend = getInputs()
    if(!toSend){
        return false
    }


    loader = document.querySelector(".loader")
    loader.style.display="block"
    
    resultDiv = document.getElementsByClassName("results")[0]
    resultDiv.textContent = ''
    console.log('sending this ', toSend)
    toSend = JSON.stringify(toSend)
    
    let results = 0
    chainurl = "https://www.chainreactioncycles.com"
    const xhr = new XMLHttpRequest()
    xhr.addEventListener('readystatechange', function() {
        if (this.readyState === this.DONE) {
            console.log('result is ', JSON.parse(this.responseText))
            results = JSON.parse(this.responseText)
            loader.style.display="none"
            resultDiv = document.querySelector(".results")
            for(i in results){
                let iplus = parseInt(i)+1
                newElement = document.createElement('p')
                newElement.innerHTML   = iplus +'.<br>'+
                                         'Brand:   '+results[i]['Brand'] + '<br>' + 
                                         'Model:   '+results[i]['Model'] + '<br>' +
                                         'Price:   '+results[i]['Price'] + '<br>' +
                                         'Type:    '+results[i]['Type']  + '<br>' +
                                         "<a href='"+chainurl+results[i]['url']+"' target='_blank'>Click to go bicycle page</a>"
                resultDiv.appendChild(newElement)
            }
        }
    })

    xhr.open('POST', 'http://127.0.0.1:5000/')
    xhr.setRequestHeader('content-type', 'application/json')

    xhr.send(toSend)
}

$(document).ready(function() {
    $('.image-link').magnificPopup({type:'image'});
  });