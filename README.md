# Cisco-Spark-Add-Users-Spaces

This project was created as I needed a consistent way to name Spaces under Cisco Spark Teams and add the same people to every space. 


## Variables:

1. api = You can find your access token by going to https://developer.ciscospark.com and clicking your avatar on the top right of the screen.
2. spaceList = You can put one Space in this list or multiple. Your users will defined later will be added to these Spaces.
3. ourTeam = This is the teamID which can be found at https://developer.ciscospark.com/endpoint-teams-get.html
4. email_addresses = Enter the email addresses you want to add to the spaces defined in spaceList.

There is a test mechanism in this script where you can comment out the #Production Team and use a test team and also #email_addresses under #PRODUCTION PEOPLE. 
