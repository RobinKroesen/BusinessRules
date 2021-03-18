# BusinessRules
Robin Kroesen
1779750

# Content filtering(voor je partner)

Bij content filtering maak je recommendations op basis van eigenschappen van producten.
In deze recommendation wordt er gekeken naar 2 eigenschap van een geselecteerd product, gender en sub-catagorie.
Ik maak met deze eigenschappen een aanbeveling voor producten in dezelfde sub-catagorie maar met het tegenovergestelde gender(alleen bij producten met man/vrouw als gender).
Dus als er een lichaamsverzorgings product voor mannen geselecteerd is geeft het lichaamsverzorgingsproducten voor vrouwen als recommendation, met als titel 'Voor je partner'.

Bij deze recommendation haalt eerst 5 willekeurige producten met het tegenovergestelde gender uit de tabel 'product' en stopt deze in een lijst. 
Hierna wordt er een tabel gegenereerd waarin het recommendation_id(primary key), het product_id (van het product waar de recommendations op gebaseerd zijn) en het recommended_product_id(het product_id van het product dat aanbevolen wordt).
En dan worden de values in de tabel gestopt.

# Collaborative filtering(Vergelijkbare gebruikers bekeken ook)

Bij collaborative filtering maak je recommendations op basis van eigenschappen van klanten.
In deze recommendation wordt er gekeken naar wat voor gedrag de klant die aan het winkelen is vertoont en geeft beveelt producten aan die klanten met het zelfde winkelgedrag ook hebben bekeken.

Er worden eerst 50 willekeurige klanten uit de tabel 'profile' geselecteerd waar de producten die ze bekeken hebben(column 'viewed_before') in een lijst worden gestopt. 
Uit deze producten worden er 5 willekeurig gekozen die als recommendation worden gegeven.
Dan wordt er een tabel gemaakt met de colommen: collab_filter_id(primary key), profile_id(profiel waar de recommendations op gebaseerd zijn) en collab_product_id(het product dat aanbevolen wordt).
