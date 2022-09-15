#!/usr/bin/node
/**
* Request status code
*/

const axios = require('axios').default;
const url = process.argv[2];

axios.get(url)
  .then(({ data }) => {
    // handle success
    const films = data.results;
    let count = 0;
    films.forEach(res => {
      res.characters.forEach(link => {
        if (link.includes('18')) count++;
      });
    });
    console.log(count);
  })
  .catch((error) => console.log(error));
