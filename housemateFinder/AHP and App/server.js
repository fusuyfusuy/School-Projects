const Express = require("express");
const BodyParser = require("body-parser");
const Helmet = require('helmet');
const MongoClient = require("mongodb").MongoClient;
const ObjectId = require("mongodb").ObjectID;
const CONNECTION_URL = "";
const DATABASE_NAME = "flatmate";
const homeAHPFunc = require("./homeAHP local").homeAHP;
const ownerAHPFunc = require("./homeownerAHP").ownerAHP;
 
var app = Express();
app.use(BodyParser.json());
app.use(BodyParser.urlencoded({ extended: true }));
app.use(Helmet());
var database, collectionPersons, collectionHomes;
 
app.listen(5000, () => {
    MongoClient.connect(CONNECTION_URL, { useNewUrlParser: true }, (error, client) => {
        if(error) {
            throw error;
        }
        database = client.db(DATABASE_NAME);
        collectionPersons = database.collection("persons");
        collectionHomes = database.collection("homes");
        console.log("Connected to `" + DATABASE_NAME + "`!");
    });
});

 app.get("/homes/:id", (request, response) => {
    collectionHomes.find({"_id": request.params.id }).toArray((error, result) => {
        if(error) {
            return response.status(500).send(error);
        }
        response.send(result);
    });
});
app.get("/homes/", (request, response) => {
    collectionHomes.find({ }).toArray((error, result) => {
        if(error) {
            return response.status(500).send(error);
        }
        response.send(result);
    });
});
app.get("/persons/:id", (request, response) => {
    collectionPersons.find({"_id": request.params.id }).toArray((error, result) => {
        if(error) {
            return response.status(500).send(error);
        }
        response.send(result);
    });
});
app.get("/persons/", (request, response) => {
    collectionPersons.find({ }).toArray((error, result) => {
        if(error) {
            return response.status(500).send(error);
        }
        response.send(result);
    });
});
app.post("/persons/", (request, response) => {
    response.send("POST RECIEVED");
    console.log(request.body);
    let locationArr = request.body.location;
    // locationArr=locationArr.split(",");
    // console.log(locationArr);
});
app.post("/api/homes/", (req, res) => {
    console.log(req.body);
    let filterArr = [0,1,2,3];
    filterArr[0]=req.body.rentRange;
    filterArr[1]=req.body.location;
    filterArr[2]=req.body.petFilter;
    filterArr[3]=req.body.smokingFilter;
    let priorityArr = req.body.priorityArr;
    console.log(filterArr, priorityArr);
    try {
        let homes = collectionHomes.find({}).toArray((error, result)=>{
            if(error){
                console.log('err err err err');
                return res.status(500).send(error);
            }
            console.log('database connected');
            try {
            	let functionRes = homeAHPFunc(filterArr, priorityArr, result); 
            	if(functionRes==-1) res.status(500).send('consistency error');
            	else res.send(functionRes);
	    }
            catch(error){res.status(500).send(error);}
        });  
        
    } catch (error) {
        res.status(500).send(error);
    }
});
app.post("/api/owners/", (req, res) => {
    // console.log(req.body);
    let filterArr = [0,1,2,3,4];
    filterArr[0]=req.body.overnightFilter;
    filterArr[1]=req.body.genderFilterSex;
    filterArr[2]=req.body.genderFilterAppeal;
    filterArr[3]=req.body.petFilter;
    filterArr[4]=req.body.smokingFilter
    let priorityArr = req.body.priorityArr;
    
    try {
        let homes = collectionHomes.find({}).toArray((error, result)=>{
            if(error){
                console.log('err err err err');
                return res.status(500).send(error);
            }
            console.log('database connected');
            
            let functionRes = ownerAHPFunc(filterArr, priorityArr, result); 
            if(functionRes==-1) res.status(500).send('consistency error');
            else res.send(functionRes);
        });  
        
    } catch (error) {
        res.status(500).send(error);
    }
})
