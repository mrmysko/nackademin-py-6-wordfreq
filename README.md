[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/cLgY1ON2)
# Uppgift 6 - Ordfrekvensanalys med funktionen `wordfreq()`

## <a name='Syfte'></a>Syfte

## <a name='Syfte-1'></a>Syfte

Syftet med denna uppgift är att utveckla studenternas förmåga att använda
dictionaries för att analysera och bearbeta textdata. Genom att skapa en
funktion som räknar ordens frekvens i en given text, övas strängmanipulation,
vilket är en central komponent i programmering och dataanalys.

<!-- vscode-markdown-toc -->

- [Syfte](#Syfte)
- [Syfte](#Syfte-1)
- [Förberedelser](#Frberedelser)
- [Beskrivning](#Beskrivning)
  - [Detaljer](#Detaljer)
    - [Skapa en funktion](#Skapaenfunktion)
    - [Tips](#Tips)
    - [Exempel](#Exempel)
  - [Inlämningsinstruktioner](#Inlmningsinstruktioner)
- [Anteckningar](#Anteckningar)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='Frberedelser'></a>Förberedelser

Innan du börjar med uppgiften, se till att du är bekväm med följande koncept:

- Grundläggande datatyper i Python (strängar, listor, dictionaries)
- Loopar (`for`-loopar och `while`-loopar)
- Funktioner och hur man definierar dem
- Strängmetoder, såsom `.split()`

## <a name='Beskrivning'></a>Beskrivning

Skriv en funktion `wordfreq` som tar en sträng som argument och returnerar en
dictionary. Denna dictionary ska innehålla alla unika ord som finns i strängen
som nycklar, och antalet gånger varje ord förekommer i strängen som värde.

### <a name='Detaljer'></a>Detaljer

#### <a name='Skapaenfunktion'></a>Skapa en funktion

- **Funktionsignatur:** `def wordfreq(text: str) -> dict:`
- **Vad den ska göra:** Funktionen tar en sträng text som argument och
  returnerar en frekvensanalys för orden i strängen. För att separera ord i
  strängen, anta att ord separeras av ett mellanslag.
- **Vad den ska skriva ut:** Inget!
- **Vad den ska returnera:** Ett dictionary där nycklarna är unika ord från
  strängen och värdena är antalet gånger dessa ord förekommer. Om den givna
  strängen är tom, ska funktionen returnera ett tomt dictionary.

#### <a name='Tips'></a>Tips

- Använd `.split()`-metoden för att dela upp strängen i en lista av ord baserad
  på mellanslag.
- Loopa igenom listan av ord och använd ett dictionary för att hålla reda på
  frekvensen av varje ord.
- Var noga med att hantera fall där strängen är tom på ett korrekt sätt.

#### <a name='Exempel'></a>Exempel

- **Anrop:** `wordfreq("hej hej på dig")`

  - **Förväntad utskrift:** Inget!
  - **Förväntat returvärde:** `{'hej': 2, 'på': 1, 'dig': 1}`

- **Anrop:** `wordfreq("ett två tre två")`

  - **Förväntad utskrift:** Inget!
  - **Förväntat returvärde:** `{'ett': 1, 'två': 2, 'tre': 1}`

- **Anrop:** `wordfreq("")`

  - **Förväntad utskrift:** Inget!
  - **Förväntat returvärde:** `{}`

- **Anrop:** `wordfreq("python programmering python")`

  - **Förväntad utskrift:** Inget!
  - **Förväntat returvärde:** `{'python': 2, 'programmering': 1}`

- **Anrop:** `wordfreq("test test test")`
  - **Förväntad utskrift:** Inget!
  - **Förväntat returvärde:** `{'test': 3}`

### <a name='Inlmningsinstruktioner'></a>Inlämningsinstruktioner

För att lämna in din uppgift, vänligen följ dessa steg:

1. **Använda Github Classroom:**

   - Du har troligen redan accepterat uppgiften via en länk som tillhandahålls
     av utbildaren och gjort en `git clone` av det tilldelade repositoriet då du
     läser denna text. Det är i detta repository du kommer att hitta `README.md`
     med ytterligare instruktioner.

2. **Modifiera `uppgift.py`:**

   - Din lösning på uppgiften ska skrivas i `uppgift.py`. Det finns specifika
     instruktioner i `uppgift.py` om var du ska placera din källkod.

3. **Lämna in med Git:**

   - När du är klar med din uppgift, använd kommandona `git add .`, `git commit`
     följt av `git push` för att skicka in dina ändringar till GitHub.

4. **Automatiska "smoke tests":**

   - Efter att du har pushat din kod kommer automatiska "smoke tests" att köras.
     Dessa tester indikeras med en grön bock om de passerar, eller ett rött
     kryss om de misslyckas. Om du får ett rött kryss, är det viktigt att du
     klickar dig fram i GitHub tills du kan se varför testerna inte passerade.

5. **Feedback och granskning från utbildaren:**

   - Om dina tester passerar med en grön bock, kan du invänta feedback från din
     utbildare. Utbildaren kan antingen sätta "Request Changes" om ytterligare
     förändringar behövs, eller "approve" om uppgiften är godkänd som den är.
     Det är viktigt att du inväntar någon av dessa innan du väljer Merge.
   - Vid "Request Changes" är det viktigt att noggrant granska feedbacken och
     göra de nödvändiga justeringarna baserat på utbildarens anvisningar för att
     säkerställa att din uppgift uppfyller alla krav.
   - Efter att utbildaren har gjort "Approve" på din inlämning, får du göra en
     "Merge" av din "Feedback"-pull request, men inte förrän ett godkännande har
     erhållits.

6. **Initiera diskussioner i "Feedback"-pull requesten:**

   - Som student är du uppmuntrad att aktivt delta i processen genom att
     initiera diskussioner i din "Feedback"-pull request. Detta är en viktig del
     av inlärningsprocessen, där du kan ställa frågor, begära förtydliganden
     eller diskutera lösningar och feedback med din utbildare. Att engagera sig
     i dessa diskussioner ger dig möjlighet att djupare förstå uppgiftens krav
     och förbättra din kod baserat på interaktionen.

## <a name='Anteckningar'></a>Anteckningar

Inga.
