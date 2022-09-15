#!/usr/bin/node
const { get } = require('axios');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

get(url)
  .then(({ data: { characters } }) => {
    characters.forEach(character => {
      get(character)
        .then(({ data: { name } }) => console.log(name));
    });
  })
  .catch((err) => console.error(err));
