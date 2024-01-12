# README #
This is a project that retrieves specific information about a Pokemon using a Django RESTFUL API system.

Note that this is just for development purposes and is not fit for live production.

### Pokemon API Requests ###
##### api/token #####
This is to generate a token provided by OAuth 2.0 that the user can use to make the following API calls.
This request requires the user to provide their authenticated username and password.
##### api/pokemon #####
This request outputs all the pokemon and their attributes to the user.
##### api/fairy #####
This request provides only fairy type pokemon to the user.
##### api/add_pokemon #####
This request adds a new pokemon provided by the user into the database.
##### api/legendary #####
This request returns all legendary pokemon.
##### api/fast_pokemon #####
This request returns the top 10 fastest pokemon.
##### api/weak_pokemon #####
This request returns the top 5 weakest pokemon.
##### api/strong_pokemon #####
This request returns the top 3 highest attack stat pokemon.
##### api/generation_three #####
This request returns all pokemon that were introduced in generation 3.
##### api/mega_pokemon #####
This request returns all pokemon that have a legendary evolution.
##### api/o_pokemon #####
This request returns all pokemon whose name begins with the letter 'O'.
