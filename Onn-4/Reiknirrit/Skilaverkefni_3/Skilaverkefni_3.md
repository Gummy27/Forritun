## <ins>Liður 1</ins>
#### O(n)
Þetta flækjustig táknar algrím sem keyrir aðeins einu sinni fyrir hvert stak. Dæmi um forrit sem eru með O(n) flækjustig er einföld for lykkja:

> fyrir hvert stak í rununni 0 til n: <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prentaðu töluna sem lykkjan er á

Prent skipuninn hefur flækjustigið O(1) og þar sem það verður endurtekið n sinnum þá er flækjustigið n * O(1) eða O(n)

#### O(n²)

Þetta flækjustig myndast þegar for lykkja er hreiðruð í annari for lykkju. Dæmið er mjög líkt fyrra dæminu nema einni for lykkju er bætt við:

> fyrir hvert stak í rununni 0 til n:<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fyrir hvert stak í rununni 0 til k:<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; prentaðu fyrra stakið sinnum seinna stakið

#### O(n * log(n))
Þarna erum við kominn í frekar flókna stærðfræði. Aðgerðunum er hægt að skipta í tvennt. Fyrst er það O(n) og síðar O(log(n)). Við vitum að O(n) er bara þegar við keyrum einu sinni í gegn en hvað er O(log(n))? O(log(n)) myndast þegar flóknari aðgerðir eru gerðar til að flýta algrímum s.s. "Divide and conquer" aðferð og fleira. Eitt dæmi um "divide and conquer" aðferð er binary search. Það er býsna flókinn aðferð sem oft flýtir fyrir leitar algrímum þar sem það notar "divide and conquer" hugmyndafræðina. Svo O(n * log(n)) er í rauninni þetta tvennt lagt saman. Mörg röðunaralgrím hafa þetta flækjustig þar sem þau nota flókna leiðir til að gera einmitt "divide and conquer". Dæmi eru Mergesort, Heapsort og Timsort.

----

## <ins>Liður 2</ins>

#### Formál
Svo fyrir þetta verkefni langaði mig ekki bara bera saman .sort og mitt bubblesort algrím. Heldur líka bera mitt bubblesort algrím við bubble sort algrím sem ég fann á netinu. 

Ég valdi að forrita bubble sort sem hefur flækjustigið O(n^2) sen er eitt það versta flækjustig sem þú getur fengið. Þetta er einmitt ástæðan fyrir því að ég gat ekki prófað lista með milljón stök. O(milljón í öðru veldi) er O(1.000.000.000.000). Að sjálfsögðu gæti ég keyrt þetta ef að ég hefði flotta skammtatölvu frá google en því miður er ég fastur með 6 ára tölvunni minni. 


Síðar er það hvernig ég tímamælti þetta. Ég ákvað að nota time module til að taka tímann:
> import time
>
> start = time.time()<br>
> time.sleep(3)<br>
> print(time.time() - start)

Þetta ætti að prenta tölu sem er mjög nálægt 3 sekúndum. Þessi aðferð er að sjálfsögðu ekki fullkominn en hún er nógu góð fyrir þetta verkefni.

#### Forrit 

Ég ákvað að reyna forrita bubblesort algrím. Það gekk bara ágætlega en það er ekki alveg fullkomið. Þú getur skoðað kóðann [hérna](https://github.com/Gummy27/Forritun/blob/master/Onn-4/Reiknirrit/Skilaverkefni_3/myBubbleSort.py).

Einnig til að gera þetta aðeins skemmtilegra þá ákvað ég að taka annað bubble sort algrím frá netinu til að bera það saman við mitt. Þú getur skoðað þann kóða [hérna](https://github.com/Gummy27/Forritun/blob/master/Onn-4/Reiknirrit/Skilaverkefni_3/netBubbleSort.py).

Og síðast en ekki síst þá er það innbyggða röðunar algrímið hjá python. Það heitir timsort og er eitt flóknasta röðunar algrím sem þú getur fundið. Svo ekki beint jafn leikur en skemmtilegt að sjá muninn.

#### Niðurstöður

|           Algrím                            | Listi með 10^4 stök | Versta tilvik | 
|:--------------------------------------------|:-----------------------------|:-------------|
| Bubblesort algrímið sem ég forritaði        | 37.91147446632385 sek   | 53.34300684928894 sek |   
| Bubblesort algrímið sem tekið var af netinu | 24.63727998733520 sek  | 38.24045228958130 sek |
| Innbyggða röðunar algrímið í Python         |  0.002961874008170 sek  | 0.0 sek|

Ef að þú vilt keyra þetta sjálfur og sjá niðurstöðurnar þínar þar gerði ég forrit sem tímamælir þetta og prentar þetta fallega út. [Kóðinn](https://github.com/Gummy27/Forritun/blob/master/Onn-4/Reiknirrit/Skilaverkefni_3/lidur_2.py)

#### Tímaflækjan
Flækjustigið á bubble sort, eins og kom fram áðan, er O(n^2) sem er eitt af það versta flækjustig sem þú getur fengið. En flækjustigið á python röðunar algríminu (timsort) er aðeins O(n log(n)). Munurinn á millir algrímana er hrikalega stór og segir margt um hver mikilvægt er að velja rétta röðunar algrímið.

----

## <ins>Liður 3</ins>

#### [Kóðinn](https://github.com/Gummy27/Forritun/blob/master/Onn-4/Reiknirrit/Skilaverkefni_3/lidur_3.py)

### <ins>Liður 4</ins>
#### Kóðinn er útskýrður.
> def fall(L):<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;haesta = max(L)<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;countL = [0]*(haesta+1)<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resultL = [0]*len(L)
>  

Nokkrar breytur er skilgreindar. haesta breytan mun aðeins vera notuð einu sinni til að skilgreina hve mörg stök countL þarf til að telja eintök af tölum. countL listinn er notaður til að telja hve margar tölur af einu tagi eru í óraðaða listanum. Og resultL er listinn sem raðað verður í á eftir.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for i in L:<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;countL[i] += 1
>  
Þessi for lykkja fer í gegnum listann countL og plúsar stökin sem samsvara tölunum í L listanum. Listinn sýnir hve margar tölur af sömu sort eru í listanum. t.d ef countL er [0, 1, 2] þá eru enginn 0, 1 tilvik af tölunni 1 og 2 tilvik af tölunni 2.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summa = 0<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for i in range(len(countL)):<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summa += countL[i]<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;countL[i] = summa

Þessi for lykkja fer í gegnum countL og plúsar stökin saman: 
Dæmi:
[0, 1, 3, 5] yrði [0, 1+0, 3+1+0, 5+3+1+0] sem er [0, 1, 4, 10]. 
Listinn sem myndast úr þessu segir staðsetningu stakana í röðuðum lista. 

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for i in range(len(L)):<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resultL[countL[L[i]]-1] = L[i]<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;countL[L[i]] -= 1
>  
Hérna kemur aðal for lykkjan sem loks raðar listann. Þetta lítur út fyrir að vera flókið en í rauninni er þetta heldur einfalt. Besta leiðin til að útskýra hvað er í gangi er að brjóta þetta aðeins niður. 

> L[i]

Þetta er frekar einfalt. For lykkjan er í raun að fara í gegnum listann L og raðar hverju staki sem lykkjan er á. 

> countL[L[i]]

Þessi kóði segir hvar talan sem L[i] er á, er í raðaða listanum. T.d.

> countL = [1, 2, 3]<br>
> L = [2, 1, 0]<br>
> countL[1] # skilar 2 sem er staðsetning staksins í resultL listanum.

> resultL[countL[L[i]]-1] = L[i]

Þarna erum við loksins komnir á raðað listann. Eins og greint var frá áðan þá skilar countL[L[i]] staðsetningu L[i] inn í raðaða listanum. Eina sem eftir er að gera er að mínusa 1 frá til að leiðrétta countL listann. 

> countL[L[i]] -= 1

Síðasta aðgerðin er að draga einn frá countL[L[i]]. Eins og þú mannst þá heldur listinn countL utan um fjölda talna í listanum L og þar sem við erum búinn að raða eitt af þeim tölum þá þurfum við ekki að hafa áhyggjur af henni lengur. 

#### Aðeins um Reiknirritið

Þetta röðunar algrím kallast "counting sort" og hefur flækjustigið O(n+k) þar sem n er lengd listans L og k er lengd listans countL. 

## <ins>Liður 5</ins>
[Forritið](https://github.com/Gummy27/Forritun/blob/master/Onn-4/Reiknirrit/Skilaverkefni_3/lidur_5.py) hefur flækjustigið O(n) þar sem það keyrir í versta falli í gegnum allan listann aðeins einu sinni.
