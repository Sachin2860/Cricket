# Cricket
 
Context: Our system has the data of the cricket teams, its players,
matches, points table)

Structure of Team:
identifier
name
logoUri

Club state

Structure of Player:
identifier
firstName
lastName
imageUri
Player jersey number
Country
Player history (matches, run, highest scores, fifties, hundreds, etc..)
Matches
Matches between the teams
Winner of the match
Points table

Get points between the teams.


Story: As a user I want a list of the Teams Which are present in our
system and When I click on the Team I would want to see the Team Name
along with the list of players of that Team.

Random choose matches between all team (fixtures)


Points between the team


Acceptance Criteria:
1. Team list should consist of <logo>, <Team Name>
2. Players list should consist of <image>, <lastName> <firstName>
3. Matches fixtures
4. Points



  Expectation:

1. Use OOPs Concepts.
2. Forms, SQLs generation are native framework code.
3. Code as if it can be deployed to production (secured from
sqlinjection and other types of hacks).
4. Must Follow solid principles.


# Running the project
  - Download the repository.
  - No need to do migrations.
  - Run the server
    ```$ python manage.py runserver```
  - Verify the project by navigating to your server address in your preferred browser.
    ```sh
    127.0.0.1:8000
  -For acessing database run
  ``` 127.0.0.1:8000/admin```
  -admin  username--admin
  -admin  password--admin
  -admin  gmail--admin@gamil.com
  



