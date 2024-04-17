#!/usr/bin/node

const request = require('request');

// Get the Movie ID from command-line arguments
const movieId = process.argv[2];

// Construct the URL for fetching characters from the Star Wars API
const url = `https://swapi.dev/api/films/${movieId}/`;

// Make a GET request to the API
request(url, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
    } else if (response.statusCode !== 200) {
        console.error('Status:', response.statusCode);
    } else {
        const filmData = JSON.parse(body);
        console.log('Characters:');
        filmData.characters.forEach((characterUrl) => {
            // Make a GET request for each character URL
            request(characterUrl, (charError, charResponse, charBody) => {
                if (charError) {
                    console.error('Error:', charError);
                } else if (charResponse.statusCode !== 200) {
                    console.error('Status:', charResponse.statusCode);
                } else {
                    const characterData = JSON.parse(charBody);
                    console.log(characterData.name);
                }
            });
        });
    }
});

