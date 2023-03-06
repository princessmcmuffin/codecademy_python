import csv
compromised_users = []

#Open 'passwords.csv', read into variable
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)

#Create empty list for compromised_users, iterate through password_csv to return the list of users found in the 'Username' column and append to compromised_users
  for row in password_csv:
    password_row = row
    compromised_users.append(password_row['Username'])

#Open 'compromised_users.txt' in write mode
with open('compromised_users.txt','w') as compromised_user_file:

#Iterate through global 'compromised_users' variable and write the list of users to 'compromised_user_file'
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)

#message boss json file to tell them the good news
import json

with open('boss_message.json','w') as     boss_message:
  boss_message_dict = {'recipient': 'The boss','message': 'Misson success'}
  json.dump(boss_message_dict, boss_message)

#create new passwords file and leave behind signature from rival hacker, framing them for the job
with open('new_passwords.csv','w') as new_passwords_obj:
  slash_null_sig = '''
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
  '''
  new_passwords_obj.write(slash_null_sig)