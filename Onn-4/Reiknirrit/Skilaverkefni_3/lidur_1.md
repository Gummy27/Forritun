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


