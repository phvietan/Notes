require('dotenv').config()
const PORT = process.env.PORT || 8000;

const express = require('express');
const bodyParser = require("body-parser");

const app = express();
app.use(express.static('public'));

//Here we are configuring express to use body-parser as middle-ware.
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

function logJsonObject(obj) {
    const arrKeyVal = Object.entries(obj);
    if (arrKeyVal.length == 0) {
        console.log("{}");
        return;
    }
    arrKeyVal.forEach(val => {
        const key = val[0];
        const value = val[1];
        console.log(`"${key}": "${value}"`);
    });
}

app.use((req, _, next) => {
    console.log(`From ip ${req.ip}`);
    console.log(`Receive ${req.method} request at: ${req.url}`);

    console.log("======================");
    console.log("======================");
    console.log("Receive headers");
    logJsonObject(req.headers);

    console.log("======================");
    console.log("======================");
    console.log("Receive body");
    logJsonObject(req.body);

    console.log("------------------------------------------------------------------------------------------------")
    console.log("------------------------------------------------------------------------------------------------")
    next();
});

const server = app.listen(PORT, function () {
   const host = server.address().address;
   const port = server.address().port;
   console.log("App listening at http://%s:%s", host, port);
})
