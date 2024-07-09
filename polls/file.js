
// var http = require('http');
// http.createServer(function (req, res) {
//   res.writeHead(200, {'Content-Type': 'text/html'});
//   res.write(req.url);
//   res.end();
// }).listen(8080);



// var http = require('http');
// var url = require('url');

// http.createServer(function (req, res) {
//   res.writeHead(200, {'Content-Type': 'text/html'});
//   var q = url.parse(req.url, true).query;
//   var txt = q.firstname + " " + q.lastname;
//   res.end(txt);
// }).listen(8080);


// var http = require('http');
// var fs = require('fs');
// http.createServer(function (req, res) {
//   fs.readFile('my1.html', function(err, data) {
//     res.writeHead(200, {'Content-Type': 'text/html'});
//     res.write(data);
//     return res.end();
//   });
// }).listen(8080);


//-------------------------------------------
//append-->to create a new file

// var fs = require('fs');
// fs.appendFile('mynewfile1.txt', 'Hello content!', function (err) {
//   if (err) throw err;
//   console.log('Saved!');
// });

//------------------------------------------------------



//w->it open the file if exists and we can edit else it will create new file

// var fs = require('fs');

// fs.open('mynewfile1.txt', 'w', function (err, file) {
//   if (err) throw err;
//   console.log('Saved!!');
// });


//delete-->unlink
// var fs = require('fs');

// fs.unlink('mynewfile1.txt', function (err) {
//   if (err) throw err;
//   console.log('File deleted!');
// });


//rename

// var fs = require('fs');

// fs.rename('mynewfile1.txt', 'myfil2.txt', function (err) {
//   if (err) throw err;
//   console.log('File Renamed!');
// });


//URL

// var url = require('url');
// var adr = 'http://localhost:8080/default.htm?year=2017&month=february';
// var q = url.parse(adr, true);

// console.log(q.host); //returns 'localhost:8080'
// console.log(q.pathname); //returns '/default.htm'
// console.log(q.search); //returns '?year=2017&month=february'

// var qdata = q.query; //returns an object: { year: 2017, month: 'february' }
// console.log(qdata.month); //returns 'february'



// var http = require('http');
// var url = require('url');
// var fs = require('fs');

// http.createServer(function (req, res) {
//   var q = url.parse(req.url, true);
//   var filename = "." + q.pathname;
//   fs.readFile(filename, function(err, data) {
//     if (err) {
//       res.writeHead(404, {'Content-Type': 'text/html'});
//       return res.end("404 Not Found");
//     } 
//     res.writeHead(200, {'Content-Type': 'text/html'});
//     res.write(data);
//     return res.end();
//   });
// }).listen(8080);


// var http = require('http');
// //var uc = require('upper-case');
// http.createServer(function (req, res) {
//   res.writeHead(200, {'Content-Type': 'text/html'});
//   var str1="Hello Mansi"
//   res.write(str1.toUpperCase());
//   res.end();
// }).listen(8080);

// var fs = require('fs');
// var rs = fs.createReadStream('./try1.txt');
// rs.on('open', function () {
//   console.log('The file is open');
// });

//---------------------------------------------------------------------
//EVENTS


// var events = require('events');
// var eventEmitter = new events.EventEmitter();

// //Create an event handler:
// var myEventHandler = function () {
//   console.log('Heyyaa!! Its Mansi Agarwal');
// }

// //Assign the event handler to an event:
// eventEmitter.on('scream', myEventHandler);

// //Fire the 'scream' event:
// eventEmitter.emit('scream');


//????????????????????????????????

// var http = require('http');
// var formidable = require('formidable');
// var fs = require('fs');

// http.createServer(function (req, res) {
//   if (req.url == '/fileupload') {
//     var form = new formidable.IncomingForm();
//     form.parse(req, function (err, fields, files) {
//       var oldpath = files.filetoupload.path;
//       var newpath = "C:\Users\MansiAgarwal\Desktop\ok" + files.filetoupload.originalFilename;
//       fs.rename(oldpath, newpath, function (err) {
//         if (err) throw err;
//         res.write('File uploaded and moved!');
//         res.end();
//       });
//  });
//   } else {
//     res.writeHead(200, {'Content-Type': 'text/html'});
//     res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
//     res.write('<input type="file" name="filetoupload"><br>');
//     res.write('<input type="submit">');
//     res.write('</form>');
//     return res.end();
//   }
// }).listen(8080);

//????????????????????????????????????????????????????

// var mysql = require('mysql');

// var con = mysql.createConnection({
//   host: "localhost",
//   user: "root",
//   password: "mansi123"
// });

// con.connect(function(err) {
//   if (err) throw err;
//   console.log("Connected!");
// });


// var mysql = require('mysql');

// var con = mysql.createConnection({
//   host: "localhost", // Change this to the correct host name if necessary
//   user: "root",      // MySQL username
//   password: "",      // MySQL password (if set)
//   port: 3306         // MySQL port (default is 3306)
// });

// con.connect(function(err) {
//   if (err) {
//     console.error('Error connecting to database:', err.stack);
//     return;
//   }
//   console.log("Connected to MySQL server!");
// });



const express = require('express');
const app = express();

// Define routes and middleware here
// ...

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});