# Liður 1
### O(n)
Þetta flækjustig táknar algrím sem keyrir aðeins einu sinni fyrir hvert stak. Dæmi um forrit sem eru með O(n) flækjustig er einföld for lykkja:

> fyrir hvert stak í rununni 0 til n:
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prentaðu töluna sem lykkjan er á

Prent skipuninn hefur flækjustigið O(1) og þar sem það verður endurtekið n sinnum þá er flækjustigið n * O(1) eða O(n)

### O(n²)

Þetta flækjustig myndast þegar tvö O(n) forrit eru keyrð saman: o(n)*o(n) = O(n²). Dæmið er mjög líkt fyrra dæminu nema einni for lykkju er bætt við:

> fyrir hvert stak í rununni 0 til n:
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fyrir hvert stak í rununni 0 til n:
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; prentaðu fyrra stakið sinnum seinna stakið

### O(n * log(n))
Þarna erum við kominn í frekar flókna stærðfræði. Aðgerðunum er hægt að skipta í tvennt. Fyrst er það O(n) og síðar O(log(n)). Við vitum að O(n) er bara þegar við keyrum einu sinni í gegn en hvað er O(log(n))? O(log(n)) myndast þegar flóknari aðgerðir eru gerðar til að flýta algrímum s.s. "Divide and conquer" aðferð og fleira. Eitt dæm,i um "divide and conquer" aðferð er binary search. Það er býsna flókinn aðferð sem oft flýtir fyrir leitar algrímum þar sem það notar "divide and conquer" hugmyndafræðina. Svo O(n * log(n)) er í rauninni þetta tvennt lagt saman. Mörg röðunaralgrím hafa þetta flækjustig þar sem þau nota flókna leiðir til að gera einmitt "divide and conquer". Dæmi eru Mergesort, Heapsort og Timsort.

----

### Liður 2

#### Formál
Svo fyrir þetta verkefni langaði mig ekki bara bera saman .sort og mitt bubblesort algrím. Heldur líka bera mitt bubblesort algrím við fagmannlegt algrím sem ég fann á netinu. Ef ég á að vera hreinskilinn þá sé ég dálítið eftir því þar sem algrímið mitt var miklu lélegra en hitt. En svona er þetta bara. 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ég valdi að forrita bubble sort sem hefur flækjustigið O(n^2) sen er eitt það versta flækjustig sem þú getur fengið. Þetta er einmitt ástæðan fyrir því að ég gat ekki prófað lista með milljón stök. O(milljón í öðru veldi) er O(1.000.000.000.000). Að sjálfsögðu gæti ég keyrt þetta ef að ég hefði flotta skammtatölvu frá google en því miður er ég fastur með 6 ára tölvunni minni. 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Síðar er það hvernig ég tímamælti þetta. Ég ákvað að nota time module til að taka tímann:
> import time
>
> start = time.time()
> time.sleep(3)
> print(time.time() - start)

Þetta ætti að prenta tölu sem er mjög nálægt 3 sekúndum. Þessi aðferð er að sjálfsögðu ekki fullkominn en hún er nógu góð fyrir þetta verkefni.

#### Forrit 

Ég ákvað að reyna forrita bubblesort algrím. Það gekk bara ágætlega en er þó aðeins lélegra en algrím sem þú finnur á netinu. Þú getur skoðað kóðann [hérna](https://github.com/Gummy27/Forritun/blob/master/Onn-4/Reiknirrit/Skilaverkefni_3/myBubbleSort.py).

Einnig til að gera þetta aðeins skemmtilegra þá ákvað ég að taka annað bubble sort algrím frá netinu til að bera það saman við mitt. Þú getur skoðað þann kóða [hérna](https://github.com/Gummy27/Forritun/blob/master/Onn-4/Reiknirrit/Skilaverkefni_3/netBubbleSort.py).

Og síðast en ekki síst þá er það innbyggða röðunar algrímið hjá python. Það heitir timsort og er eitt flóknasta röðunar algrím sem þú getur fundið. Svo ekki beint jafn leikur en skemmtilegt að sjá muninn.

#### Niðurstöður

|           Algrím                            | Listi með 10^4 stök | versta tilvik | 
|:--------------------------------------------|:-----------------------------|:-------------|
| Bubblesort algrímið sem ég forritaði        | 37.91147446632385 sek   | 53.34300684928894 sek |   
| Bubblesort algrímið sem tekið var af netinu | 24.63727998733520 sek  | 38.24045228958130 sek |
| Innbyggða röðunar algrímið í Python         |  0.002961874008170 sek  | 0.0 sek|

Ef að þú vilt keyra þetta sjálfur og sjá niðurstöðurnar þínar þar gerði ég forrit sem tímamælir þetta og prentar þetta fallega út. [Kóðinn](https://github.com/Gummy27/Forritun/blob/master/Onn-4/Reiknirrit/Skilaverkefni_3/lidur_2.py)

### Tímaflækjan
Flækjustigið á bubble sort, eins og kom fram áðan, er O(n^2) sem er eitt af það versta flækjustig sem þú getur fengið. En flækjustigið á python röðunar algríminu (timsort) er aðeins O(n log(n)). Munurinn á millir algrímana er hrikalega stór og segir margt um hver mikilvægt er að velja rétta röðunar algrímið.

----

### Liður 3

#### [Kóðinn](https://github.com/Gummy27/Forritun/blob/master/Onn-4/Reiknirrit/Skilaverkefni_3/lidur_3.py)

### Liður 4

> def fall(L):
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;haesta = max(L)
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;countL = [0]*(haesta+1)
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resultL = [0]*len(L)
>  


> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for i in L:
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;countL[i] += 1
>  
Þessi for lykkja fer í gegnum listann countL og plúsar stökin sem samsvara tölunum í L listanum. Listinn sýnir hve margar tölur af sömu sort eru í listanum. t.d ef countL er [0, 1, 2] þá eru enginn 0, 1 tilvik af tölunni 1 og 2 tilvik af tölunni 2.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summa = 0
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for i in range(len(countL)):
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summa += countL[i]
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;countL[i] = summa

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for i in range(len(L)):
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resultL[countL[L[i]]-1] = L[i]
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;countL[L[i]] -= 1
>  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return resultL
>
> L = [7,1,8,2,5,10,8,9,3,6,1]
>print(fall(L))



### Liður 5
[Forritið](https://github.com/Gummy27/Forritun/blob/master/Onn-4/Reiknirrit/Skilaverkefni_3/lidur_5.py) hefur flækjustigið O(n) þar sem það keyrir í versta falli í gegnum allan listann aðeins einu sinni.
