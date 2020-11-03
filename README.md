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

### Question by ID

https://jeopardy-rest-api.herokuapp.com/api/v1/jeopardy/questions/id=123

GET function that returns a Jeopardy question and answer based on ID. All questions have a numeric ID, starting at 1. The question order is by show air-date, but within each show, questions are grouped by category, not the order in which questions were given in the show.
