from ciscosparkapi import CiscoSparkAPI


# New instance of the CiscoSparkAPI object - Use your API key below

# API Key
api = CiscoSparkAPI(access_token="ACCESS_TOKEN_HERE")

# Define Cisco Spark Space names to be created
spaceList = ["Space1", "Space2", "Test Space"]


# Create a room and assign returned value to a variable. teamId = YOUR_TEAM_NAME
for site in spaceList:

	#ourTeam = "YOUR_TEAM_ID" #Testing
	ourTeam = "YOUR_TEAM_ID" #Production

	new_room = api.rooms.create(site, teamId=ourTeam)

	# Add people to the new_room
	#PRODUCTION PEOPLE
	email_addresses = ["user1@example.com","user2@example.com"]

	#TEST PEOPLE
	#email_addresses = ["user1@example.com","user2@example.com"]

	# Add email IDs to new Space
	for email in email_addresses:
	    api.memberships.create(new_room.id, personEmail=email)
