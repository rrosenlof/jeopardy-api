# About

A simple API for returning random Jeopardy clues used in past games.

The dataset used contains games from 1984 to 2012. I've cleaned up some clues that wouldn't work with text: audio and video clues, Clue Crew clues, and more. Some cleaning still needed, mostly for words with accents or odd punctuation.

## Usage

The project is currently hosted with Heroku at https://jeopardy-rest-api.herokuapp.com/

### Random Question

https://jeopardy-rest-api.herokuapp.com/api/v1/jeopardy/questions/random

GET function that returns a random Jeopardy question and answer.

### Random Category

https://jeopardy-rest-api.herokuapp.com/api/v1/jeopardy/categories/random

GET function that returns a full, random Jeopardy category. This means 5 questions and answers. Question amounts are a bit off, since Daily Double values are recorded as the contestant's wager, not the original question value.
