# Drie beschrijvingen

## 1. Initiëren van een startsituatie

Het is altijd tijdens het ontwikkelen, maar ook bijvoorbeeld bij het uitleggen van SuperPy aan anderen, erg prettig als **snel en eenvoudig** naar een bepaalde startsituatie gegaan kan worden. 
Een startsituatie met een vooraf gedefinieerde datum van vandaag en een voorgaande processtappen die hebben geleid tot gevuld csv-bestanden: *Bought.cvs, Sold.cvs, Expired.csv. Inventory.cvs*. 
Ik heb hiervoor het commando initiate startsituation toegevoegd en die ingericht voor het voorbeeld dat ik zelf heb gemaakt en in de gebruikershandleiding heb opgenomen. De code, waaronder de  functie def initiate(startsituation:str), is voorbereid om andere startsituaties eenvoudig in te richten.  

## 2. Alle gegevens altijd in csv-bestanden

Om mogelijk te maken dat de SuperPy-gegevens eenvoudig met andere programma’s of interfaces gedeeld kunnen worden zijn die altijd opgeslagen in csv-bestanden. Na elk commando door de gebruiker in command line interface ingevoerd of na elke bewerking door SuperPy zelf worden de cs-bestanden daarom bijgewerkt op nieuw opgebouwd.

## 3. Code stap-voor-stap opgebouwd

Als beginnend Python gebruiker in het vallen en opstaan en leren van de fouten die ik maak. Om te begrijpen waardoor een fout ontstaat heb ik m'n code vaak over meerdere coderegels verdeeld. Een eenvoudig, doch illustratief voor beeld zijn deze 2 regels uit *def total_sold_price(date:datetime)*:
- *this_sell_price = float(row[3])*
- *total_sold_price = total_sold_price + this_sell_price*
Deze hadden prima tot 1 coderegel samengevoegd kunnen worden, maar op deze wijze houd ik een scherp beeld op de uitvoering van het programma en weet precies waar die eenfoutmelding oplevert.
