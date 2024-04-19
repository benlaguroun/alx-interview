#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let people = [];
const names = [];

const requestCharacters = () => {
  return new Promise((resolve, reject) => {
    request(filmEndPoint, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        reject('Error: ' + err + ' | StatusCode: ' + res.statusCode);
      } else {
        const jsonBody = JSON.parse(body);
        people = jsonBody.characters;
        resolve();
      }
    });
  });
};

const requestNames = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        reject('Error: ' + err + ' | StatusCode: ' + res.statusCode);
      } else {
        const jsonBody = JSON.parse(body);
        names.push(jsonBody.name);
        resolve();
      }
    });
  });
};

const getCharNames = async () => {
  try {
    await requestCharacters();
    if (people.length > 0) {
      for (const p of people) {
        await requestNames(p);
      }
      console.log(names.join('\n'));
    } else {
      console.error('Error: Got no Characters for some reason');
    }
  } catch (error) {
    console.error(error);
  }
};

getCharNames();

