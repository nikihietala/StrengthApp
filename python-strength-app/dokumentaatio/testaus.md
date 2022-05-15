# Testausdokumentti

Ohjelmaa on testattu unittestilla.

## Sovelluslogiikka

UserService luokka on testattu TestUserService-testiluokalla. 

## Repositorio

UserRepository-luokka on testattu TestUserRepository-luokalla. Testit testataan ainostaan testeissä käytetyillä tiedostoilla. Tiedoston nimet löytyvät .env.test-tiedostosta.
ExerciseRepository-luokkaa ei ole testattu - siinä luokassa ei tehdä muuta kuin kirjoitetaan tiedoston sisältö.

## Testauskattavuus

![](./kuvat/testaus.jpg) 

Käyttöliittymäkerros on jätetty sovelluksen testauksen ulkopuolelle. Haarautumakattavuus on 53%, jota ExerciseRepository-luokan 0% testikattavuus tiputtaa.
Testikattavuus on >95% kun ExerciseRepositoryn jättää testauksen ulkopuolelle.


