# LoL_NamesGame
Microproject of a League of Legends champions listing game. Program pulls data from league of legends api every time it is executed. However to keep it up to date with current champion list the url link in main.py file should be manually changed according to current patch. When game starts it asks you to choose a difficulty level. It determines looks of champion table:
  1. EASY - You can see number of letters in every champion name, that was not guessed
  2. MEDIUM - You can see first letter of every not guessed champion name
  3. HARD - Just spaces for champion names oredered alphabetically

Every time the input is given, program informs you whether it's correct or not. Also it displays the table of all the spaces for champion names. It is filled with answers based on how many have alredy been guessed. The game ends when all champion names are guessed.
