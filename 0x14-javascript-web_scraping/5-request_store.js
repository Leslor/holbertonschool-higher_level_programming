#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');

axios
  .get(process.argv[2])
  .then(res => {
    fs.writeFile(process.argv[3], res.data, 'utf8', err => {
      if (err) {
        console.error(err);
      }
    });
  })
  .catch(error => {
    console.log(`code: ${error}`);
  });
