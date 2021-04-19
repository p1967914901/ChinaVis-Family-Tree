const express = require('express')
const fs = require('fs');
const child_process = require('child_process');
var bodyParser = require('body-parser'); 




const app = express()

app.get('/cluster', (req, res) => {
    const {cluster_number} = req.query
    console.log(cluster_number);
    // return ;
    child_process.exec('python E:\\virtualDesktop\\家谱\\app\\service\\kmeans.py ' + cluster_number, function (error, stdout, stderr) {
        // console.log('"object" :>> ', req.query);
        if (error) {
            console.log(error.stack);
            console.log('Error code: ' + error.code);
            console.log('Signal received: ' + error.signal);
            console.log("object")
            res.send({'success': false})
        }
        res.send(stdout)
    });
    
})


app.listen(3001, () => {
    console.log("http://localhost:3001");
})