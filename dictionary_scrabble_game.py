letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Combine letters and points to create a dictionary
letter_to_points = {key:value for key, value in zip(letters,points)}

#Add a space value to the dictionary
letter_to_points.update({" " : 0})

#Create a function that will loop through your word and calculate the score
def score_word(word):
  point_total = 0
  for letters in word:
    point_total += letter_to_points.get(letters, 0)
  return point_total

#See how many points the word "BROWNIE" scores
brownie_points = score_word("BROWNIE")
print(brownie_points)

#Add dictionary of players and the words they have played
player_to_words = {"player1" : ["BLUE, TENNIS, EXIT"], "wordNerd" : ["EARTH", "EYES", "MACHINE"], "Lexi Con" : ["ERASER", "BELLY", "HUSKY"], "Prof Reader" : ["ZAP", "COMA", "PERIOD"]}


#Loop through player_to_words, use the score_word function to determine the scores of each of the words and aggregate these to player level to work out who has won
player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)

  player_to_points = {player : player_points}

  print(player_to_points)