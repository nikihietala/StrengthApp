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