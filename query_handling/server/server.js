//  Author : Sam Mouradian
//  Name : server 
//  Description : The server module creates JSON oobjects from  
//  queries.csv to send to the GCS from a .csv to send to the GCS

const csvFilePath='queries.csv'
const csv=require('csvtojson')
var express = require('express'), bodyParser = require('body-parser');
var app = express();
var js = [];
var index = 0;
var imageLocation;
var js2send = {};
app.use(bodyParser.json());
//var csvEncoding = {encoding: 'utf16le'};
//global.index = 0;
//var timer = Math.floor(Math.random() * 5000) + 2000;


////  READS ALL DATA FROM CSV FILE AND CREATES JSON FOR EACH COLUMN
////  Implement sleep timer that sends a JSON row for a random sleep time
////  -------------------------------------------------------------------
csv()
.fromFile(csvFilePath, csvEncoding)
//.on("end_parsed",function(jsonArrayObj){
  .on('json',(jsonObj,rowIndex)=>{
    //console.log(js[index]);
  //when parse finished, result is a JSON obj for each column in .csv
  //console.log(jsonArrayObj);
  js.push(jsonObj);
  //console.log('.csv has been read...')
  //console.log(js + '\n');
})
.on('done',(error)=>{
    console.log('queries loaded into buffer... \n')
})

////  Reads 'FILENAME' from current query object and
////  sends Detected image to the '/img' route on the server
////  ---------------------------------------------------------
app.post('/img', function(req, res){
  imageLocation = js[index]["FILENAME"];
  res.status(200).sendFile(__dirname + "/detec_imgs" + "/" + imageLocation);
  console.log('img sent...');
})

////  Upon 'POST' request from GCS, 
////  send JSON to '/query' route on the server
////  ---------------------------------------------------------
app.post('/query', function(req, res){
  console.log('query requested...');
  console.log(js[index]);
  imageLocation = js[index]["FILENAME"];
  js2send = {
    "status": true,
    "query" : js[index],
    "image" : (__dirname + "/detec_imgs" + "/" + imageLocation),
    "sound" : "bleh bleh bleh"
  }
  console.log(imageLocation);
  if (index < js.length){
    res.status(200).send(js2send);
    res.sendFile
    console.log('query sent...');
    index++;
  }
  else{
    res.status(200).send('{status : false}');
    console.log('no more queries to send...');
  }
  //res.status(200).send(js[index]);
  console.log(req.body);
})
  .on('done',(error)=>{
    console.log('no more queries to send... \n');
  })
console.log('All Queries have been sent...');

//// Listen to request from GCS on port 9999
////---------------------------------------------------------
app.listen(9999, function() {
  console.log(__dirname);
  console.log('listening on port 3001')
})
