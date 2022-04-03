```mermaid
	sequenceDiagram
		main->>rautatietori: Lataajalaite()
		main->>ratikka6: Lukijalaite()
		main->>bussi244: Lukijalaite()
		main->>laitehallinto: lisaa_lataaja(rautatietori)
		main->>laitehallinto: lisaa_lukija(ratikka6)
		main->>laitehallinto: lisaa_lukija(bussi244)
		main->>lippu_luukku: osta_matkakortti("Kalle")
		lippu_luukku->>kallen_kortti: uusi_kortti = Matkakortti(Kalle)
		kallen_kortti-->>main
		main->>rautatietori: a
		rautatietori->>laitehallinto: lataa_arvoa(kallen_kortti, 3)
		laitehallinto->>kallen_kortti: kasvata_arvoa(3)
		kallen_kortti-->>main: a
		main->>ratikka6: a
		ratikka6->>laitehallinto: osta_lippu(kallen_kortti,0)
		laitehallinto->>kallen_kortti: vahenna_arvoa(1.5)
		kallen_kortti-->>main: true
		main->>bussi244: a
		bussi244->>laitehallinto: osta_lippu(kallen_kortti,2)
		laitehallinto-->>main: false	
```