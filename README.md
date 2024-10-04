# IMDB_Telbot
Search &amp; explore imdb movies with a telegram bot \🤖/
make your movie bot with this code!
bot_username: @pksenpybot
[![BinaryTree](https://github.com/pksenpai/IMDB_Telbot/blob/main/IMDB_Bot.png)](image overview)
__________________________________________________________
## > commands:
/start  -->  greeting...
-----------------------------------------------------------
/help   -->  shows commands & how it works
-----------------------------------------------------------
@pksenpybot --> if you write somethigs after this, you can uppercase or lowercase it! 
-----------------------------------------------------------
@pksenpybot search --> if you write Movie name after this, you can search movies & see its info after selection!
-----------------------------------------------------------
other options coming soon...

***********************************************************
## > .env:
  <p>To run and test the project, you must create an .env file</p>
  <p>next to the other files and enter the important constants</p>
  <p>in it as blow:</p>

```
  # Rapidapi Config
  RAPID_API_URL=https://imdb188.p.rapidapi.com/api/v1/searchIMDB
  RAPID_API_KEY= <enter your rapidapi api key>
  RAPID_API_HOST= <enter your rapidapi host>

  # OMDB Config
  OMDB_API_URL=https://www.imdb.com/title/
  OMDB_API_KEY= <enter your omdb api key>

  # Botfather Config
  TOKEN= <enter your hashed key of telegram api>
```
  <p>Creating this file & doing this to keep personal</p>
  <p>and important inputs secret and secure, such as</p>
  <p>telegram hashed api key that you get from botfather!</p>
  
  <p>omdbapi key from https://www.omdbapi.com/apikey.aspx</p>
   
***********************************************************

## > api code analysis:
  First, I wanted to use the requests library. unfortunately, there were limited free apis
  both in terms of time and speed (i wrote the code in the rapid_api.py).
  then i found a better library for api!

  I imported that in another file(omdb_api.py),
  then i serialized my api data using a class and function.

  this makes my code cleaner, more flexible and expandable. i can sord or change the data
  as i want using validators and my own standard in the dictionary.

-----------------------------------------------------------
## > Qbot code analysis:
- At the beginning of the code,
  the required packages and modules are imported,
  and some initial settings are performed.

- TOKEN and OMDB_URL are defined as constants and
  their values are set using decouple and config to
  retrieve values from environment variables.

- Settings related to event occurrence and
  error messages for logging are done.(stream on terminal)

- The start function is defined to respond to the /start command.
  This function sends a welcome message to the user.

- The help function is also defined to respond to the /help command.
  This function displays a list of various options to the user.

- The about001, about002, about003, and about004 functions are defined
  to provide explanations about different sections of the bot.

- The inlineHandle function is defined to process InlineQuery requests.
  This function performs specific operations based on the type of input
  request. Here, if the input starts with the keyword "search,"
  it performs a movie search operation on the IMDB website and
  displays the results to the user. Otherwise,(search by GET req
  use URL_API + Movie_id from our dictionary...)
  it converts the input text to uppercase and lowercase letters.

- At the end of the code, an instance of the ApplicationBuilder
  class is created, and the settings for start (start) and
  help (help) commands, as well as different sections 
  (about001, about002, about003, about004), are added to the bot.
  The inlineHandle function is also added to the bot.

- Finally, the bot enters a continuous running state using
  the run_polling function, processing requests and events.
			  
			  
