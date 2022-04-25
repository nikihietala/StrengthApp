# Arkkitehtuuri

## Rakenne

Koodin pakkaus-/luokkakaavio on:
```mermaid
	classDiagram
		ui ..> services
		services ..> repositories
		services ..> entities
		repositories ..> entities
		class ui{
		}
		class services{
			UserService
		}
		class repositories{
			UserRepository
		}
		class entities{
				User
				
		}
```

 ## Sovelluslogiikka
 
 Luokka User
```mermaid
		classDiagram
			UserService "0..1" -- "0..1" User
			UserRepository ..> User
			class User{
				username
				password
			}
```	

## Toiminnallisuudet

### Uuden käyttäjän luominen

Käyttääkseen sovellusta on luotava käyttäjätunnus. Sovellus avautuu kirjautumisnäkymään, jossa voidaan painaa "Create new user" painiketta päästäkseen uuden käyttäjän luomisnäkymään.
Seuraava sekvenssikaavio näyttää käyttäjänluonnin toiminnallisuuden:
```mermaid
		sequenceDiagram
			actor User
			participant UI
			participant UserService
			participant UserRepository
			participant EsimerkkiEero
			User->>UI: click "CREATE NEW USER" button
			UI->>UserService: create_user("EsimerkkiEero","salasana123")
			UserService->>UserRepository: find_by_username("EsimerkkiEero")
			UserRepository-->>UserService: None
			UserService->>EsimerkkiEero: User("EsimerkkiEero", "salasana123")
			UserService->>UserRepository: create(EsimerkkiEero)
			UserRepository-->>UserService: user
			UserService-->>UI: user
			User->>UI: click "GO BACK TO LOGIN" button
			UI->>UI: show_exercise_list_view()
```

### Käyttäjän kirjaantuminen

Kun sovelluksen käyttäjä on luonut käyttäjätunnuksen, hän voi kirjautua sisään kirjoittamalla käyttäjätunnuksen ja salasanan kirjautumisnäkymään, jonka jälkeen painetaan "LOGIN" painiketta.
Seuraava sekvenssikaavio näyttää kirjautumisen toiminnallisuuden:
```mermaid
		sequenceDiagram
			actor User
			participant UI
			participant UserService
			participant UserRepository
			User->>UI: click "LOGIN" button
			UI->>UserService: login("EsimerkkiEero", "salasana123")
			UserService->>UserRepository: find_by_username("EsimerkkiEero")
			UserRepository-->>UserService: user
			UserService-->>UI: user
			UI->>UI: show_exercise_list_view()
```

### Uuden tuloksen kirjaaminen

Kun käyttäjä on kirjannut itsensä sovellukseen, käyttäjä voi valita harjoituksen (esim. Squat) painamalla "Squat"-painiketta. Tämä avaa kyseisen harjoituksen näkymän, jossa voi tallentaa
uuden tuloksen. Seuraava sekvenssikaavio näyttää kuinka uuden tuloksen kirjaaminen toimii:
```mermaid
		sequenceDiagram
			actor User
			participant UI
			User->>UI: click "SQUAT"
			User->>UI: click "SAVE RESULT"
```

--kesken		
			
			
			