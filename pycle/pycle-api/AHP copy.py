import csv
import re

globalPriority = []
globalTechPriority = []
globalFlag = 0

def runAHP():
    global globalFlag
    global globalPriority
    global globalTechPriority

    userPriceMin = 300
    userPriceMax = 600
    # userType = 'Mountain',# u
    # userPrice = int((userPriceMin+userPriceMax)/2)
    userPrice = 1999
    userHeight = 220
    def userFrameFinder(height):
        if(height < 148):
            return 'XXS'
        elif(height <= 158):
            return 'XS'
        elif(height <= 168):
            return 'S'
        elif(height <= 178):
            return 'M'
        elif(height <= 185):
            return 'L'
        elif(height <= 193):
            return 'XL'
        elif(height > 193):
            return 'XXL'
    userFrame = userFrameFinder(int(userHeight))
    userTypeWeights = [5, 3, 2]
    # mountain, hybrid, road
   
    priorities = {
        'priceWeight': 1,
        'priceType': 1,
        'priceFrame': 1,
        'priceTech': 1,
        'weightType': 1,
        'weightFrame': 1,
        'weightTech': 1,
        'typeFrame': 1,
        'typeTech': 1,
        'frameTech': 1
    }
    
    techPriorities = {
        'brakeTransmission': 1,
        'brakeSuspension': 1,
        'transmissionSuspension': 1
    }
    
    priorityMatrix = [ # price         weight                       type                      frame                      tech
        [ 1,                           priorities['priceWeight'],   priorities['priceType'],   priorities['priceFrame'],  priorities['priceTech']], # price
        [ 1/priorities['priceWeight'], 1,                           priorities['weightType'],  priorities['weightFrame'], priorities['weightTech']], # weight
        [ 1/priorities['priceType'],   1/priorities['weightType'],  1,                         priorities['typeFrame'],   priorities['typeTech']], # type
        [ 1/priorities['priceFrame'],  1/priorities['weightFrame'], 1/priorities['typeFrame'], 1,                         priorities['frameTech']], # frame
        [ 1/priorities['priceTech'],   1/priorities['weightTech'],  1/priorities['typeTech'],  1/priorities['frameTech'], 1] # tech
    ]
    
    techMatrix = [ #brake                       transmission                                suspension
        [1,                                     techPriorities['brakeTransmission'],        techPriorities['brakeSuspension'] ], # brake
        [1/techPriorities['brakeTransmission'], 1,                                          techPriorities['transmissionSuspension']], # transmission
        [1/techPriorities['brakeSuspension'],   1/techPriorities['transmissionSuspension'], 1] # suspension
    ]
    

    typeMatrix = [
        [1, userTypeWeights[0]/userTypeWeights[1], userTypeWeights[0]/userTypeWeights[2]],
        [userTypeWeights[1]/userTypeWeights[0], 1, userTypeWeights[1]/userTypeWeights[2]],
        [userTypeWeights[2]/userTypeWeights[0], userTypeWeights[2]/userTypeWeights[1], 1]
    ]

    def consistencyCheck(matrix):
        matrixSum = []
        for i in range(len(matrix)):
            sum = 0
            for j in range(len(matrix)):
                sum += matrix[j][i]
            matrixSum.append(sum)
        standardizedMatrix = matrix.copy()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                standardizedMatrix[i][j] = matrix[i][j]/matrixSum[j]
        priorityVector = []
        for i in standardizedMatrix:
            sum = 0
            for j in i:
                sum += j
            priorityVector.append(sum/len(matrix))
        global globalFlag
        global globalPriority
        global globalTechPriority
        if(globalFlag == 0):
            global globalPriority
            globalPriority = priorityVector.copy()
            globalFlag = 1
        elif(globalFlag == 1):
            global globalTechPriority
            globalTechPriority = priorityVector.copy()
            globalFlag = 2
        vectorCheck = 0
        for i in priorityVector:
            vectorCheck += i
        if(round(vectorCheck, 2) != 1):
            print('ERROR PAIR-WISE PRIORITY VECTOR CALCULATION (NOT EQUAL 1) == ', vectorCheck)
            exit()
        lambdaMax = 0
        for i in range(len(matrixSum)):
            lambdaMax += matrixSum[i]*priorityVector[i]
        CI = (lambdaMax - len(matrixSum)) / (len(matrixSum) - 1)
        # CR = CI / 0.9
        if(CI<0.1):
            return bool(True)
        else:
            return bool(False)
    
    if(not consistencyCheck(priorityMatrix)): # ana ahp check, techten once yapilmali ONEMLI cunku priority vectorler fonksiyon calisma sirasina gore geliyor
        print('It is NOT CONSISTENT -- Priorities')
        exit()
    if(not consistencyCheck(techMatrix)):
        print('It is NOT CONSISTENT -- Technical')
        exit()
    
    def criteriaAHP(matrix):
        matrixSum = []
        for i in range(len(matrix)):
            sum = 0
            for j in range(len(matrix)):
                sum += matrix[j][i]
            matrixSum.append(sum)
        standardizedMatrix = matrix.copy()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                standardizedMatrix[i][j] = matrix[i][j]/matrixSum[j]
        priorityVector = []
        for i in standardizedMatrix:
            sum = 0
            for j in i:
                sum += j
            priorityVector.append(sum/len(standardizedMatrix))
        check = 0
        for i in priorityVector:
            check += i
        if(round(check, 2) == 1):
            return priorityVector
        else:
            print('CRITERIA AHP ERROR')
            return priorityVector
    
    def inchConverter(inch):
        if(float(inch) <= 12):
            return 'XXS'
        if(float(inch) <= 14):
            return 'XS'
        elif(float(inch) <= 16):
            return 'S'
        elif(float(inch) <= 18):
            return 'M'
        elif(float(inch) <= 20):
            return 'L'
        elif(float(inch) <= 22):
            return 'XL'
        elif(float(inch) > 22):
            return 'XXL'
        else:
            raise Exception('inch converter error ==> ',inch)
    
    def frameFixer(frame):
        if(frame == '------'):
            return(frame)
        inches = re.findall("\d\d.\d\d\"|\d\d.\d\"|\d\d\"", frame)
        returnAr = []
        if(inches):
            for inch in inches:
                returnAr.append(inchConverter(float(inch.replace("\"",""))))
        else:
            categories = frame.split(",")
            for i in categories:
                returnAr.append(i.strip())
        return returnAr
    
    frametoNumber = {
        'XXS': 0,
        'XS': 1,
        'S': 2,
        'M': 3,
        'L': 4,
        'XL': 5,
        'XXL': 6
    }
   
    def frameSearcher(frameAr, search):
        min = 100
        search = frametoNumber[search]
        for i in frameAr:
            if(abs(frametoNumber[i]-search)<min):
                min = abs(frametoNumber[i]-search)
                if(min==0):
                    return min
        return min
    
    def frameCalculate(left, right, userFrame):
        leftMin = frameSearcher(left, userFrame) + 1
        rightMin = frameSearcher(right, userFrame) + 1
        leftMin = 7 - leftMin
        rightMin = 7 - rightMin
        return(leftMin / rightMin)
    
    # data csvlerden aliniyor. bicycles. hybrid-mountain-road+Scores
    reader = csv.DictReader(open('/home/ubuntu/code/flaskTutorial/project/main.csv', "r", errors='ignore'), delimiter=';')
    bicycles = []
    mainData = next(reader, bool(False))
    while(mainData):
        bicycles.append(mainData)
        mainData = next(reader, bool(False))
    
    reader = csv.DictReader(open('/home/ubuntu/code/flaskTutorial/project/hybrid.csv', "r", errors='ignore'), delimiter=';')
    hybridScores = []
    score = next(reader, bool(False))
    while(score):
        hybridScores.append(score)
        score = next(reader, bool(False))
    
    reader = csv.DictReader(open('/home/ubuntu/code/flaskTutorial/project/mountain.csv', "r", errors='ignore'), delimiter=';')
    mountainScores = []
    score = next(reader, bool(False))
    while(score):
        mountainScores.append(score)
        score = next(reader, bool(False))
    
    reader = csv.DictReader(open('/home/ubuntu/code/flaskTutorial/project/road.csv', "r", errors='ignore'), delimiter=';')
    roadScores = []
    score = next(reader, bool(False))
    while(score):
        roadScores.append(score)
        score = next(reader, bool(False))

    reader = csv.DictReader(open('/home/ubuntu/code/flaskTutorial/project/bicyclesurlsave.csv', "r", errors='ignore'), delimiter=',')
    urlList = []
    score = next(reader, bool(False))
    while(score):
        urlList.append(score)
        score = next(reader, bool(False))
    

    def techScoreFinder(type, pieceType, pieceName):
        scoreTable = []
        if(type == 'Mountain'):
            scoreTable = mountainScores
        elif(type == 'Hybrid - City'):
            scoreTable = hybridScores
        elif(type == 'Road'):
            scoreTable = roadScores
        else:
            print('ERROR ON techScoreFinder. Type is ==> ', type)
            exit()
        foundFlag = 0
        if(pieceName == '------' or pieceName == 'N/A' or pieceName == 'n/a'): # data yoksa kac puan verilsin?
            return 2
        if(pieceType == 'transmission'):
            for i in scoreTable:
                if i['transmission'].lower() == pieceName.lower():
                    foundFlag = 1
                    return i['tScore']
        elif(pieceType == 'suspension'):
            if(type == 'Road'):             # road tipinda data hatali. 4 olmasi lazimken 1 girilmis.
                return 4
            for i in scoreTable:
                if i['suspension'].lower() == pieceName.lower():
                    foundFlag = 1
                    return i['sScore']
        elif(pieceType == 'brake'):
            for i in scoreTable:
                if i['brake'].lower() == pieceName.lower():
                    foundFlag = 1
                    return i['bScore']
        else:
            print('ERROR ON techScoreFinder. pieceType is ==> ', pieceType, '  ////   foundFlag is ==>',foundFlag)
            exit()
        if(foundFlag == 0):
            print('ERROR ON techScoreFinder. type ==>  ',type , '////  pieceType ==> ', pieceType, '  //// pieceName ==>  ', pieceName)
            exit()
    
    # tek tek kiyaslicaz bakalim
    typeCompare = []
    priceCompare = []
    weightCompare = []
    weightSum = 0
    frameCompare = []
    techCompare = []
    brakeCompare = []
    transmissionCompare = []
    suspensionCompare = []
    for i in range(len(bicycles)):
        typeCompare.append([])
        priceCompare.append([])
        frameCompare.append([])
        brakeCompare.append([])
        transmissionCompare.append([])
        suspensionCompare.append([])
        for j in range(len(bicycles)):
            leftType = bicycles[i]['Type']
            rightType = bicycles[j]['Type']
            leftTypeIndex = 0
            rightTypeIndex = 0
            if(leftType == 'Mountain'):
                leftTypeIndex = 0
            elif(leftType == 'Hybrid - City'):
                leftTypeIndex = 1
            elif(leftType == 'Road'):
                leftTypeIndex = 2
            if(rightType == 'Mountain'):
                rightTypeIndex = 0
            elif(rightType == 'Hybrid - City'):
                rightTypeIndex = 1
            elif(rightType == 'Road'):
                rightTypeIndex = 2
            typeCompare[i].append(typeMatrix[leftTypeIndex][rightTypeIndex])
            
            
            # PRICE
            leftPrice = float(bicycles[i]['Price'].replace(',','.'))
            rightPrice = float(bicycles[j]['Price'].replace(',','.'))
            leftPriceDiff = (abs(leftPrice - userPrice) / 300) + 1
            # burda int alinabilir belki
            rightPriceDiff = (abs(rightPrice - userPrice) / 300) + 1
            priceCompare[i].append(rightPriceDiff/leftPriceDiff)
            
            
            
            leftFrame = frameFixer(bicycles[i]['Frame Size'])
            rightFrame = frameFixer(bicycles[j]['Frame Size'])
            if(leftFrame == '------'):
                if(rightFrame == '------'):
                    frameCompare[i].append(1)
                else:
                    frameCompare[i].append(1/5)
            elif(rightFrame == '------'):
                if(leftFrame == '------'):
                    frameCompare[i].append(1)
                else:
                    frameCompare[i].append(5)
            else:
                frameCompare[i].append(frameCalculate(leftFrame, rightFrame, userFrame))
            
            
            # teknik parcalar. emin'in puanlamalarini direkt birbirine boluyorum. fena degil ama daha iyi olabilir.
            leftBrake = bicycles[i]['Brakes']
            rightBrake = bicycles[j]['Brakes']
            leftScore = int(techScoreFinder(leftType, 'brake', leftBrake))
            rightScore = int(techScoreFinder(rightType, 'brake', rightBrake))
            if(leftScore > rightScore):
                brakeCompare[i].append(leftScore-rightScore)
            elif(leftScore == rightScore):
                brakeCompare[i].append(1)
            elif(leftScore < rightScore):
                brakeCompare[i].append(1/(rightScore-leftScore))
            
            
            leftSuspension = bicycles[i]['Fork']
            rightSuspension = bicycles[j]['Fork']
            leftScore = int(techScoreFinder(leftType, 'suspension', leftSuspension))
            rightScore = int(techScoreFinder(rightType, 'suspension', rightSuspension))         
            if(leftScore > rightScore):
                suspensionCompare[i].append(leftScore-rightScore)
            elif(leftScore == rightScore):
                suspensionCompare[i].append(1)
            elif(leftScore < rightScore):
                suspensionCompare[i].append(1/(rightScore-leftScore))
            
            
            
            leftTransmission = bicycles[i]['Rear Derailleur']
            rightTransmission = bicycles[j]['Rear Derailleur']              
            leftSpeed = bicycles[i]['Speed']
            rightSpeed = bicycles[j]['Speed']
            leftScore = int(techScoreFinder(leftType, 'transmission', leftTransmission))
            rightScore = int(techScoreFinder(rightType, 'transmission', rightTransmission))
            if(leftScore > rightScore):
                transmissionCompare[i].append(leftScore-rightScore)
            elif(leftScore == rightScore):
                transmissionCompare[i].append(1)
            elif(leftScore < rightScore):
                transmissionCompare[i].append(1/(rightScore-leftScore))
        
        
        # weight isleri
        bicycle = bicycles[i]
        bicycleWeight = bicycle['Weight ']
        if(re.search("^\d+.\d+",bicycles[i]['Weight '])):
            bicycleWeight = float(re.search("^\d+.\d+",bicycles[i]['Weight ']).group().replace(',','.'))
        else: # weight olmayanlara mountain 15, road 10, hybrid 18
            if(bicycle['Type'] == 'Mountain'):
                bicycleWeight = 17
            elif(bicycle['Type'] == 'Road'):
                bicycleWeight = 12
            elif(bicycle['Type'] == 'Hybrid - City'):
                bicycleWeight = 20
            else:
                bicycleWeight = 16
        weightCompare.append(bicycleWeight)
        weightSum += bicycleWeight



    # bitti. kriter ici kiyas matrisleri hesaplanip agirliklariyla carpilsin
    for i in range(len(weightCompare)):
        weightCompare[i] = 1.0-(weightCompare[i]/weightSum)


    brakeCompareAvg = criteriaAHP(brakeCompare)
    transmissionCompareAvg = criteriaAHP(transmissionCompare)
    suspensionCompareAvg = criteriaAHP(suspensionCompare)
    priceCompareAvg = criteriaAHP(priceCompare)
    typeCompareAvg = criteriaAHP(typeCompare)
    weightCompareAvg = weightCompare
    frameCompareAvg = criteriaAHP(frameCompare)
    
    
    techCompareAvg = []
    for i in range(len(brakeCompareAvg)):
        techCompareAvg.append((brakeCompareAvg[i]*globalTechPriority[0]) + (transmissionCompareAvg[i]*globalTechPriority[1]) + (suspensionCompareAvg[i]*globalTechPriority[2]))
    
    
    for i in range(len(bicycles)):
        priceCompareAvg[i] = priceCompareAvg[i]*globalPriority[0]
        weightCompareAvg[i] = weightCompareAvg[i]*globalPriority[1]
        typeCompareAvg[i] = typeCompareAvg[i]*globalPriority[2]
        frameCompareAvg[i] = frameCompareAvg[i]*globalPriority[3]
        techCompareAvg[i] = techCompareAvg[i]*globalPriority[4]
    
    endScores = []
    for i in range(len(bicycles)):
        endScores.append(priceCompareAvg[i]+weightCompareAvg[i]+typeCompareAvg[i]+frameCompareAvg[i]+techCompareAvg[i])
    
    
    # checksum = 0,
    # for i in endScores:,
    #     checksum+=i,
    # print(round(checksum,2), ' -- ', checksum)
    
    for i in range(len(bicycles)):
        bicycles[i]['Score'] = endScores[i]
        bicycles[i]['Price Score'] = priceCompareAvg[i]
        bicycles[i]['Weight Score'] = weightCompareAvg[i]
        bicycles[i]['Type Score'] = typeCompareAvg[i]
        bicycles[i]['Frame Size Score'] = frameCompareAvg[i]
        bicycles[i]['Technical Score'] = techCompareAvg[i]
    
    endList = sorted(bicycles, key=lambda i: i['Score'],reverse=True)

    returnList = []
    for i in range(5):
        returnList.append(endList[i])
    
    # print(urlList[1])

    for i in returnList:
        bikeUrl = ''
        for j in urlList:
            if(j['title']==(i['Brand']+' '+i['Model'])):
                bikeUrl = j['url']
                break
        i['url'] = bikeUrl

    for i in returnList:
        print(i)
        print("\n")
    return returnList
    # print(f'User Input:\nType: {userTypeWeights}, Price: {userPrice},  Frame: {userFrame}\n\n')
    # j = 0
    # for i in bicycles:
    #     print(i['Brand'],', ', i['Model'])
    #     print(i['Type'],'  //  ', typeCompareAvg[j])
    #     print(i['Price'],'  //  ', priceCompareAvg[j])
    #     print(i['Weight '], '  //  ', weightCompareAvg[j])
    #     try:
    #         print(frameSearcher(frameFixer(i['Frame Size']), userFrame), '  //  ', frameCompareAvg[j])
    #     except:
    #         print(i['Frame Size'],'  //  ', frameCompareAvg[j])
    #     print('\n\n')
    #     j+=1

    
    # for i in range(10):
    #     print('Brand == ', endList[i]['Brand'],'Model == ', endList[i]['Model'],'   ///   ','Score == ', endList[i]['Score'])


runAHP()
