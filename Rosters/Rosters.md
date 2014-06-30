Rosters:

The Rosters app records information about the coaches and players on a team.

The app is comprised of the following tables and values:

Team:
	Team_ID			INT
	Team_Name		String
	Mascot			String

Coach:
	Team_ID			INT
	Coach_ID		INT
	First_Name		String
	Last_Name		String
	Position		String

Athlete:
	Team_ID			INT
	Coach_ID		INT
	Athlete_ID		INT
	First_Name		String
	Last_Name		String
	Number			Int
	Position		String

In the layout above, the data types that are capitalized are primary_keys.

In the data for Rosters, a one to many relationship is created by a team having many players and coaches, but players and coaches only having one team. A many-to-many relationship is created by a coach possibly having many athletes to train, and athletes possibly having many coaches that train them (head coach, assistant coach, position coach).
