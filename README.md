# Gruppuppgift_grupp3

Här förklarar jag Gruppexamen steg för steg.


Krav: python
Version  3.11.9
Virsuellt enviroment: venv
## steg för steg_
1. Klona repon från github till din lokala maskin.
' git clone "repo Link"
2. Går in i mappen vi klonade ner.
 cd uppgift_grupp3
3. skapa ett virtuellt enviroment
    python -m venv venv
4.Aktvierade vårt virtuella 
     Windows: .\venv\Scripts\activate
     Mac/Linux: source venv/bin`/activate
5. Installera alla dependecises
    pip install -r requirements.txt
6. Alla börja klonade repon och skapade en branch med var o ch sitt namn.
7. Vi började arbeta i våra egna brancher och gjorde ändringar i filerna.
8. När vi var klara med våra ändringar så gjorde vi en git add . , git commit -m
9. sedag gjorde vi git push -u origin med vårt branch namn.
10 vi skapade en pull request på github repon.
11. När alla var klara så megrade vi alla brancher in i main branchen.

Roller och ansvar:

Vem gjort vad fins i filen skärmbilden.






git initieraring av en ny repo
* pip install -r requirements.txt
* Ifall det inte funkar så se till att du ligger i rätt filmap. T.ex. "cd Gruppuppgift_grupp3" sen pip install.
* Genom att skriva pyton -v
*Python 3.11.9 när du skapar ditt virtual enviroment.
* När du börjar arbeta, gör alltid en git pull först. 
* Se till att skapa en branch & inte göra saker på main branchen då det skapar massa problem.
* git branch för att kolla alla branches.
* git checkout -b "ditt namn" för att skapa en ny bransch eller kolla in på andra aktiva bransches där du kan arbeta utan att störa main filen.
* När du är färdig i din branch, ctrl+s i alla filer du arbetat i innan du gör en git add . & git commit -m "added data to example file" & sedan en git push -u origin "ditt branch namn" först gången du pushar från en ny bransch. Gör du sedan ändringar i din bransch innan vi mergar räcker git push.
* Sedan initierar du en "Compare & pull request" på Github repon så vi kan se till att inget krockar med varandra. Se till att någon annan kollar på din pull request innan du mergar så vi kan ge kommenterar etc.

