#!/usr/bin/node
const axios = require('axios');
const result = {};

axios
  .get(process.argv[2])
  .then(res => {
    // let counter = 0;
    for (let j = 0; j < res.data.length; j++) {
      // console.log(res.data[j])
      // console.log(typeof res.data[j]['completed'])
      if (res.data[j].completed === Boolean('true')) {
        // console.log("ingreso")
        if (result[res.data[j].userId] !== undefined) {
          result[res.data[j].userId] += 1;
        } else {
          result[res.data[j].userId] = 1;
        }
      }
    }
    console.log(result);
  })
  .catch(error => {
    console.log(`code: ${error}`);
  });
