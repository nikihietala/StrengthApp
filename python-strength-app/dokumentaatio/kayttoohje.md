# Käyttöohje

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, avaa terminaalissa python-strength-app tiedosto ja asenna riippuvuudet komennolla:

```bash
poetry install
```

Sen jälkeen suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Sitten ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Kirjautuminen

Sovellus käynnistyy kirjautumisnäkymään:

_kuva tulee myöhemmin_

Kirjautuminen onnistuu syöttämällä käyttäjätunnus & salasana, ja painamalla "LOGIN" painiketta.

## Uuden käyttäjän luominen

Jos ei ole käyttäjätunnusta, uuden voin luoda painamalla kirjautumisnäkymän "CREATE NEW USER" painiketta, joka siirtää uuden käyttäjän luomisnäkymään.

Uusi käyttäjä luodaan syöttämällä haluttu käyttäjätunnus & salasana, ja painamalla "CREATE NEW USER" painiketta. Sovellus ilmoittaa jos käyttäjätunnuksen luonti onnistuu.
Sen jälkeen takaisin kirjautumisnäkymään pääsee painamalla "GO BACK TO LOGIN" painiketta.

Sovellus ilmoittaa jos käyttäjätunnuksen luonti ei onnistu, jolloin täytyy tehdä muutoksia:
	- Käyttäjätunnus ei saa olla jo olemassa
	- Käyttäjätunnus oltava vähintään 4 merkkiä
	- Salasana oltava vähintään 6 merkkiä

_kuva tulee myöhemmin_

## Urheiluharjoituksen valitseminen

_tulee myöhemmin_

## Uuden harjoituksen kirjaaminen

_tulee myöhemmin_

## Menneiden harjoitusten tarkastelu

_tulee myöhemmin_








