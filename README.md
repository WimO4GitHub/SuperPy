# SuperPy
N.a.v. de feedback van reviewer Djeno van de Stadt zijn onderstaande verbeteringen doorgevoerd:

Nette code
- overbodige als commentaar aangemerkt print regels weggehaald, evenals de lege regels. De opmerkingen in het Nederlands omgezet naar het Engels.

Aangepaste functionaliteit
- De opvraag van zowel revenue als profit flexibeler gemaakt, door i.p.v. te werken met today of yesterday, nu te werken met een datum. Beide gebruiken alle wijzigingen t.m. de opgegeven datum.
- Twee varianten toegevoegd (this_date_revenue en this_date_profit) om zowel revenue als profit te berekenen specifiek op de opgegeven datum. 

Nieuwe functionaliteit
- Toegevoegd door ´from rich import print as rprint´. En ingezet om belangrijke boodschappen aan de gebruiker te benadrukken door die in rood en vet te presenteren. Dat wordt bijvoorbeeld gebruikt wanneer getracht wordt een niet-bestaande beginsituatie te initialiseren. En dat gebeurt nu ook als de opgevraagde revenue of profit negatief is.

Handleidingen aangepast
- Waar nodig is zowel de gebruikers- als de technische handleiding aangepast (gemarkeerd in geel).
- Aan het concreet uitgewerkt voorbeeld in de gebruikershandleiding is per dag de alinea "Revenue en Profit" toegevoegd, waarin de opvraag van zowel revenue en profit als this_date_revenue en this_date_profit worden gebruikt.
- Beide toegevoegd als pdf, zodat de opmaak bewaakt is.
