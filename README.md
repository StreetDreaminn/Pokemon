# README #
## Pokemon ##

This is a project that retrieves specific information about a Pokemon using the Django RESTFUL API system. This project was created to take advantage of the benefits of sending data via the RESTFul architecture. The advantages of using a REST API is that it is scalable, flexible, portable, stateless, re-usable and cost effective.

Note that this is just for development purposes and is not fit for live production.

### Prerequisite ###
To install and run the API locally requires:
- The user to host the application on a CentOS 9 Linux distrubtion server.
- The user to have a running database with the necessary tables.

### How to install ###
To install and run the API locally:
1. Create a virtual environment called 'venv' by running the command `python -m venv venv`.
2. Make the run.sh file executable `chmod 777 CI/run.sh`.
3. Run the file 'run.sh'.

### How it works ###
The API hosts multiple different endpoints that can return data about a Pokemon from generation 1 to 6. In order for the user's request to be validated, the user will need to provide their request with a vaild JWT token. This can be obtained from the API by the user making a request to the api/token endpoint. The user will need to pass in their username and password in the body of their request in order for the request to be validated and for the API to return a token.

### Pokemon API Requests ###
See the API response below as an example of the type of data returned from the API after a valid request is made:
```
[
    {
        "Pokedex_No": 1,
        "Name": "Bulbasaur",
        "Type_1": "Grass",
        "Type_2": "Poison",
        "Total_Stat": 318,
        "HP": 45,
        "Attack": 49,
        "Defense": 49,
        "Sp_Attack": 65,
        "Sp_Defense": 65,
        "Speed": 45,
        "Generation": 1,
        "Legendary": false
    }
  ]
```
**api/token**

*HTTP method: POST*

This request returns a JWT access and refresh token.

**api/pokemon**

*HTTP method: GET*

This request returns data on all Pokemon in the database.

**api/fairy**

*HTTP method: GET*

This request provides only fairy type Pokemon to the user.

**api/add_pokemon**

*HTTP method: POST*

This request adds a new Pokemon provided by the user into the database.

**api/legendary**

*HTTP method: GET*

This request returns all legendary Pokemon.

**api/fast_pokemon**

*HTTP method: GET*

This request returns the top 10 fastest Pokemon.

**api/weak_pokemon**

*HTTP method: GET*

This request returns the top 5 weakest Pokemon.

**api/strong_pokemon**

*HTTP method: GET*

This request returns the top 3 highest attack stat Pokemon.

**api/generation_three**

*HTTP method: GET*

This request returns all Pokemon that were introduced in generation 3.

**api/mega_pokemon**

*HTTP method: GET*

This request returns all Pokemon that have a legendary evolution.

**api/o_pokemon**

*HTTP method: GET*

This request returns all Pokemon whose name begins with the letter 'O'.
