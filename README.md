# Gruppuppgift_grupp3
pip install -r requirements.txt
Ifall det inte funkar så se till att du ligger i rätt filmap. T.ex. "cd Gruppuppgift_grupp3" sen pip install.
Python 3.11.9 när du skapar ditt virtual enviroment.
När du börjar arbeta, gör alltid en git pull först. 
Se till att skapa en branch & inte göra saker på main branchen då det skapar massa problem.
git branch för att kolla alla branches.
git checkout -b "ditt namn" för att skapa en ny bransch eller kolla in på andra aktiva bransches där du kan arbeta utan att störa main filen.
När du är färdig i din branch, ctrl+s i alla filer du arbetat i innan du gör en git add . & git commit -m "added data to example file" & sedan en git push -u origin "ditt branch namn" först gången du pushar från en ny bransch. Gör du sedan ändringar i din bransch innan vi mergar räcker git push.
Sedan initierar du en "Compare & pull request" på Github repon så vi kan se till att inget krockar med varandra. Se till att någon annan kollar på din pull request innan du mergar så vi kan ge kommenterar etc.