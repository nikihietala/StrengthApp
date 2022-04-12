# Arkkitehtuuri

## Rakenne

```mermaid
	classDiagram
		ui ..> services
		services ..> repositories
		services ..> entities
		repositories ..> entities
		UserService "0..1" -- "0..1" User
		UserRepository ..> User
		class ui{
		}
		class services{
			UserService
		}
		class repositories{
			UserRepository
		}
		class entities{
			class User{
				username
				password
				}
		}
		
```