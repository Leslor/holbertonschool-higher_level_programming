#!/usr/bin/node
const axios = require('axios');

axios
  .get(process.argv[2])
  .then(res => {
    let counter = 0;
    for (let i = 0; i < res.data.count; ++i) {
      const listas = res.data.results[i].characters;
      // console.log(listas)
      for (let j = 0; j < listas.length; ++j) {
        const id = listas[j].split('/')[5];
        // console.log(id);
        if (id === '18') {
          counter += 1;
        }
      }
    }
    console.log(counter);
  })
  .catch(error => {
    console.log(`code: ${error}`);
  });
