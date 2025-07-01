import re

file = {}

with open('./popularne_slowa2023.txt') as f:
    for l in f:
        file[l.rstrip()] = 1


tekst = """
Bolesław Prus

Lalka

ISBN 978-83-288-2673-1





Tom I



I. Jak wygląda firma J. Mincel i S. Wokulski przez szkło butelek?

W początkach roku 1878, kiedy świat polityczny zajmował się pokojem san-stefańskim, wyborem nowego papieża albo szansami europejskiej wojny, warszawscy kupcy tudzież inteligencja pewnej okolicy Krakowskiego Przedmieścia niemniej gorąco interesowała się przyszłością galanteryjnego sklepu pod firmą J. Mincel i S. Wokulski.

W renomowanej jadłodajni, gdzie na wieczorną przekąskę zbierali się właściciele składów bielizny i składów win, fabrykanci powozów i kapeluszy, poważni ojcowie rodzin, utrzymujący się z własnych funduszów, i posiadacze kamienic bez zajęcia, równie dużo mówiono o uzbrojeniach Anglii, jak o firmie J. Mincel i S. Wokulski. Zatopieni w kłębach dymu cygar i pochyleni nad butelkami z ciemnego szkła obywatele tej dzielnicy, jedni zakładali się o wygranę lub przegranę Anglii, drudzy o bankructwo Wokulskiego; jedni nazywali geniuszem Bismarcka, drudzy — awanturnikiem Wokulskiego; jedni krytykowali postępowanie prezydenta MacMahona, inni twierdzili, że Wokulski jest zdecydowanym wariatem, jeżeli nie czymś gorszym…

Pan Deklewski, fabrykant powozów, który majątek i stanowisko zawdzięczał wytrwałej pracy w jednym fachu, tudzież radca Węgrowicz, który od dwudziestu lat był członkiem-opiekunem jednego i tego samego Towarzystwa Dobroczynności, znali S. Wokulskiego najdawniej i najgłośniej przepowiadali mu ruinę. — Na ruinie bowiem i niewypłacalności — mówił pan Deklewski — musi skończyć człowiek, który nie pilnuje się jednego fachu i nie umie uszanować darów łaskawej fortuny. — Zaś radca Węgrowicz, po każdej również głębokiej sentencji swego przyjaciela, dodawał:

— Wariat! wariat!… Awanturnik!… Józiu, przynieś no jeszcze piwa. A która to butelka?

— Szósta, panie radco. Służę piorunem!… — odpowiadał Józio.

— Już szósta?… Jak ten czas leci!… Wariat! wariat! — mruczał radca Węgrowicz.

Dla osób posilających się w tej co radca jadłodajni, dla jej właściciela, subiektów i chłopców przyczyny klęsk mających paść na S. Wokulskiego i jego sklep galanteryjny były tak jasne, jak gazowe płomyki oświetlające zakład. Przyczyny te tkwiły w niespokojnym charakterze, w awanturniczym życiu, zresztą w najświeższym postępku człowieka, który mając w ręku pewny kawałek chleba i możność uczęszczania do tej oto tak przyzwoitej restauracji, dobrowolnie wyrzekł się restauracji, sklep zostawił na Opatrzności boskiej, a sam z całą gotówką odziedziczoną po żonie pojechał na turecką wojnę robić majątek.

— A może go i zrobi… Dostawy dla wojska to gruby interes — wtrącił pan Szprot, ajent handlowy, który bywał tu rzadkim gościem.

— Nic nie zrobi — odparł pan Deklewski — a tymczasem porządny sklep diabli wezmą. Na dostawach bogacą się tylko Żydzi i Niemcy; nasi do tego nie mają głowy.

— A może Wokulski ma głowę?

— Wariat! wariat!… — mruknął radca. — Podaj no, Józiu, piwa. Która to?…

— Siódma buteleczka, panie radco. Służę piorunem.

— Już siódma?… Jak ten czas leci, jak ten czas leci…

Ajent handlowy, który z obowiązków stanowiska potrzebował mieć o kupcach wiadomości wszechstronne i wyczerpujące, przeniósł swoją butelkę i szklankę do stołu radcy i topiąc słodkie wejrzenie w jego załzawionych oczach, spytał zniżonym głosem:

— Przepraszam, ale… Dlaczego pan radca nazywa Wokulskiego wariatem?… Może mogę służyć cygarkiem… Ja trochę znam Wokulskiego. Zawsze wydawał mi się człowiekiem skrytym i dumnym. W kupcu skrytość jest wielką zaletą, duma wadą. Ale żeby Wokulski zdradzał skłonności do wariacji, tegom nie spostrzegł.

Radca przyjął cygaro bez szczególnych oznak wdzięczności. Jego rumiana twarz, otoczona pękami siwych włosów nad czołem, na brodzie i na policzkach, była w tej chwili podobna do krwawnika oprawionego w srebro.

— Nazywam go — odparł, powoli ogryzając i zapalając cygaro — nazywam go wariatem, gdyż go znam lat… Zaczekaj pan… Piętnaście… siedemnaście… osiemnaście… Było to w roku 1860… Jadaliśmy wtedy u Hopfera. Znałeś pan Hopfera?…

— Phi…

— Otóż Wokulski był wtedy u Hopfera subiektem i miał już ze dwadzieścia parę lat.

— W handlu win i delikatesów?

— Tak. I jak dziś Józio, tak on wówczas podawał mi piwo, zrazy nelsońskie…

— I z tej branży przerzucił się do galanterii? — wtrącił ajent.

— Zaczekaj pan — przerwał radca. — Przerzucił się, ale nie do galanterii, tylko do Szkoły Przygotowawczej, a potem do Szkoły Głównej, rozumie pan?… Zachciało mu się być uczonym!…

Ajent począł chwiać głową w sposób oznaczający zdziwienie.

— Istna heca — rzekł. — I skąd mu to przyszło?

— No, skąd! Zwyczajnie — stosunki z Akademią Medyczną, ze Szkołą Sztuk Pięknych… Wtedy wszystkim paliło się we łbach, a on nie chciał być gorszym od innych. W dzień służył gościom przy bufecie i prowadził rachunki, a w nocy uczył się…

— Licha musiała to być usługa.

— Taka jak innych — odparł radca, niechętnie machając ręką. — Tylko że przy posłudze był, bestia, niemiły; na najniewinniejsze słówko marszczył się jak zbój… Rozumie się, używaliśmy na nim, co wlazło, a on najgorzej gniewał się, jeżeli nazwał go kto „panem konsyliarzem”. Raz tak zwymyślał gościa, że mało obaj nie porwali się za czuby.

— Naturalnie, handel cierpiał na tym.

— Wcale nie! Bo kiedy po Warszawie rozeszła się wieść, że subiekt Hopfera chce wstąpić do Szkoły Przygotowawczej, tłumy zaczęły tam przychodzić na śniadanie. Osobliwie roiła się studenteria.

— I poszedł też do Szkoły Przygotowawczej?

— Poszedł i nawet zdał egzamin do Szkoły Głównej. No, ale co pan powiesz — ciągnął radca uderzając ajenta w kolano — że zamiast wytrwać przy nauce do końca, niespełna w rok rzucił szkołę…

— Cóż robił?

— Otóż, co… Gotował wraz z innymi piwo, które do dziś dnia pijemy, i sam w rezultacie oparł się aż gdzieś koło Irkucka.

— Heca, panie! — westchnął ajent handlowy.

— Nie koniec na tym… W roku 1870 wrócił do Warszawy z niewielkim fundusikiem. Przez pół roku szukał zajęcia, z daleka omijając handle korzenne, których po dziś dzień nienawidzi, aż nareszcie przy protekcji swego dzisiejszego dysponenta, Rzeckiego, wkręcił się do sklepu Minclowej, która akurat została wdową, i w rok potem ożenił się z babą grubo starszą od niego.

— To nie było głupie — wtrącił ajent.

— Zapewne. Jednym zamachem zdobył sobie byt i warsztat, na którym mógł spokojnie pracować do końca życia. Ale też miał on krzyż Pański z babą!

— One to umieją…

— Jeszcze jak! — prawił radca. — Patrz pan jednakże, co to znaczy szczęście. Półtora roku temu baba objadła się czegoś i umarła, a Wokulski po czteroletniej katordze został wolny jak ptaszek, z zasobnym sklepem i trzydziestu tysiącami rubli w gotowiźnie, na którą pracowały dwa pokolenia Minclów.

— Ma szczęście.

— Miał — poprawił radca — ale go nie uszanował. Inny na jego miejscu ożeniłby się z jaką uczciwą panienką i żyłby w dostatkach; bo co to, panie, dziś znaczy sklep z reputacją i w doskonałym punkcie!… Ten jednak, wariat, rzucił wszystko i pojechał robić interesa na wojnie. Milionów mu się zachciało czy kiego diabła.

— Może je będzie miał — odezwał się ajent.

— Ehe! — żachnął się radca. — Daj no, Józiu, piwa. Myślisz pan, że w Turcji znajdzie jeszcze bogatszą babę aniżeli nieboszczka Minclowa?… Józiu!…

— Służę piorunem!… Jedzie ósma…

— Ósma? — powtórzył radca — to być nie może. Zaraz… Przedtem była szósta, potem siódma… — mruczał zasłaniając twarz dłonią. — Może być, że ósma. Jak ten czas leci!…

Mimo posępne wróżby ludzi trzeźwo patrzących na rzeczy, sklep galanteryjny pod firmą J. Mincel i S. Wokulski nie tylko nie upadł, ale nawet robił dobre interesa. Publiczność zaciekawiona pogłoskami o bankructwie coraz liczniej odwiedzała magazyn, od chwili zaś kiedy Wokulski opuścił Warszawę, zaczęli zgłaszać się po towary kupcy rosyjscy. Zamówienia mnożyły się, kredyt za granicą istniał, weksle były płacone regularnie, a sklep roił się gośćmi, którym ledwo mogli wydołać trzej subiekci: jeden mizerny blondyn, wyglądający, jakby co godzinę umierał na suchoty, drugi szatyn z brodą filozofa, a ruchami księcia i trzeci elegant, który nosił zabójcze dla płci pięknej wąsiki, pachnąc przy tym jak laboratorium chemiczne.

Ani jednak ciekawość ogółu, ani fizyczne i duchowe zalety trzech subiektów, ani nawet ustalona reputacja sklepu może nie uchroniłyby go od upadku, gdyby nie zawiadował nim czterdziestoletni pracownik firmy, przyjaciel i zastępca Wokulskiego, pan Ignacy Rzecki.



II. Rządy starego subiekta

Pan Ignacy od dwudziestu pięciu lat mieszkał w pokoiku przy sklepie. W ciągu tego czasu sklep zmieniał właścicieli i podłogę, szafy i szyby w oknach, zakres swojej działalności i subiektów; ale pokój pana Rzeckiego pozostał zawsze taki sam. Było w nim to samo smutne okno, wychodzące na to samo podwórze, z tą samą kratą, na której szczeblach zwieszała się, być może, ćwierćwiekowa pajęczyna, a z pewnością ćwierćwiekowa firanka, niegdyś zielona, obecnie wypłowiała z tęsknoty za słońcem.

Pod oknem stał ten sam czarny stół obity suknem, także niegdyś zielonym, dziś tylko poplamionym. Na nim wielki czarny kałamarz wraz z wielką czarną piaseczniczką, przymocowaną do tej samej podstawki — para mosiężnych lichtarzy do świec łojowych, których już nikt nie palił, i stalowe szczypce, którymi już nikt nie obcinał knotów. Żelazne łóżko z bardzo cienkim materacem, nad nim nigdy nie używana dubeltówka, pod nim pudło z gitarą, przypominające dziecinną trumienkę, wąska kanapka obita skórą, dwa krzesła również skórą obite, duża blaszana miednica i mała szafa ciemnowiśniowej barwy stanowiły umeblowanie pokoju, który, ze względu na swoją długość i mrok w nim panujący, zdawał się być podobniejszym do grobu aniżeli do mieszkania.

Równie jak pokój, nie zmieniły się od ćwierć wieku zwyczaje pana Ignacego.

Rano budził się zawsze o szóstej; przez chwilę słuchał, czy idzie leżący na krześle zegarek, i spoglądał na skazówki, które tworzyły jedną linię prostą. Chciał wstać spokojnie, bez awantur; ale że chłodne nogi i nieco zesztywniałe ręce nie okazywały się dość uległymi jego woli, więc zrywał się, nagle wyskakiwał na środek pokoju i rzuciwszy na łóżko szlafmycę, biegł pod piec do wielkiej miednicy, w której mył się od stóp do głów, rżąc i parskając jak wiekowy rumak szlachetnej krwi, któremu przypomniał się wyścig.

Podczas obrządku wycierania się kosmatymi ręcznikami, z upodobaniem patrzył na swoje chude łydki i zarośnięte piersi, mrucząc:

„No, przecie nabieram ciała.”

W tym samym czasie zeskakiwał z kanapki jego stary pudel Ir z wybitym okiem i mocno otrząsnąwszy się, zapewne z resztek snu, skrobał do drzwi, za którymi rozlegało się pracowite dmuchanie w samowar. Pan Rzecki, wciąż ubierając się z pośpiechem, wypuszczał psa, mówił dzień dobry służącemu, wydobywał z szafy imbryk, mylił się przy zapinaniu mankietów, biegł na podwórze zobaczyć stan pogody, parzył się gorącą herbatą, czesał się nie patrząc w lustro i o wpół do siódmej był gotów.

Obejrzawszy się, czy ma krawat na szyi, a zegarek i portmonetkę w kieszeniach, pan Ignacy wydobywał ze stolika wielki klucz i trochę zgarbiony, uroczyście otwierał tylne drzwi sklepu obite żelazną blachą. Wchodzili tam obaj ze służącym, zapalali parę płomyków gazu i podczas gdy służący zamiatał podłogę, pan Ignacy odczytywał przez binokle ze swego notatnika rozkład zajęć na dzień dzisiejszy.

„Oddać w banku osiemset rubli, aha… Do Lublina wysłać trzy albumy, tuzin portmonetek… Właśnie!… Do Wiednia przekaz na tysiąc dwieście guldenów… Z kolei odebrać transport… Zmonitować rymarza za nieodesłanie walizek… Bagatela!… Napisać list do Stasia… Bagatela…”

Skończywszy czytać, zapalał jeszcze kilka płomieni i przy ich blasku robił przegląd towarów w gablotkach i szafach.

„Spinki, szpilki, portmonety… dobrze… Rękawiczki, wachlarze, krawaty… tak jest… Laski, parasole, sakwojaże… A tu — albumy, neseserki… Szafirowy wczoraj sprzedano, naturalnie!… Lichtarze, kałamarze, przyciski… Porcelana… Ciekawym, dlaczego ten wazon odwrócili?… Z pewnością… Nie, nie uszkodzony… Lalki z włosami, teatr, karuzel… Trzeba na jutro postawić w oknie karuzel, bo już fontanna spowszedniała. Bagatela!… Ósma dochodzi… Założyłbym się, że Klejn będzie pierwszy, a Mraczewski ostatni. Naturalnie… Poznał się z jakąś guwernantką i już jej kupił neseserkę na rachunek i z rabatem… Rozumie się… Byle nie zaczął kupować bez rabatu i bez rachunku…”

Tak mruczał i chodził po sklepie przygarbiony, z rękoma w kieszeniach, a za nim jego pudel. Pan od czasu do czasu zatrzymywał się i oglądał jakiś przedmiot, pies przysiadał na podłodze i skrobał tylną nogą gęste kudły, a rzędem ustawione w szafie lalki małe, średnie i duże, brunetki i blondynki, przypatrywały się im martwymi oczami.

Drzwi od sieni skrzypnęły i ukazał się pan Klejn, mizerny subiekt, ze smutnym uśmiechem na posiniałych ustach.

— A co, byłem pewny, że pan przyjdziesz pierwszy. Dzień dobry — rzekł pan Ignacy. — Paweł! gaś światło i otwieraj sklep.

Służący wbiegł ciężkim kłusem i zakręcił gaz. Po chwili rozległo się zgrzytanie ryglów, szczękanie sztab i do sklepu wszedł dzień, jedyny gość, który nigdy nie zawodzi kupca. Rzecki usiadł przy kantorku pod oknem, Klejn stanął na zwykłym miejscu przy porcelanie.

— Pryncypał jeszcze nie wraca, nie miał pan listu? — spytał Klejn.

— Spodziewam się go w połowie marca, najdalej za miesiąc.

— Jeżeli go nie zatrzyma nowa wojna.

— Staś… Pan Wokulski — poprawił się Rzecki — pisze mi, że wojny nie będzie.

— Kursa jednak spadają, a przed chwilą czytałem, że flota angielska wpłynęła na Dardanele.

— To nic, wojny nie będzie. Zresztą — westchnął pan Ignacy — co nas obchodzi wojna, w której nie przyjmie udziału Bonaparte.

— Bonapartowie skończyli już karierę.

— Doprawdy?… — uśmiechnął się ironicznie pan Ignacy. — A na czyjąż korzyść MacMahon z Ducrotem układali w styczniu zamach stanu?… Wierz mi, panie Klejn, bonapartyzm to potęga!…

— Jest większa od niej.

— Jaka? — oburzył się pan Ignacy. — Może republika z Gambettą?… Może Bismarck?…

— Socjalizm… — szepnął mizerny subiekt kryjąc się za porcelanę.

Pan Ignacy mocniej zasadził binokle i podniósł się na swym fotelu, jakby pragnąc jednym zamachem obalić nową teorię, która przeciwstawiała się jego poglądom, lecz poplątało mu szyki wejście drugiego subiekta z brodą.

— A, moje uszanowanie panu Lisieckiemu! — zwrócił się do przybyłego. — Zimny dzień mamy, prawda? Która też godzina w mieście, bo mój zegarek musi się spieszyć. Jeszcze chyba nie ma kwadransa na dziewiątą?…

— Także koncept!… Pański zegarek zawsze spieszy się z rana, a późni wieczorem — odparł cierpko Lisiecki ocierając szronem pokryte wąsy.

— Założę się, żeś pan był wczoraj na preferansie.

— Ma się wiedzieć. Cóż pan myślisz, że mi na całą dobę wystarczy widok waszych galanterii i pańskiej siwizny?

— No, mój panie, wolę być trochę szpakowatym aniżeli łysym — oburzył się pan Ignacy.

— Koncept!… — syknął pan Lisiecki. — Moja łysina, jeżeli ją kto dojrzy, jest smutnym dziedzictwem rodu, ale pańska siwizna i gderliwy charakter są owocami starości, którą… chciałbym szanować.

Do sklepu wszedł pierwszy gość: kobieta ubrana w salopę i chustkę na głowie, żądająca mosiężnej spluwaczki… Pan Ignacy bardzo nisko ukłonił się jej i ofiarował krzesło, a pan Lisiecki zniknął za szafami i wróciwszy po chwili doręczył interesantce ruchem pełnym godności żądany przedmiot. Potem zapisał cenę spluwaczki na kartce, podał ją przez ramię Rzeckiemu i poszedł za gablotkę z miną bankiera, który złożył na cel dobroczynny kilka tysięcy rubli.

Spór o siwiznę i łysinę był zażegnany.

Dopiero około dziewiątej wszedł, a raczej wpadł do sklepu pan Mraczewski, piękny, dwudziestokilkoletni blondynek, z oczyma jak gwiazdy, ustami jak korale, z wąsikami jak zatrute sztylety. Wbiegł ciągnąc za sobą od progu smugę woni i zawołał:

— Słowo honoru daję, że musi już być wpół do dziesiątej. Letkiewicz jestem, gałgan jestem, no — podły jestem, ale cóż zrobię, kiedy matka mi zachorowała i musiałem szukać doktora. Byłem u sześciu…

— Czy u tych, którym dajesz pan neseserki? — spytał Lisiecki.

— Neseserki?… Nie. Nasz doktór nie przyjąłby nawet szpilki. Zacny człowiek… Prawda, panie Rzecki, że już jest wpół do dziesiątej? Stanął mi zegarek.

— Dochodzi *dziewiąta*… — odparł ze szczególnym naciskiem pan Ignacy.

— Dopiero dziewiąta?… No, kto by myślał! A tak projektowałem sobie, że dziś przyjdę do sklepu pierwszy, wcześniej od pana Klejna…

— Ażeby wyjść przed ósmą — wtrącił pan Lisiecki.

Mraczewski utkwił w nim błękitne oczy, w których malowało się najwyższe zdumienie.

— Pan skąd wie?… — odparł. — No, słowo honoru daję, że ten człowiek ma zmysł proroczy! Właśnie dziś, słowo honoru… muszę być na mieście przed siódmą, choćbym umarł, choćbym… miał podać się do dymisji…

— Niech pan od tego zacznie — wybuchnął Rzecki — a będzie pan wolny przed jedynastą, nawet w tej chwili, panie Mraczewski. Pan powinieneś być hrabią, nie kupcem, i dziwię się, że pan od razu nie wstąpił do tamtego fachu, przy którym zawsze ma się czas, panie Mraczewski. Naturalnie!

— No, i pan w jego wieku latałeś za spódniczkami — odezwał się Lisiecki. — Co tu bawić się w morały.

— Nigdy nie latałem! — krzyknął Rzecki uderzając pięścią w kantorek.

— Przynajmniej raz wygadał się, że całe życie jest niedołęgą — mruknął Lisiecki do Klejna, który uśmiechał się podnosząc jednocześnie brwi bardzo wysoko.

Do sklepu wszedł drugi gość i zażądał kaloszy. Naprzeciw niego wysunął się Mraczewski.

— Kaloszyków żąda szanowny pan? Który numerek, jeżeli wolno spytać? Ach, szanowny pan zapewne nie pamięta! Nie każdy ma czas myśleć o numerze swoich kaloszy, to należy do nas. Szanowny pan pozwoli, że przymierzymy?… Szanowny pan raczy zająć miejsce na taburecie. Paweł! przynieś ręcznik, zdejm panu kalosze i wytrzyj obuwie…

Wbiegł Paweł ze ścierką i rzucił się do nóg przybyłemu.

— Ależ, panie, ależ przepraszam!… — tłomaczył się odurzony gość.

— Bardzo prosimy — mówił prędko Mraczewski — to nasz obowiązek. Zdaje mi się, że te będą dobre — ciągnął podając parę sczepionych nitką kaloszy. — Doskonałe, pysznie wyglądają; szanowny pan ma tak normalną nogę, że niepodobna mylić się co do numeru. Szanowny pan życzy sobie zapewne literki; jakie mają być literki?…

— L. P. — mruknął gość czując, że tonie w bystrym potoku wymowy grzecznego subiekta.

— Panie Lisiecki, panie Klejn, przybijcie z łaski swojej literki. Szanowny pan każe zawinąć dawne kalosze? Paweł! wytrzyj kalosze i okręć w bibułę. A może szanowny pan nie życzy sobie dźwigać zbytecznego ciężaru? Paweł! rzuć kalosze do paki… Należy się dwa ruble kopiejek pięćdziesiąt… Kaloszy z literkami nikt szanownemu panu nie zamieni, a to przykra rzecz znaleźć w miejsce nowych artykułów dziurawe graty… Dwa ruble pięćdziesiąt kopiejek do kasy, z tą karteczką. Panie kasjerze, pięćdziesiąt kopiejek reszty dla szanownego pana…

Nim gość oprzytomniał, ubrano go w kalosze, wydano resztę i wśród niskich ukłonów odprowadzono do drzwi. Interesant stał przez chwilę na ulicy, bezmyślnie patrząc w szybę, spoza której Mraczewski darzył go słodkim uśmiechem i ognistymi spojrzeniami. Wreszcie machnął ręką i poszedł dalej, może myśląc, że w innym sklepie kalosze bez literek kosztowałyby go dziesięć złotych.

Pan Ignacy zwrócił się do Lisieckiego i kiwał głową w sposób oznaczający podziw i zadowolenie. Mraczewski dostrzegł ten ruch kątem oka i podbiegłszy do Lisieckiego, rzekł półgłosem:

— Niech no pan patrzy, czy nasz stary nie jest podobny z profilu do Napoleona III? Nos… wąs… hiszpanka…

— Do Napoleona, kiedy chorował na kamień — odparł Lisiecki.

Na ten dowcip pan Ignacy skrzywił się z niesmakiem. Swoją drogą Mraczewski dostał urlop przed siódmą wieczorem, a w parę dni później w prywatnym katalogu Rzeckiego otrzymał notatkę:

„Był na Hugonotach w ósmym rzędzie krzeseł z niejaką Matyldą…???”

Na pociechę mógłby sobie powiedzieć, że w tym samym katalogu równie posiadają notatki dwaj inni jego koledzy, a także inkasent, posłańcy, nawet — służący Paweł. Skąd Rzecki znał podobne szczegóły z życia swych współpracowników? Jest to tajemnica, z którą przed nikim się nie zwierzał.

Około pierwszej w południe pan Ignacy zdawszy kasę Lisieckiemu, któremu pomimo ciągłych sporów ufał najbardziej, wymykał się do swego pokoiku, ażeby zjeść obiad przyniesiony z restauracji. Współcześnie z nim wychodził Klejn i wracał do sklepu o drugiej; potem obaj z Rzeckim zostawali w sklepie, a Lisiecki i Mraczewski szli na obiad. O trzeciej znowu wszyscy byli na miejscu.

O ósmej wieczór zamykano sklep; subiekci rozchodzili się i zostawał tylko Rzecki. Robił dzienny rachunek, sprawdzał kasę, układał plan czynności na jutro i przypominał sobie: czy zrobiono wszystko, co wypadało na dziś? Każdą zaniedbaną sprawę opłacał długą bezsennością i smętnymi marzeniami na temat ruiny sklepu, stanowczego upadku Napoleonidów i tego, że wszystkie nadzieje, jakie miał w życiu, były tylko głupstwem.

„Nic nie będzie! Giniemy bez ratunku” — wzdychał przewracając się na twardej pościeli.

Jeżeli dzień udał się dobrze, pan Ignacy był kontent. Wówczas przed snem czytał historię konsulatu i cesarstwa albo wycinki z gazet opisujących wojnę włoską z roku 1859, albo też, co trafiało się rzadziej, wydobywał spod łóżka gitarę i grał na niej Marsza Rakoczego przyśpiewując wątpliwej wartości tenorem.

Potem śniły mu się obszerne węgierskie równiny, granatowe i białe linie wojsk, przysłoniętych chmurą dymu… Nazajutrz miewał posępny humor i skarżył się na ból głowy.

Do przyjemniejszych dni należała u niego niedziela; wówczas bowiem obmyślał i wykonywał plany wystaw okiennych na cały tydzień.

W jego pojęciu okna nie tylko streszczały zasoby sklepu, ale jeszcze powinny były zwracać uwagę przechodniów bądź najmodniejszym towarem, bądź pięknym ułożeniem, bądź figlem. Prawe okno przeznaczone dla galanteryj zbytkownych mieściło zwykle jakiś brąz, porcelanową wazę, całą zastawę buduarowego stolika, dokoła których ustawiały się albumy, lichtarze, portmonety, wachlarze, w towarzystwie lasek, parasoli i niezliczonej ilości drobnych, a eleganckich przedmiotów. W lewym znowu oknie, napełnionym okazami krawatów, rękawiczek, kaloszy i perfum, miejsce środkowe zajmowały zabawki, najczęściej poruszające się.

Niekiedy podczas tych samotnych zajęć w starym subiekcie budziło się dziecko. Wydobywał wtedy i ustawiał na stole wszystkie mechaniczne cacka. Był tam niedźwiedź wdrapujący się na słup, był piejący kogut, mysz, która biegała, pociąg, który toczył się po szynach, cyrkowy pajac, który cwałował na koniu, dźwigając drugiego pajaca, i kilka par, które tańczyły walca przy dźwiękach niewyraźnej muzyki. Wszystkie te figury pan Ignacy nakręcał i jednocześnie puszczał w ruch. A gdy kogut zaczął piać łopocząc sztywnymi skrzydłami, gdy tańczyły martwe pary, co chwilę potykając się i zatrzymując, gdy ołowiani pasażerowie pociągu, jadącego bez celu, zaczęli przypatrywać mu się ze zdziwieniem i gdy cały ten świat lalek, przy drgającym świetle gazu, nabrał jakiegoś fantastycznego życia, stary subiekt podparłszy się łokciami śmiał się cicho i mruczał:

— Hi! hi! hi! dokąd wy jedziecie, podróżni?… Dlaczego narażasz kark, akrobato?… Co wam po uściskach, tancerze?… Wykręcą się sprężyny i pójdziecie na powrót do szafy. Głupstwo, wszystko głupstwo!… a wam, gdybyście myśleli, mogłoby się zdawać, że to jest coś wielkiego!…

Po takich i tym podobnych monologach szybko składał zabawki i rozdrażniony chodził po pustym sklepie, a za nim jego brudny pies.

„Głupstwo handel… głupstwo polityka… głupstwo podróż do Turcji… głupstwo całe życie, którego początku nie pamiętamy, a końca nie znamy… Gdzież prawda?…”

Ponieważ tego rodzaju zdania wypowiadał niekiedy głośno i publicznie, więc uważano go za bzika, a poważne damy, mające córki na wydaniu, nieraz mówiły.

— Oto do czego prowadzi mężczyznę starokawalerstwo!

Z domu pan Ignacy wychodził rzadko i na krótko i zwykle kręcił się po ulicach, na których mieszkali jego koledzy albo oficjaliści sklepu. Wówczas jego ciemnozielona algierka lub tabaczkowy surdut, popielate spodnie z czarnym lampasem i wypłowiały cylinder, nade wszystko zaś jego nieśmiałe zachowanie się zwracały powszechną uwagę. Pan Ignacy wiedział to i coraz bardziej zniechęcał się do spacerów. Wolał przy święcie kłaść się na łóżku i całymi godzinami patrzeć w swoje zakratowane okno, za którym widać było szary mur sąsiedniego domu, ozdobiony jednym jedynym, również zakratowanym oknem, gdzie czasami stał garnczek masła albo wisiały zwłoki zająca.

Lecz im mniej wychodził, tym częściej marzył o jakiejś dalekiej podróży na wieś lub za granicę. Coraz częściej spotykał we snach zielone pola i ciemne bory, po których błąkałby się, przypominając sobie młode czasy. Powoli zbudziła się w nim głucha tęsknota do tych krajobrazów, więc postanowił natychmiast po powrocie Wokulskiego wyjechać gdzieś na całe lato.

— Choć raz przed śmiercią, ale na kilka miesięcy — mówił kolegom, którzy nie wiadomo dlaczego uśmiechali się z tych projektów.

Dobrowolnie odcięty od natury i ludzi, utopiony w wartkim, ale ciasnym wirze sklepowych interesów, czuł coraz mocniej potrzebę wymiany myśli. A ponieważ jednym nie ufał, inni go nie chcieli słuchać, a Wokulskiego nie było, więc rozmawiał sam z sobą i — w największym sekrecie pisywał pamiętnik.



III. Pamiętnik starego subiekta

…Ze smutkiem od kilku lat uważam, że na świecie jest coraz mniej dobrych subiektów i rozumnych polityków, bo wszyscy stosują się do mody. Skromny subiekt co kwartał ubiera się w spodnie nowego fasonu, w coraz dziwniejszy kapelusz i coraz inaczej wykładany kołnierzyk. Podobnież dzisiejsi politycy co kwartał zmieniają wiarę: onegdaj wierzyli w Bismarcka, wczoraj w Gambettę, a dziś w Beaconsfielda, który niedawno był Żydkiem.

Już widać zapomniano, że w sklepie nie można stroić się w modne kołnierzyki, tylko je sprzedawać, bo w przeciwnym razie gościom zabraknie towaru, a sklepowi gości. Zaś polityki nie należy opierać na szczęśliwych osobach, tylko na wielkich dynastiach. Metternich był taki sławny jak Bismarck, a Palmerston sławniejszy od Beaconsfielda i — któż dziś o nich pamięta? Tymczasem ród Bonapartych trząsł Europą za Napoleona I, potem za Napoleona III, a i dzisiaj, choć niektórzy nazywają go bankrutem, wpływa na losy Francji przez wierne swoje sługi, MacMahona i Ducrota.

Zobaczycie, co jeszcze zrobi Napoleonek IV, który po cichu uczy się sztuki wojennej u Anglików! Ale o to mniejsza. W tej bowiem pisaninie chcę mówić nie o Bonapartym, ale o sobie, ażeby wiedziano, jakim sposobem tworzyli się dobrzy subiekci i choć nie uczeni, ale rozsądni politycy. Do takiego interesu nie trzeba akademii, lecz przykładu — w domu i w sklepie.

Ojciec mój był za młodu żołnierzem, a na starość woźnym w Komisji Spraw Wewnętrznych. Trzymał się prosto jak sztaba, miał nieduże faworyty i wąs do góry; szyję okręcał czarną chustką i nosił srebrny kolczyk w uchu.

Mieszkaliśmy na Starym Mieście z ciotką, która urzędnikom prała i łatała bieliznę. Mieliśmy na czwartym piętrze dwa pokoiki, gdzie niewiele było dostatków, ale dużo radości, przynajmniej dla mnie. W naszej izdebce najokazalszym sprzętem był stół, na którym ojciec powróciwszy z biura kleił koperty; u ciotki zaś pierwsze miejsce zajmowała balia. Pamiętam, że w pogodne dnie puszczałem na ulicy latawce, a w razie słoty wydmuchiwałem w izbie bańki mydlane.

Na ścianach u ciotki wisieli sami święci; ale jakkolwiek było ich sporo, nie dorównali jednak liczbą Napoleonom, którymi ojciec przyozdabiał swój pokój. Był tam jeden Napoleon w Egipcie, drugi pod Wagram, trzeci pod Austerlitz, czwarty pod Moskwą, piąty w dniu koronacji, szósty w apoteozie. Gdy zaś ciotka zgorszona tyloma świeckimi obrazami, zawiesiła na ścianie mosiężny krucyfiks, ojciec, ażeby — jak mówił — nie obrazić Napoleona, kupił sobie jego brązowe popiersie i także umieścił je nad łóżkiem.

— Zobaczysz, niedowiarku — lamentowała nieraz ciotka — że za te sztuki będą cię pławić w smole.

— I!… Nie da mi cesarz zrobić krzywdy — odpowiadał ojciec.

Często przychodzili do nas dawni koledzy ojca: pan Domański, także woźny, ale z Komisji Skarbu, i pan Raczek, który na Dunaju miał stragan z zieleniną. Prości to byli ludzie (nawet pan Domański trochę lubił anyżówkę), ale roztropni politycy. Wszyscy, nie wyłączając ciotki, twierdzili jak najbardziej stanowczo, że choć Napoleon I umarł w niewoli, ród Bonapartych jeszcze wypłynie. Po pierwszym Napoleonie znajdzie się jakiś drugi, a gdyby i ten źle skończył, przyjdzie następny, dopóki jeden po drugim nie uporządkują świata.

— Trzeba być zawsze gotowym na pierwszy odgłos! — mówił mój ojciec.

— Bo nie wiecie dnia ani godziny — dodawał pan Domański.

A pan Raczek, trzymając fajkę w ustach, na znak potwierdzenia pluł aż do pokoju ciotki.

— Napluj mi acan w balię, to ci dam!… — wołała ciotka.

— Może jejmość i dasz, ale ja nie wezmę — mruknął pan Raczek plując w stronę komina.

— U… cóż to za chamy te całe grenadierzyska! — gniewała się ciotka.

— Jejmości zawsze smakowali ułani. Wiem, wiem…

Później pan Raczek ożenił się z moją ciotką…

…Chcąc, ażebym zupełnie był gotów, gdy wybije godzina sprawiedliwości, ojciec sam pracował nad moją edukacją.

Nauczył mię czytać, pisać, kleić koperty, ale nade wszystko — musztrować się. Do musztry zapędzał mnie w bardzo wczesnym dzieciństwie, kiedy mi jeszcze zza pleców wyglądała koszula. Dobrze to pamiętam, gdyż ojciec komenderując: „Pół obrotu na prawo!” albo „Lewe ramię naprzód — marsz!…”, ciągnął mnie w odpowiednim kierunku za ogon tego ubrania.

Była to najdokładniej prowadzona nauka.

Nieraz w nocy budził mnie ojciec krzykiem: „Do broni!…”, musztrował pomimo wymyślań i łez ciotki i kończył zdaniem:

— Ignaś! zawsze bądź gotów, wisusie, bo nie wiemy dnia ani godziny… Pamiętaj, że Bonapartów Bóg zesłał, ażeby zrobili porządek na świecie, a dopóty nie będzie porządku ani sprawiedliwości, dopóki nie wypełni się testament cesarza.

Nie mogę powiedzieć, ażeby niezachwianą wiarę mego ojca w Bonapartych i sprawiedliwość podzielali dwaj jego koledzy. Nieraz pan Raczek, kiedy mu dokuczył ból w nodze, klnąc i stękając mówił:

— E! wiesz, stary, że już za długo czekamy na nowego Napoleona. Ja siwieć zaczynam i coraz gorzej podupadam, a jego jak nie było, tak i nie ma. Niedługo porobią się z nas dziady pod kościół, a Napoleon po to chyba przyjdzie, ażeby z nami śpiewać godzinki.

— Znajdzie młodych.

— Co za młodych! Lepsi z nich przed nami poszli w ziemię, a najmłodsi — diabła warci. Już są między nimi i tacy, co o Napoleonie nie słyszeli.

— Mój słyszał i zapamięta — odparł ojciec mrugając okiem w moją stronę.

Pan Domański jeszcze bardziej upadał na duchu.

— Świat idzie do gorszego — mówił trzęsąc głową. — Wikt coraz droższy, za kwaterę zabraliby ci całą pensję, a nawet co się tyczy anyżówki, i w tym jest szachrajstwo. Dawniej rozweseliłeś się kieliszkiem, dziś po szklance jesteś taki czczy, jakbyś się napił wody. Sam Napoleon nie doczekałby się sprawiedliwości!

A na to odpowiedział ojciec:

— Będzie sprawiedliwość, choćby i Napoleona nie stało. Ale i Napoleon się znajdzie.

— Nie wierzę — mruknął pan Raczek.

— A jak się znajdzie, to co?… — spytał ojciec.

— Nie doczekamy tego.

— Ja doczekam — odparł ojciec — a Ignaś doczeka jeszcze lepiej.

Już wówczas zdania mego ojca głęboko wyrzynały mi się w pamięci, ale dopiero późniejsze wypadki nadały im cudowny, nieomal proroczy charakter.

Około roku 1840 ojciec zaczął niedomagać. Czasami po parę dni nie wychodził do biura, a wreszcie na dobre legł w łóżku.

Pan Raczek odwiedzał go co dzień, a raz patrząc na jego chude ręce i wyżółkłe policzki szepnął:

— Hej! stary, już my chyba nie doczekamy się Napoleona.

Na co ojciec spokojnie odparł:

— Ja tam nie umrę, dopóki o nim nie usłyszę.

Pan Raczek pokiwał głową, a ciotka łzy otarła myśląc, że ojciec bredzi. Jak tu myśleć inaczej, jeżeli śmierć już kołatała do drzwi, a ojciec jeszcze wyglądał Napoleona…

Było już z nim bardzo źle, nawet przyjął ostatnie sakramenta, kiedy w parę dni później wbiegł do nas pan Raczek dziwnie wzburzony i stojąc na środku izby zawołał:

— A wiesz, stary, że znalazł się Napoleon?…

— Gdzie? — krzyknęła ciotka.

— Jużci we Francji.

Ojciec zerwał się, lecz znowu upadł na poduszki. Tylko wyciągnął do mnie rękę i patrząc wzrokiem, którego nie zapomnę, wyszeptał:

— Pamiętaj!… Wszystko pamiętaj…

Z tym umarł.

W późniejszym życiu przekonałem się, jak proroczymi były poglądy ojca. Wszyscy widzieliśmy drugą gwiazdę napoleońską, która obudziła Włochy i Węgry; a chociaż spadła pod Sedanem, nie wierzę w jej ostateczne zagaśnięcie. Co mi tam Bismarck, Gambetta albo Beaconsfield! Niesprawiedliwość dopóty będzie władać światem, dopóki nowy Napoleon nie urośnie.

W parę miesięcy po śmierci ojca pan Raczek i pan Domański wraz z ciotką Zuzanną zebrali się na radę: co ze mną począć? Pan Domański chciał mnie zabrać do swoich biur i powoli wypromować na urzędnika; ciotka zalecała rzemiosło, a pan Raczek zieleniarstwo. Lecz gdy zapytano mnie: do czego mam ochotę? odpowiedziałem, że do sklepu.

— Kto wie, czy to nie będzie najlepsze — zauważył pan Raczek. — A do jakiegoż byś chciał kupca?

— Do tego na Podwalu, co ma we drzwiach pałasz, a w oknie kozaka.

— Wiem — wtrąciła ciotka. — On chce do Mincla.

— Można spróbować — rzekł pan Domański. — Wszyscy przecież znamy Mincla.

Pan Raczek na znak zgody plunął aż w komin.

— Boże miłosierny — jęknęła ciotka — ten drab już chyba na mnie pluć zacznie, kiedy brata nie stało… Oj! nieszczęśliwa ja sierota!…

— Wielka rzecz! — odezwał się pan Raczek. — Wyjdź jejmość za mąż, to nie będziesz sierotą.

— A gdzież ja znajdę takiego głupiego, co by mnie wziął?

— Phi! może i ja bym się ożenił z jejmością, bo nie ma mnie kto smarować — mruknął pan Raczek, ciężko schylając się do ziemi, ażeby wypukać popiół z fajki. Ciotka rozpłakała się, a wtedy odezwał się pan Domański:

— Po co robić duże ceregiele. Jejmość nie masz opieki, on nie ma gospodyni; pobierzcie się i przygarnijcie Ignasia, a będziecie nawet mieli dziecko. Jeszcze tanie dziecko, bo Mincel da mu wikt i kwaterę, a wy tylko odzież.

— Hę?… — spytał pan Raczek patrząc na ciotkę.

— No, oddajcie pierwej chłopca do terminu, a potem… może się odważę — odparła ciotka. — Zawsze miałam przeczucie, że marnie skończę…

— To i jazda do Mincla! — rzekł pan Raczek podnosząc się z krzesełka. — Tylko jejmość nie zrób mi zawodu! — dodał grożąc ciotce pięścią.

Wyszli z panem Domańskim i może w półtorej godziny wrócili obaj mocno zarumienieni. Pan Raczek ledwie oddychał, a pan Domański z trudnością trzymał się na nogach, podobno z tego, że nasze schody były bardzo niewygodne.

— Cóż?… — spytała ciotka.

— Nowego Napoleona wsadzili do prochowni! — odpowiedział pan Domański.

— Nie do prochowni, tylko do fortecy. A–u… A–u… — dodał pan Raczek i rzucił czapkę na stół.

— Ale z chłopcem co?

— Jutro ma przyjść do Mincla z odzieniem i bielizną — odrzekł pan Domański. — Nie do fortecy A–u…, A–u… tylko do Ham–ham czy Cham… bo nawet nie wiem…

— Zwariowaliście, pijaki! — krzyknęła ciotka chwytając pana Raczka za ramię.

— Tylko bez poufałości! — oburzył się pan Raczek. — Po ślubie będzie poufałość, teraz… Ma przyjść do Mincla jutro z bielizną i odzieniem… Nieszczęsny Napoleonie!…

Ciotka wypchnęła za drzwi pana Raczka, potem pana Domańskiego i wyrzuciła za nimi czapkę.

— Precz mi stąd, pijaki!

— Wiwat Napoleon! — zawołał pan Raczek, a pan Domański zaczął śpiewać:


Przechodniu, gdy w tę stronę zwrócisz swoje oko,
Przybliż się i rozważaj ten napis głęboko…
Przybliż się i rozważaj ten napis głęboko.

Głos jego stopniowo cichnął, jakby zagłębiając się w studni, potem umilkł na schodach, lecz znowu doleciał nas z ulicy. Po chwili zrobił się tam jakiś hałas, a gdy wyjrzałem oknem, zobaczyłem, że pana Raczka policjant prowadził do ratusza.

Takie to wypadki poprzedziły moje wejście do zawodu kupieckiego.

Sklep Mincla znałem od dawna, ponieważ ojciec wysyłał mnie do niego po papier, a ciotka po mydło. Zawsze biegłem tam z radosną ciekawością, ażeby napatrzeć się wiszącym za szybami zabawkom. O ile pamiętam, był tam w oknie duży kozak, który sam przez się skakał i machał rękoma, a we drzwiach — bęben, pałasz i skórzany koń z prawdziwym ogonem.

Wnętrze sklepu wyglądało jak duża piwnica, której końca nigdy nie mogłem dojrzeć z powodu ciemności. Wiem tylko, że po pieprz, kawę i liście bobkowe szło się na lewo do stołu, za którym stały ogromne szafy od sklepienia do podłogi napełnione szufladami. Papier zaś, atrament, talerze i szklanki sprzedawano przy stole na prawo, gdzie były szafy z szybami, a po mydło i krochmal szło się w głąb sklepu, gdzie było widać beczki i stosy pak drewnianych.

Nawet sklepienie było zajęte. Wisiały tam długie szeregi pęcherzy naładowanych gorczycą i farbami, ogromna lampa z daszkiem, która w zimie paliła się cały dzień, sieć pełna korków do butelek, wreszcie — wypchany krokodylek, długi może na półtora łokcia.

Właścicielem sklepu był Jan Mincel, starzec z rumianą twarzą i kosmykiem siwych włosów pod brodą. W każdej porze dnia siedział on pod oknem na fotelu obitym skórą, ubrany w niebieski barchanowy kaftan, biały fartuch i takąż szlafmycę. Przed nim na stole leżała wielka księga, w której notował dochód, a tuż nad jego głową wisiał pęk dyscyplin, przeznaczonych głównie na sprzedaż. Starzec odbierał pieniądze, zdawał gościom resztę, pisał w księdze, niekiedy drzemał, lecz pomimo tylu zajęć, z niepojętą uwagą czuwał nad biegiem handlu w całym sklepie. On także, dla uciechy przechodniów ulicznych, od czasu do czasu pociągał za sznurek skaczącego w oknie kozaka i on wreszcie, co mi się najmniej podobało, za rozmaite przestępstwa karcił nas jedną z pęka dyscyplin.

Mówię: nas, bo było nas trzech kandydatów do kary cielesnej: ja tudzież dwaj synowcy starego — Franc i Jan Minclowie.

Czujności pryncypała i jego biegłości w używaniu sarniej nogi doświadczyłem zaraz na trzeci dzień po wejściu do sklepu.

Franc odmierzył jakiejś kobiecie za dziesięć groszy rodzynków. Widząc, że jedno ziarno upadło na kontuar (stary miał w tej chwili oczy zamknięte), podniosłem je nieznacznie i zjadłem. Chciałem właśnie wyjąć pestkę, która wcisnęła mi się między zęby, gdy uczułem na plecach coś, jakby mocne dotknięcie rozpalonego żelaza.

— A, szelma! — wrzasnął stary Mincel i nim zdałem sobie sprawę z sytuacji, przeciągnął po mnie jeszcze parę razy dyscyplinę, od wierzchu głowy do podłogi.

Zwinąłem się w kłębek z bólu, lecz od tej pory nie śmiałem wziąć do ust niczego w sklepie. Migdały, rodzynki, nawet rożki miały dla mnie smak pieprzu.

Urządziwszy się ze mną w taki sposób, stary zawiesił dyscyplinę na pęku, wpisał rodzynki i z najdobroduszniejszą miną począł ciągnąć za sznurek kozaka. Patrząc na jego półuśmiechniętą twarz i przymrużone oczy, prawie nie mogłem wierzyć, że ten jowialny staruszek posiada taki zamach w ręku. I dopiero teraz spostrzegłem, że ów kozak widziany z wnętrza sklepu wydaje się mniej zabawnym niż od ulicy.

Sklep nasz był kolonialno-galanteryjno-mydlarski. Towary kolonialne wydawał gościom Franc Mincel, młodzieniec trzydziestokilkoletni, z rudą głową i zaspaną fizjognomią. Ten najczęściej dostawał dyscypliną od stryja, gdyż palił fajkę, późno wchodził za kontuar, wymykał się z domu po nocach, a nade wszystko niedbale ważył towar. Młodszy zaś, Jan Mincel, który zawiadywał galanterią i obok niezgrabnych ruchów odznaczał się łagodnością, był znowu bity za wykradanie kolorowego papieru i pisywanie na nim listów do panien.

Tylko August Katz, pracujący przy mydle, nie ulegał żadnym surowcowym upomnieniom. Mizerny ten człeczyna odznaczał się niezwykłą punktualnością. Najraniej przychodził do roboty, krajał mydło i ważył krochmal jak automat; jadł, co mu podano, w najciemniejszym kącie sklepu, prawie wstydząc się tego, że doświadcza ludzkich potrzeb. O dziesiątej wieczorem gdzieś znikał.

W tym otoczeniu upłynęło mi osiem lat, z których każdy dzień był podobny do wszystkich innych dni, jak kropla jesiennego deszczu do innych kropli jesiennego deszczu. Wstawałem rano o piątej, myłem się i zamiatałem sklep. O szóstej otwierałem główne drzwi tudzież okiennicę. W tej chwili gdzieś z ulicy zjawiał się August Katz, zdejmował surdut, kładł fartuch i milcząc stawał między beczką mydła szarego a kolumną ułożoną z cegiełek mydła żółtego. Potem drzwiami od podwórka wbiegał stary Mincel mrucząc: Morgen!, poprawiał szlafmycę, dobywał z szuflady księgę, wciskał się w fotel i parę razy ciągnął za sznurek kozaka. Dopiero po nim ukazywał się Jan Mincel i ucałowawszy stryja w rękę stawał za swoim kontuarem, na którym podczas lata łapał muchy, a w zimie kreślił palcem albo pięścią jakieś figury.

Franca zwykle sprowadzano do sklepu. Wchodził z oczyma zaspanymi, ziewający, obojętnie całował stryja w ramię i przez cały dzień skrobał się w głowę w sposób, który mógł oznaczać wielką senność lub wielkie zmartwienie. Prawie nie było ranka, ażeby stryj patrząc na jego manewry nie wykrzywiał mu się i nie pytał:

— No… a gdzie, ty szelma, latała?

Tymczasem na ulicy budził się szmer i za szybami sklepu coraz częściej przesuwali się przechodnie. To służąca, to drwal, jejmość w kapturze, to chłopak od szewca, to jegomość w rogatywce szli w jedną i drugą stronę jak figury w ruchomej panoramie. Środkiem ulicy toczyły się wozy, beczki, bryczki — tam i na powrót… Coraz więcej ludzi, coraz więcej wozów, aż nareszcie utworzył się jeden wielki potok uliczny, z którego co chwilę ktoś wpadał do nas za sprawunkiem.

— Pieprzu za trojaka…

— Proszę funt kawy…

— Niech pan da ryżu…

— Pół funta mydła…

— Za grosz liści bobkowych…

Stopniowo sklep zapełniał się po największej części służącymi i ubogo odzianymi jejmościami. Wtedy Franc Mincel krzywił się najwięcej: otwierał i zamykał szuflady, obwijał towar w tutki z szarej bibuły, wbiegał na drabinkę, znowu zwijał, robiąc to wszystko z żałosną miną człowieka, któremu nie pozwalają ziewnąć. W końcu zbierało się takie mnóstwo interesantów, że i Jan Mincel, i ja musieliśmy pomagać Francowi w sprzedaży.

Stary wciąż pisał i zdawał resztę, od czasu do czasu dotykając palcami swojej białej szlafmycy, której niebieski kutasik zwieszał mu się nad okiem. Czasem szarpnął kozaka, a niekiedy z szybkością błyskawicy zdejmował dyscyplinę i ćwiknął nią którego ze swych synowców. Nader rzadko mogłem zrozumieć: o co mu chodzi? synowcy bowiem niechętnie objaśniali mi przyczyny jego popędliwości.

Około ósmej napływ interesantów zmniejszał się. Wtedy w głębi sklepu ukazywała się gruba służąca z koszem bułek i kubkami (Franc odwracał się do niej tyłem), a za nią — matka naszego pryncypała, chuda staruszka w żółtej sukni, w ogromnym czepcu na głowie, z dzbankiem kawy w rękach. Ustawiwszy na stole swoje naczynie, staruszka odzywała się schrypniętym głosem:

— Gut Morgen, meine Kinder! Der Kaffee ist schon fertig…

I zaczynała rozlewać kawę w białe fajansowe kubki.

Wówczas zbliżał się do niej stary Mincel i całował ją w rękę mówiąc:

— Gut Morgen, meine Mutter!

Za co dostawał kubek kawy z trzema bułkami.

Potem przychodził Franc Mincel, Jan Mincel, August Katz, a na końcu ja. Każdy całował staruszkę w suchą rękę, porysowaną niebieskimi żyłami, każdy mówił:

— Gut Morgen, Grossmutter!

I otrzymywał należny mu kubek tudzież trzy bułki.

A gdyśmy z pośpiechem wypili naszą kawę, służąca zabierała pusty kosz i zamazane kubki, staruszka swój dzbanek i obie znikały.

Za oknem wciąż toczyły się wozy i płynął w obie strony potok ludzki, z którego co chwila odrywał się ktoś i wchodził do sklepu.

— Proszę krochmalu…

— Dać migdałów za dziesiątkę…

— Lukrecji za grosz…

— Szarego mydła…

Około południa zmniejszał się ruch za kontuarem towarów kolonialnych, a za to coraz częściej zjawiali się interesanci po stronie prawej sklepu, u Jana. Tu kupowano talerze, szklanki, żelazka, młynki, lalki, a niekiedy duże parasole, szafirowe lub pąsowe. Nabywcy, kobiety i mężczyźni, byli dobrze ubrani, rozsiadali się na krzesłach i kazali sobie pokazywać mnóstwo przedmiotów targując się i żądając coraz to nowych.

Pamiętam, że kiedy po lewej stronie sklepu męczyłem się bieganiną i zawijaniem towarów, po prawej — największe strapienie robiła mi myśl: czego ten a ten gość chce naprawdę i — czy co kupi? W rezultacie jednak i tutaj dużo się sprzedawało; nawet dzienny dochód z galanterii był kilka razy większy aniżeli z towarów kolonialnych i mydła.

Stary Mincel i w niedzielę bywał w sklepie. Rano modlił się, a około południa kazał mi przychodzić do siebie na pewien rodzaj lekcji.

— Sag mir — powiedz mi: was ist das? co to jest? Das ist Schublade — to jest szublada. Zobacz, co jest w te szublade. Es ist Zimmt — to jest cynamon. Do czego potrzebuje się cynamon? do zupe, do legumine potrzebuje się cynamon. Co to jest cynamon? Jest taki kora z jedne drzewo. Gdzie mieszka taki drzewo cynamon? W Indii mieszka taki drzewo. Patrz na globus — tu leży Indii. Daj mnie za dziesiątkę cynamon… O, du Spitzbub!… jak tobie dam dziesięć razy dyscyplin, ty będziesz wiedział, ile sprzedać za dziesięć groszy cynamon…

W ten sposób przechodziliśmy każdą szufladę w sklepie i historię każdego towaru. Gdy zaś Mincel nie był zmęczony, dyktował mi jeszcze zadania rachunkowe, kazał sumować księgi albo pisywać listy w interesach naszego sklepu.

Mincel był bardzo porządny, nie cierpiał kurzu, ścierał go z najdrobniejszych przedmiotów. Jednych tylko dyscyplin nigdy nie potrzebował okurzać dzięki swoim niedzielnym wykładom buchalterii, jeografii i towaroznawstwa.

Powoli, w ciągu paru lat, tak przywykliśmy do siebie, że stary Mincel nie mógł obejść się beze mnie, a ja nawet jego dyscypliny począłem uważać za coś, co należało do familijnych stosunków. Pamiętam, że nie mogłem utulić się z żalu, gdy raz zepsułem kosztowny samowar, a stary Mincel zamiast chwytać za dyscyplinę — odezwał się:

— Co ty zrobila, Ignac?… Co ty zrobila!…

Wolałbym dostać cięgi wszystkimi dyscyplinami, aniżeli znowu kiedy usłyszeć ten drżący głos i zobaczyć wylęknione spojrzenie pryncypała.

Obiady w dzień powszedni jadaliśmy w sklepie, naprzód dwaj młodzi Minclowie i August Katz, a następnie ja z pryncypałem. W czasie święta wszyscy zbieraliśmy się na górze i zasiadaliśmy do jednego stołu. Na każdą Wigilię Bożego Narodzenia Mincel dawał nam podarunki, a jego matka w największym sekrecie urządzała nam (i swemu synowi) choinkę. Wreszcie w pierwszym dniu miesiąca wszyscy dostawaliśmy pensję (ja brałem 10 złotych). Przy tej okazji każdy musiał wylegitymować się z porobionych oszczędności: ja, Katz, dwaj synowcy i służba. Nierobienie oszczędności, a raczej nieodkładanie co dzień choćby kilku groszy, było w oczach Mincla takim występkiem jak kradzież. Za mojej pamięci przewinęło się przez nasz sklep paru subiektów i kilku uczniów, których pryncypał dlatego tylko usunął, że nic sobie nie oszczędzili. Dzień, w którym się to wydało, był ostatnim ich pobytu. Nie pomogły obietnice, zaklęcia, całowania po rękach, nawet upadanie do nóg. Stary nie ruszył się z fotelu, nie patrzył na petentów, tylko wskazując palcem drzwi wymawiał jeden wyraz: fort! fort!… Zasada robienia oszczędności stała się już u niego chorobliwym dziwactwem.

Dobry ten człowiek miał jedną wadę, oto — nienawidził Napoleona. Sam nigdy o nim nie wspominał, lecz na dźwięk nazwiska Bonapartego dostawał jakby ataku wścieklizny; siniał na twarzy, pluł i wrzeszczał: szelma! szpitzbub! rozbójnik!…

Usłyszawszy pierwszy raz tak szkaradne wymysły nieomal straciłem przytomność. Chciałem coś hardego powiedzieć staremu i uciec do pana Raczka, który już ożenił się z moją ciotką. Nagle dostrzegłem, że Jan Mincel zasłoniwszy usta dłonią coś mruczy i robi miny do Katza. Wytężam słuch i — oto co mówi Jan:

— Baje stary, baje! Napoleon był chwat, choćby za to samo, że wygnał hyclów Szwabów. Nieprawda, Katz?

A August Katz zmrużył oczy i dalej krajał mydło.

Osłupiałem ze zdziwienia, lecz w tej chwili bardzo polubiłem Jana Mincla i Augusta Katza. Z czasem przekonałem się, że w naszym małym sklepie istnieją aż dwa wielkie stronnictwa, z których jedno, składające się ze starego Mincla i jego matki, bardzo lubiło Niemców, a drugie, złożone z młodych Minclów i Katza, nienawidziło ich. O ile pamiętam, ja tylko byłem neutralny.

W roku 1846 doszły nas wieści o ucieczce Ludwika Napoleona z więzienia. Rok ten był dla mnie ważny, gdyż zostałem subiektem, a nasz pryncypał, stary Jan Mincel, zakończył życie z powodów dosyć dziwnych.

W roku tym handel w naszym sklepie nieco osłabnął, już to z racji ogólnych niepokojów, już z tej, że i pryncypał za często i za głośno wymyślał na Ludwika Napoleona. Ludzie poczęli zniechęcać się do nas, a nawet ktoś (może Katz?…) wybił nam jednego dnia szybę w oknie.

Otóż wypadek ten, zamiast całkiem odstręczyć publiczność, zwabił ją do sklepu i przez tydzień mieliśmy tak duże obroty jak nigdy; aż zazdrościli nam sąsiedzi. Po tygodniu jednakże sztuczny ruch na nowo osłabnął i znowu były w sklepie pustki.

Pewnego wieczora w czasie nieobecności pryncypała, co już stanowiło fakt niezwykły, wpadł nam drugi kamień do sklepu. Przestraszeni Minclowie pobiegli na górę i szukali stryja, Katz poleciał na ulicę szukać sprawcy zniszczenia, a wtem ukazało się dwu policjantów ciągnących… Proszę zgadnąć kogo?… Ani mniej, ani więcej — tylko naszego pryncypała oskarżając go, że to on wybił szybę teraz, a zapewne i poprzednio…

Na próżno staruszek wypierał się: nie tylko bowiem widziano jego zamach, ale jeszcze znaleziono przy nim kamień… Poszedł też nieborak do ratusza.

Sprawa po wielu tłomaczeniach i wyjaśnieniach naturalnie zatarła się; ale stary od tej chwili zupełnie stracił humor i począł chudnąć. Pewnego zaś dnia usiadłszy na swym fotelu pod oknem już nie podniósł się z niego. Umarł oparty brodą na księdze handlowej, trzymając w ręce sznurek, którym poruszał kozaka.

Przez kilka lat po śmierci stryja synowcy prowadzili wspólnie sklep na Podwalu i dopiero około 1850 roku podzielili się w ten sposób, że Franc został na miejscu z towarami kolonialnymi, a Jan z galanterią i mydłem przeniósł się na Krakowskie, do lokalu, który zajmujemy obecnie. W kilka lat później Jan ożenił się z piękną Małgorzatą Pfeifer, ona zaś (niech spoczywa w spokoju) zostawszy wdową oddała rękę swoją Stasiowi Wokulskiemu, który tym sposobem odziedziczył interes prowadzony przez dwa pokolenia Minclów.

Matka naszego pryncypała żyła jeszcze długi czas; kiedy w roku 1853 wróciłem z zagranicy, zastałem ją w najlepszym zdrowiu. Zawsze schodziła rano do sklepu i zawsze mówiła:

— Gut Morgen meine Kinder! Der Kaffee ist schon fertig…

Tylko głos jej z roku na rok przyciszał się, dopóki wreszcie nie umilknął na wieki.

Za moich czasów pryncypał był ojcem i nauczycielem praktykantów i najczujniejszym sługą sklepu; jego matka lub żona były gospodyniami, a wszyscy członkowie rodziny pracownikami. Dziś pryncypał bierze tylko dochody z handlu, najczęściej nie zna go i najwięcej troszczy się o to, ażeby jego dzieci nie zostały kupcami. Nie mówię tu o Stasiu Wokulskim, który ma szersze zamiary, tylko myślę w ogólności, że kupiec powinien siedzieć w sklepie i wyrabiać sobie ludzi, jeżeli chce mieć porządnych.

Słychać, że Andrassy zażądał sześćdziesięciu milionów guldenów na nieprzewidziane wydatki. Więc i Austria zbroi się, a tymczasem Staś pisze mi, że — nie będzie wojny. Ponieważ nigdy nie był fanfaronem, więc chyba być musi bardzo wtajemniczonym w politykę; a w takim razie siedzi w Bułgarii nie przez miłość do handlu.

Ciekawym, co on zrobi! Ciekawym!…



IV. Powrót

Jest niedziela, szkaradny dzień marcowy; zbliża się południe, lecz ulice Warszawy są prawie puste. Ludzie nie wychodzą z domów albo kryją się w bramach, albo skuleni uciekają przed siekącym ich deszczem i śniegiem. Prawie nie słychać turkotu dorożek, gdyż dorożki stoją. Dorożkarze opuściwszy kozioł wchodzą pod budy swoich powozów, a zmoczone deszczem i zasypane śniegiem konie wyglądają tak, jakby pragnęły schować się pod dyszel i nakryć własnymi uszami.

Pomimo, a może z powodu tak brzydkiego czasu pan Ignacy siedzący w swoim zakratowanym pokoju jest bardzo wesół. Interesa sklepowe idą wybornie, wystawa w oknach na przyszły tydzień już ułożona, a nade wszystko — lada dzień ma powrócić Wokulski. Nareszcie pan Ignacy zda komuś rachunki i ciężar kierowania sklepem, najdalej zaś za dwa miesiące wyjedzie sobie na wakacje. Po dwudziestu pięciu latach pracy — i jeszcze jakiej! — należy mu się ten wypoczynek. Będzie rozmyślał tylko o polityce, będzie chodził, będzie biegał i skakał po polach i lasach, będzie świstał, a nawet śpiewał jak za młodu. Gdyby nie te bóle reumatyczne, które zresztą na wsi ustąpią…

Więc choć deszcz ze śniegiem bije w zakratowane okna, choć pada tak gęsto, że w pokoju jest mrok, pan Ignacy ma wiosenny humor. Wydobywa spod łóżka gitarę, dostraja ją i wziąwszy kilka akordów, zaczyna śpiewać przez nos pieśń bardzo romantyczną:


Wiosna się budzi w całej naturze
Witana rzewnym słowików pieniem;
W zielonym gaju, ponad strumieniem,
Kwitną prześliczne dwie róże.

Czarowne te dźwięki budzą śpiącego na kanapie pudla, który poczyna przypatrywać się jedynym okiem swemu panu. Dźwięki te robią więcej, gdyż wywołują na podwórzu jakiś ogromny cień, który staje w zakratowanym oknie i usiłuje zajrzeć do wnętrza izby, czym zwraca na siebie uwagę pana Ignacego.

„Tak, to musi być Paweł” — myśli pan Ignacy.

Ale Ir jest innego zdania, zeskakuje bowiem z kanapy i z niepokojem wącha drzwi, jakby czuł kogoś obcego.

Słychać szmer w sieniach. Jakaś ręka poszukuje klamki, nareszcie otwierają się drzwi i na progu staje ktoś odziany w wielkie futro upstrzone śniegiem i kroplami deszczu.

— Kto to? — pyta się pan Ignacy i na twarz występują mu silne rumieńce.

— Jużeś o mnie zapomniał, stary?… — cicho i powoli odpowiada gość.

Pan Ignacy miesza się coraz bardziej. Zasadza na nos binokle, które mu spadają, potem wydobywa spod łóżka trumienkowate pudło, śpiesznie chowa gitarę i toż samo pudełko wraz z gitarą kładzie na swoim łóżku.

Tymczasem gość zdjął wielkie futro i baranią czapkę, a jednooki Ir obwąchawszy go poczyna kręcić ogonem, łasić się i z radosnym skomleniem przypadać mu do nóg.

Pan Ignacy zbliża się do gościa wzruszony i zgarbiony więcej niż kiedykolwiek.

— Zdaje mi się… — mówi zacierając ręce — zdaje mi się, że mam przyjemność…

Potem gościa prowadzi do okna mrugając powiekami.

— Staś… jak mi Bóg miły!…

Klepie go po wypukłej piersi, ściska za prawą i za lewą rękę, a nareszcie oparłszy na jego ostrzyżonej głowie swoją dłoń wykonywa nią taki ruch, jakby mu chciał maść wetrzeć w okolicę ciemienia.

— Cha! cha! cha! — śmieje się pan Ignacy. — Staś we własnej osobie… Staś z wojny!… Cóż to, dopiero teraz przypomniałeś sobie, że masz sklep i przyjaciół? — dodaje, mocno uderzając go w łopatkę. — Niech mię diabli wezmą, jeżeli nie jesteś podobny do żołnierza albo marynarza, ale nigdy do kupca… Przez osiem miesięcy nie był w sklepie!… Co za pierś… co za łeb…

Gość także się śmiał. Objął Ignacego za szyję i po kilka razy gorąco ucałował go w oba policzki, które stary subiekt kolejno nadstawiał mu, nie oddając jednak pocałunków.

— No i cóż słychać, stary, u ciebie? — odezwał się gość. — Wychudłeś, pobladłeś…

— Owszem, trochę nabieram ciała.

— Posiwiałeś… Jakże się masz?

— Wybornie. I w sklepie jest nieźle, trochę zwiększyły się nam obroty. W styczniu i lutym mieliśmy targu za dwadzieścia pięć tysięcy rubli… Staś kochany!… Osiem miesięcy nie było go w domu… Bagatela… Może siądziesz?

— Rozumie się — odpowiedział gość siadając na kanapie, na której wnet umieścił się Ir i oparł mu głowę na kolanach.

Pan Ignacy przysunął sobie krzesło.

— Może co zjesz? Mam szynkę i trochę kawioru.

— Owszem.

— Może co wypijesz? Mam butelkę niezłego węgrzyna, ale tylko jeden cały kieliszek.

— Będę pił szklanką — odparł gość.

Pan Ignacy zaczął dreptać po pokoju, kolejno otwierając szafę, kuferek i stolik.

Wydobył wino i schował je na powrót, potem rozłożył na stole szynkę i kilka bułek. Ręce i powieki drżały mu i sporo czasu upłynęło, nim o tyle się uspokoił, że zgromadził na jeden punkt poprzednio wyliczone zapasy. Dopiero kieliszek wina przywrócił mu silnie zachwianą równowagę moralną.

Wokulski tymczasem jadł.

— No, cóż nowego? — rzekł spokojniejszym tonem pan Ignacy trącając gościa w kolano.

— Domyślam się, że ci chodzi o politykę — odparł Wokulski. — Będzie pokój.

— A po cóż zbroi się Austria?

— Zbroi się za sześćdziesiąt milionów guldenów?… Chce zabrać Bośnię i Hercegowinę.

Ignacemu rozszerzyły się źrenice.

— Austria chce zabrać?… — powtórzył. — Za co?…

— Za co? — uśmiechnął się Wokulski. — Za to, że Turcja nie może jej tego zabronić.

— A cóż Anglia?

— Anglia także dostanie kompensatę.

— Na koszt Turcji?

— Rozumie się. Zawsze słabi ponoszą koszta zatargów między silnymi.

— A sprawiedliwość? — zawołał Ignacy.

— Sprawiedliwym jest to, że silni mnożą się i rosną, a słabi giną. Inaczej świat stałby się domem inwalidów, co dopiero byłoby niesprawiedliwością.

Ignacy posunął się z krzesłem.

— I ty to mówisz, Stasiu?… Na serio, bez żartów?

Wokulski zwrócił na niego spokojne wejrzenie.

— Ja mówię — odparł. — Cóż w tym dziwnego? Czyliż to samo prawo nie stosuje się do mnie, do ciebie, do nas wszystkich?… Za dużo płakałem nad sobą, ażebym się miał rozczulać nad Turcją.

Pan Ignacy spuścił oczy i umilkł. Wokulski jadł.

— No, a jakże tobie poszło? — zapytał Rzecki już zwykłym tonem.

Wokulskiemu błysnęły oczy. Położył bułkę i oparł się o poręcz kanapy.

— Pamiętasz — rzekł — ile wziąłem pieniędzy, gdym stąd wyjeżdżał?

— Trzydzieści tysięcy rubli, całą gotówkę.

— A jak ci się zdaje: ile przywiozłem?

— Pięćdzie… ze czterdzieści tysięcy… Zgadłem?… — pytał Rzecki, niepewnie patrząc na niego.

Wokulski nalał szklankę wina i wypił ją powoli.

— Dwieście pięćdziesiąt tysięcy rubli, z tego dużą część w złocie — rzekł dobitnie. — A ponieważ kazałem zakupić banknoty, które po zawarciu pokoju sprzedam, więc będę miał przeszło trzysta tysięcy rubli…

Rzecki pochylił się ku niemu i otworzył usta.

— Nie bój się — ciągnął Wokulski. — Grosz ten zarobiłem uczciwie, nawet ciężko, bardzo ciężko. Cały sekret polega na tym, żem miał bogatego wspólnika i że kontentowałem się cztery i pięć razy mniejszym zyskiem niż inni. Toteż mój kapitał ciągle wzrastający był w ciągłym ruchu. — No — dodał po chwili — miałem też szalone szczęście… Jak gracz, któremu dziesięć razy z rzędu wychodzi ten sam numer w rulecie. Gruba gra?… prawie co miesiąc stawiałem cały majątek, a co dzień życie.

— I tylko po to jeździłeś tam? — zapytał Ignacy.

Wokulski drwiąco spojrzał na niego.

— Czy chciałeś, ażebym został tureckim Wallenrodem?…

— Narażać się dla majątku, gdy się ma spokojny kawałek chleba!… — mruknął pan Ignacy kiwając głową i podnosząc brwi.

Wokulski zadrżał z gniewu i zerwał się z kanapy.

— Ten spokojny chleb — mówił zaciskając pięści — dławił mnie i dusił przez lat sześć!… Czy już nie pamiętasz, ile razy na dzień przypominano mi dwa pokolenia Minclów albo anielską dobroć mojej żony? Czy był kto z dalszych i bliższych znajomych, wyjąwszy ciebie, który by mię nie dręczył słowem, ruchem, a choćby spojrzeniem? Ileż to razy mówiono o mnie i prawie do mnie, że karmię się z fartucha żony, że wszystko zawdzięczam pracy Minclów, a nic, ale to nic — własnej energii, choć przecie ja podźwignąłem ten kramik, zdwoiłem jego dochody…

Mincle i zawsze Mincle!… Dziś niech mnie porównają z Minclami. Sam jeden przez pół roku zarobiłem dziesięć razy więcej aniżeli dwa pokolenia Minclów przez pół wieku. Na zdobycie tego, com ja zdobył pomiędzy kulą, nożem i tyfusem, tysiąc Minclów musiałoby się pocić w swoich sklepikach i szlafmycach. Teraz już wiem, ilu jestem wart Minclów, i jak mi Bóg miły, dla podobnego rezultatu drugi raz powtórzyłbym moją grę! Wolę obawiać się bankructwa i śmierci aniżeli wdzięczyć się do tych, którzy kupią u mnie parasol, albo padać do nóg tym, którzy w moim sklepie raczą zaopatrywać się w waterklozety…

— Zawsze ten sam! — szepnął Ignacy.

Wokulski ochłonął. Oparł się na ramieniu Ignacego i zaglądając mu w oczy rzekł łagodnie:

— Nie gniewasz się, stary?

— Czego? Albo nie wiem, że wilk nie będzie pilnował baranów… Naturalnie…

— Cóż u was słychać? — powiedz mi.

— Akurat tyle, co pisałem ci w raportach. Interesa dobrze idą, towarów przybyło, a jeszcze więcej zamówień. Trzeba jednego subiekta.

— Weźmiemy dwu, sklep rozszerzymy, będzie wspaniały.

— Bagatela!

Wokulski spojrzał na niego z boku i uśmiechnął się widząc, że stary odzyskuje dobry humor.

— Ale co w mieście słychać? W sklepie, dopóki ty w nim jesteś, musi być dobrze.

— W mieście…

— Z dawnych kundmanów nie ubył kto? — przerwał mu Wokulski, coraz szybciej chodząc po pokoju.

— Nikt! Przybyli nowi.

— A… a…

Wokulski stanął jakby wahając się. Nalał znowu szklankę wina i wypił duszkiem.

— A Łęcki kupuje u nas?…

— Częściej bierze na rachunek.

— Więc bierze… — Tu Wokulski odetchnął. — Jakże on stoi?

— Zdaje się, że to skończony bankrut i bodajże w tym roku zlicytują mu nareszcie kamienicę.

Wokulski pochylił się nad kanapą i zaczął bawić się z Irem.

— Proszę cię… A panna Łęcka nie wyszła za mąż?

— Nie.

— A nie wychodzi?…

— Bardzo wątpię. Kto dziś ożeni się z panną mającą wielkie wymagania, a żadnego posagu? Zestarzeje się, choć ładna. Naturalnie…

Wokulski wyprostował się i przeciągnął. Jego surowa twarz nabrała dziwnie rzewnego wyrazu.

— Mój kochany stary! — mówił biorąc Ignacego za rękę — mój poczciwy stary przyjacielu! Ty nawet nie domyślasz się, jakim ja szczęśliwy, że cię widzę, i jeszcze w tym pokoju. Pamiętasz, ilem ja tu spędził wieczorów i nocy… jak mnie karmiłeś… jak oddawałeś mi co lepsze odzienie… Pamiętasz?…

Rzecki uważnie spojrzał na niego i pomyślał, że wino musi być dobre, skoro aż tak rozwiązało usta Wokulskiemu.

Wokulski usiadł na kanapie i oparłszy głowę o ścianę mówił jakby do siebie:

— Nie masz pojęcia, co ja wycierpiałem, oddalony od wszystkich, niepewny, czy już kogo zobaczę, tak strasznie samotny. Bo widzisz, najgorszą samotnością nie jest ta, która otacza człowieka, ale ta pustka w nim samym, kiedy z kraju nie wyniósł ani cieplejszego spojrzenia, ani serdecznego słówka, ani nawet iskry nadziei…

Pan Ignacy poruszył się na krześle z zamiarem protestu.

— Pozwól sobie przypomnieć — odezwał się — że z początku pisywałem listy bardzo życzliwe, owszem, może nawet za sentymentalne. Zraziły mnie dopiero twoje krótkie odpowiedzi.

— Alboż ja do ciebie mam żal?…

— Tym mniej możesz go mieć do innych pracowników, którzy nie znają cię tak jak ja.

Wokulski ocknął się.

— Ależ ja do żadnego z nich nie mam pretensji. Może — odrobinę — do ciebie, żeś tak mało pisał o… mieście… W dodatku bardzo często ginął „Kurier” na poczcie, robiły się luki w wiadomościach, a wtedy męczyły mnie najgorsze przeczucia.

— Z jakiej racji? Wszakże u nas nie było wojny — odparł ze zdziwieniem pan Ignacy.

— Ach tak!… Nawet dobrze bawiliście się. Pamiętam, w grudniu mieliście świetne żywe obrazy. Kto to w nich występował?…

— No, ja na takie głupstwa nie chodzę.

— To prawda. A ja tego dnia dałbym — bodaj — dziesięć tysięcy rubli, ażeby je zobaczyć. Głupstwo jeszcze większe!… Czy nie tak?…

— Zapewne — chociaż dużo tu tłomaczy samotność, nudy…

— A może tęsknota — przerwał Wokulski. — Zjadała mi ona każdą chwilę wolną od pracy, każdą godzinę odpoczynku. Nalej mi wina, Ignacy.

Wypił, zaczął znowu chodzić po pokoju i mówić przyciszonym głosem:

— Pierwszy raz spadło to na mnie w czasie przeprawy przez Dunaj trwającej od wieczora do nocy. Płynąłem sam i Cygan przewoźnik. Nie mogąc rozmawiać przypatrywałem się okolicy. Były w tym miejscu piaszczyste brzegi, jak u nas. I drzewa podobne do naszych wierzb, wzgórza porośnięte leszczyną i kępy lasów sosnowych. Przez chwilę zdawało mi się, że jestem w kraju, i że nim noc zapadnie, znowu was zobaczę. Noc zapadła, ale jednocześnie zniknęły mi z oczu brzegi. Byłem sam na ogromnej smudze wody, w której odbijały się nikłe gwiazdy.

Wówczas przyszło mi na myśl, że tak daleko jestem od domu, że dziś ostatnim między mną i wami łącznikiem są tylko te gwiazdy, że w tej chwili u was może nikt nie patrzy na nie, nikt o mnie nie pamięta, nikt!… Uczułem jakby wewnętrzne rozdarcie i wtedy dopiero przekonałem się, jak głęboką mam ranę w duszy.

— Prawda, że nigdy nie interesowały mnie gwiazdy — szepnął pan Ignacy.

— Od tego dnia uległem dziwnej chorobie — mówił Wokulski. — Dopóki rozpisywałem listy, robiłem rachunki, odbierałem towary, rozsyłałem moich ajentów, dopókim bodaj dźwigał i wyładowywał zepsute wozy albo czuwał nad skradającym się grabieżcą, miałem względny spokój. Ale gdym oderwał się od interesów, a nawet gdym na chwilę złożył pióro, czułem ból, jakby mi — czy ty rozumiesz, Ignacy? — jakby mi ziarno piasku wpadło do serca. Bywało, chodzę, jem, rozmawiam, myślę przytomnie, rozpatruję się w pięknej okolicy, nawet śmieję się i jestem wesół, a mimo to czuję jakieś tępe ukłucie, jakiś drobny niepokój, jakąś nieskończenie małą obawę.

Ten stan chroniczny, męczący nad wszelki wyraz, lada okoliczność rozdmuchiwała w burzę. Drzewo znajomej formy, jakiś obdarty pagórek, kolor obłoku, przelot ptaka, nawet powiew wiatru bez żadnego zresztą powodu budził we mnie tak szaloną rozpacz, że uciekałem od ludzi. Szukałem ustroni tak pustej, gdzie bym mógł upaść na ziemię i nie podsłuchany przez nikogo, wyć z bólu jak pies.

Czasami w tej ucieczce przed samym sobą doganiała mnie noc. Wtedy spoza krzaków, zwalonych pni i rozpadlin wychodziły naprzeciw mnie jakieś szare cienie i smutnie kiwały głowami o wyblakłych oczach. A wszystkie szelesty liści, daleki turkot wozów, szmery wód zlewały się w jeden głos żałosny, który mnie pytał: „Przechodniu nasz, ach! co się z tobą stało?…”

Ach, co się ze mną stało…

— Nic nie rozumiem — przerwał Ignacy. — Cóż to za szał?

— Co?… Tęsknota

— Za czym?

Wokulski drgnął.

— Za czym? No… za wszystkim… za krajem…

— Dlaczegożeś nie wracał?

— A cóż by mi dał powrót?… Zresztą — nie mogłem.

— Nie mogłeś? — powtórzył Ignacy.

— Nie mogłem… i basta! Nie miałem po co wracać — odparł niecierpliwie Wokulski. — Umrzeć tu czy tam, wszystko jedno… daj mi wina — zakończył nagle, wyciągając rękę.

Rzecki spojrzał w jego rozgorączkowaną twarz i odsunął butelkę.

— Daj pokój — rzekł — już i tak jesteś rozdrażniony…

— Dlatego chcę pić…

— Dlatego nie powinieneś pić — przerwał Ignacy. — Za wiele mówisz… może więcej, aniżelibyś chciał — dodał z naciskiem.

Wokulski cofnął się. Zastanowił się i odparł potrząsając głową:

— Mylisz się.

— Zaraz ci dowiodę — odpowiedział Ignacy przyciszonym głosem. — Ty nie jeździłeś tam wyłącznie dla zrobienia pieniędzy…

— Zapewne — rzekł Wokulski po namyśle.

— Bo i na co trzysta tysięcy rubli tobie, któremu wystarczało tysiąc na rok?…

— To prawda.

Rzecki zbliżył swoje usta do jego ucha.

— Jeszcze ci powiem, że pieniędzy tych nie przywiozłeś dla siebie…

— Kto wie, czyś nie zgadł.

— Zgaduję więcej, aniżeli myślisz…

Wokulski nagle roześmiał się.

— Aha, więc tak sądzisz? — zawołał. — Upewniam cię, że nic nie wiesz, stary marzycielu.

— Boję się twojej trzeźwości, pod wpływem której gadasz jak wariat. Rozumiesz mnie, Stasiu?…

Wokulski wciąż się śmiał.

— Masz rację, nie przywykłem pić i wino uderzyło mi do głowy. Ale — już zebrałem zmysły. Powiem ci tylko, że mylisz się gruntownie. A teraz, ażeby ocalić mnie od zupełnego upicia, wypij sam — za pomyślność moich zamiarów.

Ignacy nalał kieliszek i mocno ściskając rękę Wokulskiemu, rzekł:

— Za pomyślność wielkich zamiarów…

— Wielkich dla mnie, ale w rzeczywistości bardzo skromnych.

— Niech i tak będzie — mówił Ignacy. — Jestem tak stary, że mi wygodniej nic nie wiedzieć; jestem już nawet tak stary, że pragnę tylko jednej rzeczy — pięknej śmierci. Daj mi słowo, że gdy przyjdzie czas, zawiadomisz mnie…

— Tak, gdy przyjdzie czas, będziesz moim swatem.

— Już byłem i nieszczęśliwie… — rzekł Ignacy.

— Z wdową przed siedmioma laty?

— Przed piętnastoma.

— Znowu swoje — roześmiał się Wokulski. — Zawsze ten sam!

— I tyś ten sam. Za pomyślność twoich zamiarów… Jakiekolwiek są, wiem jedno, że muszą być godne ciebie. A teraz — milczę…

To powiedziawszy Ignacy wypił wino, a kieliszek rzucił na ziemię. Szkło rozbiło się z brzękiem, który obudził Ira.

— Chodźmy do sklepu — rzekł Ignacy. — Bywają rozmowy, po których dobrze jest mówić o interesach.

Wydobył ze stolika klucz i wyszli. W sieni wionął na nich mokry śnieg. Rzecki otworzył drzwi sklepu i zapalił kilka lamp.

— Co za towary! — zawołał Wokulski. — Chyba wszystko nowe?

— Prawie. Chcesz zobaczyć?… Tu jest porcelana. Zwracam ci uwagę…

— Później… Daj mi księgę.

— Dochodów?…

— Nie, dłużników.

Rzecki otworzył biurko, wydobył księgę i podsunął fotel. Wokulski usiadł i rzuciwszy okiem na listę, wyszukał w niej jedno nazwisko.

— Sto czterdzieści rubli — mówił czytając. — No, to wcale niedużo…

— Któż to? — zapytał Ignacy. — A… Łęcki…

— Panna Łęcka ma także otwarty kredyt… bardzo dobrze — ciągnął Wokulski zbliżywszy twarz do księgi, jakby w niej pismo było niewyraźne. — A… a… Onegdaj wzięła portmonetkę… Trzy ruble?… to chyba za drogo…

— Wcale nie — wtrącił Ignacy. — Portmonetka doskonała, sam ją wybierałem.

— Z którychże to? — spytał niedbale Wokulski i zamknął księgę.

— Z tej gablotki. Widzisz, jakie to cacka.

— Musiała jednak dużo między nimi przerzucić… Jest podobno wymagająca…

— Wcale nie przerzucała, dlaczego miałaby przerzucać? — odparł Ignacy. — Obejrzała tę…

— Tę?…

— A chciała wziąć tę…

— Ach, tę… — szepnął Wokulski biorąc do ręki portmonetkę.

— Ale ja poradziłem jej inną, w tym guście…

— Wiesz co, że to jednak jest ładny wyrób.

— Tamta, którą ja wybrałem, była jeszcze ładniejsza.

— Ta bardzo mi się podoba. Wiesz… ja ją wezmę, bo moja już na nic…

— Czekaj, znajdę ci lepszą — zawołał Rzecki.

— Wszystko jedno. Pokaż inne towary, może jeszcze co mi się przyda.

— Spinki masz?… Krawat, kalosze, parasol…

— Daj mi parasol, no… i krawat. Sam wybierz. Będę dziś jedynym gościem i w dodatku zapłacę gotówką.

— Bardzo dobry zwyczaj — odparł uradowany Rzecki. Prędko wydobył krawat z szuflady i parasol z okna i podał je ze śmiechem Wokulskiemu. — Po strąceniu rabatu — dodał — jako handlujący, zapłacisz siedem rubli. Pyszny parasol… Bagatela…

— To już wrócimy do ciebie — rzekł Wokulski.

— Nie obejrzysz sklepu? — spytał Ignacy.

— Ach, co mnie to ob…

— Nie obchodzi cię twój własny sklep, taki piękny sklep?… — zdziwił się Ignacy.

— Gdzież znowu, czy możesz przypuszczać… Ale jestem trochę zmęczony.

— Słusznie — odparł Rzecki. — Co racja, to racja. Więc idźmy.

Pozakręcał lampy i, przepuściwszy Wokulskiego, zamknął sklep. W sieni znowu spotkał ich mokry śnieg i Paweł niosący obiad.



V. Demokratyzacja pana i marzenia panny z towarzystwa

Pan Tomasz Łęcki z jedyną córką Izabelą i kuzynką panną Florentyną nie mieszkał we własnej kamienicy, lecz wynajmował lokal, złożony z ośmiu pokojów, w stronie Alei Ujazdowskiej. Miał tam salon o trzech oknach, gabinet własny, gabinet córki, sypialnię dla siebie, sypialnię dla córki, pokój stołowy, pokój dla panny Florentyny i garderobę, nie licząc kuchni i mieszkania dla służby, składającej się ze starego kamerdynera Mikołaja, jego żony, która była kucharką, i panny służącej, Anusi.

Mieszkanie posiadało wielkie zalety. Było suche, ciepłe, obszerne, widne. Miało marmurowe schody, gaz, dzwonki elektryczne i wodociągi. Każdy pokój w miarę potrzeby łączył się z innymi lub tworzył zamkniętą w sobie całość. Sprzętów wreszcie miało liczbę dostateczną, ani za mało, ani za wiele, a każdy odznaczał się raczej wygodną prostotą aniżeli skaczącymi do oczu ozdobami. Kredens budził w widzu uczucie pewności, że z niego nie zginą srebra; łóżko przywodziło na myśl bezpieczny spoczynek dobrze zasłużonych; stół można było obciążyć, na krześle usiąść bez obawy załamania się, na fotelu marzyć.

Kto tu wszedł, miał swobodę ruchu; nie potrzebował lękać się, że mu coś zastąpi drogę lub że on coś zepsuje. Czekając na gospodarza nie nudził się, otaczały go bowiem rzeczy, które warto było oglądać. Zarazem widok przedmiotów, wyrobionych nie wczoraj i mogących służyć kilku pokoleniom, nastrajał go na jakiś ton uroczysty.

Na tym poważnym tle dobrze zarysowywali się jego mieszkańcy.

Pan Tomasz Łęcki był to sześdziesięciokilkoletni człowiek, niewysoki, pełnej tuszy, krwisty. Nosił nieduże wąsy białe i do góry podczesane włosy, tej samej barwy. Miał siwe, rozumne oczy, postawę wyprostowaną, chodził ostro. Na ulicy ustępowano mu z drogi — a ludzie prości mówili: oto musi być pan z panów.

Istotnie, pan Łęcki liczył w swoim rodzie całe szeregi senatorów. Ojciec jego jeszcze posiadał miliony, a on sam za młodu krocie. Później jednak część majątku pochłonęły zdarzenia polityczne, resztę — podróże po Europie i wysokie stosunki. Pan Tomasz bywał bowiem przed rokiem 1870 na dworze francuskim, następnie na wiedeńskim i włoskim. Wiktor Emanuel, oczarowany pięknością jego córki, zaszczycał go swoją przyjaźnią i nawet chciał mu nadać tytuł hrabiego. Nie dziw, że pan Tomasz po śmierci wielkiego króla przez dwa miesiące nosił na kapeluszu krepę.

Od paru lat pan Tomasz nie ruszał się z Warszawy, za mało mając już pieniędzy, ażeby błyszczeć na dworach. Za to jego mieszkanie stało się ogniskiem eleganckiego świata i było nim aż do czasu rozejścia się pogłosek, że pan Tomasz postradał nie tylko swój majątek, ale nawet posag panny Izabeli.

Pierwsi cofnęli się epuzerowie, za nimi damy mające brzydkie córki, z pozostałą zaś resztą zerwał sam pan Tomasz i ograniczył swoje znajomości wyłącznie do stosunków z familią. Lecz gdy i tu zauważył zniżenie się uczuciowej temperatury, zupełnie wycofał się z towarzystwa, a nawet ku zgorszeniu wielu szanownych osób, jako właściciel domu w Warszawie, wpisał się do Resursy Kupieckiej. Chciano go tam zrobić prezesem, ale nie zgodził się.

Tylko jego córka bywała u sędziwej hrabiny Karolowej i paru jej przyjaciółek, co znowu dało początek pogłosce, że pan Tomasz jeszcze posiada majątek i że zerwał z towarzystwem w części przez dziwactwo, w części dla poznania rzeczywistych przyjaciół i wybrania córce męża, który by ją kochał dla niej samej, nie dla posagu.

Więc znowu dokoła panny Łęckiej począł zbierać się tłum wielbicieli, a na stoliku w jej salonie stosy biletów wizytowych. Gości jednak nie przyjmowano, co zresztą między nimi nie wywołało zbyt wielkiego oburzenia, ponieważ rozeszła się trzecia z kolei pogłoska, że Łęckiemu licytują kamienicę.

Tym razem w towarzystwie powstał zamęt. Jedni twierdzili, że pan Tomasz jest zdeklarowanym bankrutem, drudzy gotowi byli przysiąc, że zataił majątek, aby zapewnić szczęście jedynaczce. Kandydaci do małżeństwa i ich rodziny znaleźli się w dręczącej niepewności. Ażeby więc nic nie ryzykować i nic nie stracić, składali hołdy pannie Izabeli nie angażując się zbytecznie i po cichu rzucali w jej domu swoje karty, prosząc Boga, ażeby ich czasem nie zaproszono przed wyklarowaniem się sytuacji.

O rewizytach ze strony pana Tomasza nie było mowy. Usprawiedliwiano go ekscentrycznością i smutkiem po Wiktorze Emanuelu.

Tymczasem pan Tomasz w dzień spacerował po Alejach, a wieczorem grywał w wista w resursie. Fizjognomia jego była zawsze tak spokojna, a postawa tak dumna, że wielbiciele jego córki zupełnie potracili głowy. Rozważniejsi czekali, ale śmielsi poczęli znowu darzyć ją powłóczystymi spojrzeniami, cichym westchnieniem lub drżącym uściskiem ręki, na co panna odpowiadała lodowatą, a niekiedy pogardliwą obojętnością.

Panna Izabela była niepospolicie piękną kobietą. Wszystko w niej było oryginalne i doskonałe. Wzrost więcej niż średni, bardzo kształtna figura, bujne włosy blond z odcieniem popielatym, nosek prosty, usta trochę odchylone, zęby perłowe, ręce i stopy modelowe. Szczególne wrażenie robiły jej oczy, niekiedy ciemne i rozmarzone, niekiedy pełne iskier wesołości, czasem jasnoniebieskie i zimne jak lód.

Uderzająca była gra jej fizjognomii. Kiedy mówiła, mówiły jej usta, brwi, nozdrza, ręce, cała postawa, a nade wszystko oczy, którymi zdawało się, że chce przelać swoją duszę w słuchacza. Kiedy słuchała, zdawało się, że chce wypić duszę z opowiadającego. Jej oczy umiały tulić, pieścić, płakać bez łez, palić i mrozić. Niekiedy można było myśleć, że rozmarzona otoczy kogoś rękami i oprze mu głowę na ramieniu; lecz gdy szczęśliwy topniał z rozkoszy, nagle wykonywała jakiś ruch, który mówił, że schwycić jej niepodobna, gdyż albo wymknie się, albo odepchnie, albo po prostu każe lokajowi wyprowadzić wielbiciela za drzwi…

Ciekawym zjawiskiem była dusza panny Izabeli.

Gdyby ją kto szczerze zapytał: czym jest świat, a czym ona sama? niezawodnie odpowiedziałaby, że świat jest zaczarowanym ogrodem, napełnionym czarodziejskimi zamkami, a ona — boginią czy nimfą uwięzioną w formy cielesne.

Panna Izabela od kolebki żyła w świecie pięknym i nie tylko nadludzkim, ale — nadnaturalnym. Sypiała w puchach, odziewała się w jedwabie i hafty, siadała na rzeźbionych i wyściełanych hebanach lub palisandrach, piła z kryształów, jadała ze sreber i porcelany kosztownej jak złoto.

Dla niej nie istniały pory roku, tylko wiekuista wiosna, pełna łagodnego światła, żywych kwiatów i woni. Nie istniały pory dnia, gdyż nieraz przez całe miesiące kładła się spać o ósmej rano, a jadała obiad o drugiej po północy. Nie istniały różnice położeń jeograficznych, gdyż w Paryżu, Wiedniu, Rzymie, Berlinie czy Londynie znajdowali się ci sami ludzie, te same obyczaje, te same sprzęty, a nawet te same potrawy: zupy z wodorostów Oceanu Spokojnego, ostrygi z Morza Północnego, ryby z Atlantyku albo z Morza Śródziemnego, zwierzyna ze wszystkich krajów, owoce ze wszystkich części świata. Dla niej nie istniała nawet siła ciężkości, gdyż krzesła jej podsuwano, talerze podawano, ją samą na ulicy wieziono, na schody wprowadzano, na góry wnoszono.

Woalka chroniła ją od wiatru, kareta od deszczu, sobole od zimna, parasolka i rękawiczki od słońca. I tak żyła z dnia na dzień, z miesiąca na miesiąc, z roku na rok, wyższa nad ludzi, a nawet nad prawa natury. Dwa razy spotkała ją straszna burza, raz w Alpach, drugi — na Morzu Śródziemnym. Truchleli najodważniejsi, ale panna Izabela ze śmiechem przysłuchiwała się łoskotowi druzgotanych skał i trzeszczeniu okrętu, ani przypuszczając możliwości niebezpieczeństwa. Natura urządziła dla niej piękne widowisko z piorunów, kamieni i morskiego odmętu, jak w innym czasie pokazała jej księżyc nad Jeziorem Genewskim albo nad wodospadem Renu rozdarła chmury, które zakrywały słońce. To samo przecie robią co dzień maszyniści teatrów i nawet w zdenerwowanych damach nie wywołują obawy.

Ten świat wiecznej wiosny, gdzie szeleściły jedwabie, rosły tylko rzeźbione drzewa, a glina pokrywała się artystycznymi malowidłami, ten świat miał swoją specjalną ludność. Właściwymi jego mieszkańcami były księżniczki i książęta, hrabianki i hrabiowie tudzież bardzo stara i majętna szlachta obojej płci. Znajdowały się tam jeszcze damy zamężne i panowie żonaci w charakterze gospodarzy domów, matrony strzegące wykwintnego obejścia i dobrych obyczajów i starzy panowie, którzy zasiadali na pierwszych miejscach przy stole, oświadczali młodzież, błogosławili ją i grywali w karty. Byli też biskupi, wizerunki Boga na ziemi, wysocy urzędnicy, których obecność zabezpieczała świat od nieporządków społecznych i trzęsienia ziemi, a nareszcie dzieci, małe cherubiny, zesłane z nieba po to, ażeby starsi mogli urządzać kinderbale.

Wśród stałej ludności zaczarowanego świata ukazywał się od czasu do czasu zwykły śmiertelnik, który na skrzydłach reputacji potrafił wzbić się aż do szczytów Olimpu. Zwykle bywał nim jakiś inżynier, który łączył oceany albo wiercił czy też budował Alpy. Był jakiś kapitan, który w walce z dzikimi stracił swoją kompanię, a sam okryty ranami ocalał dzięki miłości murzyńskiej księżniczki. Był podróżnik, który podobno odkrył nową część świata, rozbił się z okrętem na bezludnej wyspie i bodaj czy nie kosztował ludzkiego mięsa.

Bywali tam wreszcie sławni malarze, a nade wszystko natchnieni poeci, którzy w sztambuchach hrabianek pisywali ładne wiersze, mogli kochać się bez nadziei i uwieczniać wdzięki swoich okrutnych bogiń naprzód w gazetach, a następnie w oddzielnych tomikach, drukowanych na welinowym papierze.

Cała ta ludność, między którą ostrożnie przesuwali się wygalonowani lokaje, damy do towarzystwa, ubogie kuzynki i łaknący wyższych posad kuzyni, cała ta ludność obchodziła wieczne święto.

Od południa składano sobie i oddawano wizyty i rewizyty albo zjeżdżano się w magazynach. Ku wieczorowi bawiono się przed obiadem, w czasie obiadu i po obiedzie. Potem jechano na koncert lub do teatru, ażeby tam zobaczyć inny sztuczny świat, gdzie bohaterowie rzadko kiedy jedzą i pracują, ale za to wciąż gadają sami do siebie — gdzie niewierność kobiet staje się źródłem wielkich katastrof i gdzie kochanek, zabity przez męża w piątym akcie, na drugi dzień zmartwychwstaje w pierwszym akcie, ażeby popełniać te same błędy i gadać do siebie nie będąc słyszanym przez osoby obok stojące. Po wyjściu z teatru znowu zbierano się w salonach, gdzie służba roznosiła zimne i gorące napoje, najęci artyści śpiewali, młode mężatki słuchały opowiadań porąbanego kapitana o murzyńskiej księżniczce, panny rozmawiały z poetami o powinowactwie dusz, starsi panowie wykładali inżynierom swoje poglądy na inżynierię, a damy w średnim wieku półsłówkami i spojrzeniami walczyły między sobą o podróżnika, który jadł ludzkie mięso. Potem zasiadano do kolacji, gdzie usta jadły, żołądki trawiły, a buciki rozmawiały o uczuciach lodowatych serc i marzeniach głów niezawrotnych. A potem — rozjeżdżano się, ażeby w śnie rzeczywistym nabrać sił do snu życia.

Poza tym czarodziejskim był jeszcze inny świat — zwyczajny.

O jego istnieniu wiedziała panna Izabela i nawet lubiła mu się przypatrywać z okna karety, wagonu albo z własnego mieszkania. W takich ramach i z takiej odległości wydawał on się jej malowniczym i nawet sympatycznym. Widywała rolników powoli orzących ziemię — duże fury ciągnione przez chudą szkapę — roznosicieli owoców i jarzyn — starca, który tłukł kamienie na szosie — posłańców idących gdzieś z pośpiechem — ładne i natrętne kwiaciarki — rodzinę złożoną z ojca, bardzo otyłej matki i czworga dzieci, parami trzymających się za ręce — eleganta niższej sfery, który jechał dorożką i rozpierał się w sposób bardzo zabawny — czasem pogrzeb. I mówiła sobie, że tamten świat, choć niższy, jest ładny; jest nawet ładniejszy od obrazów rodzajowych, gdyż porusza się i zmienia co chwilę.

I jeszcze wiedziała panna Izabela, że jak w oranżeriach rosną kwiaty, a w winnicach winogrona, tak w tamtym, niższym świecie, wyrastają rzeczy jej potrzebne. Stamtąd pochodzi jej wierny Mikołaj i Anusia, tam robią rzeźbione fotele, porcelany, kryształy i firanki, tam rodzą się froterzy, tapicerowie, ogrodnicy i panny szyjące suknie. Będąc raz w magazynie kazała zaprowadzić się do szwalni i bardzo ciekawym wydał się jej widok kilkudziesięciu pracownic, które krajały, fastrygowały i układały na formach fałdy ubrań. Była pewna, że robi im to wielką przyjemność, ponieważ te panny, które brały jej miarę albo przymierzały suknie, były zawsze uśmiechnięte i bardzo zainteresowane tym, ażeby strój leżał na niej dobrze.

I jeszcze wiedziała panna Izabela, że na tamtym, zwyczajnym świecie trafiają się ludzie nieszczęśliwi. Więc każdemu ubogiemu, o ile spotkał ją, kazała dawać po kilka złotych; raz spotkawszy mizerną matkę z bladym jak wosk dzieckiem przy piersi oddała jej bransoletę, a brudne, żebrzące dzieci obdarzała cukierkami i całowała z pobożnym uczuciem. Zdawało się jej, że w którymś z tych biedaków, a może w każdym, jest utajony Chrystus, który zastąpił jej drogę, ażeby dać okazję do spełnienia dobrego czynu.

W ogóle dla ludzi z niższego świata miała serce życzliwe. Przychodziły jej na myśl słowa Pisma świętego: „W pocie czoła pracować będziesz.”. Widocznie popełnili oni jakiś ciężki grzech, skoro skazano ich na pracę; ależ tacy jak ona aniołowie nie mogli nie ubolewać nad ich losem. Tacy jak ona, dla której największą pracą było dotknięcie elektrycznego dzwonka albo wydanie rozkazu.

Raz tylko niższy świat zrobił na niej potężne wrażenie.

Pewnego dnia, we Francji, zwiedzała fabrykę żelazną. Zjeżdżając z góry, w okolicy pełnej lasów i łąk, pod szafirowym niebem zobaczyła otchłań wypełnioną obłokami czarnych dymów i białych par i usłyszała głuchy łoskot, zgrzyt i sapanie machin. Potem widziała piece, jak wieże średniowiecznych zamków, dyszące płomieniami — potężne koła, które obracały się z szybkością błyskawic — wielkie rusztowania, które same toczyły się po szynach — strumienie rozpalonego do białości żelaza i półnagich robotników, jak spiżowe posągi, o ponurych wejrzeniach. Ponad tym wszystkim — krwawa łuna, warczenie kół, jęki miechów, grzmot młotów i niecierpliwe oddechy kotłów, a pod stopami dreszcz wylęknionej ziemi.

Wtedy zdało się jej, że z wyżyn szczęśliwego Olimpu zstąpiła do beznadziejnej otchłani Wulkana, gdzie cyklopowie kują pioruny mogące zdruzgotać sam Olimp. Przyszły jej na myśl legendy o zbuntowanych olbrzymach, o końcu tego pięknego świata, w którym przebywała, i pierwszy raz w życiu ją, boginię, przed którą gięli się marszałkowie i senatorzy, zdjęła trwoga.

— To są straszni ludzie, papo… — szepnęła do ojca.

Ojciec milczał, tylko mocniej przycisnął jej ramię.

— Ale kobietom oni nic złego nie zrobią?

— Tak, nawet oni — odpowiedział pan Tomasz.

W tej chwili pannę Izabelę ogarnął wstyd na myśl, że troszczyła się tylko o kobiety. Więc szybko dodała:

— A jeżeli nam, to i wam nie zrobią nic złego…

Ale pan Tomasz uśmiechnął się i potrząsnął głową. W owym czasie dużo mówiono o zbliżającym się końcu starego świata, a pan Tomasz głęboko odczuwał to, z wielkimi trudnościami wydobywając pieniądze od swoich pełnomocników.

Odwiedziny fabryki stanowiły ważną epokę w życiu panny Izabeli. Z religijną czcią czytywała ona poezje swego dalekiego kuzyna, Zygmunta, i zdawało się jej, że dziś znalazła ilustrację do Nie-Boskiej komedii. Odtąd często marzyła o zmroku, że na górze kąpiącej się w słońcu, skąd zjeżdżał jej powóz do fabryki, stoją Okopy Św. Trójcy, a w tej dolinie zasnutej dymami i parą było obozowisko zbuntowanych demokratów, gotowych lada chwila ruszyć do szturmu i zburzyć jej piękny świat.

Teraz dopiero zrozumiała, jak gorąco kocha tę swoją duchową ojczyznę, gdzie kryształowe pająki zastępują słońce, dywany — ziemię, posągi i kolumny — drzewa. Tę drugą ojczyznę, która ogarnia arystokrację wszystkich narodów, wykwintność wszystkich czasów i najpiękniejsze zdobycze cywilizacji.

I to wszystko miałoby runąć, umrzeć albo rozpierzchnąć się!… Rycerska młodzież, która śpiewa z takim uczuciem, tańczy z wdziękiem, pojedynkuje się z uśmiechem albo skacze na środku jeziora w wodę za zgubionym kwiatkiem?… Mają zginąć te ukochane przyjaciółki, które okrywały ją tyloma pieszczotami albo siedząc u jej nóg opowiadały jej tyle drobnych tajemnic, albo oddalone od niej pisywały takie długie, bardzo długie listy, w których tkliwe uczucia mieszały się z nader wątpliwą ortografią?

A ta dobra służba, która ze swymi panami postępuje tak, jakby zaprzysięgała im dozgonną miłość, wierność i posłuszeństwo? A te modystki, które zawsze witają ją z uśmiechem i tak pamiętają o najdrobniejszym szczególe jej toalety, tak dokładnie wiedzą o jej triumfach? A te piękne konie, którym jaskółka mogłaby zazdrościć lotu, a te psy mądre i przywiązane jak ludzie, a te ogrody, gdzie ręka ludzka powznosiła pagórki, wylewała strumienie, modelowała drzewa?… I to wszystko miałoby kiedyś zniknąć?…

Od tych rozmyślań przybył pannie Izabeli na twarz nowy wyraz — łagodnego smutku, który ją robił jeszcze piękniejszą. Mówiono, że już zupełnie dojrzała.

Rozumiejąc, że wielki świat jest wyższym światem, panna Izabela dowiedziała się powoli, że do tych wyżyn wzbić się można i stale na nich przebywać tylko za pomocą dwóch skrzydeł: urodzenia i majątku. Urodzenie zaś i majątek są przywiązane do pewnych wybranych familii, jak kwiat i owoc pomarańczy do pomarańczowego drzewa. Bardzo też jest możliwym, że dobry Bóg widząc dwie dusze z pięknymi nazwiskami, połączone węzłem sakramentu, pomnaża ich dochody i zsyła im na wychowanie aniołka, który w dalszym ciągu podtrzymuje sławę rodów swoimi cnotami, dobrym ułożeniem i pięknością. Stąd wynika obowiązek oględnego zawierania małżeństw, na czym najlepiej znają się stare damy i sędziwi panowie. Wszystko znaczy trafny dobór nazwisk i majątków. Miłość bowiem, nie ta szalona, o jakiej marzą poeci, ale prawdziwie chrześcijańska, zjawia się dopiero po sakramencie i najzupełniej wystarcza, ażeby żona umiała pięknie prezentować się w domu, a mąż z powagą asystować jej w świecie.

Tak było dawniej i było dobrze, według zgodnej opinii wszystkich matron. Dziś zapomniano o tym i jest źle: mnożą się mezalianse i upadają wielkie rodziny.

„I nie ma szczęścia w małżeństwach” — dodawała po cichu panna Izabela, której młode mężatki opowiedziały niejeden sekret domowy.

Dzięki nawet tym opowiadaniom nabrała dużego wstrętu do małżeństwa i lekkiej wzgardy dla mężczyzn.

Mąż w szlafroku, który ziewa przy żonie, całuje ją mając pełne usta dymu z cygar, często odzywa się: „A dajże mi spokój”, albo po prostu: „Głupia jesteś!…” — ten mąż, który robi hałasy w domu za nowy kapelusz, a za domem wydaje pieniądze na ekwipaże dla aktorek, to wcale nieciekawe stworzenie. Co najgorsze, że każdy z nich przed ślubem był gorącym wielbicielem, mizerniał nie widząc długo swej pani, rumienił się, kiedy ją spotkał, a nawet niejeden obiecywał zastrzelić się z miłości.

Toteż mając lat osiemnaście, panna Izabela tyranizowała mężczyzn chłodem. Kiedy Wiktor Emanuel raz pocałował ją w rękę, uprosiła ojca, że tego samego dnia wyjechali z Rzymu. W Paryżu oświadczył się jej pewien bogaty hrabia francuski; odpowiedziała mu, że jest Polką i za cudzoziemca nie wyjdzie. Podolskiego magnata odepchnęła zdaniem, że odda swoją rękę tylko temu, kogo pokocha, a na co się jeszcze nie zanosi, a oświadczyny jakiegoś amerykańskiego milionera zbyła wybuchem śmiechu.

Takie postępowanie na kilka lat wytworzyło dokoła panny pustkę. Podziwiano ją i wielbiono, ale z daleka; nikt bowiem nie chciał narażać się na szyderczą odmowę.

Po przejściu pierwszego niesmaku panna Izabela zrozumiała, że małżeństwo trzeba przyjąć takim, jakie jest. Była już zdecydowana wyjść za mąż, pod tym wszakże warunkiem, aby przyszły towarzysz — podobał się jej, miał piękne nazwisko i odpowiedni majątek. Rzeczywiście, trafiali się jej ludzie piękni, majętni i utytułowani; na nieszczęście jednak, żaden nie łączył w sobie wszystkich trzech warunków, więc — znowu upłynęło kilka lat.

Nagle rozeszły się wieści o złym stanie interesów pana Tomasza i — z całego legionu konkurentów — zostało pannie Izabeli tylko dwu poważnych: pewien baron i pewien marszałek, bogaci, ale starzy.

Teraz spostrzegła panna Izabela, że w wielkim świecie usuwa jej się grunt pod nogami, więc zdecydowała się obniżyć skalę wymagań. Ale że baron i marszałek pomimo swoich majątków budzili w niej niepokonaną odrazę, więc odkładała stanowczą decyzję z dnia na dzień. Tymczasem pan Tomasz zerwał z towarzystwem. Marszałek nie mogąc się doczekać odpowiedzi wyjechał na wieś, strapiony baron za granicę i — panna Izabela pozostała kompletnie samą. Wprawdzie wiedziała, że każdy z nich wróci na pierwsze zawołanie, ale — którego tu wybrać?… jak przytłumić wstręt?… Nade wszystko zaś, czy podobna robić z siebie taką ofiarę mając niejaką pewność, że kiedyś odzyska majątek, i wiedząc, że wówczas znowu będzie mogła wybierać. Tym razem już wybierze, poznawszy, jak ciężko jej żyć poza towarzystwem salonów…

Jedna rzecz w wysokim stopniu ułatwiała jej wyjście za mąż dla stanowiska. Oto panna Izabela nigdy nie była zakochaną. Przyczyniał się do tego jej chłodny temperament, wiara, że małżeństwo obejdzie się bez poetycznych dodatków, nareszcie miłość idealna, najdziwniejsza, o jakiej słyszano. Raz zobaczyła w pewnej galerii rzeźb posąg Apollina, który na niej zrobił tak silne wrażenie, że kupiła piękną jego kopię i ustawiła w swoim gabinecie. Przypatrywała mu się całymi godzinami, myślała o nim i kto wie, ile pocałunków ogrzało ręce i nogi marmurowego bóstwa?… I stał się cud: pieszczony przez kochającą kobietę głaz ożył. A kiedy pewnej nocy zapłakana usnęła, nieśmiertelny zstąpił ze swego piedestału i przyszedł do niej w laurowym wieńcu na głowie, jaśniejący mistycznym blaskiem.

Siadł na krawędzi jej łóżka, długo patrzył na nią oczyma, z których przeglądała wieczność, a potem objął ją w potężnym uścisku i pocałunkami białych ust ocierał łzy i chłodził jej gorączkę.

Odtąd nawiedzał ją coraz częściej i omdlewającej w jego objęciach szeptał on, bóg światła, tajemnice nieba i ziemi, jakich dotychczas nie wypowiedziano w śmiertelnym języku. A przez miłość dla niej sprawił jeszcze większy cud, gdyż w swym boskim obliczu kolejno ukazywał jej upiększone rysy tych ludzi, którzy kiedykolwiek zrobili na niej wrażenie.

Raz był podobnym do odmłodzonego jenerała-bohatera, który wygrał bitwę i z wyżyn swego siodła patrzył na śmierć kilku tysięcy walecznych. Drugi raz przypominał twarz najsławniejszego tenora, któremu kobiety rzucały kwiaty pod nogi, a mężczyźni wyprzęgali konie z powozu. Inny raz był wesołym i pięknym księciem krwi jednego z najstarszych domów panujących; inny raz dzielnym strażakiem, który za wydobycie trzech osób z płomieni na piątym piętrze dostał legię honorową; inny raz był wielkim rysownikiem, który przytłaczał świat bogactwem swojej fantazji, a inny raz weneckim gondolierem albo cyrkowym atletą nadzwyczajnej urody i siły.

Każdy z tych ludzi przez pewien czas zaprzątał tajemne myśli panny Izabeli, każdemu poświęcała najcichsze westchnienia rozumiejąc, że dla tych czy innych powodów kochać go nie może i — każdy z nich za sprawą bóstwa ukazywał się w jego postaci, w półrzeczywistych marzeniach. A od tych widzeń oczy panny Izabeli przybrały nowy wyraz — jakiegoś nadziemskiego zamyślenia. Niekiedy spoglądały one gdzieś ponad ludzi i poza świat; a gdy jeszcze jej popielate włosy na czole ułożyły się tak dziwnie, jakby je rozwiał tajemniczy podmuch, patrzącym zdawało się, że widzą anioła albo świętą.

Przed rokiem w jednej z takich chwil zobaczył pannę Izabelę Wokulski. Odtąd serce jego nie zaznało spokoju.

Prawie w tym samym czasie pan Tomasz zerwał z towarzystwem i na znak swoich rewolucyjnych usposobień zapisał się do Resursy Kupieckiej. Tam z pomiatanymi niegdyś garbarzami, szczotkarzami i dystylatorami grywał w wista, głosząc na prawo i na lewo, że arystokracja nie powinna zasklepiać się w wyłączności, ale przodować oświeconemu mieszczaństwu, a przez nie narodowi. Za co wywzajemniając się dumni dziś garbarze, szczotkarze i dystylatorzy raczyli przyznawać, że pan Tomasz jest jedynym arystokratą, który pojął swe obowiązki względem kraju i spełnia je sumiennie. Mogli byli dodać: spełnia co dzień od dziewiątej wieczór do północy.

I kiedy w ten sposób pan Tomasz dźwigał jarzmo stanowiska, panna Izabela trawiła się w samotności i ciszy swego pięknego lokalu. Nieraz Mikołaj już twardo drzemał w fotelu, panna Florentyna, zatkawszy sobie uszy watą, na dobre spała, a do pokoju panny Izabeli sen jeszcze nie zapukał odpędzany przez wspomnienia. Wtedy zrywała się z łóżka i odziana w lekki szlafroczek całymi godzinami chodziła po salonie, gdzie dywan głuszył jej kroki i tylko tyle było światła, ile go rzucały dwie skąpe latarnie uliczne.

Chodziła, a w ogromnym pokoju tłoczyły się jej smutne myśli i widziadła osób, które tu kiedyś bywały. Tu drzemie stara księżna; tu dwie hrabiny informują się u prałata, czy można dziecko ochrzcić wodą różaną? Tu rój młodzieży zwraca ku niej tęskne spojrzenia albo udanym chłodem usiłuje podniecić w niej ciekawość; a tam girlanda panien, które pieszczą ją wzrokiem, podziwiają albo jej zazdroszczą. Pełno świateł, szelestów, rozmów, których większa część, jak motyle około kwiatów, krążyły około jej piękności. Gdzie ona się znalazła, tam obok niej wszystko bladło; inne kobiety były jej tłem, a mężczyźni niewolnikami.

I to wszystko przeszło!… I dziś w tym salonie — chłodno, ciemno i pusto… Jest tylko ona i niewidzialny pająk smutku, który zawsze zasnuwa szarą siecią te miejsca, gdzie byliśmy szczęśliwi i skąd szczęście uciekło. Już uciekło!… Panna Izabela wyłamywała sobie palce, ażeby pohamować się od łez, których wstyd jej było nawet w pustce i w nocy.

Wszyscy ją opuścili, z wyjątkiem — hrabiny Karolowej, która, kiedy wezbrał jej zły humor, przychodziła tu i szeroko zasiadłszy na kanapie, prawiła wśród westchnień:

— Tak, droga Belciu, musisz przyznać, że popełniłaś kilka błędów nie do darowania. Nie mówię o Wiktorze Emanuelu, bo tamto był przelotny kaprys króla trochę liberalnego i zresztą bardzo zadłużonego. Na takie stosunki trzeba mieć więcej — nie powiem: taktu, ale — doświadczenia — ciągnęła hrabina, skromnie spuszczając powieki. — Ale wypuścić czy — jeśli chcesz — odrzucić hrabiego Saint-Auguste, to już daruj!… Człowiek młody, majętny, bardzo dobrze, i jeszcze z taką karierą!… Teraz właśnie przewodniczy jednej deputacji do Ojca świętego i zapewne dostanie specjalne błogosławieństwo dla całej rodziny, no a hrabia Chambord nazywa go cher cousin… Ach, Boże!

— Myślę, ciociu, że martwić się tym już za późno — wtrąciła panna Izabela.

— Alboż ja chcę cię martwić, biedne dziecko! I bez tego czekają cię ciosy, które ukoić może tylko głęboka wiara. Zapewne wiesz, że ojciec stracił wszystko, nawet resztę twego posagu?

— Cóż ja na to poradzę?

— A jednak ty tylko możesz radzić i powinnaś — mówiła hrabina z naciskiem. — Marszałek nie jest wprawdzie Adonisem, no — ale… Gdyby nasze obowiązki były do spełnienia łatwe, nie istniałaby zasługa. Zresztą, mój Boże, któż nam broni mieć na dnie duszy jakiś ideał, o którym myśl osładza najcięższe chwile? Na koniec, mogę cię zapewnić, że położenie pięknej kobiety, mającej starego męża, nie należy do najgorszych. Wszyscy interesują się nią, mówią o niej, składają hołdy jej poświęceniu, a znowu stary mąż jest mniej wymagający od męża w średnim wieku…

— Ach, ciociu…

— Tylko bez egzaltacji, Belciu! Nie masz lat szesnastu i na życie musisz patrzeć serio. Nie można przecie dla jakiejś idiosynkrazji poświęcić bytu ojca, a choćby Flory i waszej służby. Wreszcie pomyśl, ile ty przy twym szlachetnym serduszku mogłabyś zrobić dobrego rozporządzając znacznym majątkiem.

— Ależ, ciociu, marszałek jest obrzydliwy. Jemu nie żony trzeba, ale niańki, która by mu ocierała usta.

— Nie upieram się przy marszałku, więc baron…

— Baron jeszcze starszy, farbuje się, różuje i ma jakieś plamy na rękach.

Hrabina podniosła się z kanapy.

— Nie nalegam, moja droga, nie jestem swatką, to należy do pani Meliton. Zwracam tylko uwagę, że nad ojcem wisi katastrofa.

— Mamy przecie kamienicę.

— Którą sprzedają najdalej po św. Janie, tak że nawet twoja suma spadnie.

— Jak to — dom, który kosztował sto tysięcy, sprzedadzą za sześćdziesiąt?…

— Bo on nie wart więcej, bo ojciec za dużo wydał. Wiem to od budowniczego, który oglądał go z polecenia Krzeszowskiej.

— Więc w ostateczności mamy serwis… srebra… — wybuchnęła panna Izabela załamując ręce.

Hrabina ucałowała ją kilkakrotnie.

— Drogie, kochane dziecko — mówiła łkając — że też właśnie ja muszę tak ranić ci serce!… Słuchaj więc… Ojciec ma jeszcze długi wekslowe, jakieś parę tysięcy rubli. Otóż te długi… uważasz… te długi ktoś skupił… kilka dni temu, w końcu marca. Domyślamy się, że to zrobiła Krzeszowska…

— Cóż za nikczemność! — szepnęła panna Izabela. — Ale mniejsza o nią… Na pokrycie paru tysięcy rubli wystarczy mój serwis i srebra.

— Są one warte bez porównania więcej, ale — kto dziś kupi rzeczy tak kosztowne?

— W każdym razie spróbuję — mówiła rozgorączkowana panna Izabela. — Poproszę panią Meliton, ona mi to ułatwi…

— Zastanów się jednak, czy nie szkoda tak pięknych pamiątek.

Panna Izabela roześmiała się.

— Ach, ciociu… Więc mam wahać się pomiędzy sprzedaniem siebie i serwisu?… Bo na to, ażeby zabierano nam meble, nigdy nie pozwolę… Ach, ta Krzeszowska… to wykupywanie weksli… co za ohyda!

— No, może to jeszcze nie ona.

— Więc chyba znalazł się jakiś nowy nieprzyjaciel, gorszy od niej.

— Może to ciotka Honorata — uspokajała ją hrabina — czy ja wiem? Może chce dopomóc Tomaszowi, ale zawieszając nad nim groźbę. Lecz bądź zdrowa, moje kochane dziecię, adieu…

Na tym skończyła się rozmowa w języku polskim, gęsto ozdobionym francuszczyzną, co robiło go podobnym do ludzkiej twarzy okrytej wysypką.



VI. W jaki sposób nowi ludzie ukazują się nad starymi horyzontami

Początek kwietnia, jeden z tych miesięcy, które służą za przejście między zimą i wiosną. Śnieg już zniknął, ale nie ukazała się jeszcze zieloność; drzewa są czarne, trawniki szare i niebo szare: wygląda jak marmur poprzecinany srebrnymi i złotawymi nitkami.

Jest około piątej po południu. Panna Izabela siedzi w swoim gabinecie i czyta najnowszą powieść Zoli: Une page d'amour. Czyta bez uwagi, co chwilę podnosi oczy, spogląda w okno i półświadomie formułuje sąd, że gałązki drzew są czarne, a niebo szare. Znowu czyta, spogląda po gabinecie i półświadomie myśli, że jej meble kryte błękitną materią i jej niebieski szlafroczek mają jakiś szary odcień i że festony białej firanki są podobne do wielkich sopli śniegu. Potem zapomina, o czym myślała w tej chwili, i pyta się w duchu: „O czym ja myślałam?… Ach, prawda, o kweście wielkotygodniowej…” I nagle czuje ochotę przejechania się karetą, a jednocześnie czuje żal do nieba, że jest takie szare, że złotawe żyłki na nim są tak wąskie… Dręczy ją jakiś cichy niepokój, jakieś oczekiwanie, ale nie jest pewna, na co czeka: czy na to, ażeby chmury się rozdarły, czy na to, ażeby wszedł lokaj i wręczył jej list zapraszający na wielkotygodniową kwestę? Już taki krótki czas, a jej nie proszą.

Znowu czyta powieść, ten rozdział, kiedy podczas gwiaździstej nocy p. Rambaud naprawiał zepsutą lalkę małej Joasi. Helena tonęła we łzach bezprzedmiotowego żalu, a opat Jouve radził, ażeby wyszła za mąż. Panna Izabela odczuwa ten żal i kto wie, czy gdyby w tej chwili ukazały się na niebie gwiazdy, zamiast chmur, czy nie rozpłakałaby się tak jak Helena. Wszak to już ledwo parę dni do kwesty, a jej jeszcze nie proszą. Że zaproszą, o tym wie, ale dlaczego zwłóczą?…

„Te kobiety, które zdają się tak gorąco szukać Boga, bywają niekiedy nieszczęśliwymi istotami, których serce wzburzyła namiętność. Idą do kościoła, ażeby tam wielbić mężczyznę” — mówił opat Jouve.

„Poczciwy opat, jak on chciał uspokoić tę biedną Helenę!” — myśli panna Izabela i nagle odrzuca książkę. Opat Jouve przypomniał jej, że już od dwu miesięcy haftuje pas do kościelnego dzwonka i że go jeszcze nie skończyła. Podnosi się z fotelu i przysuwa do okna stolik z tamburkiem, z pudełkiem różnokolorowych jedwabiów z kolorowym deseniem; rozwija pas i zaczyna gorliwie wyszywać na nim róże i krzyże. Pod wpływem pracy w sercu budzi się otucha. Kto tak, jak ona, służy Kościołowi, nie może być zapomnianym przy wielkotygodniowej kweście. Wybiera jedwabie, nawłóczy igły i szyje wciąż. Oko jej przebiega od wzoru do haftu, ręka spada z góry na dół, wznosi się z dołu do góry, ale w myśli zaczyna rodzić się pytanie dotyczące kostiumu na groby i toalety na Wielkanoc. Pytanie to wkrótce zapełnia jej całą uwagę, zasłania oczy i zatrzymuje rękę. Suknia, kapelusz, okrywka i parasolka, wszystko musi być nowe, a tu tak niewiele czasu i nie tylko nic nie zamówione, ale nawet nie wybrane!…

Tu przypomina sobie, że jej serwis i srebra już znajdują się u jubilera, że już trafia się jakiś nabywca i że dziś lub jutro będą sprzedane. Panna Izabela czuje ściśnięcie serca za serwisem i srebrami, lecz doznaje niejakiej ulgi na myśl o kweście i nowej toalecie. Może mieć bardzo piękną, ale jaką?…

Odsuwa tamburek i ze stolika, na którym leżą Szekspir, Dante, album europejskich znakomitości tudzież kilka pism, bierze: „Le Moniteur de la Mode” i zaczyna go przeglądać z największą uwagą. Oto jest toaleta obiadowa; oto ubiory wiosenne dla panienek, panien, mężatek, młodych mężatek i ich matek; oto suknie wizytowe, ceremonialne, spacerowe; sześć nowych form kapeluszy, z dziesięć materiałów, kilkadziesiąt barw… Co tu wybrać, o Boże?… Niepodobna wybierać bez naradzenia się z panną Florentyną i z magazynierką…

Panna Izabela z niechęcią odrzuca monitora mody i siada na szezlongu w postaci półleżącej. Ręce splecione jak do modlitwy opiera na poręczy, głowę na rękach i patrzy w niebo rozmarzonymi oczyma. Kwesta wielkotygodniowa, nowa toaleta, chmury na niebie, wszystko miesza się w jej wyobraźni na tle żalu za serwisem i lekkiego uczucia wstydu, że go sprzedaje.

„Ach, wszystko jedno!” — mówi sobie i znowu pragnie, ażeby chmury rozdarły się choć na chwilę. Ale chmury zgęszczają się, a w jej sercu wzmaga się żal, wstyd i niepokój. Spojrzenie jej pada na stolik stojący tuż obok szezlonga i na książkę do nabożeństwa oprawną w kość słoniową. Panna Izabela bierze do rąk książkę i powoli, kartka za kartką, wyszukuje w niej modlitwy: Acte de resignation, a znalazłszy, zaczyna czytać:

„Que votre nom soit beni à jamais, bien qui avez voulu m'éprouver par cette peine.”. W miarę jak czyta, szare niebo wyjaśnia się, a przy ostatnich słowach… „et d'attendre en paix votre divin secours…”, chmury pękają, ukazuje się kawałek czystego błękitu, gabinet panny Izabeli napełnia się światłem, a jej dusza spokojem. Teraz jest pewna, że modły jej zostały wysłuchane, że będzie miała najpiękniejszą toaletę i najlepszy kościół do kwesty.

W tej chwili delikatnie otwierają się drzwi gabinetu; staje w nich panna Florentyna, wysoka, czarno ubrana, nieśmiała, trzyma w dwu palcach list i mówi cicho:

— Od pani Karolowej.

— Ach, w sprawie kwesty — odpowiada panna Izabela z czarującym uśmiechem. — Cały dzień nie zaglądałaś do mnie, Florciu.

— Nie chcę ci przeszkadzać.

— W nudzeniu się?… — pyta panna Izabela. — Kto wie, czy nie byłoby nam weselej nudzić się w jednym pokoju.

— List… — mówi nieśmiała osoba w czarnej sukni, wyciągając rękę do Izabeli.

— Znam jego treść — przerywa panna Izabela. — Posiedź trochę u mnie i jeżeli nie zrobi ci subiekcji, przeczytaj ten list.

Panna Florentyna siada nieśmiało na fotelu, delikatnie bierze z biurka nożyk i z największą ostrożnością przecina kopertę. Kładzie na biurku nożyk, potem kopertę, rozwija papier i cichym, melodyjnym głosem czyta list pisany po francusku:

„Droga Belu! wybacz, że odzywam się w sprawie, którą tylko ty i twój ojciec macie prawo rozstrzygać. Wiem, drogie dziecię, że pozbywasz się tego serwisu i sreber, sama mi zresztą o tym mówiłaś. Wiem też, że znalazł się nabywca, który ofiarowuje wam pięć tysięcy rubli, moim zdaniem za mało, choć w tych czasach trudno spodziewać się więcej. Po rozmowie jednak, jaką miałam w tej materii z Krzeszowską, zaczynam lękać się, ażeby piękne te pamiątki nie przeszły w niewłaściwe ręce.

Chciałabym temu zapobiec, proponuję ci więc, jeżeli zgodzisz się, trzy tysiące rubli pożyczki na zastaw wspomnianego serwisu i sreber. Sądzę, że dziś wygodniej będzie im u mnie, gdy ojciec twój znajduje się w takich kłopotach. Odebrać je będziesz mogła, kiedy zechcesz, a w razie mojej śmierci nawet bez zwracania pożyczki.

Nie narzucam się, tylko proponuję. Rozważ, jak ci będzie wygodniej, a nade wszystko pomyśl o następstwach.

O ile cię znam, byłabyś boleśnie dotkniętą usłyszawszy kiedyś, że nasze rodzinne pamiątki zdobią stół jakiego bankiera albo należą do wyprawy jego córki.

Zasyłam ci tysiące pocałunków.

Joanna

P. S. Wyobraź sobie, co za szczęście spotkało moją ochronkę. Będąc wczoraj w sklepie tego sławnego Wokulskiego przymówiłam się o mały datek dla sierot. Liczyłam na jakie kilkanaście rubli, a on, czy uwierzysz, ofiarował mi tysiąc, wyraźnie: tysiąc rubli, i jeszcze powiedział, że na moje ręce nie śmiałby złożyć mniejszej sumy. Kilku takich Wokulskich, a czuję, że na starość zostałabym demokratką.”

Panna Florentyna skończywszy list nie śmiała oderwać od niego oczu. Wreszcie odważyła się i spojrzała: panna Izabela siedziała na szezlongu blada, z zaciśniętymi rękami.

— Cóż ty na to, Florciu? — spytała po chwili.

— Myślę — odparła cicho zapytana — że pani Karolowa na początku listu najtrafniej osądziła swoje stanowisko w tej sprawie.

— Co za upokorzenie! — szepnęła panna Izabela, nerwowo bijąc ręką w szezlong.

— Upokorzeniem jest proponować komuś trzy tysiące rubli na zastaw sreber, i to wówczas, gdy obcy ofiarowują pięć tysięcy… Innego nie widzę.

— Jak ona nas traktuje… My chyba naprawdę jesteśmy zrujnowani…

— Ależ, Belciu!… — przerwała ożywiając się panna Florentyna. — Właśnie ten cierpki list dowodzi, że nie jesteście zrujnowani. Ciotka lubi być cierpką, ale umie oszczędzać nieszczęście. Gdyby wam groziła ruina, znaleźlibyście w niej tkliwą i delikatną pocieszycielkę.

— Dziękuję za to.

— I nie potrzebujesz obawiać się tego. Jutro wpłynie nam pięć tysięcy rubli, za które można prowadzić dom przez pół roku… choćby przez kwartał. Za parę miesięcy…

— Zlicytują nam kamienicę…

— Prosta forma, i nic więcej. Owszem, możecie zyskać, podczas gdy dzisiaj kamienica jest tylko ciężarem. No, a po ciotce Hortensji dostaniesz ze sto tysięcy rubli. Zresztą — dodała po chwili panna Florentyna podnosząc brwi — ja sama nie jestem pewna, czy i ojciec nie ma jeszcze majątku. Wszyscy są tego zdania…

Panna Izabela wychyliła się z szezlonga i ujęła rękę panny Florentyny.

— Florciu — rzekła zniżając głos — komu ty to mówisz?… Więc naprawdę uważasz mnie tylko za pannę na wydaniu, która nic nie widzi i niczego nie pojmuje?… Myślisz, że nie wiem — domówiła jeszcze ciszej — że już miesiąc, jak pieniądze na utrzymanie domu pożyczasz od Mikołaja…

— Może właśnie ojciec chce tego…

— Czy i tego chce, ażebyś mu co rano podkładała kilka rubli do pugilaresu?

Panna Florentyna spojrzała jej w oczy i poruszyła głową.

— Za dużo wiesz — odparła — ale nie wszystko. Już od dwu tygodni, może od dziesięciu dni widzę, że ojciec miewa po kilkanaście rubli…

— Więc zaciąga długi…

— Nie, ojciec nigdy nie zaciąga długów w mieście. Każdy wierzyciel przychodzi z pożyczką do domu i w gabinecie ojca dostaje kwit albo procent. Nie znasz go pod tym względem.

— Więc skądże teraz ma pieniądze?

— Nie wiem. Widzę, że ma, i słyszę, że zawsze je miał.

— Po cóż w takim razie zezwala na sprzedaż sreber? — pytała natarczywie panna Izabela.

— Może chce zirytować rodzinę.

— A kto wykupił jego weksle?

Panna Florentyna zrobiła rękoma ruch oznaczający rezygnację.

— Nie wykupiła ich Krzeszowska — rzekła — to wiem na pewno. — Więc — albo ciotka Hortensja, albo…

— Albo?…

— Albo sam ojciec. Czy nie wiesz, ile rzeczy robi ojciec, ażeby zaniepokoić rodzinę, a potem śmiać się…

— Za cóż chciałby mnie, nas niepokoić?

— Myśli, że ty jesteś spokojna. Córka powinna nieograniczenie ufać ojcu.

— Ach, tak!… — szepnęła panna Izabela zamyślając się.

Czarno ubrana kuzynka z wolna podniosła się z fotelu i cicho wyszła.

Panna Izabela znowu poczęła patrzeć na swój pokój, który wydał się jej popielatym, na czarne gałązki, które chwiały się za oknem, na parę wróbli świergoczących może o budowie gniazda, na niebo, które stało się jednolicie szarym, bez żadnej jaśniejszej prążki. W jej pamięci znowu odżyła sprawa kwesty i nowej toalety, ale obie wydały się jej tak małymi, tak prawie śmiesznymi, że myśląc o nich nieznacznie wzruszyła ramionami.

Dręczyły ją inne pytania: czyby nie oddać serwisu hrabinie Karolowej — i — skąd ojciec ma pieniądze? Jeżeli miał je dawniej, dlaczego pozwolił na zaciąganie długów u Mikołaja?… A jeżeli nie miał, z jakiego źródła czerpie je dziś?… Jeżeli ona odda serwis i srebra ciotce, może stracić okazję do korzystnego pozbycia się ich, a jeżeli sprzeda za pięć tysięcy, pamiątki te naprawdę mogą dostać się w niewłaściwe ręce, jak pisała hrabina.

Nagle przerwał się ten bieg myśli: bystre jej ucho usłyszało w dalszych pokojach szmer. Było to męskie stąpanie, miarowe, spokojne. W salonie stłumił je nieco dywan, w pokoju jadalnym wzmocniło się, w jej sypialni przycichło, jakby ktoś szedł na palcach.

— Proszę, papo — odezwała się panna Izabela usłyszawszy pukanie do swych drzwi.

Wszedł pan Tomasz. Ona podniosła się z szezlonga, ale ojciec nie pozwolił na to. Objął ją w ramiona, ucałował w głowę i zanim usiadł przy niej, rzucił okiem w duże lustro na ścianie. Zobaczył tam swoją piękną twarz, siwe wąsy, swój ciemny żakiet bez zarzutu, gładkie spodnie, jakby dopiero co wyszły od krawca, i uznał, że wszystko jest dobrze.

— Słyszę — rzekł do córki uśmiechając się — że panienka odbiera korespondencje, które jej psują humor.

— Ach, papo, gdybyś wiedział, jakim tonem przemawia ciotka…

— Zapewne tonem osoby chorej na nerwy. Za to nie możesz mieć do niej żalu.

— Gdyby tylko żal. Ja boję się, że ona ma rację i że nasze srebra mogą naprawdę znaleźć się na jakim bankierskim stole.

Przytuliła głowę do ramienia ojca. Pan Tomasz spojrzał niechcący w lusterko na stoliku i przyznał w duchu, że oboje w tej chwili tworzą bardzo piękną grupę. Szczególniej dobrze odbijała obawa rozlana na twarzy córki od jego spokoju. Uśmiechnął się.

— Bankierskie stoły!… — powtórzył. — Srebra naszych przodków bywały już na stołach Tatarów, Kozaków, zbuntowanych chłopów, i nie tylko nam to nie uchybiało, ale nawet przynosiło zaszczyt. Kto walczy, naraża się na straty.

— Tracili przez wojnę i na wojnie — wtrąciła panna Izabela.

— A dziś nie ma wojny?… Zmieniła się tylko broń: zamiast kosą albo jataganem walczą rublem. Joasia dobrze to rozumiała sprzedając nie serwis — ale rodzinny majątek, albo rozbierając na wybudowanie spichlerza ruiny zamku.

— Więc jesteśmy zwyciężeni!… — szepnęła panna Izabela.

— Nie, dziecko — odparł pan Tomasz prostując się. — My dopiero zaczniemy triumfować i bodaj czy nie tego boi się moja siostra i jej koteria. Oni tak głęboko zasnęli, że razi ich każdy objaw żywotności, każdy mój śmielszy krok — dodał jakby do siebie.

— Twój, papo?

— Tak. Myśleli, że poproszę ich o pomoc. Sama Joasia chętnie zrobiłaby mnie swoim plenipotentem. Ja natomiast podziękowałem im za emeryturę i zbliżyłem się do mieszczaństwa. Zyskałem u tych ludzi powagę, która zaczyna trwożyć nasze sfery. Myśleli, że zejdę na drugi plan, a widzą, że mogę wysunąć się na pierwszy.

— Ty, papo?

— Ja. Dotychczas milczałem nie mając odpowiednich wykonawców. Dziś znalazłem takiego, który zrozumiał moje idee, i zacznę działać.

— Któż to jest? — spytała panna Izabela, ze zdumieniem patrząc na ojca.

— Niejaki Wokulski, kupiec, żelazny człowiek. Przy jego pomocy zorganizuję nasze mieszczaństwo, stworzę towarzystwo do handlu ze Wschodem, tym sposobem dźwignę przemysł…

— Ty, papo?

— I wówczas zobaczymy, kto wysunie się naprzód, choćby przy możliwych wyborach do rady miejskiej…

Panna Izabela słuchała z szeroko otwartymi oczyma.

— Czy ten człowiek — szepnęła — o którym mówisz, papo, nie jest jakim aferzystą, awanturnikiem?…

— Nie znasz go więc? — spytał pan Tomasz. — On jednak jest jednym z naszych dostawców.

— Sklep znam, bardzo ładny — mówiła panna Izabela zamyślając się. — Jest tam stary subiekt, który wygląda trochę na dziwaka, ale nadzwyczajnie uprzejmy… Ach, zdaje mi się, że kilka dni temu poznałam i właściciela… Wygląda na gbura…

— Wokulski gbur?… — zdziwił się pan Tomasz. — Jest on wprawdzie trochę sztywny, ale bardzo grzeczny.

Panna Izabela wstrząsnęła głową.

— Niemiły człowiek — odpowiedziała z ożywieniem. — Teraz przypominam go sobie… Będąc we wtorek w sklepie zapytałam go o cenę wachlarza. Trzeba było widzieć, jak spojrzał na mnie!… Nie odpowiedział nic, tylko wyciągnął swoją ogromną czerwoną rękę do subiekta (nawet dość eleganckiego chłopca) i mruknął głosem, w którym czuć było gniew: panie Morawski czy Mraczewski (bo nie pamiętam), pani zapytuje o cenę wachlarza. A… nieciekawego znalazł papo wspólnika!… — śmiała się panna Izabela.

— Szalonej energii człowiek, żelazny człowiek — odparł pan Tomasz. — Oni tacy. Poznasz ich, bo myślę urządzić w domu parę zebrań. Wszyscy oryginalni, ale ten oryginalniejszy od innych.

— Papa tych panów chce przyjmować?…

— Muszę naradzać się z niektórymi. A co do naszych — dodał patrząc w oczy córce — zapewniam cię, że gdy usłyszą, kto u mnie bywa, ani jednego nie zabraknie w salonie.

W tej chwili weszła panna Florentyna zapraszając na obiad. Pan Tomasz podał rękę córce i przeszli we troje do jadalnego pokoju, gdzie już znajdowała się waza tudzież Mikołaj odziany we frak i wielki biały krawat.

— Śmieję się z Belci — rzekł pan Tomasz do kuzynki, która nalewała rosół z wazy. — Wyobraź sobie, Floro, że Wokulski zrobił na niej wrażenie gbura. Czy ty go znasz?

— Któż by dziś nie znał Wokulskiego — odpowiedziała panna Florentyna podając Mikołajowi talerz dla pana. — No, elegancki on nie jest, ale — robi wrażenie…

— Pnia z czerwonymi rękoma — wtrąciła ze śmiechem panna Izabela.

— On mi przypomina Trostiego, pamiętasz, Belu, tego pułkownika strzelców w Paryżu — odpowiedział Pan Tomasz.

— A mnie posąg triumfującego gladiatora — melodyjnym głosem dodała panna Florentyna. — Pamiętasz Belu, we Florencji, tego z podniesionym mieczem? Twarz surowa, nawet dzika, ale piękna.

— A czerwone ręce?… — zapytała panna Izabela.

— Odmroził je na Syberii — wtrąciła panna Florentyna z akcentem.

— Cóż on tam robił?

— Pokutował za uniesienia młodości — rzekł pan Tomasz. — Można mu to przebaczyć.

— Ach, więc jest i bohaterem!…

— I milionerem — dodała panna Florentyna.

— I milionerem? — powtórzyła panna Izabela. — zaczynam wierzyć, że papo zrobił dobry wybór przyjmując go na wspólnika. Chociaż…

— Chociaż?… — spytał ojciec.

— Co powie świat na tę spółkę?

— Kto ma siłę w rękach, ma świat u nóg.

Właśnie Mikołaj obniósł polędwicę, gdy w przedpokoju zadzwoniono. Stary służący wyszedł i po chwili wrócił z listem na srebrnej, a może platerowanej tacy.

— Od pani hrabiny — rzekł.

— Do ciebie, Belu — dodał pan Tomasz biorąc list do ręki. — Pozwolisz, że cię zastąpię w połknięciu tej nowej pigułki.

Otworzył list, zaczął go czytać i ze śmiechem podał pannie Izabeli.

— Oto — zawołał — cała Joasia jest w tym liście. Nerwy, zawsze nerwy!…

Panna Izabela odsunęła talerz i z niepokojem przebiegła papier oczyma. Lecz stopniowo twarz jej wypogodziła się.

— Słuchaj, Florciu — rzekła — bo to ciekawe.

„Droga Belu! — pisze ciotka. — Zapomnij, aniołku, o moim poprzednim liście. W rezultacie twój serwis nic mnie nie obchodzi i znajdziemy inny, gdy będziesz szła za mąż. Ale chodzi mi, ażebyś koniecznie kwestowała tylko ze mną, i właśnie o tym miałam zamiar pisać poprzednio, nie o serwisie. Biedne moje nerwy! jeżeli nie chcesz ich do reszty rozstroić, musisz zgodzić się na moją prośbę.

Grób w naszym kościele będzie cudowny. Mój poczciwy Wokulski daje fontannę, sztuczne ptaszki śpiewające, pozytywkę, która będzie grała same poważne kawałki, i mnóstwo dywanów. Hozer dostarcza kwiatów, a amatorowie urządzają koncert na organ, skrzypce, wiolonczelę i głosy. Jestem zachwycona, ale gdyby mi wśród tych cudów zabrakło ciebie, rozchorowałabym się. A więc tak?… Ściskam cię i całuję po tysiąc razy, kochająca ciotka.

Joanna





Postscriptum. Jutro jedziemy do magazynu zamówić dla ciebie kostium wiosenny. Umarłabym, gdybyś go nie przyjęła.”

Panna Izabela była rozpromieniona. List ten spełniał wszystkie jej nadzieje.

— Wokulski jest nieporównany! — rzekł śmiejąc się Pan Tomasz. — Szturmem zdobył Joasię, która nie tylko nie będzie mi wymawiała wspólnika, lecz nawet gotowa o niego walczyć ze mną.

Mikołaj podał kurczęta.

— Musi to być jednakże genialny człowiek — zauważyła panna Florentyna.

— Wokulski?… no, nie — mówił pan Tomasz. — Jest to człowiek szalonej energii, ale co się tyczy daru kombinowania, nie powiem, ażeby posiadał go w wysokim stopniu.

— Zdaje mi się, że składa tego dowody.

— Wszystko to są dowody tylko energii — odpowiedział pan Tomasz. — Dar kombinacji, genialny umysł poznaje się w innych rzeczach, choćby… w grze. Ja z nim dosyć często grywam w pikietę, gdzie koniecznie trzeba kombinować. Rezultat jest taki, że przegrałem osiem do dziesięciu rubli, a wygrałem około siedemdziesięciu, chociaż — nie mam pretensji do geniuszu! — dodał skromnie.

Pannie Izabeli wypadł z ręki widelec. Pobladła i chwyciwszy się za czoło szepnęła:

— A!… a!…

Ojciec i panna Florentyna zerwali się z krzeseł.

— Co ci jest Belu?… — spytał zatrwożony pan Tomasz.

— Nic — odpowiedziała wstając od stołu — migrena. Od godziny czułam, że będę ją mieć… To nic, papo…

Pocałowała ojca w rękę i wyszła do swego pokoju.

— Nagła migrena powinna by przejść zaraz — rzekł Pan Tomasz. — Pójdź do niej, Florciu. Ja na chwilę wyjdę do miasta, bo muszę zobaczyć się z kilkoma osobami, ale wcześniej wrócę. Tymczasem czuwaj nad nią, kochana Florciu, proszę cię o to — mówił pan Tomasz ze spokojną fizjognomią człowieka, bez którego poleceń albo prośby nie może być dobrze na świecie.

— Zaraz do niej pójdę, tylko tu zrobię porządek — odpowiedziała panna Florentyna, dla której ład w domu był sprawą ważniejszą od czyjejkolwiek migreny.

Już mrok ogarnął ziemię… Panna Izabela jest znowu sama w swoim gabinecie; upadła na szezlong i obu rękami zasłoniła oczy. Spod kaskady tkanin spływających aż na podłogę wysunął się jej wąski pantofelek i kawałek pończoszki; ale tego nikt nie widzi ani ona o tym nie myśli. W tej chwili jej duszę znowu targa gniew, żal i wstyd. Ciotka ją przeprosiła, ona sama będzie kwestować przy najładniejszym grobie i będzie miała najpiękniejszy kostium; lecz mimo to — jest nieszczęśliwą… Doznaje takich uczuć, jak gdyby wszedłszy do pełnego salonu ujrzała nagle na swym nowym kostiumie ogromną tłustą plamę obrzydłej formy i koloru, jakby suknię wytarzano gdzieś na kuchennych schodach. Myśl o tym jest dla niej tak wstrętna, że ślina napływa jej do ust.

Co za straszne położenie!… Już miesiąc zadłużają się u swego lokaja, a od dziesięciu dni jej ojciec na swoje drobne wydatki wygrywa pieniądze w karty… Wygrać można; panowie wygrywają tysiące, ale — nie na opędzenie pierwszych potrzeb, i przecież — nie od kupców. Ach, gdyby można, upadłaby ojcu do nóg i błagała go, ażeby nie grywał z tymi ludźmi, a przynajmniej nie teraz, kiedy ich stan majątkowy jest tak ciężki. Za kilka dni, gdy odbierze pieniądze za swój serwis, sama wręczy ojcu paręset rubli prosząc, ażeby je przegrał do tego pana Wokulskiego, ażeby wynagrodził go hojniej, niż ona wynagrodzi Mikołaja za zaciągnięte długi.

Ale czyż jej wypada zrobić to, a nawet mówić o tym ojcu?…

„Wokulski?… Wokulski?… — szepcze panna Izabela. — Któż to jest ten Wokulski, który dziś tak nagle ukazał się jej od razu z kilku stron, pod rozmaitymi postaciami. Co on ma do czynienia z jej ciotką, z ojcem?…”

I otóż zdaje się jej, że już od kilku tygodni coś słyszała o tym człowieku. Jakiś kupiec niedawno ofiarował parę tysięcy rubli na dobroczynność, ale nie była pewna, czy to był handlujący strojami damskimi, czy futrami. Potem mówiono, że także jakiś kupiec podczas wojny bułgarskiej dorobił się wielkiego majątku, tylko nie uważała, czy dorobił się szewc, u którego ona bierze buciki, czy jej fryzjer? I dopiero teraz przypomina sobie, że ten kupiec, który dał pieniądze na dobroczynność, i ten, który zyskał duży majątek, są jedną osobą, że to właśnie jest ów Wokulski, który do jej ojca przegrywa w karty, a którego jej ciotka, znana z dumy hrabina Karolowa, nazywa: „mój poczciwy Wokulski!…”

W tej chwili przypomina sobie nawet fizjognomię tego człowieka, który w sklepie nie chciał z nią mówić, tylko cofnąwszy się za ogromne japońskie wazony przypatrywał się jej posępnie. Jak on na nią patrzył…

Jednego dnia weszła z panną Florentyną na czekoladę do cukierni, przez figle. Usiadły przy oknie, za którym zebrało się kilkoro obdartych dzieci. Dzieci spoglądały na nią, na czekoladę i na ciastka z ciekawością i łakomstwem głodnych zwierzątek, a ten kupiec — tak samo na nią patrzył.

Lekki dreszcz przebiegł pannę Izabelę. I to ma być wspólnik jej ojca?… Do czego ten wspólnik?… Skąd jej ojcu przyszło do głowy zawiązywać jakieś towarzystwa handlowe, tworzyć jakieś rozległe plany, o których nigdy dawniej nie marzył?… Chce przy pomocy mieszczaństwa wysunąć się na czoło arystokracji; chce zostać wybranym do rady miejskiej, której nie było i nie ma?…

Ależ ten Wokulski to naprawdę jakiś aferzysta, może oszust, który potrzebuje głośnego nazwiska na szyld do swoich przedsiębiorstw. Bywały takie wypadki. Ileż pięknych nazwisk szlachty niemieckiej i węgierskiej unurzało się w operacjach handlowych, których ona nawet nie rozumie, a ojciec chyba nie więcej.

Zrobiło się już zupełnie ciemno; na ulicy zapalono latarnie, których blask wpadał do gabinetu panny Izabeli malując na suficie ramę okna i zwoje firanki. Wyglądało to jak krzyż na tle jasności, którą powoli zasłania gęsty obłok.

„Gdzie to ja widziałam taki krzyż, taką chmurę i jasność?…” — zapytała się panna Izabela. Zaczęła przypominać sobie widziane w życiu okolice i — marzyć.

Zdawało się jej, że powozem jedzie przez jakąś znaną miejscowość. Krajobraz jest podobny do olbrzymiego pierścienia, utworzonego z lasów i zielonych gór, a jej powóz znajduje się na krawędzi pierścienia i zjeżdża na dół. Czy on zjeżdża? bo ani zbliża się do niczego, ani od niczego nie oddala, tak jakby stał w miejscu. Ale zjeżdża: widać to po wizerunku słońca, które odbija się w lakierowanym skrzydle powozu i drgając, z wolna posuwa się w tył. Zresztą słychać turkot… To turkot dorożki na ulicy?… Nie, to turkoczą machiny pracujące gdzieś w głębi owego pierścienia gór i lasów. Widać tam nawet, na dole, jakby jezioro czarnych dymów i białych par, ujęte w ramę zieloności.

Teraz panna Izabela spostrzega ojca, który siedzi przy niej i z uwagą ogląda sobie paznokcie, od czasu do czasu rzucając okiem na krajobraz. Powóz ciągle stoi na krawędzi pierścienia niby bez ruchu, a tylko wizerunek słońca, odbitego w lakierowanym skrzydle, wolno posuwa się ku tyłowi. Ten pozorny spoczynek czy też utajony ruch w wysokim stopniu drażni pannę Izabelę. „Czy my jedziemy, czy stoimy?” — pyta ojca. Ale ojciec nie odpowiada nic, jakby jej nie widział; ogląda swoje piękne paznokcie i czasami rzuca okiem na okolicę…

Wtem (powóz ciągle drży i słychać turkot) z głębi jeziora czarnych dymów i białych par wynurza się do pół figury jakiś człowiek. Ma krótko ostrzyżone włosy, śniadą twarz, która przypomina Trostiego, pułkownika strzelców (a może gladiatora z Florencji?), i ogromne czerwone dłonie. Odziany jest w zasmoloną koszulę z rękawami zawiniętymi wyżej łokcia; w lewej ręce, tuż przy piersi, trzyma karty ułożone w wachlarz, w prawej, którą podniósł nad głowę, trzyma jedną kartę, widocznie w tym celu, aby ją rzucić na przód siedzenia powozu. Reszty postaci nie widać spośród dymu.

„Co on robi, ojcze?” — pyta się zalękniona panna Izabela.

„Gra ze mną w pikietę” — odpowiada ojciec, również trzymając w rękach karty.

„Ależ to straszny człowiek, papo!”

„Nawet tacy nie robią nic złego kobietom” — odpowiada pan Tomasz.

Teraz dopiero panna Izabela spostrzega, że człowiek w koszuli patrzy na nią jakimś szczególnym wzrokiem, ciągle trzymając kartę nad głową. Dym i para, kotłujące w dolinie, chwilami zasłaniają jego rozpiętą koszulę i surowe oblicze; tonie wśród nich — nie ma go. Tylko spoza dymu widać blady połysk jego oczów, a nad dymem obnażoną do łokcia rękę i — kartę.

„Co znaczy ta karta, papo?…” — zapytuje ojca.

Ale ojciec spokojnie patrzy we własne karty i nie powiada nic, jakby jej nie widział.

„Kiedyż nareszcie wyjedziemy z tego miejsca?…”

Ale choć powóz drży i słońce odbite w skrzydle posuwa się ku tyłowi, ciągle u stopni widać jezioro dymu, a w nim zanurzonego człowieka, jego rękę nad głową i — kartę.

Pannę Izabelę ogarnia nerwowy niepokój, skupia wszystkie wspomnienia, wszystkie myśli, ażeby odgadnąć co znaczy karta, którą trzyma ten człowiek?…

Czy to są pieniądze, które przegrał do ojca w pikietę? Chyba nie. Może ofiara, jaką złożył Towarzystwu Dobroczynności? I to nie. Może tysiąc rubli, które dał ciotce na ochronę, a może to jest kwit na fontannę, ptaszki i dywany do ubrania grobu Pańskiego?… Także nie; to wszystko nie niepokoiłoby jej.

Stopniowo pannę Izabelę napełnia wielka bojaźń. Może to są weksle jej ojca, które ktoś niedawno wykupił?… W takim razie wziąwszy pieniądze za srebra i serwis spłaci ten dług najpierwej i uwolni się od podobnego wierzyciela. Ale człowiek pogrążony w dymie wciąż patrzy jej w oczy i karty nie rzuca. Więc może… Ach!…

Panna Izabela zrywa się z szezlonga, potrąca w ciemności o taburet i drżącymi rękoma dzwoni. Dzwoni już drugi raz, nie odpowiada nikt, więc wybiega do przedpokoju i we drzwiach spotyka pannę Florentynę, która chwyta ją za rękę i mówi ze zdziwieniem:

— Co tobie, Belciu?…

Światło w przedpokoju nieco oprzytomnia pannę Izabelę. Uśmiecha się.

— Weź, Florciu, lampę do mego pokoju. Papa jest?

— Przed chwilą wyjechał.

— A Mikołaj?

— Zaraz wróci, poszedł oddać list posłańcowi. Czy gorzej boli cię głowa? — pyta panna Florentyna.

— Nie — śmieje się panna Izabela — tylko zdrzemnęłam się i tak mi się coś majaczyło.

Panna Florentyna bierze lampę i obie z kuzynką idą do jej gabinetu. Panna Izabela siada na szezlongu, zasłania ręką oczy przed światłem i mówi:

— Wiesz, Florciu, namyśliłam się, nie sprzedam moich sreber obcemu. Mogą naprawdę dostać się Bóg wie w jakie ręce. Siądź zaraz, jeżeliś łaskawa, przy moim biurku i napisz do ciotki, że… przyjmuję jej propozycję. Niech nam pożyczy trzy tysiące rubli i niech weźmie serwis i srebra.

Panna Florentyna patrzy na nią z najwyższym zdumieniem, wreszcie odpowiada:

— To jest niemożliwe, Belciu.

— Dlaczego?…

— Przed kwadransem otrzymałam list od pani Meliton, że srebra i serwis już kupione.

— Już?… Kto je kupił? — woła panna Izabela chwytając kuzynkę za ręce.

Panna Florentyna jest zmieszana.

— Podobno jakiś kupiec z Rosji… — mówi, lecz czuć, że mówi nieprawdę.

— Ty coś wiesz, Florciu!… Proszę cię, powiedz!… — błaga ją panna Izabela. Jej oczy napełniają się łzami.

— Zresztą tobie powiem, tylko nie zdradź tajemnicy przed ojcem — prosi kuzynka.

— Więc kto?… No, kto kupił?…

— Wokulski — odpowiada panna Florentyna.

Pannie Izabeli w jednej chwili obeschły oczy nabierając przy tym barwy stalowej. Odpycha z gniewem ręce kuzynki, przechodzi tam i na powrót swój gabinet, wreszcie siada na foteliku naprzeciw panny Florentyny. Nie jest już przestraszoną i zdenerwowaną pięknością, ale wielką damą, która ma zamiar kogoś ze służby osądzić, a może wydalić.

— Powiedz mi, kuzynko — mówi pięknym kontraltowym głosem — co to za śmieszny spisek knujecie przeciwko mnie?

— Ja?… spisek?… — powtarza panna Florentyna, przyciskając rękoma piersi. — Nie rozumiem cię, Belu…

— Tak. Ty, pani Meliton i ten… zabawny bohater… Wokulski…

— Ja i Wokulski?… — powtarza panna Florentyna. Tym razem zdziwienie jej jest tak szczere, że wątpić nie można.

— Przypuśćmy, że nie spiskujesz — ciągnie dalej Panna Izabela — ale coś wiesz…

— O Wokulskim wiem to, co wszyscy. Ma sklep, w którym kupujemy, zrobił majątek na wojnie…

— A o tym, że wciąga papę do spółki handlowej, nie słyszałaś?

Wyraziste oczy panny Florentyny zrobiły się bardzo dużymi.

— Ojca twego wciąga do spółki?… — rzekła wzruszając ramionami. — Do jakiejże spółki może go wciągnąć?…

I w tej chwili przestrasza się własnych słów…

Panna Izabela nie mogła wątpić o jej niewinności; znowu parę razy przeszła się po gabinecie z ruchami zamkniętej lwicy i nagle zapytała:

— Powiedzże mi przynajmniej: co sądzisz o tym człowieku?

— Ja o Wokulskim?… Nic o nim nie sądzę, wyjąwszy chyba to, że szuka rozgłosu i stosunków.

— Więc dla rozgłosu ofiarował tysiąc rubli na ochronę?

— Z pewnością. Dał przecie dwa razy tyle na dobroczynność.

— A dlaczego kupił mój serwis i srebra?

— Zapewne dlatego, ażeby je z zyskiem sprzedać — odpowiedziała panna Florentyna. — W Anglii za podobne rzeczy dobrze płacą.

— A dlaczego… wykupił weksle papy?

— Skąd wiesz, że to on? W tym nie miałby żadnego interesu.

— Nic nie wiem — pochwyciła gorączkowo panna Izabela — ale wszystko przeczuwam, wszystko rozumiem… Ten człowiek chce zbliżyć się do nas…

— Już się przecie poznał z ojcem — wtrąciła panna Florentyna.

— Więc do mnie chce się zbliżyć!… — zawołała panna Izabela z wybuchem. — Poznałam to po…

Wstyd jej było dodać: „po jego spojrzeniu”.

— Czy nie uprzedzasz się, Belciu?…

— Nie. To, czego doznaję w tej chwili, nie jest uprzedzeniem, ale raczej jasnowidzeniem. Nawet nie domyślasz się, jak ja dawno znam tego człowieka, a raczej — od jak dawna on mnie prześladuje. Teraz dopiero przypominam sobie, że przed rokiem nie było przedstawienia w teatrze, nie było koncertu, odczytu, na którym bym go nie spotkała, i dopiero dziś ta… bezmyślna figura wydaje mi się straszną…

Panna Florentyna aż cofnęła się z fotelikiem, szepcząc:

— Więc przypuszczasz, żeby się ośmielił…

— Zagustować we mnie?… — przerwała ze śmiechem panna Izabela. — Tego nawet nie myślałabym mu bronić. Nie jestem ani tak naiwna, ani tak fałszywie skromna, ażeby nie wiedzieć, że się podobam… mój Boże! nawet służbie… Kiedyś gniewało mnie to jak żebranina, która zastępuje nam drogę na ulicach, dzwoni do mieszkań albo pisuje listy z prośbą o wsparcie. Ale dziś — tylko zrozumiałam lepiej słowa Zbawcy: „Komu wiele dano, od tego wiele żądać będą.”.

— Zresztą — dodała wzruszając ramionami — mężczyźni w tak bezceremonialny sposób zaszczycają nas swoim uwielbieniem, że nie tylko już nie dziwię się ich nadskakiwaniu albo impertynenckim spojrzeniom, ale temu, gdy jest inaczej. Jeżeli w salonie spotkam człowieka, który mi nie mówi o swej sympatii i cierpieniach albo nie milczy posępnie w sposób zdradzający jeszcze większą sympatię i cierpienia, albo nie okazuje mi lodowatej obojętności, co ma być oznaką najwyższej sympatii i cierpień, wtedy — czuję, że mi czegoś brak, jak gdybym zapomniała wachlarza albo chusteczki… O, ja ich znam! tych wszystkich donżuanów, poetów, filozofów, bohaterów, te wszystkie tkliwe, bezinteresowne, złamane, rozmarzone albo silne dusze… Znam całą tę maskaradę i zapewniam cię, że dobrze się nią bawię. Cha! cha! cha!… jacy oni śmieszni…

— Nie rozumiem cię, Belciu… — wtrąciła panna Florentyna rozkładając ręce.

— Nie rozumiesz?… Więc chyba nie jesteś kobietą.

Panna Florentyna zrobiła gest przeczący, a następnie powątpiewający.

— Posłuchaj — przerwała panna Izabela. — Od roku już straciliśmy stanowisko w świecie. Nie zaprzeczaj, bo tak jest, wszyscy o tym wiemy. Dziś jesteśmy zrujnowani.

— Przesadzasz…

— Ach, Floro, nie pocieszaj mnie, nie kłam!… Czyżeś nie słyszała przy obiedzie, że nawet tych kilkanaście rubli, które ma obecnie mój ojciec, są wygrane w karty od…

Panna Izabela mówiąc to drżała na całym ciele. Oczy jej błyszczały, na twarzy miała wypieki.

— Otóż w takiej chwili przychodzi ten… kupiec, nabywa nasze weksle, nasz serwis, opętuje mego ojca i ciotkę, czyli — ze wszystkich stron otacza mnie sieciami jak myśliwiec zwierzynę. To już nie smutny wielbiciel, to nie konkurent, którego można odrzucić, to… zdobywca!… On nie wzdycha, ale zakrada się do łask ciotki, ręce i nogi oplątuje ojcu, a mnie chce porwać gwałtem, jeżeli nie zmusić do tego, ażebym mu się sama oddała… Czy rozumiesz tę wyrafinowaną nikczemność?

Panna Florentyna przestraszyła się.

— W takim razie masz bardzo prosty sposób. Powiedz…

— Komu i co?… Czy ciotce, która gotowa popierać tego pana, ażeby mnie zmusić do oddania ręki marszałkowi?… Czy może mam powiedzieć ojcu, przerazić go i przyśpieszyć katastrofę? Jedno tylko zrobię: nie pozwolę ojcu, ażeby zaciągał się do jakichkolwiek spółek, choćbym miała włóczyć mu się u nóg, choćbym miała… zabronić mu tego w imieniu zmarłej matki….

Panna Florentyna patrzy na nią z zachwytem…

— Doprawdy, Belciu — rzekła — przesadzasz. Z twoją energią i taką genialną domyślnością…

— Nie znasz tych ludzi, a ja widziałam ich przy pracy. W ich rękach stalowe szyny zwijają się jak wstążki. To straszni ludzie. Oni dla swoich celów umieją poruszyć wszystkie siły ziemskie, jakich my nawet nie znamy. Oni potrafią łamać, usidlać, płaszczyć się, wszystko ryzykować, nawet — cierpliwie czekać…

— Mówisz na podstawie czytanych romansów.

— Mówię na mocy moich przeczuć, które ostrzegają… wołają, że ten człowiek po to jeździł na wojnę, ażeby mnie zdobyć. I ledwie wrócił, już mnie ze wszystkich stron obsacza… Ale niech się strzeże!… Chce mnie kupić? dobrze, niech kupuje!… przekona się, że jestem bardzo droga… Chce mnie złapać w sieci?… Dobrze, niech je rozsnuwa… ale ja mu się wymknę, choćby — w objęcia marszałka… O Boże! nawet nie domyślałam się, jak głęboką jest przepaść, w którą spadamy, dopóki nie zobaczyłam takiego dna. Z salonów Kwirynału do sklepu… To już nawet nie upadek, to hańba…

Siadła na szezlongu i utuliwszy głowę rękoma szlochała.



VII. Gołąb wychodzi na spotkanie węża

Serwis i srebra familii Łęckich były już sprzedane i nawet jubiler odniósł panu Tomaszowi pieniądze, strąciwszy dla siebie sto kilkadziesiąt rubli składowego i za pośrednictwo. Mimo to hrabina Karolowa nie przestała kochać panny Izabeli; owszem — jej energia i poświęcenie, okazane przy sprzedaży pamiątek, zbudziły w sercu starej damy nowe źródło uczuć rodzinnych. Nie tylko uprosiła pannę Izabelę o przyjęcie pięknego kostiumu, nie tylko co dzień bywała u niej albo ją wzywała do siebie, ale jeszcze (co było dowodem niesłychanej łaski) na całą Wielką Środę ofiarowała jej swój powóz.

— Przejedź się, aniołku, po mieście — mówiła hrabina całując siostrzenicę — i pozałatwiaj drobne sprawunki. Tylko pamiętaj, żebyś mi za to w czasie kwesty wyglądała ślicznie… Tak ślicznie, jak to tylko ty potrafisz!… Proszę cię…

Panna Izabela nie odpowiedziała nic, ale jej spojrzenie i rumieniec kazały domyślać się, że z całą gotowością spełni wolę ciotki.

W Wielką Środę, punkt o jedynastej rano, panna Izabela już siedziała w otwartym powozie wraz ze swoją nieodstępną towarzyszką, panną Florentyną. Po Alei chodziły wiosenne powiewy roznosząc tę szczególną, surową woń, która poprzedza pękanie liści na drzewach i ukazanie się pierwiosnków; szare trawniki nabrały zielonawego odcienia; słońce grzało tak mocno, że panie otworzyły parasolki.

— Śliczny dzień — westchnęła panna Izabela patrząc na niebo, gdzieniegdzie poplamione białymi obłokami.

— Gdzie jaśnie panienka rozkaże jechać? — spytał lokaj zatrzasnąwszy drzwiczki powozu.

— Do sklepu Wokulskiego — z nerwowym pośpiechem odpowiedziała panna Izabela.

Lokaj skoczył na kozioł i spasione gniade konie ruszyły uroczystym kłusem parskając i wyrzucając łbami.

— Dlaczego, Belciu, do Wokulskiego? — zapytała trochę zdziwiona panna Florentyna.

— Chcę sobie kupić paryskie rękawiczki, kilka flakonów perfum…

— To samo dostaniemy gdzie indziej.

— Chcę tam — odpowiedziała sucho panna Izabela.

Od paru dni męczył ją osobliwy niepokój, jakiego już raz doznała w życiu. Będąc przed laty za granicą w ogrodzie aklimatyzacyjnym zobaczyła w jednej z klatek ogromnego tygrysa, który spał oparty o kratę w taki sposób, że mu część głowy i jedno ucho wysunęło się na zewnątrz.

Widząc to panna Izabela uczuła nieprzepartą chęć pochwycenia tygrysa za ucho. Zapach klatki napełniał ją wstrętem, potężne łapy zwierzęcia nieopisaną trwogą, lecz mimo to czuła, że — musi tygrysa przynajmniej dotknąć w ucho.

Dziwny ten pociąg wydał się jej samej niebezpiecznym i nawet śmiesznym. Przemogła się więc i poszła dalej; lecz po paru minutach — wróciła. Znowu cofnęła się, przejrzała inne klatki, starała się o czym innym myśleć. Na próżno. Wróciła się i choć tygrys już nie spał, tylko mrucząc lizał swoje straszliwe łapy, panna Izabela podbiegła do klatki, wsunęła rękę i — drżąca i blada — dotknęła tygrysiego ucha.

W chwilę później wstydziła się swego szaleństwa, lecz zarazem czuła to gorzkie zadowolenie znane ludziom, którzy usłuchają w ważnej sprawie głosu instynktu.

Dziś zbudziło się w niej podobnego rodzaju pragnienie.

Gardziła Wokulskim, serce jej zamierało na samo przypuszczenie, że ten człowiek mógł zapłacić za srebra więcej, niż były warte, a mimo to czuła nieprzeparty pociąg — wejść do sklepu, spojrzeć w oczy Wokulskiemu i zapłacić mu za parę drobiazgów tymi właśnie pieniędzmi, które pochodziły od niego. Strach ją zdejmował na myśl spotkania, lecz niewytłomaczony instynkt popychał.

Na Krakowskim już z daleka zobaczyła szyld z napisem: J. Mincel i S. Wokulski, a o jeden dom bliżej nowy, jeszcze nie wykończony sklep o pięciu oknach frontu, z lustrzanymi szybami. Z kilku pracujących przy nim rzemieślników i robotników jedni od wewnątrz wycierali szyby, drudzy złocili i malowali drzwi i futryny, inni umocowywali przed oknami ogromne mosiężne bariery.

— Cóż to za sklep budują? — spytała panny Florentyny.

— Chyba dla Wokulskiego, bo słyszałam, że wziął obszerniejszy lokal.

„Dla mnie ten sklep!” — pomyślała panna Izabela szarpiąc rękawiczki.

Powóz stanął, lokaj zeskoczył z kozła i pomógł paniom wysiąść. Lecz gdy następnie otworzył z łoskotem drzwi do sklepu Wokulskiego, panna Izabela tak osłabła, że nogi zachwiały się pod nią. Przez chwilę chciała wrócić do powozu i uciec stąd; wnet jednak opanowała się i z podniesioną głową weszła.

Pan Rzecki stał już na środku sklepu i zacierając ręce, witał ją niskimi ukłonami. W głębi pan Lisiecki, podczesując piękną brodę, okrągłymi i pełnymi godności ruchami prezentował brązowe kandelabry jakiejś damie, która siedziała na krześle. Mizerny Klejn wybierał laski młodzieńcowi, który na widok panny Izabeli szybko uzbroił się w binokle — a pachnący heliotropem Mraczewski palił wzrokiem i sztyletował wąsikami dwie rumiane panienki, które towarzyszyły damie i oglądały toaletowe cacka.

Na prawo ode drzwi, za kantorkiem, siedział Wokulski schylony nad rachunkami.

Gdy panna Izabela weszła, młodzieniec oglądający laski poprawił kołnierzyk na szyi, dwie panienki spojrzały na siebie, pan Lisiecki urwał w połowie swój okrągły frazes o stylu kandelabrów, ale zatrzymał okrągłą pozę, a nawet dama słuchająca jego wykładu ciężko odwróciła się na krześle. Przez chwilę sklep zaległa cisza, którą dopiero panna Izabela przerwała odezwawszy się pięknym kontraltem:

— Czy zastałyśmy pana Mraczewskiego?…

— Panie Mraczewski!… — pochwycił pan Ignacy.

Mraczewski już stał przy pannie Izabeli, zarumieniony jak wiśnia, pachnący jak kadzielnica, z pochyloną głową, jak kita wodnej trzciny.

— Przyszłyśmy prosić pana o rękawiczki.

— Numerek pięć i pół — odparł Mraczewski i już trzymał pudełko, które mu nieco drżało w rękach pod wpływem spojrzenia panny Izabeli.

— Otóż nie… — przerwała panna ze śmiechem. — Pięć i trzy czwarte… Już pan zapomniał!…

— Pani, są rzeczy, których się nigdy nie zapomina. Jeżeli jednak rozkazuje pani pięć i trzy czwarte, będę służył w nadziei, że niebawem znowu zaszczyci nas pani swoją obecnością. Bo rękawiczki pięć i trzy czwarte — dodał z lekkim westchnieniem, podsuwając jej kilka innych pudełek — stanowczo zsuną się z rączek…

— Geniusz! — cicho szepnął pan Ignacy mrugając na Lisieckiego, który pogardliwie ruszył ustami.

Dama siedząca na krześle zwróciła się do kandelabrów, dwie panny do toaletki z oliwkowego drzewa, młodzieniec w binoklach począł znowu wybierać laski i — rzeczy w sklepie przeszły do spokojnego trybu. Tylko rozgorączkowany Mraczewski zeskakiwał i wbiegał na drabinkę, wysuwał szuflady i wydobywał coraz nowe pudełka tłomacząc pannie Izabeli po polsku i po francusku, że nie może nosić innych rękawiczek, tylko pięć i pół, ani używać innych perfum, tylko oryginalnych Atkinsona, ani ozdabiać swego stolika innymi drobiazgami, jak paryskimi.

Wokulski pochylił się nad kantorkiem tak, że żyły nabrzmiały mu na czole, i — wciąż rachował w myśli:

„29 a 36 — to 65, a 15 to 80, a 73 — to… to…”

Tu urwał i spod oka spojrzał w stronę panny Izabeli rozmawiającej z Mraczewskim. Oboje stali zwróceni do niego profilem; dostrzegł więc pałający wzrok subiekta przykuty do panny Izabeli, na co ona w sposób demonstracyjny odpowiadała uśmiechem i spojrzeniami łagodnej zachęty.

„29 a 36 — to 65, a 15…” — liczył w myśli Wokulski, lecz nagle pióro prysło mu w ręku. Nie podnosząc głowy wydobył nową stalówkę z szuflady, a jednocześnie, nie wiadomo jakim sposobem, z rachunku wypadło mu pytanie:

„I ja mam niby to ją kochać?… Głupstwo! Przez rok cierpiałem na jakąś chorobę mózgową, a zdawało mi się, że jestem zakochany… 29 a 36… 29 a 36… Nigdym nie przypuszczał, ażeby mogła mi być tak dalece obojętną… Jak ona patrzy na tego osła… No, jest to widocznie osoba, która kokietuje nawet subiektów, a czy tego samego nie robi z furmanami i lokajami!… Pierwszy raz czuję spokój… o Boże… A tak go bardzo pragnąłem…”

Do sklepu weszło jeszcze parę osób, do których niechętnie zwrócił się Mraczewski, powoli wiążąc paczki.

Panna Izabela zbliżyła się do Wokulskiego i wskazując w jego stronę parasolką rzekła dobitnie:

— Floro, bądź łaskawa zapłacić temu panu. Wracamy do domu.

— Kasa jest tu — odezwał się Rzecki podbiegając do panny Florentyny. Wziął od niej pieniądze i oboje cofnęli się w głąb sklepu.

Panna Izabela z wolna podsunęła się tuż do kantorka, za którym siedział Wokulski. Była bardzo blada. Zdawało się, że widok tego człowieka wywiera na nią wpływ magnetyczny.

— Czy mówię z panem Wokulskim?

Wokulski powstał z krzesła i odparł obojętnie:

— Jestem do usług.

— Wszakże to pan kupił nasz serwis i srebra? — mówiła zdławionym głosem.

— Ja, pani.

Teraz panna Izabela zawahała się. Po chwili jednak słaby rumieniec wrócił jej na twarz. Ciągnęła dalej:

— Zapewne pan sprzeda te przedmioty?

— W tym celu je kupiłem.

Rumieniec panny Izabeli wzmocnił się.

— Przyszły nabywca w Warszawie mieszka? — pytała dalej.

— Rzeczy tych nie sprzedam tutaj, lecz za granicą. Tam… dadzą mi wyższą cenę — dodał spostrzegłszy w jej oczach zapytanie.

— Pan spodziewa się dużo zyskać?

— Dlatego, ażeby zyskać, kupiłem.

— Czy i dlatego mój ojciec nie wie, że srebra te są w pańskim ręku? — rzekła ironicznie.

Wokulskiemu drgnęły usta.

— Serwis i srebra nabyłem od jubilera. Sekretu z tego nie robię. Osób trzecich do sprawy nie mieszam, ponieważ to nie jest w zwyczajach handlowych.

Pomimo tak szorstkich odpowiedzi panna Izabela odetchnęła. Nawet oczy jej nieco pociemniały i straciły połysk nienawiści.

— A gdyby mój ojciec namyśliwszy się chciał odkupić te przedmioty, za jaką cenę odstąpiłby je pan teraz?

— Za jaką kupiłem. Rozumie się z doliczeniem procentu w stosunku… sześć… do ośmiu od sta rocznie…

— I wyrzekłby się pan spodziewanego zysku?… Dlaczegóż to?… — przerwała mu z pośpiechem.

— Dlatego, proszę pani, że handel opiera się nie na zyskach spodziewanych, ale na ciągłym obrocie gotówki.

— Żegnam pana i… dziękuję za wyjaśnienia — rzekła panna Izabela widząc, że jej towarzyszka już kończy rachunki.

Wokulski ukłonił się i znowu usiadł do swej księgi.

Gdy lokaj zabrał paczki i panie zajęły miejsca w powozie, panna Florentyna odezwała się tonem wyrzutu:

— Mówiłaś z tym człowiekiem, Belu?…

— Tak i nie żałuję tego. On wszystko skłamał, ale…

— Co znaczy to: *ale*?… — z niepokojem zapytała panna Florentyna.

— Nie pytaj mnie… Nic do mnie nie mów, jeżeli nie chcesz, ażebym rozpłakała się na ulicy…

A po chwili dodała po francusku:

— Zresztą, może zrobiłam źle przyjeżdżając tutaj, ale… wszystko mi jedno!…

— Myślę, Belciu — rzekła, z powagą sznurując usta, jej towarzyszka — że należałoby pomówić o tym z ojcem albo z ciotką.

— Chcesz powiedzieć — przerwała panna Izabela — że muszę pomówić z marszałkiem albo z baronem? Na to zawsze będzie czas; dziś nie mam jeszcze odwagi.

Przerwała się rozmowa. Panie milcząc wróciły do domu; panna Izabela cały dzień była rozdrażniona.

Po wyjściu panny Izabeli ze sklepu Wokulski wziął się znowu do rachunków i bez błędu zsumował dwie duże kolumny cyfr. W połowie trzeciej zatrzymał się i dziwił się temu spokojowi, jaki zapanował w jego duszy. Po całorocznej gorączce i tęsknocie przerywanej wybuchami szału skąd naraz ta obojętność? Gdyby można było jakiegoś człowieka nagle przerzucić z balowej sali do lasu albo z dusznego więzienia na chłodne i obszerne pole, nie doznałby innych wrażeń ani głębszego zdumienia.

„Widocznie przez rok ulegałem częściowemu obłąkaniu” — myślał Wokulski. — „Nie było niebezpieczeństwa, nie było ofiary, której nie poniósłbym dla tej osoby, i ledwiem ją zobaczył, już nic mnie nie obchodzi…

A jak ona rozmawiała ze mną. Ile tam było pogardy dla marnego kupca… »Zapłać temu panu!…« Paradne są te wielkie damy; próżniak, szuler, nawet złodziej, byle miał nazwisko, stanowi dla nich dobre towarzystwo, choćby fizjognomią zamiast ojca przypominał lokaja swej matki. Ale kupiec — jest pariasem… Co mnie to wreszcie obchodzi; gnijcie sobie w spokoju!”

Znowu dodał jedną kolumnę nie uważając nawet, co się dzieje w sklepie.

„Skąd ona wie — myślał dalej — że ja kupiłem serwis i srebra?… A jak wybadywała, czym nie zapłacił więcej niż warte! Z przyjemnością ofiarowałbym im ten pamiątkowy drobiazg. Winienem jej dozgonną wdzięczność, bo gdyby nie szał dla niej, nie dorobiłbym się majątku i spleśniałbym za kantorkiem. A teraz może mi smutno będzie bez tych żalów, rozpaczy i nadziei… Głupie życie!… Po ziemi gonimy marę, którą każdy nosi we własnym sercu, i dopiero gdy stamtąd ucieknie, poznajemy, że to był obłęd… No, nigdy bym nie przypuszczał, że mogą istnieć tak cudowne kuracje. Przed godziną byłem pełen trucizny, a w tej chwili jestem tak spokojny i — jakiś pusty, jakby uciekła ze mnie dusza i wnętrzności, a została tylko skóra i odzież. Co ja teraz będę robił? czym będę żył?… Chyba pojadę na wystawę do Paryża, a potem w Alpy…”

W tej chwili zbliżył się do niego na palcach Rzecki i szepnął:

— Pyszny jest ten Mraczewski, co? Jak on umie rozmawiać z kobietami!

— Jak fryzjerczyk, którego uzuchwalono — odpowiedział Wokulski nie odrywając oczu od księgi.

— Nasze klientki zrobiły go takim — odpowiedział stary subiekt, lecz widząc, że przeszkadza pryncypałowi, cofnął się. Wokulski znowu wpadł w zadumę. Nieznacznie spojrzał na Mraczewskiego i dopiero w tej chwili zauważył, że młody człowiek ma coś szczególnego w fizjognomii.

„Tak — myślał — on jest bezczelnie głupi i zapewne dlatego podoba się kobietom.”

Śmiać mu się chciało i ze spojrzeń panny Izabeli, wysyłanych pod adresem pięknego młodzieńca, i z własnych przywidzeń, które dziś tak nagle go opuściły.

Wtem drgnął; usłyszał imię panny Izabeli i spostrzegł, że w sklepie nie ma nikogo z gości.

— No, ale dzisiaj toś się pan nie ukrywał ze swoimi amorami — mówił ze smutnym uśmiechem Klejn do Mraczewskiego.

— Ale bo jak ona na mnie patrzyła, to ach!… — westchnął Mraczewski, jedną rękę kładąc na piersi, drugą podkręcając wąsika. — Jestem pewny — mówił — że za parę dni otrzymam wonny bilecik. Potem — pierwsza schadzka, potem: „dla pana łamię zasady, w jakich mnie wychowano”, a potem: „czy nie gardzisz mną?” Chwila wcześniej jest bardzo rozkoszną, ale w chwilę później człowiek jest tak zakłopotany…

— Co pan blagujesz! — przerwał mu Lisiecki. — Znamy przecież pańskie konkiety: nazywają się Matyldami, którym pan imponujesz porcją pieczeni i kuflem piwa.

— Matyldy są na co dzień, damy na święta. Ale Iza będzie największym świętem. Słowo honoru daję, że nie znam kobiety, która by na mnie tak piekielne robiła wrażenie… No, ale bo też i ona lgnie do mnie!

Trzasnęły drzwi i do sklepu wszedł jegomość szpakowaty; zażądał breloku do zegarka, a krzyczał i stukał laską tak mocno, jakby miał zamiar kupić całą japońszczyznę.

Wokulski słuchał przechwałek Mraczewskiego bez ruchu. Doświadczał wrażenia, jakby mu na głowę i na piersi spadały ciężary.

— W rezultacie nic mnie to nie obchodzi — szepnął.

Po szpakowatym jegomościu weszła do sklepu dama żądająca parasola, później pan w średnim wieku chcący nabyć kapelusz, potem młody człowiek żądający cygarnicy, nareszcie trzy panny, z których jedna kazała podać sobie rękawiczki Szolca, ale koniecznie Szolca, bo innych nie używa.

Wokulski złożył księgę, z wolna podniósł się z fotelu i sięgnąwszy po kapelusz stojący na kantorku skierował się ku drzwiom. Czuł brak oddechu i jakby rozsadzanie czaszki.

Pan Ignacy zabiegł mu drogę.

— Wychodzisz?… Może zajrzysz do tamtego sklepu — rzekł.

— Nigdzie nie zajrzę, jestem zmęczony — odpowiedział Wokulski nie patrząc mu w oczy.

Gdy wyszedł, Lisiecki trącił Rzeckiego w ramię.

— Coś stary jakby zaczynał robić bokami — szepnął.

— No — odparł pan Ignacy — puszczenie w ruch takiego interesu jak moskiewski to nie chy-chy. Rozumie się.

— Po cóż się w to wdaje?

— Po to, żeby miał nam z czego pensje podwyższać — surowo odpowiedział pan Ignacy.

— A niechże sobie zakłada sto nowych interesów, nawet w Irkucku, byle tak co roku podwyższał — rzekł Lisiecki. — Ja z nim się o to spierać nie będę. Ale swoją drogą, uważam, że jest diabelnie zmieniony, osobliwie dzisiaj. Żydzi, panie, Żydzi — dodał — jak zwąchają jego projekta, dadzą mu łupnia.

— Co tam Żydzi…

— Żydzi, mówię, Żydzi!… Wszystkich trzymają za łeb i nie pozwolą, ażeby im bruździł jakiś Wokulski, nie Żyd ani nawet meches.

— Wokulski zwiąże się ze szlachtą — odpowiedział Ignacy — a i tam są kapitały.

— Kto wie, co gorsze: Żyd czy szlachcic — wtrącił mimochodem Klejn i podniósł brwi w sposób bardzo żałosny.



VIII. Medytacje

Znalazłszy się na ulicy Wokulski stanął na chodniku, jakby namyślając się, dokąd iść. Nie ciągnęło go nic w żadną stronę. Dopiero gdy przypadkiem spojrzał w prawo, na swój nowo wykończony sklep, przed którym już zatrzymywali się ludzie, odwrócił się ze wstrętem i poszedł w lewo.

„Dziwna rzecz, jak mnie to wszystko mało obchodzi” — rzekł do siebie. Potem myślał o tych kilkunastu ludziach, którym już daje zajęcie, i o tych kilkudziesięciu, którzy od pierwszego maja mieli dostać u niego zajęcie, o tych setkach, dla których w ciągu roku miał stworzyć nowe źródła pracy, i o tych tysiącach, którzy dzięki jego tanim towarom mogliby sobie poprawić nędzny byt — i — czuł, że ci wszyscy ludzie i ich rodziny nic go w tej chwili nie interesują.

„Sklep odstąpię, nie zawiążę spółki i wyjadę za granicę” — myślał.

„A zawód, jaki zrobisz ludziom, którzy w tobie położyli nadzieję?”

„Zawód?… Alboż mnie samego nie spotkał zawód?…”

Wokulski idąc poczuł jakąś niewygodę; lecz dopiero zastanowiwszy się osądził, że męczy go ciągłe ustępowanie z drogi; przeszedł więc na drugą stronę ulicy, gdzie ruch był mniejszy.

„A jednak ten Mraczewski jest infamis! — myślał. — Jak można mówić takie rzeczy w sklepie? »Za parę dni otrzymam bilecik, a potem — schadzka!… Ha, sama sobie winna, nie trzeba kokietować błaznów… Zresztą — wszystko mi jedno.”

Czuł w duszy dziwną pustkę, a na samym jej dnie coś, jakby kroplę piekącej goryczy. Żadnych sił, żadnych pragnień, nic, tylko tę kroplę tak małą, że jej niepodobna dojrzeć, a tak gorzką, że cały świat można by nią zatruć.

„Chwilowa apatia, wyczerpanie, brak wrażeń… Za dużo myślę o interesach” — mówił.

Stanął i patrzył. Dzień przedświąteczny i ładna pogoda wywabiły mnóstwo ludzi na bruk miejski. Sznur powozów i pstrokaty falujący tłum między Kopernikiem i Zygmuntem wyglądał jak stado ptaków, które właśnie w tej chwili unosiły się nad miastem dążąc ku północy.

„Szczególna rzecz — mówił. — Każdy ptak w górze i każdy człowiek na ziemi wyobraża sobie, że idzie tam, dokąd chce. I dopiero ktoś stojący na boku widzi, że wszystkich razem pcha naprzód jakiś fatalny prąd, mocniejszy od ich przewidywań i pragnień. Może nawet ten sam, który unosi smugę iskier wydmuchniętych przez lokomotywę podczas nocy?… Błyszczą przez mgnienie oka, aby zgasnąć na całą wieczność, i to nazywa się życiem.


Mijają ludzkie pokolenia
Jak fale, gdy wiatr morzem zmąci;
I nie masz godów ich pamięci,
I nie masz bólów ich wspomnienia.

Gdzie ja to czytałem?… Wszystko jedno.”

Nieustanny turkot i szmer wydał się Wokulskiemu nieznośnym, a wewnętrzna pustka straszliwą. Chciał czymś się zająć i przypomniał sobie, że jeden z zagranicznych kapitalistów pytał go o zdanie w kwestii bulwarów nad Wisłą. Zdanie już miał wyrobione: Warszawa całym swoim ogromem ciąży i zsuwa się ku Wiśle. Gdyby brzeg rzeki obwarować bulwarami, powstałaby tam najpiękniejsza część miasta: gmachy, sklepy, aleje…

„Trzeba spojrzeć, jak by to wyglądało?” — szepnął Wokulski i skręcił na ulicę Karową.

Przy bramie wiodącej tam zobaczył bosego, przewiązanego sznurami tragarza, który pił wodę prosto z wodotrysku; zachlapał się od stóp do głów, ale miał bardzo zadowoloną minę i śmiejące się oczy.

„Jużci, ten ma, czego pragnął. Ja, ledwiem zbliżył się do źródła, widzę, że nie tylko ono znikło, ale nawet wysychają moje pragnienia. Pomimo to mnie zazdroszczą, a nad nim każą się litować. Co za potworne nieporozumienie!”

Na Karowej odetchnął. Zdawało mu się, że jest jedną z plew, które już odrzucił młyn wielkomiejskiego życia, i że powoli spływa sobie gdzieś na dół tym rynsztokiem zaciśniętym odwiecznymi murami.

„Cóż bulwary?… — myślał. — Postoją jakiś czas, a potem będą walić się, zarośnięte zielskiem i odrapane, jak te oto ściany. Ludzie, którzy je budowali z wielką pracą, mieli także na celu zdrowie, bezpieczeństwo, majątek, a może zabawy i pieszczoty. I gdzie oni są?… Zostały po nich spękane mury, jak skorupa po ślimaku dawnej epoki. A cały pożytek z tego stosu cegieł i tysiąca innych stosów będzie, że przyszły geolog nazwie je skałą ludzkiego wyrobu, jak my dziś koralowe rafy albo kredę nazywamy skałami wyrobu pierwotniaków.


I cóż ma z trudu swego człowiek?…
I z prac tych, które wszczął pod słońcem?…
Znikomość — jego dzieła gońcem,
A żywot jego mgnieniem powiek.

Gdziem ja to czytał, gdzie?… Mniejsza o to.”

Zatrzymał się w połowie drogi i patrzył na ciągnącą się u jego stóp dzielnicę między Nowym Zjazdem i Tamką. Uderzyło go podobieństwo do drabiny, której jeden bok stanowi ulica Dobra, drugi — linia od Garbarskiej do Topieli, a kilkanaście uliczek poprzecznych formują jakby szczeble.

„Nigdzie nie wejdziemy po tej leżącej drabinie — myślał. — To chory kąt, dziki kąt.”

I rozważał pełen goryczy, że ten płat ziemi nadrzecznej, zasypany śmieciem z całego miasta, nie urodzi nic nad parterowe i jednopiętrowe domki barwy czekoladowej i jasnożółtej, ciemnozielonej i pomarańczowej. Nic, oprócz białych i czarnych parkanów, otaczających puste place, skąd gdzieniegdzie wyskakuje kilkupiętrowa kamienica jak sosna, która ocalała z wyciętego lasu, przestraszona własną samotnością.

„Nic, nic!…” — powtarzał tułając się po uliczkach, gdzie widać było rudery zapadnięte niżej bruku, z dachami porosłymi mchem, lokale z okiennicami dniem i nocą zamkniętymi na sztaby, drzwi zabite gwoździami, naprzód i w tył powychylane ściany, okna łatane papierem albo zatkane łachmanem. Szedł, przez brudne szyby zaglądał do mieszkań i nasycał się widokiem szaf bez drzwi, krzeseł na trzech nogach, kanap z wydartym siedzeniem, zegarów o jednej skazówce z porozbijanymi cyferblatami.

Szedł i cicho śmiał się na widok wyrobników wiecznie czekających na robotę, rzemieślników, którzy trudnią się tylko łataniem starej odzieży, przekupek, których całym majątkiem jest kosz zeschłych ciastek — na widok obdartych mężczyzn, mizernych dzieci i kobiet niezwykle brudnych.

„Oto miniatura kraju — myślał — w którym wszystko dąży do spodlenia i wytępienia rasy. Jedni giną z niedostatku, drudzy z rozpusty. Praca odejmuje sobie od ust, ażeby karmić niedołęgów; miłosierdzie hoduje bezczelnych próżniaków, a ubóstwo nie mogące zdobyć się na sprzęty otacza się wiecznie głodnymi dziećmi, których największą zaletą jest wczesna śmierć.

Tu nie poradzi jednostka z inicjatywą, bo wszystko sprzysięgło się, ażeby ją spętać i zużyć w pustej walce — o nic.”

Potem w wielkich konturach przyszła mu na myśl jego własna historia. Kiedy dzieckiem będąc łaknął wiedzy — oddano go do sklepu z restauracją. Kiedy zabijał się nocną pracą będąc subiektem — wszyscy szydzili z niego, zacząwszy od kuchcików, skończywszy na upijającej się w sklepie inteligencji. Kiedy nareszcie dostał się do uniwersytetu — prześladowano go porcjami, które niedawno podawał gościom.

Odetchnął dopiero na Syberii. Tam mógł pracować, tam zdobył uznanie i przyjaźń Czerskich, Czekanowskich, Dybowskich. Wrócił do kraju prawie uczonym, lecz gdy w tym kierunku szukał zajęcia, zakrzyczano go i odesłano do handlu…

„To taki piękny kawałek chleba w tak ciężkich czasach!”

No i wrócił do handlu, a wtedy zawołano, że się sprzedał i żyje na łasce żony, z pracy Minclów.

Traf zdarzył, iż po kilku latach żona umarła zostawiając mu dość spory majątek. Pochowawszy ją, Wokulski odsunął się nieco od sklepu, a znowu zbliżył się do książek. I może z galanteryjnego kupca zostałby na dobre uczonym przyrodnikiem, gdyby znalazłszy się raz w teatrze nie zobaczył panny Izabeli.

Siedziała w loży z ojcem i panną Florentyną, ubrana w białą suknię. Nie patrzyła na scenę, która w tej chwili skupiała uwagę wszystkich, ale gdzieś przed siebie, nie wiadomo gdzie i na co. Może myślała o Apollinie?…

Wokulski przypatrywał się jej cały czas.

Zrobiła na nim szczególne wrażenie. Zdawało mu się, że już kiedyś ją widział i że ją dobrze zna. Wpatrzył się lepiej w jej rozmarzone oczy i nie wiadomo skąd przypomniał sobie niezmierny spokój syberyjskich pustyń, gdzie bywa niekiedy tak cicho, że prawie słychać szelest duchów wracających ku zachodowi. Dopiero później przyszło mu na myśl, że on nigdzie i nigdy jej nie widział, ale — że jest tak coś — jakby na nią od dawna czekał.

„Tyżeś to czy nie ty?…” — pytał się w duchu, nie mogąc od niej oczu oderwać.

Odtąd mało pamiętał o sklepie i o swoich książkach, lecz ciągle szukał okazji do widywania panny Izabeli w teatrze, na koncertach lub na odczytach. Uczuć swoich nie nazwałby miłością i w ogóle nie był pewny, czy dla oznaczenia ich istnieje w ludzkim języku odpowiedni wyraz. Czuł tylko, że stała się ona jakimś mistycznym punktem, w którym zbiegają się wszystkie jego wspomnienia, pragnienia i nadzieje, ogniskiem, bez którego życie nie miałoby stylu, a nawet sensu. Służba w sklepie kolonialnym, uniwersytet, Syberia, ożenienie się z wdową po Minclu, a w końcu mimowolne pójście do teatru, gdy wcale nie miał chęci — wszystko to były ścieżki i etapy, którymi los prowadził go do zobaczenia panny Izabeli.

Od tej pory czas miał dla niego dwie fazy. Kiedy patrzył na pannę Izabelę, czuł się absolutnie spokojnym i jakby większym; nie widząc — myślał o niej i tęsknił. Niekiedy zdawało mu się, że w jego uczuciach tkwi jakaś omyłka i że panna Izabela nie jest żadnym środkiem jego duszy, ale zwykłą, a może nawet bardzo pospolitą panną na wydaniu. A wówczas przychodził mu do głowy dziwaczny projekt:

„Zapoznam się z nią i wprost zapytam: czy ty jesteś tym, na co przez całe życie czekałem?… Jeżeli nie jesteś, odejdę bez pretensji i żalu…”

W chwilę później spostrzegał, że projekt ten zdradza umysłowe zboczenie. Kwestię więc: czym jest, a czym nie jest, odłożył na bok, a postanowił, bądź co bądź, zapoznać się z panną Izabelą.

Wtedy przekonał się, że między jego znajomymi nie ma człowieka, który mógłby go wprowadzić do domu Łęckich. Co gorsze: pan Łęcki i panna byli klientami jego sklepu, lecz taki stosunek, zamiast ułatwić, utrudniał raczej znajomość.

Stopniowo sformułował sobie warunki zapoznania się z panną Izabelą. Ażeby mógł nic więcej tylko szczerze rozmówić się z nią, należało:

Nie być kupcem albo być bardzo bogatym kupcem.

Być co najmniej szlachcicem i posiadać stosunki w sferach arystokratycznych.

Nade wszystko zaś mieć dużo pieniędzy.

Wylegitymowanie się ze szlachectwa nie było rzeczą trudną.

W maju roku zeszłego Wokulski wziął się do tej sprawy, którą jego wyjazd do Bułgarii o tyle przyspieszył, że już w grudniu miał dyplom, z majątkiem było znacznie trudniej; w tym przecie dopomógł mu los.

W początkach wojny wschodniej przejeżdżał przez Warszawę bogaty moskiewski kupiec, Suzin, przyjaciel Wokulskiego jeszcze z Syberii. Odwiedził Wokulskiego i gwałtem zachęcał go do przyjęcia udziału w dostawach dla wojska.

— Zbierz pieniędzy, Stanisławie Piotrowiczu, ile się da — mówił — a uczciwe słowo, zrobisz okrągły milionik!…

Następnie półgłosem wyłożył mu swoje plany.

Wokulski wysłuchał jego projektów. Do wykonania jednych nie chciał należeć, inne przyjął, lecz wahał się. Żal mu było opuścić miasto, w którym przynajmniej widywał pannę Izabelę. Ale gdy w czerwcu ona wyjechała do ciotki, a Suzin począł naglić go depeszami, Wokulski zdecydował się i podniósł całą gotówkę po żonie w ilości rs trzydzieści tysięcy, którą nieboszczka trzymała nietykalną w banku.

Na kilka dni przed wyjazdem zaszedł do znajomego lekarza Szumana, z którym pomimo obustronnej życzliwości widywali się nieczęsto. Lekarz, Żyd, stary kawaler, żółty, mały, z czarną brodą, miał reputację dziwaka. Posiadając majątek leczył darmo i o tyle tylko, o ile było mu to potrzebnym do studiów etnograficznych; przyjaciołom zaś swoim raz na zawsze dał jedną receptę:

„Używaj wszystkich środków, od najmniejszej dozy oleju do największej dozy strychniny, a coś ci z tego pomoże, nawet na — nosaciznę.”

Gdy Wokulski zadzwonił do mieszkania lekarza, ten właśnie był zajęty gatunkowaniem włosów rozmaitych osobników rasy słowiańskiej, germańskiej i semickiej i przy pomocy mikroskopu mierzył dłuższe i krótsze średnice ich przekrojów.

— A, jesteś?… — rzekł do Wokulskiego odwracając głowę. — Nałóż sobie fajkę, jeżeli chcesz, i kładź się na kanapie, jeżeli się zmieścisz.

Gość zapalił fajkę i położył się, jak mu kazano, doktór robił swoje. Przez pewien czas obaj milczeli, wreszcie odezwał się Wokulski:

— Powiedz mi: czy medycyna zna taki stan umysłu, w którym człowiekowi wydaje się, że jego rozproszone dotychczas wiadomości i… uczucia złączyły się jakby w jeden organizm?

— Owszem. Przy ciągłej pracy umysłowej i dobrym odżywianiu mogą wytworzyć się w mózgu nowe komórki albo — skojarzyć się między sobą dawne. No i wówczas z rozmaitych departamentów mózgu i z rozmaitych dziedzin wiedzy tworzy się jedna całość.

— A co znaczy taki stan umysłu, w którym człowiek obojętnieje dla śmierci, ale za to poczyna tęsknić do legend o życiu wiecznym?…

— Obojętność dla śmierci — odpowiedział doktór — jest cechą umysłów dojrzałych, a pociąg do życia wiecznego — zapowiedzią nadchodzącej starości.

Znowu umilkli. Gość palił fajkę, gospodarz kręcił się nad mikroskopem.

— Czy myślisz — spytał Wokulski — że można… kochać kobietę w sposób idealny, nie pożądając jej?

— Naturalnie. Jest to jedna z masek, w którą lubi przebierać się instynkt utrwalenia gatunku.

— Instynkt — gatunek — instynkt utrwalenia czegoś i — utrwalenie gatunku!… — powtórzył Wokulski. — Trzy wyrazy, a cztery głupstwa.

— Zrób szóste — odpowiedział doktór nie odejmując oka od szkła — i ożeń się.

— Szóste?… — rzekł Wokulski podnosząc się na kanapie. — A gdzież piąte?

— Piąte już zrobiłeś: zakochałeś się.

— Ja?… W moim wieku?…

— Czterdzieści pięć lat — to epoka ostatniej miłości, najgorszej — odpowiedział doktór.

— Znawcy mówią, że pierwsza miłość jest najgorsza — szepnął Wokulski.

— Nieprawda. Po pierwszej czeka cię sto innych, ale po setnej pierwszej — już nic. Żeń się; jedyny to ratunek na twoją chorobę.

— Dlaczegożeś ty się nie ożenił?

— Bo mi narzeczona umarła — odpowiedział doktór pochyliwszy się na tył fotelu i patrząc w sufit. — Więc zrobiłem, com mógł: otrułem się chloroformem. Było to na prowincji. Ale Bóg zesłał dobrego kolegę, który wysadził drzwi i uratował mnie. Najpodlejszy rodzaj miłosierdzia!… Ja zapłaciłem za drzwi zepsute, a kolega odziedziczył moją praktykę ogłosiwszy, żem wariat…

Znowu wrócił do włosów i mikroskopu.

— A jaki z tego sens moralny dla ostatniej miłości? — spytał Wokulski.

— Ten, że samobójcom nie należy przeszkadzać — odpowiedział doktór.

Wokulski poleżał jeszcze z kwadrans, potem podniósł się, postawił w kącie fajkę i schyliwszy się nad doktorem ucałował go.

— Bywaj zdrów, Michale.

Doktór zerwał się od stołu.

— No?…

— Wyjeżdżam do Bułgarii

— Po co?

— Zostanę wojskowym dostawcą. Muszę zrobić duży majątek!… — odparł Wokulski.

— Albo?…

— Albo… nie wrócę.

Doktór popatrzył mu w oczy i mocno ścisnął go za rękę.

— Sit tibi terra levis — rzekł spokojnie. Odprowadził go do drzwi i znowu wziął się do swojej roboty.

Już Wokulski był na schodach, gdy doktór wybiegł za nim i zawołał wychylając się przez poręcz:

— Gdybyś jednak wrócił, nie zapomnij przywieźć mi włosów: bułgarskich, tureckich i tak dalej, od obu płci. Tylko pamiętaj: w oddzielnych pakietach z notatkami. Wiesz przecie, jak to robić…

…Wokulski ocknął się z tych dawnych wspomnień.

Nie ma doktora ani jego mieszkania i nawet ich od dziesięciu miesięcy nie widział. Tu jest błotnista ulica Radna, tam Browarna. Na górze spoza nagich drzew wyglądają żółte gmachy uniwersyteckie; na dole parterowe domki, puste place i parkany, a niżej — Wisła.

Obok niego stał jakiś człowiek w wypłowiałej kapocie z rudawym zarostem. Zdjął czapkę i pocałował Wokulskiego w rękę. Wokulski przypatrzył mu się uważniej.

— Wysocki?… — rzekł. — Co ty tu robisz?

— Tu mieszkamy, wielmożny panie, w tym domu — odpowiedział człowiek wskazując na niską lepiankę.

— Dlaczego nie przyjeżdżasz po transporta? — pytał Wokulski.

— Czym przyjadę, panie, kiedy jeszcze na Nowy Rok koń mi padł.

— Cóż robisz?

— A ot tak — razem nic. Zimowaliśmy u brata, co jest dróżnikiem na Wiedeńskiej Kolei. Ale i jemu bieda, bo go ze Skierniewic przenieśli pod Częstochowę. W Skierniewicach ma trzy morgi i żył jak bogacz, a dzisiaj i on kiepski, i grunt wynędznieje bez dozoru.

— No, a z wami co teraz?

— Kobieta niby trochę pierze, ale takim, co nie bardzo mają czym płacić, a ja — ot tak… Marniejemy, panie… nie pierwsi i nie ostatni. Jeszcze póki wielkiego postu, to człowiek krzepi się mówiący: dzisiaj pościsz za dusze zmarłe, jutro na pamiątkę, że Chrystus Pan nic nie jadł, pojutrze, na intencję, ażeby Bóg złe odmienił. Zaś po świętach nie będzie nawet sposobu i dzieciom wytłomaczyć, na jaką intencję nie jedzą…

Ale i wielmożny pan coś markotnie wygląda? Taki już widać czas nastał, że wszyscy muszą zginąć — westchnął ubogi człowiek.

Wokulski zamyślił się.

— Komorne wasze zapłacone? — spytał.

— Nawet nie ma, panie, co płacić, bo nas i tak wypędzą.

— A dlaczego nie przyszedłeś do sklepu, do pana Rzeckiego? — spytał Wokulski.

— Nie śmiałem, panie. Koń odszedł, wóz u Żyda, kubrak na mnie jak na dziadzie… Z czymże było przyjść i jeszcze ludziom głowę zaprzątać?…

Wokulski wydobył portmonetkę.

— Masz tu — rzekł — dziesięć rubli na święta. Jutro w południe przyjdziesz do sklepu i dostaniesz kartkę na Pragę. Tam u handlarza wybierzesz sobie konia, a po świętach przyjeżdżaj do roboty. U mnie zarobisz ze trzy ruble na dzień, więc dług spłacisz łatwo. Zresztą dasz sobie radę.

Ubogi człowiek dotknąwszy pieniędzy zaczął się trząść.

Uważnie słuchał Wokulskiego, a łzy spływały mu po wychudzonej twarzy.

— Czy panu powiedział kto — zapytał po chwili — że z nami jest… ot tak?… Bo już nam ktoś — dodał szeptem — przysyłał siostrę miłosierdzia, będzie z miesiąc. Mówiła, że muszę być ladaco, i dała nam kartkę na pud węgla z Żelaznej ulicy. Czy może pan tak sam z siebie?…

— Idź do domu, a jutro bądź w sklepie — odparł Wokulski.

— Idę, panie — odpowiedział człowiek kłaniając się do ziemi.

Odszedł, lecz przystawał na drodze; widocznie rozmyślał nad niespodziewanym szczęściem.

W tej chwili Wokulskiego tknęło szczególne przeczucie.

— Wysocki!… — zawołał. — A twemu bratu jak na imię?

— Kasper — odpowiedział człowiek wracając pędem.

— Przy jakiej mieszka stacji?

— Przy Częstochowie, panie.

— Idź do domu. Może Kaspra przeniosą do Skierniewic.

Ale ten zamiast iść, zbliżył się.

— Przepraszam, wielmożny panie — rzekł nieśmiało — ale jak mnie kto zaczepi: skąd mam tyle pieniędzy?…

— Powiedz, że na rachunek wziąłeś ode mnie.

— Rozumiem, panie… Bóg… niech Bóg…

Ale Wokulski już nie słuchał; szedł w stronę Wisły myśląc:

„Jakże oni szczęśliwi, ci wszyscy, w których tylko głód wywołuje apatię, a jedynym cierpieniem jest zimno. I jak łatwo ich uszczęśliwić!… Nawet moim skromnym majątkiem mógłbym wydźwignąć parę tysięcy rodzin. Nieprawdopodobne, a przecież — tak jest.”

Wokulski doszedł do brzegu Wisły i zdumiał się. Na kilkumorgowej przestrzeni wznosił się tu pagórek najobrzydliwszych śmieci, cuchnących, nieomal ruszających się pod słońcem, a o kilkadziesiąt kroków dalej leżały zbiorniki wody, którą piła Warszawa.

„O, tutaj — myślał — jest ognisko wszelkiej zarazy. Co człowiek dziś wyrzuci ze swego mieszkania, jutro wypije; później przenosi się na Powązki i z drugiej znowu strony miasta razi bliźnich pozostałych przy życiu.

Bulwar tutaj, kanały i woda źródlana na górze i — można by ocalić rokrocznie kilka tysięcy ludzi od śmierci, a kilkadziesiąt tysięcy od chorób… Niewielka praca, a zysk nieobliczony; natura umie wynagradzać.”

Na stoku i w szczelinach obmierzłego wzgórza spostrzegł niby postacie ludzkie. Było tu kilku drzemiących na słońcu pijaków czy złodziei, dwie śmieciarki i jedna kochająca się para, złożona z trędowatej kobiety i suchotniczego mężczyzny, który nie miał nosa. Zdawało się, że to nie ludzie, ale widma ukrytych tutaj chorób, które odziały się w wykopane w tym miejscu szmaty. Wszystkie te indywidua zwietrzyły obcego człowieka; nawet śpiący podnieśli głowy i z wyrazem zdziczałych psów przypatrywali się gościowi.

Wokulski uśmiechnął się.

„Gdybym tu przyszedł w nocy, na pewno wyleczyliby mnie z melancholii. Jutro już spoczywałbym pod tymi śmieciami, które — wreszcie — są tak wygodnym grobem jak każdy inny. Na górze zrobiłby się wrzask, ścigano by i wyklinano tych poczciwców, a oni — może wyświadczyliby mi łaskę.


O, bo nie znają, w snach mogilnych
Drzemiący, ciężkich trosk żywota,
I duch się ich już nie szamota
W pragnieniach — tęsknych a bezsilnych..

Ależ ja zaczynam być naprawdę sentymentalny?… muszę mieć nerwy dobrze rozbite. Bulwar jednak nie wytępiłby takich oto Mohikanów; przenieśliby się na Pragę albo za Pragę, uprawialiby w dalszym ciągu swoje rzemiosło, kochaliby się jak ta dwójeczka, ba, nawet mnożyliby się. Co za piękne, ojczyzno, będziesz miała potomstwo, urodzone i wychowane na tym śmietniku, z matki okrytej wysypką i beznosego ojca!…

Moje dzieci byłyby inne; po niej wzięłyby piękność, po mnie siłę… No, ale ich nie będzie. W tym kraju tylko choroba, nędza i zbrodnia znajdują weselne łożnice, nawet przytułki dla potomstwa.

Strach, co tu się stanie za kilka generacji… A przecie jest proste lekarstwo: praca obowiązkowa — słusznie wynagradzana. Ona jedna może wzmocnić lepsze indywidua, a bez krzyku wytępić złe i… mielibyśmy ludność dzielną, jak dziś mamy zagłodzoną lub chorą.”

A potem, nie wiadomo z jakiej racji, pomyślał:

„Cóż z tego, że trochę kokietuje?… Kokieteria u kobiet jest jak barwa i zapach u kwiatów. Taka już ich natura, że każdemu chcą się podobać, nawet Mraczewskim…

Dla wszystkich kokieteria, a dla mnie: »zapłać temu panu!…« Może ona myśli, że ja oszukałem ich na kupnie srebra?… To byłoby kapitalne!”

Nad samym brzegiem Wisły leżał stos belek. Wokulski uczuł znużenie, siadł i patrzył. W spokojnej powierzchni wody odbijała się Saska Kępa, już zieleniejąca, i praskie domy z czerwonymi dachami; na środku rzeki stała nieruchoma berlinka. Nie większym wydawał się ten okręt, który zeszłego lata widział Wokulski na Morzu Czarnym, unieruchomiony z powodu zepsucia się machin.

„Leciał jak ptak i nagle utknął; zabrakło w nim motoru. Spytałem się wówczas: a może i ja kiedyś stanę w biegu? — no, i stanąłem. Jakież to pospolite sprężyny wywołują ruch w świecie: trochę węgla ożywia okręt, trochę serca — człowieka…”

W tej chwili żółtawy, za wczesny motyl przeleciał mu nad głową w stronę miasta.

„Ciekawym, skąd on się wziął? — myślał Wokulski. — Natura miewa kaprysy i — analogie — dodał. — Motyle istnieją także w rodzaju ludzkim: piękna barwa, latanie nad powierzchnią życia, karmienie się słodyczami, bez których giną — oto ich zajęcie. A ty, robaku, nurtuj ziemię i przerabiaj ją na grunt zdolny do siewu. Oni bawią się, ty pracuj; dla nich istnieje wolna przestrzeń i światło, a ty ciesz się jednym tylko przywilejem: zrastania się, jeżeli cię rozdepcze ktoś nieuważny.

I tobież to wzdychać do motyla, głupi?… I dziwić się, że ma wstręt do ciebie?… Jakiż łącznik może istnieć między mną i nią?…

No, gąsienica jest także podobna do robaka, póki nie zostanie motylem. Ach więc to ty masz zostać motylem, kupcze galanteryjny? Dlaczegóż by nie? Ciągłe doskonalenie się jest prawem świata, a ileż to kupieckich rodów w Anglii zostało lordowskimi mościami?

W Anglii!… Tam jeszcze istnieje epoka twórcza w społeczeństwie; tam wszystko doskonali się i wstępuje na wyższe szczeble. Owszem, tam nawet ci wyżsi przyciągają do siebie nowe siły. Lecz u nas wyższa warstwa zakrzepła jak woda na mrozie i nie tylko wytworzyła osobny gatunek, który nie łączy się z resztą, ma do niej wstręt fizyczny, ale jeszcze własną martwotą krępuje wszelki ruch z dołu. Co się tu łudzić: ona i ja to dwa różne gatunki istot, naprawdę jak motyl i robak. Mam dla jej skrzydeł opuszczać swoją norę i innych robaków?… To są moi — ci, którzy leżą tam na śmietniku, i może dlatego są nędzni, a będą jeszcze nędzniejsi, że ja chcę wydawać po trzydzieści tysięcy rubli rocznie na zabawę w motyla. Głupi handlarzu, podły człowieku!…

Trzydzieści tysięcy rubli znaczą tyle, co sześćdziesiąt drobnych warsztatów albo sklepików, z których żyją całe rodziny. I to ja mam byt ich zniszczyć, wyssać z nich ludzkie dusze i wypędzić na ten śmietnik?…

No dobrze, ale gdyby nie ona, czy miałbym dziś majątek?… Kto wie, co się stanie ze mną i z tymi pieniędzmi bez niej? Może właśnie dopiero przy niej nabiorą one twórczych własności; może choć kilkanaście rodzin z nich skorzysta?…”

Wokulski odwrócił się i nagle zobaczył na ziemi swój własny cień. Potem przypomniał sobie, że ten cień chodzi przed nim, za nim albo obok niego zawsze i wszędzie, jak myśl o tamtej kobiecie chodziła za nim wszędzie i zawsze, na jawie i we śnie, mieszając się do wszystkich jego celów, planów i czynów.

„Nie mogę wyrzec się jej” — szepnął rozkładając ręce, jakby tłomaczył się komuś.

Wstał z belek i wrócił do miasta.

Idąc przez ulicę Oboźną, przypomniał sobie furmana Wysockiego, któremu koń padł, i zdawało mu się, że widzi cały szereg wozów, przed którymi leżą padłe konie, cały szereg rozpaczających nad nimi furmanów, a przy każdym gromadę mizernych dzieci i żonę, która pierze bieliznę takim, co płacić nie mogą.

„Koń?…” — szepnął Wokulski i czegoś serce mu się ścisnęło.

Raz w marcu przechodząc Aleją Jerozolimską zobaczył tłum ludzi, czarny wóz węglarski stojący w poprzek drogi pod bramą, a o parę kroków dalej wyprzężonego konia.

— Co się to stało?

— Koń złamał nogę — odparł wesoło jeden z przechodniów, który miał fiołkowy szalik na szyi i trzymał ręce w kieszeniach.

Wokulski mimochodem spojrzał na delikwenta. Chudy koń z wytartymi bokami stał przywiązany do młodego drzewka unosząc w górę tylną nogę. Stał cicho, patrzył wywróconym okiem na Wokulskiego i gryzł z bólu gałązkę okrytą szronem.

„Dlaczego dziś dopiero przypomniał mi się ten koń? — myślał Wokulski — dlaczego ogarnia mnie taki żal?”

Szedł Oboźną pod górę, rozmarzony, i czuł, że w ciągu kilku godzin, które spędził w nadrzecznej dzielnicy, zaszła w nim jakaś zmiana. Dawniej — dziesięć lat temu, rok temu, wczoraj jeszcze, przechodząc ulicami nie spotykał na nich nic szczególnego. Snuli się ludzie, jeździły dorożki, sklepy otwierały gościnne objęcia dla przechodniów. Ale teraz przybył mu jakby nowy zmysł. Każdy obdarty człowiek wydawał mu się istotą wołającą o ratunek tym głośniej, że nic nie mówił, tylko rzucał trwożne spojrzenia jak ów koń ze złamaną nogą. Każda uboga kobieta wydawała mu się praczką, która wyżartymi od mydła rękami powstrzymuje rodzinę nad brzegiem nędzy i upadku. Każde mizerne dziecko wydawało mu się skazanym na śmierć przedwczesną albo na spędzanie dni i nocy w śmietniku przy ulicy Dobrej.

I nie tylko obchodzili go ludzie. Czuł zmęczenie koni ciągnących ciężkie wozy i ból ich karków tartych do krwi przez chomąto. Czuł obawę psa, który szczekał na ulicy zgubiwszy pana, i rozpacz chudej suki z obwisłymi wymionami, która na próżno biegała od rynsztoka do rynsztoka szukając strawy dla siebie i szczeniąt. Jeszcze, na domiar cierpień, bolały go drzewa obdarte z kory, bruki podobne do powybijanych zębów, wilgoć na ścianach, połamane sprzęty i podarta odzież.

Zdawało mu się, że każda taka rzecz jest chora albo zraniona, że skarży się: „Patrz, jak cierpię…”, i że tylko on słyszy i rozumie jej skargi. A ta szczególna zdolność odczuwania cudzego bólu urodziła się w nim dopiero dziś, przed godziną.

Rzecz dziwna! przecie miał już ustaloną opinię hojnego filantropa. Członkowie Towarzystwa Dobroczynności we frakach składali mu podziękowania za ofiarę dla wiecznie łaknącej instytucji; hrabina Karolowa we wszystkich salonach opowiadała o pieniądzach, które złożył na jej ochronę; jego służba i subiekci sławili go za podwyższenie im pensji. Ale Wokulskiemu rzeczy te nie sprawiały żadnej przyjemności, tak jak on sam nie przywiązywał do nich żadnej wagi. Rzucał tysiące rubli do kas urzędowych dobroczyńców, ażeby kupić za to rozgłos nie pytając, co się zrobi z pieniędzmi.

I dopiero dziś, kiedy dziesięcioma rublami wydobył człowieka z niedoli, kiedy nikt nie mógł głosić przed światem o jego szlachetności, dopiero dziś poznał: co to jest ofiara. Dopiero dziś przed jego zdumionym okiem stanęła nowa, nie znana dotychczas część świata — nędza, której trzeba pomagać.

„Tak, alboż ja dawniej nie widywałem nędzy?…” — szepnął Wokulski.

I przypomniał sobie całe szeregi ludzi obdartych, mizernych, a szukających pracy, chudych koni, głodnych psów, drzew z obdartą korą i połamanymi gałęźmi. Wszystko to przecie spotykał bez wrażenia. I dopiero gdy wielki ból osobisty zaorał mu i zbronował duszę, na tym gruncie użyźnionym krwią własną i skropionym niewidzialnymi dla świata łzami wyrosła osobliwa roślina: współczucie powszechne, ogarniające wszystko — ludzi, zwierzęta, nawet przedmioty, które nazywają martwymi.

„Doktór powiedziałby, że utworzyła mi się nowa komórka w mózgu albo że połączyło się kilka dawnych” — pomyślał.

„Tak, ale co dalej?…”

Dotychczas bowiem miał tylko jeden cel: zbliżyć się do panny Izabeli. Dziś przybył mu drugi: wydobyć z niedostatku Wysockiego.

„Mała rzecz!…”

„Przenieść jego brata pod Skierniewice…” — dodał jakiś głos.

„Drobnostka.”

Ale poza tymi dwoma ludźmi stanęło zaraz kilku innych, za nimi jeszcze kilku, potem olbrzymi tłum borykający się z wszelkiego rodzaju nędzą i wreszcie — cały ocean cierpień powszechnych, które wedle sił należało zmniejszać, a przynajmniej powściągnąć od dalszego rozlewu.

„Przywidzenia… abstrakcyjne… zdenerwowanie!” — szepnął Wokulski.

To była jedna droga. Na końcu bowiem drugiej widział cel realny i jasno określony — pannę Izabelę.

„Nie jestem Chrystusem, ażeby poświęcać się za całą ludzkość.”

„Więc na początek zapomnij o Wysockich” — odparł głos wewnętrzny.

„No, głupstwo! Jakkolwiek jestem dziś rozkołysany, ależ nie mogę być śmieszny — myślał Wokulski. — Zrobię, co się da i komu można, lecz osobistego szczęścia nie wyrzeknę się, to darmo…”

W tej chwili stanął przed drzwiami swego sklepu i wszedł tam.

W sklepie zastał Wokulski tylko jedną osobę. Była to dama wysoka, w czarnych szatach, nieokreślonego wieku. Przed nią leżał stos neseserek: drewnianych, skórzanych, pluszowych i metalowych, prostych i ozdobnych, najdroższych i najtańszych, a — wszyscy subiekci byli na służbie. Klein podawał coraz nowe neseserki, Mraczewski chwalił towar, a Lisiecki akompaniował mu ruchami ręki i brody. Tylko pan Ignacy wybiegł naprzeciw pryncypała.

— Z Paryża przyszedł transport — rzekł do Wokulskiego. — Myślę, że trzeba odebrać jutro.

— Jak chcesz.

— Z Moskwy obstalunki za dziesięć tysięcy rubli, na początek maja.

— Spodziewałem się.

— Z Radomia za dwieście rubli, ale furman upomina się na jutro.

Wokulski ruszył ramionami.

— Trzeba raz zerwać z tym kramarstwem — odezwał się po chwili. — Interes żaden, a wymagania ogromne.

— Zerwać z naszymi kupcami?… — spytał zdziwiony Rzecki.

— Zerwać z Żydami — wtrącił półgłosem Lisiecki. — Bardzo dobrze robi szef wycofując się z tych parszywych stosunków. Nieraz aż wstyd wydawać reszty, tak pieniądze zalatują cebulą.

Wokulski nic nie odpowiedział. Usiadł do swej księgi i udawał, że rachuje, ale naprawdę nie robił nic, nie miał siły. Przypomniał sobie tylko swoje niedawne marzenia o uszczęśliwieniu ludzkości i osądził, że musi być mocno zdenerwowany.

„Rozigrał się we mnie sentymentalizm i fantazja — myślał. — Zły to znak. Mogę ośmieszyć się, zrujnować…”

I machinalnie przypatrywał się niezwykłej fizjognomii damy, która wybierała neseserki. Była ubrana skromnie, miała gładko uczesane włosy. Na jej twarzy białej i razem żółtej malował się głęboki smutek; spoza ust przyciętych wyglądała złość, a ze spuszczonych oczu błyskał czasami gniew, niekiedy pokora.

Mówiła głosem cichym i łagodnym, a targowała się jak stu skąpców. To było za drogie, tamto za tanie; tu plusz stracił barwę, tam zaraz odlezie skórka, a ówdzie ukazuje się rdza na okuciach. Lisiecki już cofnął się od niej rozgniewany, Klejn odpoczywał, a tylko Mraczewski rozmawiał z nią jak z osobą znajomą.

W tej chwili otworzyły się drzwi sklepu i ukazał się w nich — jeszcze oryginalniejszy jegomość. Lisiecki powiedział o nim, że jest podobny do suchotnika, któremu w trumnie zaczęły odrastać wąsy i faworyty. Wokulski zauważył, że gość ma gapiowato otwarte usta, a za ciemnymi binoklami nosi duże oczy, z których przeglądało jeszcze większe roztargnienie.

Gość wszedł kończąc rozmowę z kimś na ulicy, lecz wnet cofnął się, aby swego towarzysza pożegnać. Potem znowu wszedł i znowu cofnął się zadzierając do góry głowę, jakby czytał szyld. Nareszcie wszedł na dobre, ale drzwi za sobą nie zamknął. Wypadkowo spojrzał na damę i — spadły mu z nosa ciemne binokle.

— A… a… a!… — zawołał.

Ale dama gwałtownie odwróciła się od niego do neseserek i upadła na krzesło.

Do przybysza wybiegł Mraczewski i uśmiechając się dwuznacznie, zapytał:

— Pan baron rozkaże?…

— Spinki, uważa pan, spinki zwyczajne, złote albo stalowe… Tylko, rozumie pan, muszą być w kształcie czapki dżokejskiej i — z biczem…

Mraczewski otworzył gablotkę ze spinkami.

— Wody… — odezwała się dama słabym głosem.

Rzecki nalał jej wody z karafki i podał z oznakami współczucia.

— Pani dobrodziejce słabo?… Może by doktora…

— Już mi lepiej — odparła.

Baron oglądał spinki, ostentacyjnie odwracając się tyłem do damy.

— A może, czy nie sądzi pan, byłyby lepsze spinki w formie podków? — pytał Mraczewskiego.

— Myślę, że panu baronowi potrzebne są i te, i te. Sportsmeni noszą tylko oznaki sportsmeńskie, ale lubią odmianę.

— Powiedz mi pan — odezwała się nagle dama do Klejna — na co podkowy ludziom, którzy nie mają za co utrzymywać koni?…

— Otóż, proszę pana — mówił baron — wybrać mi jeszcze parę drobiazgów w formie podkowy…

— Może by popielniczkę? — zapytał Mraczewski.

— Dobrze, popielniczkę — odparł baron.

— Może gustowny kałamarz z siodłem, dżokejką, szpicrutą?

— Proszę o gustowny kałamarz z siodłem i dżokejką…

— Powiedz mi pan — mówiła dama do Klejna podniesionym głosem — czy wam nie wstyd zwozić tak kosztowne drobiazgi, kiedy kraj jest zrujnowany?… Czy nie wstyd kupować konie wyścigowe…

— Drogi panie — zawołał nie mniej głośno baron do Mraczewskiego — zapakuj wszystkie te garnitury, popielniczkę, kałamarz i odeszlij mi do domu. Macie prześliczny wybór towarów… Serdecznie dziękuję… Adieu!…

I wybiegł ze sklepu wracając się parę razy i spoglądając na szyld nad drzwiami.

Po odejściu oryginalnego barona w sklepie zapanowało milczenie. Rzecki patrzył na drzwi, Klejn na Rzeckiego, a Lisiecki na Mraczewskiego, który znajdując się z tyłu damy krzywił się w sposób bardzo dwuznaczny.

Dama z wolna podniosła się z krzesła i zbliżyła się do kantorka, za którym siedział Wokulski.

— Czy mogę spytać — rzekła drżącym głosem — ile panu winien jest ten pan, który dopiero co wyszedł?…

— Rachunki tego pana ze mną, szanowna pani, gdyby je miał, należą tylko do niego i do mnie — odpowiedział Wokulski kłaniając się.

— Panie — ciągnęła dalej rozdrażniona dama — jestem Krzeszowska, a ten pan jest moim mężem. Długi jego obchodzą mnie, ponieważ on zagarnął mój majątek, o który w tej chwili toczy się między nami proces…

— Daruje pani — przerwał Wokulski — ale stosunki między małżonkami do mnie nie należą.

— Ach, więc tak?… Zapewne, że dla kupca jest to najwygodniej. Adieu.

I opuściła sklep trzaskając drzwiami.

W kilka minut po jej odejściu wbiegł do sklepu baron. Parę razy wyjrzał na ulicę, a następnie zbliżył się do Wokulskiego.

— Najmocniej przepraszam — rzekł usiłując utrzymać binokle na nosie — ale jako stały gość pański, ośmielę się w zaufaniu zapytać: co mówiła dama, która wyszła przed chwilą?… Bardzo przepraszam za moją śmiałość, ale w zaufaniu…

— Nic nie mówiła, co by kwalifikowało się do powtórzenia — odparł Wokulski.

— Bo uważa pan, jest to, niestety! moja żona… Pan wie, kto jestem… Baron Krzeszowski… Bardzo zacna kobieta, bardzo światła, ale skutkiem śmierci naszej córki trochę zdenerwowana i niekiedy… Pojmuje pan?… Więc nic?…

— Nic.

Baron ukłonił się i już we drzwiach skrzyżował spojrzenia z Mraczewskim, który mrugnął na niego.

— Więc tak?… — rzekł baron, ostro patrząc na Wokulskiego.

I wybiegł na ulicę. Mraczewski skamieniał i oblał się rumieńcem powyżej włosów. Wokulski trochę pobladł, lecz spokojnie usiadł do rachunków.

— Cóż to za oryginalne diabły, panie Mraczewski? — spytał Lisiecki.

— A to cała historia! — odparł Mraczewski przypatrując się spod oka Wokulskiemu. — Jest to baron Krzeszowski, wielki dziwak, i jego żona, trochę narwana. Nawet skuzynowani ze mną, ale cóż!… — westchnął spoglądając w lustro. — Ja nie mam pieniędzy, więc muszę być w handlu; oni jeszcze mają, więc są moimi kundmanami…

— Mają bez pracy!… — wtrącił Klejn. — Ładny porządek świata, co?

— No, no… już mnie pan do swoich porządków nie nawracaj — odparł Mraczewski. — Otóż pan baron i pani baronowa od roku prowadzą ze sobą wojnę. On chce rozwodu, na co ona się nie zgadza; ona chce przepędzić go od zarządu swoim majątkiem, na co on się nie zgadza. Ona nie pozwala mu trzymać koni, szczególniej jednego wyścigowca; a on nie pozwala jej kupić kamienicy po Łęckich, w której pani Krzeszowska mieszka i gdzie straciła córkę. Oryginały!… Bawią ludzi wymyślając jedno na drugie…

Opowiadał lekkim tonem i kręcił się po sklepie z miną panicza, który przyszedł tu na chwilkę, ale zaraz wyjdzie. Wokulski mienił się siedząc na fotelu; już nie mógł znieść głosu Mraczewskiego.

„Kuzyn Krzeszowskich… — myślał. — Dostanie bilet miłosny od panny Izabeli… A, infamis!…”

I przemógłszy się wrócił do swej księgi. Do sklepu znowu poczęli wchodzić goście, wybierać towary, targować się, płacić. Ale Wokulski widział tylko ich cienie, pogrążony w pracy. A im dłuższe sumował kolumny, im większe wypadały mu sumy, tym bardziej czuł, że w sercu kipi mu jakiś gniew bezimienny. O co?… na kogo?… mniejsza. Dosyć, że ktoś za to zapłaci, pierwszy z brzegu.

Około siódmej sklep już stanowczo wyludnił się, subiekci rozmawiali, Wokulski wciąż rachował. Wtem znowu usłyszał nieznośny głos Mraczewskiego, który mówił aroganckim tonem:

— Co mi pan, panie Klejn, będzie zawracał głowę!… Wszyscy socjaliści są złodzieje, bo chcieliby dzielić się cudzym, i — szubrawcy, bo mają na dwu jedną parę butów i nie wierzą w chustki do nosa.

— Nie mówiłbyś pan tak — odparł smutnie Klejn — gdybyś przeczytał choć z parę broszurek, nawet niedużych.

— Błazeństwo… — przerwał Mraczewski włożywszy ręce w kieszenie. — Będę czytał broszury, które chcą zniszczyć rodzinę, wiarę i własność!… No, takich głupich nie znajdziesz pan w Warszawie.

Wokulski zamknął księgę i włożył ją do kantorka. W tej chwili znowu weszły do sklepu trzy panie żądając rękawiczek.

Targ z nimi przeciągnął się z kwadrans. Wokulski siedział na fotelu i patrzył w okno; gdy zaś damy wyszły, odezwał się tonem bardzo spokojnym:

— Panie Mraczewski.

— Co pan każe?… — spytał piękny młodzieniec biegnąc do kantorka krokiem kontredansowym.

— Od jutra niech pan postara się o inne miejsce — rzekł krótko Wokulski.

Mraczewski osłupiał.

— Dlaczego, panie szefie?… Dlaczego?…

— Dlatego, że u mnie już pan nie ma miejsca.

— Jakiż powód?… Przecie chyba nic złego nie zrobiłem? Gdzież pójdę, jeżeli pan tak nagle pozbawi mię posady?…

— Świadectwo dostanie pan dobre — odparł Wokulski. — Pan Rzecki wypłaci panu pensję za następny kwartał, wreszcie — za pięć miesięcy… A powód jest ten, że ja i pan nie pasujemy do siebie… Zupełnie nie pasujemy. — Mój Ignacy, zrób z panem Mraczewskim rachunek do pierwszego października.

To powiedziawszy Wokulski wstał z fotelu i wyszedł na ulicę.

Dymisja Mraczewskiego zrobiła takie wrażenie, że subiekci nie przemówili między sobą ani słowa, a pan Rzecki kazał zamknąć sklep, chociaż nie było jeszcze ósmej. Pobiegł zaraz do mieszkania Wokulskiego, lecz go tam nie zastał. Przyszedł drugi raz o jedynastej w nocy, lecz w oknach było ciemno, i pan Ignacy wrócił do siebie zgnębiony.

Na drugi dzień, w Wielki Czwartek, Mraczewski już nie pokazał się w sklepie. Pozostali koledzy jego byli smutni i czasem naradzali się między sobą po cichu.

Około pierwszej przyszedł Wokulski. Lecz nim usiadł do kantorka, otworzyły się drzwi i zwykłym wahającym się krokiem wbiegł pan Krzeszowski zadając sobie wiele trudu nad osadzeniem binokli na nosie.

— Panie Wokulski — zawołał roztargniony gość, prawie ode drzwi. — W tej chwili dowiaduję się… Jestem Krzeszowski… Dowiaduję się, że ten biedny Mraczewski z mojej winy otrzymał dymisję. Ależ, panie Wokulski, ja wczoraj bynajmniej nie miałem pretensji do pana… Ja szanuję dyskrecję, jaką okazał pan w sprawie mojej i mojej żony… Ja wiem, że pan jej odpowiedział, jak przystało na dżentelmena…

— Panie baronie — odparł Wokulski — ja nie prosiłem pana o świadectwo przyzwoitości. Poza obrębem tego — co pan każe?…

— Przyszedłem prosić o przebaczenie biednemu Mraczewskiemu, który nawet…

— Do pana Mraczewskiego nie mam żadnej pretensji, nawet tej, ażeby do mnie wracał.

Baron przygryzł wargi. Chwilę milczał, jakby odurzony szorstką odmową; na koniec ukłonił się i cicho powiedziawszy: „Przepraszam…”, opuścił sklep.

Panowie Klejn i Lisiecki cofnęli się za szafy i po krótkiej naradzie wrócili do sklepu, od czasu do czasu rzucając na siebie smutne, lecz wymowne spojrzenia.

Około trzeciej po południu ukazała się pani Krzeszowska. Zdawało się, że jest bledsza, żółciejsza i jeszcze czarniej ubrana niż wczoraj. Lękliwie obejrzała się po sklepie, a spostrzegłszy Wokulskiego zbliżyła się do kantorka.

— Panie — rzekła cicho — dziś dowiedziałam się, że pewien młody człowiek, Mraczewski, z mojej winy stracił u pana miejsce. Jego nieszczęśliwa matka…

— Pan Mraczewski już nie jest u mnie i nie będzie — odparł Wokulski z ukłonem. — Czym więc mogę pani służyć?…

Pani Krzeszowska miała widocznie ułożoną dłuższą mowę. Na nieszczęście, spojrzała Wokulskiemu w oczy i… z wyrazem: „Przepraszam…”, wyszła ze sklepu.

Panowie Klejn i Lisiecki — mrugnęli na siebie wymowniej niż dotychczas, lecz poprzestali na jednomyślnym wzruszeniu ramionami.

Dopiero około piątej po południu zbliżył się do Wokulskiego Rzecki. Oparł ręce na kantorku i rzekł półgłosem:

— Matka tego Mraczewskiego, Staśku, jest bardzo biedna kobieta…

— Zapłać mu pensję do końca roku — odparł Wokulski.

— Myślę… Stasiu, myślę, że nie można aż tak karać człowieka za to, że ma inne niż my przekonania polityczne…

— Polityczne?… — powtórzył Wokulski takim tonem, że panu Ignacemu przeszedł mróz po kościach…

— Zresztą, powiem ci — ciągnął dalej pan Ignacy — szkoda takiego subiekta. Chłopak piękny, kobiety go pasjami lubią…

— Piękny? — odparł Wokulski. — Więc niech pójdzie na utrzymanie, jeżeli taki piękny.

Pan Ignacy cofnął się. Panowie Lisiecki i Klejn już nawet nie spoglądali na siebie.

W godzinę później przyszedł do sklepu niejaki pan Zięba, którego Wokulski przedstawił jako nowego subiekta.

Pan Zięba miał około lat trzydziestu; był może tak przystojny jak Mraczewski, ale wyglądał nierównie poważniej i taktowniej. Nim sklep zamknięto, już zaznajomił się, a nawet zdobył przyjaźń swoich kolegów. Pan Rzecki odkrył w nim zagorzałego bonapartystę; pan Lisiecki wyznał, że on sam obok Zięby jest bardzo bladym antysemitą, a pan Klejn doszedł do wniosku, że Zięba musi być co najmniej biskupem socjalizmu.

Słowem, wszyscy byli kontenci, a pan Zięba spokojny.



IX. Kładki, na których spotykają się ludzie różnych światów

W Wielki Piątek z rana Wokulski przypomniał sobie, że dziś i jutro hrabina Karolowa i panna Izabela będą kwestowały przy grobach.

„Trzeba tam pójść i coś dać — pomyślał i wyjął z kasy pięć złotych półimperiałów. — Chociaż — dodał po chwili — posłałem im już dywany, ptaszki śpiewające, pozytywkę, nawet fontannę!… To chyba wystarczy na zbawienie jednej duszy. Nie pójdę.”

Po południu jednak zrobił sobie uwagę, że może hrabina Karolowa liczy na niego. A w takim razie nie wypada cofać się lub złożyć tylko pięć półimperiałów. Wydobył więc z kasy jeszcze pięć i wszystkie zawinął w bibułkę.

„Co prawda — mówił do siebie — będzie tam panna Izabela, a tej nie można ofiarować dziesięciu półimperiałów.”

Więc rozwinął swój rulon, znowu dołożył dziesięć sztuk złota i jeszcze raz namyślał się: „Iść czy nie iść?…”

„Nie — powiedział — nie będę należał do tej jarmarcznej dobroczynności.”

Rzucił rulon do kasy i w piątek nie poszedł na groby.

Ale w Wielką Sobotę sprawa przedstawiła mu się całkiem z nowego punktu.

„Oszalałem! — mówił. — Więc jeżeli nie pójdę do kościoła, gdzież ją spotkam?… Jeżeli nie pieniędzmi, czym zwrócę na siebie jej uwagę?… Tracę rozsądek…”

Lecz jeszcze wahał się i dopiero około drugiej po południu, gdy Rzecki z powodu święta kazał już sklep zamykać, Wokulski wziął z kasy dwadzieścia pięć półimperiałów i poszedł w stronę kościoła.

Nie wszedł tam jednak od razu; coś go zatrzymywało. Chciał zobaczyć pannę Izabelę, a jednocześnie lękał się tego i wstydził się swoich półimperiałów.

„Rzucić stos złota!… Jakie to imponujące w papierowych czasach i — jakie to dorobkiewiczowskie… No, ale co robić, jeżeli one właśnie na pieniądze czekają?… Może nawet będzie za mało?…”

Chodził tam i na powrót po ulicy naprzeciw kościoła nie mogąc od niego oczu oderwać.

„Już idę — myślał. — Zaraz… jeszcze chwilkę… Ach, co się ze mną stało!…” — dodał czując, że jego rozdarta dusza nawet na tak prosty czyn nie może zdobyć się bez wahań.

Teraz przypomniał sobie: jak on dawno nie był w kościele.

„Kiedyż to?… Na ślubie raz… Na pogrzebie żony drugi raz…”

Lecz i w tym, i w tamtym wypadku nie wiedział dobrze, co się koło niego dzieje; więc patrzył w tej chwili na kościół jak na rzecz zupełnie nową dla siebie.

„Co to jest za ogromny gmach, który zamiast kominów ma wieże, w którym nikt nie mieszka, tylko śpią prochy dawno zmarłych?… Na co ta strata miejsca i murów, komu dniem i nocą pali się światło, w jakim celu schodzą się tłumy ludzi?…

Na targ idą po żywność, do sklepów po towary, do teatru po zabawę, ale po co tutaj?…”

Mimo woli porównywał drobny wzrost stojących pod kościołem pobożnych z olbrzymimi rozmiarami świętego budynku i przyszła mu myśl szczególna. Że jak kiedyś na ziemi pracowały potężne siły dźwigając z płaskiego lądu łańcuchy gór, tak kiedyś w ludzkości istniała inna niezmierna siła, która wydźwignęła tego rodzaju budowle. Patrząc na podobne gmachy można by sądzić, że w głębi naszej planety mieszkali olbrzymowie, którzy wydzierając się gdzieś w górę, podważali skorupę ziemską i zostawiali ślady tych ruchów w formie imponujących jaskiń.

„Dokąd oni wydzierali się? Do innego, podobno wyższego świata. A jeżeli morskie przypływy dowodzą, że księżyc nie jest złudnym blaskiem, tylko realną rzeczywistością, dlaczego te dziwne budynki nie miałyby stwierdzać rzeczywistości innego świata?… Czyliż on słabiej pociąga za sobą dusze ludzkie aniżeli księżyc fale oceanu?…

Wszedł do kościoła i zaraz na wstępie znowu uderzył go nowy widok. Kilka żebraczek i żebraków błagało o jałmużnę, którą Bóg zwróci litościwym w życiu przyszłym. Jedni z pobożnych całowali nogi Chrystusa umęczonego przez państwo rzymskie, inni w progu upadłszy na kolana wznosili do góry ręce i oczy, jakby zapatrzeni w nadziemską wizję. Kościół pogrążony był w ciemności, której nie mógł rozproszyć blask kilkunastu świec płonących w srebrnych kandelabrach. Tu i ówdzie na posadzce świątyni widać było niewyraźne cienie ludzi leżących krzyżem albo zgiętych ku ziemi, jakby kryli się ze swoją pobożnością pełną pokory. Patrząc na te ciała nieruchome można było myśleć, że na chwilę opuściły je dusze i uciekły do jakiegoś lepszego świata.

„Rozumiem teraz — pomyślał Wokulski — dlaczego odwiedzanie kościołów umacnia wiarę. Tu wszystko urządzone jest tak, że przypomina wieczność.”

Od pogrążonych w modlitwie cieniów wzrok jego pobiegł ku światłu. I zobaczył w różnych punktach świątyni stoły okryte dywanami, na nich tace pełne bankocetli, srebra i złota, a dokoła nich damy siedzące na wygodnych fotelach, odziane w jedwab, pióra i aksamity, otoczone wesołą młodzieżą. Najpobożniejsze pukały na przechodniów, wszystkie rozmawiały i bawiły się jak na raucie.

Zdawało się Wokulskiemu, że w tej chwili widzi przed sobą trzy światy. Jeden (dawno już zeszedł z ziemi), który modlił się i dźwigał na chwałę Boga potężne gmachy. Drugi, ubogi i pokorny, który umiał modlić się, lecz wznosił tylko lepianki, i — trzeci, który dla siebie murował pałace, ale już zapomniał o modlitwie i z domów bożych zrobił miejsce schadzek; jak niefrasobliwe ptaki, które budują gniazda i zawodzą pieśni na grobach poległych bohaterów.

„A czymże ja jestem, zarówno obcy im wszystkim?…”

„Może jesteś okiem żelaznego przetaka, w który rzucę ich wszystkich, aby oddzielić stęchłe plewy od ziarna” — odpowiedział mu jakiś głos.

Wokulski obejrzał się. „Przywidzenie chorej wyobraźni.” Jednocześnie przy czwartym stole, w głębi kościoła, spostrzegł hrabinę Karolową i pannę Izabelę. Obie również siedziały nad tacą z pieniędzmi i trzymały w rękach książki, zapewne do nabożeństwa. Za krzesłem hrabiny stał służący w czarnej liberii.

Wokulski poszedł ku nim potrącając klęczących i omijając inne stoły, przy których pukano na niego zawzięcie. Zbliżył się do tacy i ukłoniwszy się hrabinie, położył swój rulon imperiałów.

„Boże — pomyślał — jak ja głupio muszę wyglądać z tymi pieniędzmi.”

Hrabina odłożyła książkę.

— Witam cię, panie Wokulski — rzekła. — Wiesz, myślałam, że już nie przyjdziesz, i powiem ci, że nawet było mi trochę przykro.

— Mówiłam cioci, że przyjdzie, i do tego z workiem złota — odezwała się po angielsku panna Izabela.

Hrabinie wystąpił na czoło rumieniec i gęsty pot. Zlękła się słów siostrzenicy przypuszczając, że Wokulski rozumie po angielsku.

— Proszę cię, panie Wokulski — rzekła prędko — siądź tu na chwilę, bo delegowany nas opuścił. Pozwolisz, że ułożę twoje imperiały na wierzchu, dla zawstydzenia tych panów, którzy wolą wydawać pieniądze na szampana…

— Ależ niech się ciocia uspokoi — wtrąciła panna Izabela znowu po angielsku. — On z pewnością nie rozumie…

Tym razem i Wokulski zarumienił się.

— Proszę cię, Belu — rzekła hrabina tonem uroczystym — pan Wokulski… który tak hojną ofiarę złożył na naszą ochronę…

— Słyszałam — odpowiedziała panna Izabela po polsku, na znak powitania przymykając powieki.

— Pani hrabina — rzekł trochę żartobliwie Wokulski — chce mnie pozbawić zasługi w życiu przyszłym, chwaląc postępki, które zresztą mogłem spełniać w widokach zysku.

— Domyślałam się tego — szepnęła panna Izabela po angielsku.

Hrabina o mało nie zemdlała czując, że Wokulski musi domyślać się znaczenia słów jej siostrzenicy, choćby nie znał żadnego języka.

— Możesz, panie Wokulski — rzekła z gorączkowym pośpiechem — możesz łatwo zdobyć sobie zasługę w życiu przyszłym, choćby… przebaczając urazy…

— Zawsze je przebaczam — odparł nieco zdziwiony.

— Pozwól sobie powiedzieć, że nie zawsze — ciągnęła hrabina. — Jestem stara kobieta i twoja przyjaciółka, panie Wokulski — dodała z naciskiem — więc zrobisz mi pewne ustępstwo…

— Czekam na rozkazy pani.

— Onegdaj dałeś dymisję jednemu z twoich… urzędników, niejakiemu Mraczewskiemu…

— Za cóż to?… — nagle odezwała się panna Izabela.

— Nie wiem — rzekła hrabina. — Podobno chodziło o różnicę przekonań politycznych czy coś w tym guście…

— Więc ten młody człowiek ma przekonania?… — zawołała panna Izabela. — To ciekawe!…

Powiedziała to w sposób tak zabawny, że Wokulski poczuł, jak ustępuje mu z serca niechęć do Mraczewskiego.

— Nie o przekonania chodziło, pani hrabino — odezwał się — ale o nietaktowne uwagi o osobach, które odwiedzają nasz magazyn.

— Może te osoby same postępują nietaktownie — wtrąciła panna Izabela.

— Im wolno, one za to płacą — odpowiedział spokojnie Wokulski. — Nam nie.

Silny rumieniec wystąpił na twarz panny Izabeli. Wzięła książkę i zaczęła czytać.

— Ale swoją drogą dasz się ubłagać, panie Wokulski — rzekła hrabina. — Znam matkę tego chłopca, i wierz mi, że przykro patrzeć na jej rozpacz…

Wokulski zamyślił się.

— Dobrze — odpowiedział — dam mu posadę, ale w Moskwie.

— A jego biedna matka?… — zapytała hrabina tonem proszącym.

— Więc podwyższę mu o dwieście… o trzysta rubli pensję — odparł.

W tej chwili zbliżyło się do stołu kilkoro dzieci, którym hrabina zaczęła rozdawać obrazki. Wokulski wstał z fotelu i aby nie przeszkadzać pobożnym zajęciom, przeszedł na stronę panny Izabeli.

Panna Izabela podniosła oczy od książki i dziwnym wzrokiem patrząc na Wokulskiego spytała:

— Pan nigdy nie cofa swoich postanowień?

— Nie — odpowiedział. Ale w tej chwili spuścił oczy.

— A gdybym poprosiła za tym młodym człowiekiem?…

Wokulski spojrzał na nią zdumiony.

— W takim razie odpowiedziałbym, że pan Mraczewski stracił miejsce, ponieważ niestosownie odzywał się o osobach, które zaszczyciły go trochę łaskawszym tonem w rozmowie… Jeżeli jednak pani każe…

Teraz panna Izabela spuściła oczy, zmieszana w wysokim stopniu.

— A… a!… wszystko mi jedno w rezultacie, gdzie osiedli się ten młody człowiek. Niech jedzie i do Moskwy.

— Tam też pojedzie — odparł Wokulski. — Moje uszanowanie paniom — dodał kłaniając się.

Hrabina podała mu rękę.

— Dziękuję ci, panie Wokulski, za pamięć i proszę, ażebyś przyszedł do mnie na święcone. Bardzo cię proszę, panie Wokulski — dodała z naciskiem.

Nagle spostrzegłszy jakiś ruch na środku kościoła zwróciła się do służącego:

— Idźże, mój Ksawery, do pani prezesowej i proś, ażeby nam pozwoliła swego powozu. Powiedz, że nam koń zachorował.

— Na kiedy jaśnie pani rozkaże? — spytał służący.

— Tak… za półtorej godziny. Prawda, Belu, że nie posiedzimy tu dłużej?

Służący podszedł do stołu przy drzwiach.

— Więc do jutra, panie Wokulski — rzekła hrabina. — Spotkasz u mnie wielu znajomych. Będzie kilku panów z Towarzystwa Dobroczynności…

„Aha!…” — pomyślał Wokulski żegnając hrabinę. Czuł dla niej w tej chwili taką wdzięczność, że na jej ochronę oddałby połowę majątku.

Panna Izabela z daleka kiwnęła mu głową i, znowu spojrzała w sposób, który wydał mu się bardzo niezwykłym. A gdy Wokulski zniknął w cieniach kościoła, rzekła do hrabiny:

— Cioteczka kokietuje tego pana. Ej! ciociu, to zaczyna być podejrzane…

— Twój ojciec ma słuszność — odparła hrabina — ten człowiek może być użyteczny. Zresztą za granicą podobne stosunki należą do dobrego tonu.

— A jeżeli te stosunki przewrócą mu w głowie?… — spytała panna Izabela.

— W takim razie dowiódłby, że ma słabą głowę — odpowiedziała krótko hrabina biorąc się do książki nabożnej.

Wokulski nie opuścił kościoła, ale w pobliżu drzwi skręcił w boczną nawę. Tuż przy grobie Chrystusa, naprzeciw stolika hrabiny, stał w kącie pusty konfesjonał. Wokulski wszedł do niego, przymknął drzwiczki i niewidzialny, przypatrywał się pannie Izabeli.

Trzymała w ręku książkę spoglądając od czasu do czasu na drzwi kościelne. Na twarzy jej malowało się zmęczenie i nudy. Czasami do stolika zbliżały się dzieci po obrazki; panna Izabela niektórym podawała je sama z takim ruchem, jakby chciała powiedzieć: ach, kiedyż się to skończy!…

„I to wszystko robi się nie przez pobożność ani przez miłość do dzieci, ale dla rozgłosu i w celu wyjścia za mąż — pomyślał Wokulski. — No i ja także — dodał — niemało robię dla reklamy i ożenienia się. Świat ładnie urządzony! Zamiast po prostu pytać się: kochasz mnie czy nie kochasz? albo: chcesz mnie czy nie chcesz? ja wyrzucam setki rubli, a ona kilka godzin nudzi się na wystawie i udaje pobożną.

A jeżeli odpowiedziałaby, że mnie nie kocha? Wszystkie te ceremonie mają dobrą stronę: dają czas i możność zaznajomienia się.

Źle to jednak nie umieć po angielsku… Dziś wiedziałbym, co o mnie myśli: bo jestem pewny, że o mnie mówiła do swej ciotki. Trzeba nauczyć się…

Albo weźmy takie głupstwo jak powóz?… Gdybym miał powóz, mógłbym ją teraz odesłać do domu z ciotką, i znowu zawiązałby się między nami jeden węzeł… Tak, powóz przyda mi się w każdym razie. Przysporzy z tysiąc rubli wydatków na rok, ale cóż zrobię? Muszę być gotowym na wszystkich punktach.

Powóz… angielszczyzna… przeszło dwieście rubli na jedną kwestę!… I to robię ja, który tym pogardzam… Właściwie jednak — na cóż będę wydawał pieniądze, jeżeli nie na zapewnienie sobie szczęścia? Co mnie obchodzą jakieś teorie oszczędności, gdy czuję ból w sercu?…”

Dalszy bieg myśli przerwała mu smutna, brzęcząca melodia. Była to muzyka szkatułki grającej, po której nastąpił świegot sztucznych ptaków; a gdy one milkły, rozlegał się cichy szelest fontanny, szept modlitw i westchnienia pobożnych.

W nawie, u konfesjonału, u drzwi kaplicy grobowej widać było zgięte postacie klęczących. Niektórzy czołgali się do krucyfiksu na podłodze i ucałowawszy go kładli na tacy drobne pieniądze wydobyte z chustki do nosa.

W głębi kaplicy, w powodzi światła, leżał biały Chrystus otoczony kwiatami. Zdawało się Wokulskiemu, że pod wpływem migotliwych płomyków twarz jego ożywia się przybierając wyraz groźby albo litości i łaski. Kiedy pozytywka wygrywała Łucję z Lamermooru albo kiedy ze środka kościoła doleciał stukot pieniędzy i francuskie wykrzykniki, oblicze Chrystusa ciemniało. Ale kiedy do krucyfiksu zbliżył się jaki biedak i opowiadał Ukrzyżowanemu swoje strapienia, Chrystus otwierał martwe usta i w szmerze fontanny powtarzał błogosławieństwa i obietnice…

„Błogosławieni cisi… Błogosławieni smutni…”

Do tacy podeszła młoda, uróżowana dziewczyna. Położyła srebrną czterdziestówkę, ale nie śmiała dotknąć krzyża. Klęczący obok z niechęcią patrzyli na jej aksamitny kaftanik i jaskrawy kapelusz. Ale gdy Chrystus szepnął: „Kto z was jest bez grzechu, niech rzuci na nią kamieniem”, padła na posadzkę i ucałowała jego nogi jak niegdyś Maria Magdalena.

„Błogosławieni, którzy łakną sprawiedliwości… Błogosławieni, którzy płaczą…”

Z głębokim wzruszeniem przypatrywał się Wokulski pogrążonemu w kościelnym mroku tłumowi, który z tak cierpliwą wiarą od osiemnastu wieków oczekuje spełnienia się boskich obietnic.

„Kiedyż to będzie!…” — pomyślał.

„Pośle Syn Człowieczy anioły swoje, a oni zbiorą wszystkie zgorszenia i tych, którzy nieprawość czynią, jako zbiera się kąkol i pali się go ogniem.”

Machinalnie spojrzał na środek kościoła. Przy bliższym stoliku hrabina drzemała, a panna Izabela ziewała, przy dalszym trzy nie znane mu damy zaśmiewały się z opowiadań jakiegoś wykwintnego młodzieńca.

„Inny świat… inny świat!… — myślał Wokulski. — Co za fatalność popycha mnie w tamtą stronę?”

W tej chwili tuż obok konfesjonału stanęła, a potem uklękła osoba młoda, ubrana bardzo starannie, z małą dziewczynką.

Wokulski przypatrzył się jej i dostrzegł, że jest niezwykle piękna. Uderzył go nade wszystko wyraz jej twarzy, jakby do tego grobu przyszła nie z modlitwą, ale z zapytaniem i skargą.

Przeżegnała się, lecz zobaczywszy tacę wydobyła woreczek z pieniędzmi.

— Idź, Helusiu — rzekła półgłosem do dziecka — połóż to na tacy i pocałuj Pana Jezusa.

— Gdzie, proszę mamy, pocałować?

— W rączkę i w nóżkę…

— I w buzię?

— W buzię nie można.

— Ech, co tam!… — Pobiegła do tacy i pochyliła się nad krzyżem.

— A widzi mama — zawołała powracając — pocałowałam i Pan Jezus nic nie powiedział.

— Niech Helusia będzie grzeczna — odparła matka. — Lepiej uklęknij i zmów paciorek.

— Jaki paciorek?

— Trzy Ojcze nasz, trzy Zdrowaś…

— Taki duży paciorek?… a ja taka malutka…

— No, to zmów jedno Zdrowaś… Tylko uklęknij… Patrz się tam…

— Już patrzę. Zdrowaś Maria, łaski pełna… Czy to, proszę mamy, ptaszki śpiewają?

— Ptaszki sztuczne. Mów paciorek.

— Jakie to sztuczne?

— Zmów pierwej paciorek.

— Kiedy nie pamiętam, gdzie skończyłam…

— Więc mów za mną: Zdrowaś Maria…

— Śmierci naszej. Amen — dokończyła dziewczynka. — A z czego robią się sztuczne ptaszki?

— Heluniu, bądź cicho, bo nigdy cię nie pocałuję — szepnęła strapiona matka. — Masz tu książkę i oglądaj obrazki, jak Pan Jezus był męczony.

Dziewczynka usiadła z książką na stopniach konfesjonału i ucichła.

„Co to za miła dziecina! — myślał Wokulski. — Gdyby była moją, zdaje się, że odzyskałbym równowagę umysłu, którą dziś tracę z dnia na dzień. I matka prześliczna kobieta. Jakie włosy, profil, oczy… Prosi Boga, ażeby zmartwychwstało ich szczęście… Piękna i nieszczęśliwa; musi być wdową.

Ot, gdybym ją był spotkał rok temu.

I jestże tu ład na świecie?… O krok od siebie staje dwoje ludzi nieszczęśliwych; jedno szuka miłości i rodziny, drugie może walczy z biedą i brakiem opieki. Każde znalazłoby w drugim to, czego potrzebuje, no — i nie zejdą się… Jedno przychodzi błagać Boga o miłosierdzie, drugie wyrzuca pieniądze dla stosunków. Kto wie, czy paręset rubli nie byłoby dla tej kobiety szczęściem? Ale ona ich nie dostanie; Bóg w tych czasach nie słucha modlitwy uciśnionych.

A gdyby jednak dowiedzieć się, kto ona jest?… Może bym potrafił jej dopomóc. Dlaczego wzniosłe obietnice Chrystusa nie mają być spełnione, choćby przez takich jak ja niedowiarków, skoro pobożni zajmują się czym innym?” W tej chwili Wokulskiemu zrobiło się gorąco… Do stolika hrabiny zbliżył się elegancki młodzieniec i coś położył na tacy. Na jego widok panna Izabela zarumieniła się i oczy jej nabrały tego dziwnego wyrazu, który zawsze tak zastanawiał Wokulskiego.

Na wezwanie hrabiny elegant siadł na tym samym fotelu, który niedawno zajmował Wokulski, i zawiązała się żywa rozmowa. Wokulski nie słyszał jej treści, tylko czuł, że w mózgu wypala mu się obraz tego towarzystwa. Kosztowny dywan, srebrna taca zasypana na wierzchu garścią imperiałów, dwa świeczniki, dziesięć płomyków, hrabina odziana w grubą żałobę, młody człowiek zapatrzony w pannę Izabelę i ona — rozpromieniona. Nawet ten szczegół nie uszedł jego uwagi, że od blasku płomyków hrabinie świecą się policzki, młodemu człowiekowi koniec nosa, a pannie Izabeli oczy.

„Czy oni kochają się? — myślał. — Więc dlaczegóż by się nie pobrali?… — Może on nie ma pieniędzy… Lecz w takim razie: co znaczą jej spojrzenia?… Podobne rzucała dziś na mnie. Prawda, że panna na wydaniu musi mieć kilku albo i kilkunastu wielbicieli i wabić wszystkich, ażeby… sprzedać się najwięcej ofiarującemu!”

Przyszedł delegowany. Hrabina podniosła się z fotelu, to samo zrobiła panna Izabela i przystojny młodzieniec, i wszyscy troje z wielkim szelestem poszli ku drzwiom zatrzymując się przy innych stolikach. Każdy z asystującej tam młodzieży gorąco witał pannę Izabelę, a ona każdego obdarzała tymi samymi, zupełnie tymi samymi spojrzeniami, które Wokulskiemu zachwiały rozum. Wreszcie wszystko ucichło: hrabina i panna Izabela opuściły kościół.

Wokulski ocknął się i spojrzał bliżej siebie. Pięknej pani z dzieckiem już nie było.

„Jaka szkoda!” — szepnął i uczuł lekkie ściśnięcie serca.

Natomiast obok krzyża leżącego na ziemi wciąż klęczała młoda dziewczyna w aksamitnym kaftaniku i jaskrawym kapeluszu. Gdy zwróciła oczy na oświetlony grób, jej także błysnęło coś na wyróżowanych policzkach. Jeszcze raz ucałowała nogi Chrystusowi, ciężko podniosła się i wyszła.

„Błogosławieni, którzy płaczą… Niechże przynajmniej tobie zmarły Chrystus dotrzyma obietnicy” — pomyślał Wokulski i wyszedł za nią.

W kruchcie spostrzegł, że dziewczyna rozdaje jałmużnę dziadom. I opanowała go okrutna boleść na myśl, że z dwu kobiet, z których jedna chce się sprzedać za majątek, a druga już się sprzedaje z nędzy, ta druga, okryta hańbą, wobec jakiegoś wyższego trybunału może byłaby lepszą i czystszą.

Na ulicy zrównał się z nią i zapytał:

— Dokąd idziesz?

Na jej twarzy znać było ślady łez. Podniosła na Wokulskiego apatyczne wejrzenie i odparła:

— Mogę pójść z panem.

— Tak mówisz?… Więc chodź.

Nie było jeszcze piątej, dzień duży; kilku przechodniów obejrzało się za nimi.

„Trzeba być kompletnym błaznem, ażeby robić coś podobnego — pomyślał Wokulski idąc w stronę sklepu. — Mniejsza o skandal, ale co, u diabła, za projekta snują mi się po łbie? Apostolstwo?… Szczyt głupoty.

Wreszcie — wszystko mi jedno; jestem tylko wykonawcą cudzej woli.”

Wszedł w bramę domu, w którym znajdował się sklep, i skręcił do pokoju Rzeckiego, a za nim dziewczyna. Pan Ignacy był u siebie i zobaczywszy szczególną parę, rozłożył ręce z podziwu.

— Czy możesz wyjść na kilka minut? — zapytał go Wokulski.

Pan Ignacy nie odpowiedział nic. Wziął klucz od tylnych drzwi sklepu i opuścił pokój.

— Dwu? — szepnęła dziewczyna wyjmując szpilkę z kapelusza.

— Za pozwoleniem — przerwał jej Wokulski. — Dopiero co byłaś w kościele, wszak prawda, moja pani?

— Pan mnie widział?

— Modliłaś się i płakałaś. Czy mogę wiedzieć, z jakiego powodu?

Dziewczyna zdziwiła się i wzruszając ramionami odparła:

— Czy pan jest ksiądz, że się o to pyta?

A przypatrzywszy się uważniej Wokulskiemu dodała:

— Eh! także zawracanie głowy… Dowcipny!

Zabierała się do odejścia, ale zatrzymał ją Wokulski.

— Poczekaj. Jest ktoś, który chciałby ci dopomóc, więc nie spiesz się i odpowiadaj szczerze…

Znowu przypatrzyła mu się. Nagle oczy jej zaśmiały się, a na twarz wystąpił rumieniec.

— Wiem — zawołała — pan pewnie od tego starego pana!… On kilka razy obiecywał, że mnie weźmie… Czy on bardzo bogaty?… Pewnie, że bardzo… Jeździ powozem i siada w pierwszych rzędach w teatrze.

— Posłuchaj mnie — przerwał — i odpowiadaj: czegoś płakała w kościele?

— A bo, widzi pan… — zaczęła dziewczyna i opowiedziała tak cyniczną historię jakiegoś sporu z gospodynią, że słuchając jej Wokulski pobladł.

„Oto zwierzę!” — szepnął.

— Poszłam na groby — mówiła dalej dziewczyna — myślałam, że się trochę rozerwę. Gdzie tam, com wspomniała o starej, to aż mi łzy pociekły ze złości. Zaczęłam prosić Pana Boga, ażeby albo starą choroba zatłukła, albo żebym ja od niej wyszła. I widać Bóg wysłuchał, kiedy ten pan chce mnie zabrać.

Wokulski siedział bez ruchu. Wreszcie zapytał:

— Ile masz lat?

— Mówi się, że szesnaście, ale naprawdę mam dziewiętnaście.

— Chcesz stamtąd wyjść?

— A — choćby do piekła. Już mi tak dokuczyli… Ale…

— Cóż?

— Pewnie nic z tego nie będzie… Wyjdę dziś, to po świętach sprowadzą mnie i zapłacą jak wtedy w karnawale, com później tydzień leżała.

— Nie sprowadzą.

— Akurat! Mam przecie dług…

— Duży?

— Oho!… z pięćdziesiąt rubli. Nie wiem nawet, skąd się wziął, bo za wszystko płacę podwójnie. Ale jest… U nas tak zawsze. A jeszcze jak usłyszą, że tamten pan ma pieniądze, to powiedzą, że ich okradłam, i narachują, ile im się podoba.

Wokulski czuł, że opuszcza go odwaga.

— Powiedz mi, czy ty zechcesz pracować?

— A co będę miała do roboty?

— Nauczysz się szyć.

— To na nic. Byłam przecie w szwalni. Ale z ośmiu rubli na miesiąc nikt nie wyżyje. Wreszcie — jestem tyle jeszcze warta, że mogę nikogo nie obszywać.

Wokulski podniósł głowę.

— Nie chcesz wyjść stamtąd!

— Ale chcę!

— Więc decyduj się natychmiast. Albo weźmiesz się do roboty, bo darmo nikt na świecie chleba nie jada…

— I to nieprawda — przerwała. — Ten stary pan nic przecie nie robi, a pieniądze ma. Nieraz też mówił, że mnie już o nic głowa nie zaboli…

— Nie pójdziesz do żadnego pana, tylko do magdalenek. Albo wracaj na miejsce.

— Magdalenki mnie nie wezmą. Trzeba zapłacić dług i mieć poręczenie…

— Wszystko będzie załatwione, jeżeli tam pójdziesz.

— Jakże ja do nich pójdę?

— Dam ci list, który zaraz odniesiesz, i tam zostaniesz. Chcesz czy nie chcesz?…

— Ha! niech pan da list. Zobaczę, jak mi tam będzie.

Usiadła i oglądała się po pokoju.

Wokulski napisał list, opowiedział, gdzie ma iść, i w końcu dodał:

— Masz wóz i przewóz. Będziesz dobra i pracowita, będzie ci dobrze; ale jeżeli nie skorzystasz z okazji, rób, co ci się podoba. Możesz iść.

Dziewczyna roześmiała się.

— To stara będzie się wściekać… To jej narobię… Cha… Cha!… Ale… może pan tylko naciąga?

— Idź — odpowiedział Wokulski wskazując drzwi.

Jeszcze raz przypatrzyła mu się z uwagą i wyszła wzruszając ramionami.

W chwilę po jej odejściu ukazał się pan Ignacy.

— Cóż to za znajomość? — spytał kwaśno.

— Prawda!… — rzekł zamyślony Wokulski. — Nie widziałem jeszcze podobnego bydlęcia, chociaż znam dużo bydląt.

— W samej Warszawie jest ich tysiące — odparł Rzecki.

— Wiem. Tępienie ich do niczego nie doprowadzi, bo ciągle się odradzają, więc wniosek, że prędzej czy później społeczeństwo musi się przebudować od fundamentów do szczytu. Albo zgnije.

— Aha!… — szepnął Rzecki. — Domyślałem się tego.

Wokulski pożegnał go. Doświadczał takich uczuć, jak chory na gorączkę, którego oblano zimną wodą.

„Nim jednak przebuduje się społeczność — myślał — widzę, że sfera mojej filantropii bardzo się uszczupli. Majątek mój nie wystarczyłby na uszlachetnianie instynktów nieludzkich. Wolę ziewające kwestarki niżeli modlące się i płaczące potwory.”

Obraz panny Izabeli ukazał mu się otoczony jaśniejszym niż kiedykolwiek blaskiem. Krew biła mu do głowy i upokarzał się w duchu na myśl, że z podobnym stworzeniem mógł ją zestawić!

„Wolęż ja wyrzucać pieniądze na powozy i konie aniżeli na tego rodzaju — nieszczęścia!…”

W Wielką Niedzielę Wokulski najętym powozem zajechał przed mieszkanie hrabiny. Zastał już długi szereg ekwipażów bardzo rozmaitego dostojeństwa. Były tam eleganckie dorożki obsługujące złotą młodzież i dorożki zwyczajne, wzięte na godziny przez emerytów; stare karety, stare konie, stara uprząż i służba w wytartej liberii, i nowe, prosto z Wiednia powoziki, przy których lokaje mieli kwiaty w butonierkach, a furmani opierali bat na biodrze, jak marszałkowską buławę. Nie brakło i fantastycznych kozaków, odzianych w spodnie tak szerokie, jakby tam właśnie ich panowie umieścili swoją ambicję.

Dostrzegł też mimochodem, że w gronie zebranych woźniców służba wielkich panów zachowywała się w sposób pełen godności, bankierscy chcieli rej wodzić, za co im wymyślano, a dorożkarze byli najrezolutniejsi. Furmani zaś powozów najętych trzymali się blisko siebie, gardzący resztą i przez nią pogardzani.

Gdy Wokulski wszedł do przysionka, siwy szwajcar w czerwonej wstędze ukłonił mu się głęboko i otworzył drzwi do kontramarkarni, gdzie dżentelmen w czarnym fraku zdjął z niego palto. Jednocześnie zaś zabiegł mu drogę Józef, lokaj hrabiny, który dobrze znał Wokulskiego; przenosił bowiem z jego sklepu do kościoła pozytywkę i śpiewające ptaszki.

— Jaśnie pani czeka — rzekł Józef.

Wokulski sięgnął do kamizelki i dał mu pięć rubli czując, że poczyna sobie jak parweniusz.

„Ach, jakiż ja jestem głupi! — myślał. — Nie, nie jestem głupi. Jestem tylko dorobkiewicz, który w tym państwie musi opłacać się każdemu na każdym kroku. No, nawracanie jawnogrzesznic kosztuje więcej.”

Szedł po marmurowych schodach ozdobionych kwiatami, a Józef przed nim. Na pierwszej kondygnacji miał kapelusz na głowie, na drugiej zdjął go nie wiedząc, czy robi stosownie, czy niestosownie.

„W rezultacie mógłbym między nich wszystkich wejść w kapeluszu na głowie” — rzekł do siebie.

Dostrzegł, że Józef mimo swego wieku, więcej niż średniego, biegł po schodach jak łania i na górze gdzieś się podział, a Wokulski został sam nie wiedząc dokąd udać się i komu się zameldować. Była to krótka chwila, lecz w Wokulskim gniew zakipiał.

„Jakimi to oni formami obwarowali się, co? — pomyślał. — A… gdybym to mógł wszystko zwalić!…”

I przywidziało mu się w ciągu kilkunastu sekund, że między nim a tym czcigodnym światem form wykwintnych musi się stoczyć walka, w której albo ten świat runie, albo — on zginie.

„Więc dobrze, zginę… Ale zostawię po sobie pamiątkę!…”

„Zostawisz przebaczenie i litość” — szepnął mu jakiś głos.

„Czyżem ja aż tak nikczemny!”

„Nie, jesteś aż tak szlachetny.”

Ocknął się — przy nim stał pan Tomasz Łęcki.

— Witam cię, panie Stanisławie — rzekł z właściwą mu majestatycznością. — Witam cię tym goręcej, że przybycie twoje do nas łączy się z bardzo miłym wypadkiem w rodzinie…

„Czyżby zaręczyła się panna Izabela?…” — pomyślał Wokulski i pociemniało mu w oczach.

— Wyobraź pan sobie, że z okazji twego tu przybycia… Słyszysz, panie Stanisławie?… Z okazji twojej wizyty u nas ja pogodziłem się z panią Joanną, z moją siostrą… Ale pan zbladłeś?… Znajdziesz tu wielu znajomych… Nie wyobrażaj sobie, że arystokracja jest tak straszną…

Wokulski otrząsnął się.

— Panie Łęcki — odparł chłodno — w moim namiocie pod Plewną bywali więksi panowie. I byli dla mnie tyle łaskawi, że niełatwo wzruszę się widokiem nawet tak wielkich, jakich… nie znajdę w Warszawie.

— A… A!… — szepnął pan Tomasz i ukłonił mu się. Wokulski zdumiał się.

„Oto fagas! — przemknęło mu przez głowę. — I ja… ja!… miałbym z takimi ludźmi robić sobie ceremonie?…”

Pan Łęcki wziął go pod rękę i w sposób bardzo uroczysty wprowadził do pierwszego salonu, gdzie byli sami mężczyźni.

— Widzisz pan: hrabia… — zaczął pan Tomasz.

— Znam — odparł Wokulski, a w duchu dodał: — „Winien mi ze trzysta rubli…”

— Bankier… — objaśniał dalej pan Tomasz. Ale nim powiedział nazwisko, bankier sam zbliżył się do nich i przywitawszy Wokulskiego rzekł:

— Bój się pan Boga, z Paryża ogromnie ekscytują nas o te bulwary… Czy im pan odpowiedziałeś?

— Pierwej chciałem porozumieć się z panem — odparł Wokulski.

— Więc zejdźmy się gdzie. Kiedy pan jesteś w domu?

— Nie mam stałej godziny, wolę być u pana.

— To wstąp pan do mnie we środę na śniadanie i raz skończmy.

Pożegnali się. Pan Tomasz czulej przycisnął ramię Wokulskiego.

— Jenerał… — zaczął.

Jenerał ujrzawszy Wokulskiego podał mu rękę i przywitali się jak starzy znajomi.

Pan Tomasz stawał się coraz tkliwszym dla Wokulskiego i zaczynał dziwić się widząc, że kupiec galanteryjny zna najwybitniejsze osobistości w mieście, a nie zna tylko tych, którzy odznaczali się tytułem albo majątkiem, nic zresztą nie robiąc.

Przy wejściu do drugiego salonu, gdzie było kilka dam, zastąpiła im drogę hrabina Karolowa. Koło niej przesunął się służący Józef.

„Rozstawili pikiety — pomyślał Wokulski — ażeby nie skompromitować dorobkiewicza. Grzecznie to z ich strony, ale…”

— Jakże się cieszę, panie Wokulski — rzekła hrabina odbierając go panu Tomaszowi — jakże się cieszę, że spełniłeś moją prośbę… Jest tu właśnie osoba, która pragnie poznać się z panem.

W pierwszym salonie ukazanie się Wokulskiego zrobiło pewną sensację.

— Jenerale — mówił hrabia — hrabina zaczyna nam sprowadzać kupców galanteryjnych. Ten Wokulski…

— On taki kupiec jak ja i pan — odparł jenerał.

— Mój książę — mówił inny hrabia — skąd wziął się tu ten jakiś Wokulski?

— Zaprosiła go gospodyni — odparł książę.

— Nie mam przesądu co do kupców — ciągnął dalej hrabia — ale ten Wokulski, który zajmował się dostawą w czasie wojny i zrobił na niej majątek…

— Tak… tak… — przerwał książę. — Ten rodzaj majątków bywa zwykle niepewny, ale za Wokulskiego ręczę. Hrabina mówiła ze mną, a ja zapytywałem oficerów, którzy byli na wojnie, między innymi mojego siostrzeńca. Otóż o Wokulskim było jedno zdanie, że dostawa, której się on dotknął, była uczciwa. Nawet żołnierze, ile razy dostali dobry chleb, mówili, że musiał być pieczony z mąki od Wokulskiego. Więcej hrabiemu powiem — ciągnął książę — że Wokulski, który swoją rzetelnością zwrócił na siebie uwagę osób najwyżej położonych, miewał bardzo ponętne propozycje. W styczniu tego oto roku dawano mu dwakroć sto tysięcy rubli tylko za firmę do pewnego przedsiębiorstwa i nie przyjął…

Hrabia uśmiechnął się i rzekł:

— Miałby więcej o dwakroć sto tysięcy rubli…

— Miałby, ale nie byłby dziś tutaj — odparł książę i kiwnąwszy głową hrabiemu odszedł.

— Stary wariat — szepnął hrabia, pogardliwie spoglądając za księciem.

W trzecim salonie, dokąd wszedł z hrabiną Wokulski, znajdował się bufet tudzież mnóstwo większych i mniejszych stolików, przy których dwójkami, trójkami, nawet czwórkami siedzieli zaproszeni. Kilku służących roznosiło potrawy i wina, a dyrygowała nimi panna Izabela, widocznie zastępując gospodynię. Miała na sobie bladoniebieską suknię i wielkie perły na szyi. Była tak piękna i tak majestatyczna w ruchach, że Wokulski patrząc na nią skamieniał.

„Nawet marzyć o niej nie mogę!…” — pomyślał z rozpaczą.

Jednocześnie we framudze okna spostrzegł młodego człowieka, który był wczoraj na grobach, a dziś siedział sam przy małym stoliczku nie spuszczając oka z panny Izabeli.

„Naturalnie, że ją kocha!” — myślał Wokulski i doznał takiego wrażenia, jakby owionął go chłód grobu.

„Jestem zgubiony” — dodał w duchu.

Wszystko to trwało kilka sekund.

— Czy widzisz pan tę staruszkę między biskupem i jenerałem? — odezwała się hrabina. — Jest to prezesowa Zasławska, moja najlepsza przyjaciółka, która koniecznie chce pana poznać. Jest panem bardzo zajęta — ciągnęła hrabina z uśmiechem — jest bezdzietna i ma parę ładnych wnuczek. Zróbże pan dobry wybór!… Tymczasem przypatrz się jej, a gdy ci panowie odejdą, przedstawię pana. A… książę…

— Witam pana — odezwał się książę do Wokulskiego. — Kuzynka pozwoli?…

— Bardzo proszę — odparła hrabina. — Macie tu panowie wolny stolik… Ja opuszczę was na chwilę…

Odeszła.

— Siądźmy, panie Wokulski — mówił książę. — Wybornie zdarzyło się, ponieważ mam do pana ważny interes. Wyobraź pan sobie, że pańskie projekta wywołały wielki popłoch między naszymi bawełnianymi fabrykantami… Wszak dobrze powiedziałem — bawełnianymi?… Oni utrzymują, że pan chce zabić nasz przemysł… Czy istotnie konkurencja, którą pan stwarza, jest tak groźna?…

— Mam wprawdzie — odparł Wokulski — u moskiewskich fabrykantów kredyt do wysokości trzech, nawet czterech milionów rubli, ale jeszcze nie wiem, czy pójdą ich wyroby.

— Straszna!… straszna cyfra! — szepnął książę. — Czy nie widzisz pan w niej istotnego niebezpieczeństwa dla naszych fabryk?

— Ach, nie. Widzę tylko nieznaczne zmniejszenie ich kolosalnych dochodów, co zresztą mnie nie obchodzi. Ja mam obowiązek dbać tylko o własny zysk i o taniość dla nabywców; nasz zaś towar będzie tańszy.

— Czy jednak rozważyłeś pan tę kwestię jako obywatel?… — rzekł książę ściskając go za rękę. — My już tak niewiele mamy do stracenia…

— Mnie się zdaje, że jest to dość po obywatelsku dostarczyć konsumentom tańszego towaru i złamać monopol fabrykantów, którzy zresztą tyle mają z nami wspólnego, że wyzyskują naszych konsumentów i robotników.

— Tak pan sądzisz?… Nie pomyślałem o tym. Mnie zresztą nie obchodzą fabrykanci, ale kraj, nasz kraj, biedny kraj…

— Czym można panom służyć? — odezwała się nagle, zbliżywszy się do nich, panna Izabela.

Książę i Wokulski powstali.

— Jakże jesteś dziś piękna, kuzynko — rzekł książę ściskając ją za rękę. — Żałuję doprawdy, że nie jestem moim własnym synem… Chociaż — może to i lepiej! Bo gdybyś mnie odrzuciła, co jest prawdopodobne, byłbym bardzo nieszczęśliwy… Ach, przepraszam!… — spostrzegł się książę. — Pozwolisz, kuzynko, przedstawić sobie pana Wokulskiego. Dzielny człowiek, dzielny obywatel… to ci wystarczy, wszak prawda?…

— Mam już przyjemność… — szepnęła panna Izabela odpowiadając na ukłon.

Wokulski spojrzał jej w oczy i dostrzegł takie przerażenie, taki smutek, że go znowu opanowała desperacja.

„Po com ja tu wchodził?…” — pomyślał.

Spojrzał na framugę okna i znowu zobaczył młodego człowieka, który ciągle siedział sam nad nietkniętym talerzem zasłaniając oczy ręką.

„Ach, po com ja tu przyszedł, nieszczęśliwy…” — myślał Wokulski czując taki ból, jakby mu serce wyrywano kleszczami.

— Może pan choć wina pozwoli? — pytała panna Izabela przypatrując mu się ze zdziwieniem.

— Co pani każe — odparł machinalnie.

— Musimy się lepiej poznać, panie Wokulski — mówił książę. — Musisz pan zbliżyć się do naszej sfery, w której, wierz mi, są rozumy i szlachetne serca, ale — brak inicjatywy…

— Jestem dorobkiewiczem, nie mam tytułu… — odparł Wokulski chcąc cośkolwiek odpowiedzieć.

— Przeciwnie, masz pan… jeden tytuł: pracę, drugi: uczciwość, trzeci: zdolności, czwarty: energię… Tych tytułów nam potrzeba do odrodzenia kraju, to nam daj, a przyjmiemy cię jak… brata…

Zbliżyła się hrabina.

— Pozwoli książę?… — rzekła. — Panie Wokulski…

Podała mu rękę i poszli oboje do fotelu prezesowej.

— Oto jest, prezesowo, pan Stanisław Wokulski — odezwała się hrabina do staruszki ubranej w ciemną suknię i kosztowne koronki.

— Siądź, proszę cię — rzekła prezesowa wskazując mu krzesło obok. — Stanisław ci na imię, tak?… A, z którychże to Wokulskich?…

— Z tych… nie znanych nikomu — odparł — a najmniej chyba pani.

— A nie służyłże twój ojciec w wojsku?

— Ojciec nie, tylko stryj.

— I gdzież to on służył, nie pamiętasz?… Czy nie było mu na imię także Stanisław?

— Tak, Stanisław. Był porucznikiem, a później kapitanem w siódmym pułku liniowym…

— W pierwszej brygadzie, drugiej dywizji — przerwała prezesowa. — Widzisz, moje dziecko, że nie jesteś mi tak nie znany… Żyjeż on jeszcze?…

— Umarł przed pięcioma laty.

Prezesowej zaczęły drżeć ręce. Otworzyła mały flakonik i powąchała go.

— Umarł, powiadasz?… Wieczny mu odpoczynek!… Umarł… A nie zostałaż ci jaka po nim pamiątka?

— Złoty krzyż…

— Tak, złoty krzyż… I nicże więcej?

— Miniatura stryja z roku 1828, malowana na kości słoniowej.

Prezesowa coraz częściej podnosiła flakonik; ręce drżały jej coraz silniej.

— Miniatura… — powtórzyła. — A wieszże, kto ją malował?… I nicże więcej nie zostało?

— Była jeszcze paczka papierów i jakaś druga miniatura…

— Coże się z nimi dzieje?… — nalegała coraz niespokojniej prezesowa.

— Te przedmioty stryj sam opieczętował na kilka dni przed śmiercią i kazał włożyć je do swojej trumny.

— A… a!… — szepnęła staruszka i rzewnie się rozpłakała.

W sali zrobił się ruch. Przybiegła zatrwożona panna Izabela, potem hrabina, wzięły prezesową pod ręce i z wolna wyprowadziły do dalszych pokojów. W jednej chwili na Wokulskiego zwróciły się wszystkie oczy. Zaczęto z cicha szeptać.

Widząc, że wszyscy na niego patrzą i o nim mówią, Wokulski zmieszał się. Ażeby jednak pokazać obecnym, że ta osobliwa popularność nic go nie obchodzi, wypił jeden po drugim dwa kieliszki wina stojące na stoliku i wtedy spostrzegł, że jeden kieliszek, z winem węgierskim, należał do jenerała, a drugi, z czerwonym, do biskupa.

„Ładnie się urządzam — rzekł do siebie. — Gotowi jeszcze powiedzieć, że zrobiłem afront staruszce, ażeby wypić wino jej sąsiadom…”

Wstał z zamiarem wyjścia i zrobiło mu się gorąco na myśl o defiladzie przez dwa salony, w których czekają go rózgi spojrzeń i szeptów. Ale zabiegł mu drogę książę mówiąc:

— Pewnie rozmawialiście państwo z prezesową o bardzo dawnych czasach, kiedy aż do łez doszło. Prawda, że zgadłem?… Wracając do tematu, który nam przerwano, czy nie sądzisz pan, że dobrze byłoby założyć w kraju polską fabrykę tanich tkanin?…

Wokulski potrząsnął głową.

— Wątpię, ażeby się to udało — odparł. — Trudno myśleć o wielkich fabrykach tym, którzy nie mogą zdobyć się na małe ulepszenia w już istniejących…

— Mianowicie?…

— Mówię o młynach — ciągnął Wokulski. — Za parę lat będziemy sprowadzali nawet mąkę, bo nasi młynarze nie chcą zastąpić kamieni — walcami.

— Pierwszy raz słyszę?… Siądźmy tu — mówił książę ciągnąc go do obszernej framugi — i opowiedz pan, co to znaczy?

W salonach tymczasem rozmawiano.

— Jakaś zagadkowa figura ten pan — mówiła po francusku dama w brylantach do damy w strusim piórze. — Pierwszy raz widziałam prezesową płaczącą.

— Naturalnie, historia miłosna — odpowiedziała dama z piórem. — W każdym razie zrobił ktoś złośliwego figla hrabinie i prezesowej wprowadzając tego jegomościa.

— Przypuszczasz pani, że…

— Jestem pewna — odparła wzruszając ramionami. — Niech pani wreszcie spojrzy na niego. Maniery bardzo złe, ale cóż to za fizjognomia, jaka duma!… Szlachetnej rasy nie ukryje się nawet pod łachmanami.

— Zadziwiające!… — mówiła dama w brylantach. — Bo i ten jego majątek, jakoby zrobiony w Bułgarii…

— Naturalnie. To zarazem tłomaczy, dlaczego prezesowa pomimo bogactw tak mało wydaje na siebie.

— I książę bardzo na niego łaskaw…

— Przez litość, czy nie za mało?… Niech tylko pani spojrzy na nich obu…

— Sądziłabym, że nie ma ani śladu podobieństwa.

— Zapewne, ale… ta duma, pewność siebie… Z jaką oni swobodą rozmawiają…

Przy innym stoliku naradzali się trzej panowie.

— No, hrabina zrobiła zamach stanu — mówił brunet z grzywką.

— I udał się jej. Ten Wokulski trochę sztywny, ale ma w sobie coś — odpowiedział pan siwy.

— W każdym razie kupiec…

— Czymże kupiec gorszy od bankierów?

— Kupiec galanteryjny, sprzedaje portmonetki — nalegał brunet.

— My czasami sprzedajemy herby… — wtrącił trzeci, szczupły staruszek z siwymi faworytami.

— Jeszcze zechce ożenić się tutaj…

— Tym lepiej dla panien.

— Ja bym mu sam oddał córkę. Człowiek, słyszę, porządny, bogaty, posagu nie strwoni…

Koło nich szybko przeszła hrabina.

— Panie Wokulski — rzekła wyciągając wachlarz w kierunku framugi.

Wokulski przybiegł do niej. Podała mu rękę i we dwoje opuścili salon. Osamotnionego księcia zaraz otoczyli mężczyźni; niektórzy prosili go, ażeby zapoznał ich z Wokulskim.

— Warto, warto!… — mówił zadowolony książę. — Takiego nie było jeszcze między nami. Gdybyśmy dawniej zbliżyli się do nich, nasz nieszczęśliwy kraj wyglądałby inaczej.

Usłyszała to mijająca ich właśnie panna Izabela i — pobladła. Przystąpił do niej młody człowiek z wczorajszej kwesty.

— Zmęczyła się pani? — rzekł.

— Trochę — odpowiedziała ze smutnym uśmiechem. — Przychodzi mi do głowy dziwne pytanie — dodała po chwili — czy ja też potrafiłabym walczyć?…

— Czy z sercem? — zapytał. — Nie warto…

Panna Izabela wzruszyła ramionami.

— Ach, gdzież znowu z sercem. Myślę o prawdziwej walce z silnym nieprzyjacielem.

Ścisnęła go za rękę i opuściła salon.

Wokulski prowadzony przez hrabinę minął długi szereg pokojów. W jednym z nich, z dala od zaproszonych gości, rozlegały się śpiewy i dźwięki fortepianu. Gdy weszli tam, uderzył go szczególny widok. Jakiś młody człowiek grał na fortepianie; z dwu bardzo przystojnych dam, stojących przy nim, jedna udawała skrzypce, druga klarnet; przy tej zaś muzyce tańczyło kilka par, między którymi znajdował się tylko jeden mężczyzna.

— Oj! wy zbytnicy! — zgromiła ich hrabina.

Odpowiedzieli wybuchem śmiechu, nie przerywając zabawy.

Minęli i ten pokój i weszli na schody.

— Ot, widzisz — rzekła hrabina — to jest najwyższa arystokracja. Zamiast siedzieć w salonie, uciekli tutaj dokazywać.

„Jaki oni mają rozum!” — pomyślał Wokulski.

I zdawało mu się, że między tymi ludźmi życie upływa prościej i weselej aniżeli między nadętym mieszczaństwem albo arystokratyzującą szlachtą.

Na górze, w pokoju odciętym od zgiełku i nieco przyćmionym, siedziała w fotelu prezesowa.

— Zostawiam was tu, moi państwo — rzekła hrabina. — Nagadajcie się, bo ja muszę wracać.

— Dziękuję ci, Joasiu — odpowiedziała prezesowa. — Siądźże, proszę cię — zwróciła się do Wokulskiego.

A gdy zostali sami, dodała:

— Nawet nie wiesz, ile obudziłeś we mnie wspomnień.

Teraz dopiero Wokulski spostrzegł, że między tą damą a jego stryjem musiał istnieć jakiś niezwykły stosunek. Opanowało go niespokojne zdumienie.

„Dzięki Bogu — pomyślał — że jestem legalnym dzieckiem moich rodziców.”

— Proszę cię — zaczęła prezesowa — mówisz, że stryj twój umarł. Gdzieże on, biedak, pochowany?

— W Zasławiu, gdzie mieszkał od powrotu z emigracji.

Prezesowa znowu podniosła chustkę do oczu.

— Doprawdy?… Ach, ja niewdzięczna!… Byłżeś kiedy u niego?… Nie mówiłże ci nic… Nie oprowadzał cię?… Wszakże tam, na górze, są ruiny zamku, prawda? Stojąż one jeszcze?

— Tam właśnie, do zamku, stryj co dzień chodził na spacer i całe godziny przesiadywaliśmy z nim na dużym kamieniu…

— Patrzajże?… Znam ten kamień; siedzieliśmy wtedy oboje na nim i patrzyliśmy to na rzekę, to na obłoki, których bieg niepowrotny uczył nas, że tak ucieka szczęście. Czuję to dopiero dzisiaj. A studnia jestże w zamku i zawsze głęboka?

— Bardzo głęboka. Tylko trafić do niej trudno, bo wejście zamaskowały gruzy. Dopiero stryj mi ją pokazał.

— Wieszże ty — mówiła prezesowa — że w chwili ostatniego z nim pożegnania myśleliśmy: czy by się do tej studni nie rzucić? Nikt by nas tam nie odszukał i na wieki zostalibyśmy razem. Zwyczajnie — szalona młodość…

Otarła oczy i ciągnęła dalej:

— Bardzo… bardzo lubiłam go, a myślę, że i on mnie trochę… kiedy tak pamiętał wszystko. Ale on był ubożuchny oficer, a ja na nieszczęście bogata, i do tego jeszcze bliska krewna dwu jenerałów. No i rozdzielono nas… Może też byliśmy zanadto cnotliwi… Ale cicho!… cicho… — dodała śmiejąc się i płacząc. — Takie rzeczy wolno mówić kobietom dopiero w siódmym krzyżyku.

Łkanie przerwało jej mowę. Powąchała swój flakonik, odpoczęła i zaczęła znowu:

— Bywają wielkie zbrodnie na świecie, ale chyba największą jest zabić miłość. Tyle lat upłynęło, prawie pół wieku; wszystko przeszło: majątek, tytuły, młodość, szczęście… Sam tylko żal nie przeszedł i pozostał, mówię ci, taki świeży, jakby to było wczoraj. Ach, gdyby nie wiara, że jest inny świat, w którym podobno wynagrodzą tutejsze krzywdy, kto wie, czy nie przeklęłoby się i życia, i jego konwenansów… Ale ty mnie nie rozumiesz, bo wy dziś macie mocniejsze głowy, lecz zimniejsze aniżeli my serca.

Wokulski siedział ze spuszczonymi oczyma. Coś dławiło go, szarpało za piersi. Wpił sobie paznokcie w ręce i myślał, ażeby jak najprędzej stąd wyjść i już nie słuchać skarg, które odnawiały w nim najboleśniejsze rany.

— A maż on, biedaczysko, jaki nagrobek? — spytała po chwili prezesowa.

Wokulski zarumienił się. Nigdy nie przychodziło mu do głowy, ażeby zmarli potrzebowali czegoś więcej nad grudę ziemi.

— Nie ma — ciągnęła prezesowa widząc jego zakłopotanie. — Nie tobie dziwię się, moje dziecko, żeś o nagrobku nie pamiętał, ale sobie wyrzucam, żem zapomniała o człowieku.

Zadumała się i nagle, położywszy na jego ramieniu swoją wychudłą i drżącą rękę, rzekła zniżonym głosem:

— Mam do ciebie prośbę… Powiedz, że ją spełnisz…

— Z pewnością — odparł Wokulski.

— Pozwól, ażebym ja mu postawiła nagrobek. Ale że sama jechać tam nie mogę, więc ty mnie wyręczysz. Weź stąd kamieniarza, niechaj rozłupie ten kamień, wiesz, ten, na którym siadywaliśmy na górze, pod zamkiem, i niech jedną połowę ustawią na jego grobie. Cokolwiek będzie kosztować, zapłacisz, a zwrócę ci razem z dozgonną wdzięcznością. Zrobiszże to?

— Zrobię.

— To dobrze, dziękuję ci… Myślę, że mu przyjemniej będzie spoczywać pod kamieniem, który słyszał nasze rozmowy i patrzył na łzy. Ach, jak ciężko wspominać… A napis, wieszże jaki?… — mówiła dalej. — Kiedyśmy się rozłączali, zostawił mi parę strofek z Mickiewicza. Pewnie czytałeś je kiedy.


Jak cień tym dłuższy, gdy padnie z daleka,
Tym szerzej koło żałobne roztoczy,
Tak pamięć o mnie: im dalej ucieka,
Tym grubszym kirem twą duszę zamroczy…

O, prawda to!… I studnię, która miała nas połączyć, chciałabym upamiętnić w jakiś sposób…

Wokulski wstrząsnął się i patrzył gdzieś szeroko otwartymi oczyma.

— Co tobie? — zapytała prezesowa.

— Nic — odparł z uśmiechem. — Śmierć zajrzała mi w oczy.

— Nie dziw się: krąży koło mnie starej, zatem muszą ją widzieć moi sąsiedzi. Więc zrobisz, o co cię proszę?

— Tak.

— Bądźże u mnie po świętach i… często przychodź. Może się trochę ponudzisz, ale może i ja, niedołężna, przydam ci się na co. A teraz idź już na dół, idź…

Wokulski pocałował ją w rękę, ona go parę razy w głowę; potem dotknęła dzwonka. Wszedł służący.

— Sprowadźże pana do sali — rzekła.

Wokulski był odurzony. Nie wiedział, którędy idzie, nie zdawał sobie sprawy z tego, o czym rozmawiali z prezesową. Czuł tylko, że znajduje się w jakimś odmęcie dużych komnat, starodawnych portretów, cichych stąpań, nieokreślonej woni. Otaczały go kosztowne meble, ludzie pełni delikatności, o jakiej nigdy nie marzył, a nad tym wszystkim, jak poemat, unosiły się wspomnienia starej arystokratki, przesiąknięte westchnieniami i łzami.

„Cóż to za świat?… Co to za świat?…”

A jednak jeszcze mu czegoś brakło. Chciał choć raz spojrzeć na pannę Izabelę.

„No, w sali ją zobaczy…”

Lokaj otworzył drzwi do sali. Znowu wszystkie głowy zwróciły się w jego stronę i ucichły rozmowy jak szum odlatującego ptactwa. Nastała chwila ciszy, w której wszyscy patrzyli na Wokulskiego, a on nie widział nikogo, tylko rozgorączkowanym spojrzeniem szukał bladoniebieskiej sukni.

„Tu jej nie ma” — pomyślał.

— No, tylko patrzcie, jak on sobie nic z was nie robi!… — szepnął śmiejąc się staruszek z siwymi faworytami.

„Musi być w drugiej sali” — mówił do siebie Wokulski.

Spostrzegł hrabinę i zbliżył się do niej.

— Cóż, skończyliście państwo konferencję? — spytała hrabina. — Prawda, jaka to miła osoba, prezesowa?… Ma pan w niej wielką przyjaciółkę, nie większą jednak aniżeli we mnie. Zaraz przedstawię pana… Pan Wokulski!… — dodała zwracając się do damy w brylantach.

— A ja zaraz przystępuję do interesu — rzekła dama patrząc na niego z góry. — Nasze sierotki potrzebują kilku sztuk płótna…

Hrabina lekko zarumieniła się.

— Tylko kilku?… — powtórzył Wokulski i spojrzał na brylanty wyniosłej damy, reprezentujące wartość kilkuset sztuk najcieńszego płótna. — Po świętach — dodał — będę miał honor na ręce pani hrabiny przysłać płótno…

Ukłonił się, jakby chciał odchodzić.

— Chcesz nas pan pożegnać? — spytała trochę zmieszana hrabina.

— Ależ to impertynent! — rzekła dama w brylantach do swej towarzyszki w strusim piórze.

— Żegnam panią hrabinę i dziękuję za zaszczyt, jaki mi pani raczyła wyrządzić!… — mówił Wokulski całując gospodynię w rękę.

— Tylko do widzenia, panie Wokulski, wszak prawda?… Dużo będziemy mieli interesów ze sobą.

I w drugim salonie nie było panny Izabeli. Wokulski uczuł niepokój.

„Przecież muszę na nią spojrzeć… Kto wie, jak prędko spotkamy się w podobnych warunkach…”

— A, jesteś pan — zawołał książę. — Już wiem, jaki ułożyliście spisek z panem Łęckim. Spółka do handlu ze Wschodem — wyborna myśl! Musicie i mnie do niej przyjąć… Musimy poznać się bliżej… — A widząc, że Wokulski milczy, dodał: — Prawda, jakim ja nudny, panie Wokulski? Ale to nic nie pomoże; musicie zbliżyć się do nas, pan i panu podobni i — razem idźmy. Wasze firmy są także herbami, nasze herby są także firmami, które gwarantują rzetelność w prowadzeniu interesów…

Ściskali się za ręce i Wokulski coś odpowiedział, ale co?… — nie było mu wiadome. Niepokój jego wzrastał; na próżno szukał panny Izabeli.

— Chyba jest dalej — szepnął z trwogą, idąc do ostatniego salonu.

Tu pochwycił go pan Łęcki z oznakami niebywałej tkliwości.

— Już pan wychodzisz? Więc do widzenia, drogi panie. Po świętach u mnie pierwsza sesja i w imię boże zaczynajmy.

„Nie ma jej!” — myślał Wokulski żegnając się z panem Tomaszem.

— Ale wiesz pan — szepnął Łęcki — zrobiłeś szalony efekt. Hrabina nie posiada się z radości, książę mówi tylko o tobie… A jeszcze ten wypadek z prezesową… No… cudownie!… Nie można było marzyć o zdobyciu lepszej pozycji…

Wokulski stał już w progu. Jeszcze raz szklanymi oczyma powiódł po sali i — wyszedł z desperacją w sercu.

„Może wypadałoby wrócić i pożegnać ją?… Przecież zastępowała miejsce gospodyni…” — myślał, powoli schodząc ze schodów.

Nagle drgnął słysząc szelest sukni w wielkiej galerii.

„Ona…”

Podniósł głowę i zahaczył damę w brylantach.

Ktoś podał mu palto. Wokulski wyszedł na ulicę zatoczywszy się jak pijany.

„Cóż mi po świetnej pozycji, jeżeli jej tam nie ma?”

— Konie pana Wokulskiego! — zawołał z sieni szwajcar, pobożnie ściskając trzyrublówkę. Łzami zaszłe oczy i nieco zachrypnięty głos świadczyły, że obywatel ten nawet na trudnym posterunku czci jednak pierwszy dzień Wielkiejnocy.

— Konie pana Wokulskiego!… Konie Wokulskiego!… Wokulski, zajeżdżaj!… — powtórzyli stojący furmani.

Środkiem Alei z wolna toczyły się dwa szeregi dorożek i powozów w stronę Belwederu i od Belwederu. Ktoś z jadących spostrzegł na chodniku Wokulskiego i ukłonił mu się.

„Kolega!” — szepnął Wokulski i zarumienił się.

Gdy sprowadzono mu powóz, zrazu chciał wsiąść, lecz rozmyślił się.

— Wracaj, bracie, do domu — rzekł do furmana dając mu na piwo.

Powóz odjechał ku miastu. Wokulski zmieszał się z przechodniami i poszedł w stronę Ujazdowskiego placu. Szedł z wolna i przypatrywał się jadącym. Wielu spomiędzy nich znał osobiście. Oto rymarz, który dostarcza mu wyrobów skórzanych, jedzie na spacer z żoną, grubą jak beczka cukru, i wcale ładną córką, z którą chciano go swatać. Oto syn rzeźnika, który do sklepu, niegdyś Hopfera, dostarczał wędlin. Oto bogaty cieśla z liczną rodziną. Wdowa po dystylatorze, również mająca duży majątek i również gotowa oddać rękę Wokulskiemu. Tu garbarz, tam dwaj subiekci bławatni, dalej krawiec męski, mularz, jubiler, piekarz — a oto — jego współzawodnik, kupiec galanteryjny, w zwykłej dorożce.

Większa ich część nie widziała Wokulskiego, niektórzy jednak spostrzegli go i kłaniali mu się; lecz byli i tacy, którzy spostrzegłszy go nie kłaniali się, a nawet uśmiechali się złośliwie. Z całego mnóstwa tych kupców, przemysłowców i rzemieślników, równych mu stanowiskiem, niekiedy bogatszych od niego i dawniej znanych w Warszawie, on tylko jeden był dziś na święconym u hrabiny. Żaden z tamtych, on tylko jeden!…

„Mam nieprawdopodobne szczęście — myślał. — W pół roku zrobiłem majątek krociowy, za parę lat mogę mieć milion… Nawet prędzej… Dziś już mam wstęp na salony, a za rok?… Niektórym z tych, co przed chwilą ocierali się o mnie, przed siedemnastoma laty mogłem usługiwać w sklepie, a nie usługiwałem chyba dlatego, że żaden nie wstąpiłby tam. Z komórki przy sklepie do buduaru hrabiny, co za skok!… Czy aby ja nie za prędko awansuję?” — dodał z tajemną trwogą w sercu.

Był już na rozległym placu Ujazdowskim, w którego południowej części znajdowały się zabawy ludowe. Pomieszane dźwięki katarynek, odgłosy trąb i zgiełk kilkunastutysiącznego tłumu ogarniał go jak fala nadpływającej powodzi. Widział jak na dłoni długi szereg huśtawek, kołyszących się w prawo i w lewo niby ogromne wahadła o potężnym rozmachu. Potem drugi szereg — szybko kręcących się namiotów, z dachami w różnokolorowe pasy. Potem trzeci szereg — bud zielonych, czerwonych i żółtych, gdzie przy wejściu jaśniały potworne malowidła, a na dachu ukazywali się jaskrawo odziani pajace albo olbrzymie lalki. A we środku placu — dwa wysokie słupy, na które teraz właśnie wspinali się amatorowie frakowych garniturów i kilkurublowych zegarków.

Wśród tych wszystkich czasowych a brudnych budynków roił się rozbawiony tłum.

Wokulskiemu przypomniały się lata dziecinne. Jakże mu wtedy, wygłodzonemu, smakowała bułka i serdelek! Jak wyobrażał sobie siadłszy na konia w karuzeli, że jest wielkim wojownikiem! Jak szalonego doznawał upojenia wylatując do góry na huśtawce! Co to była za rozkosz pomyśleć, że dziś nic nie robi i jutro nic nie będzie robił — za cały rok. A z czym da się porównać ta pewność, że dziś położy się spać o dziesiątej i jutro, gdyby chciał, wstanie także o dziesiątej przeleżawszy dwanaście godzin z rzędu!

„I to ja byłem, ja?… — mówił do siebie zdumiony. — Mnie tak cieszyły rzeczy, które w tej chwili tylko wstręt budzą?… Tyle tysięcy otacza mnie rozradowanych biedaków, a ja, bogacz przy nich, cóż mam?… Niepokój i nudy, nudy i niepokój… Właśnie kiedy mógłbym posiadać to, co kiedyś było moim marzeniem, nie mam nic, bo dawne pragnienia wygasły. A tak wierzyłem w swoje wyjątkowe szczęście!…”

W tej chwili potężny krzyk wydarł się z tłumu. Wokulski ocknął się i na szczycie słupa zobaczył jakąś ludzką figurę.

„Aha, triumfator!” — rzekł do siebie Wokulski, ledwie trzymając się na nogach pod naciskiem tłumu, który biegł, klaskał, wiwatował, wskazywał palcami bohatera, pytał o jego nazwisko. Zdawało się, że zdobywcę frakowego garnituru na rękach zaniosą do miasta, wtem — zapał ostygł. Ludzie biegli wolniej, nawet zatrzymywali się, okrzyki cichły, wreszcie zupełnie umilkły. Chwilowy triumfator zsunął się ze szczytu i w parę minut zapomniano o nim.

„Przestroga dla mnie…” — szepnął Wokulski ocierając pot z czoła.

Plac i rozbawione tłumy obmierzły mu do reszty. Zawrócił do miasta.

Środkiem Alei wciąż toczyły się dorożki i powozy. W jednym Wokulski zobaczył bladoniebieską suknię.

„Panna Izabela?…”

Serce poczęło mu bić gwałtownie.

„Nie, nie ona.”

O paręset kroków dalej spostrzegł jakąś piękną twarz kobiecą i dystyngowane ruchy.

„Ona?… Nie. Skądże by wreszcie ona?”

I tak szedł przez całe Aleje, plac Aleksandra, przez Nowy Świat, ciągle upatrując kogoś i ciągle doznając zawodu.

„Więc to jest moje szczęście? — myślał. — Nie pragnę tego, co mógłbym mieć, a szarpię się za tym, czego nie mam. Więc to jest szczęście?… Kto wie, czy śmierć jest takim złem, jak wyobrażają sobie ludzie.”

I pierwszy raz uczuł tęsknotę do twardego, nieprzespanego snu, którego nie niepokoiłyby żadne pragnienia, nawet żadne nadzieje.

W tym samym czasie panna Izabela, wróciwszy od ciotki do domu, prawie z przedpokoju zawołała do panny Florentyny:

— Wiesz?… był na przyjęciu!…

— Kto?

— No ten, Wokulski…

— Dlaczegóż być nie miał, skoro go zaproszono — odparła panna Florentyna.

— Ależ to zuchwalstwo… Ależ to niesłychane!… i jeszcze, wyobraź sobie, ciotka jest nim oczarowana, książę nieledwie mu się narzuca, a wszyscy chórem uważają go za jakąś znakomitość… I ty nic na to?…

Panna Florentyna uśmiechnęła się smutnie.

— Znam to. Bohater sezonu. W zimie był takim pan Kazimierz, a przed kilkunastu laty nawet… ja — dodała cicho.

— Ależ uważaj, kim on jest?… Kupiec… kupiec!…

— Moja Belu — odpowiedziała panna Florentyna — pamiętam sezony, kiedy nasz świat zachwycał się nawet cyrkowcami. Przejdzie i to.

— Boję się tego człowieka — szepnęła panna Izabela.



X. Pamiętnik starego subiekta

…Mamy tedy nowy sklep: pięć okien frontu, dwa magazyny, siedmiu subiektów i szwajcara we drzwiach. Mamy jeszcze powóz błyszczący jak świeżo wyglancowane buty, parę kasztanowatych koni, furmana i lokaja — w liberii. I to wszystko spadło na nas w początkach maja, kiedy Anglia, Austria, a nawet skołatana Turcja uzbrajały się na łeb, na szyję!

— Kochany Stasiu — mówiłem do Wokulskiego — wszyscy kupcy śmieją się, że tak dużo wydajemy w niepewnych czasach.

— Kochany Ignasiu — odpowiedział mi Wokulski — a my śmiać się będziemy ze wszystkich kupców, kiedy nadejdą czasy pewniejsze. Dziś właśnie jest pora do robienia interesów.

— Ależ europejska wojna — mówię — wisi na włosku. W takim razie na pewno czeka nas bankructwo.

— Żartuj z wojny — odpowiada Staś. — Cały ten hałas uspokoi się za parę miesięcy, a my tymczasem zdystansujemy wszystkich współzawodników.

— No — i wojny nie ma. W naszym sklepie ruch jak na odpuście, do naszych składów zwożą i wywożą towary jak do młyna, a pieniądze płyną do kas nie gorzej od plew. Kto by Stasia nie znał, powiedziałby, że to genialny kupiec; ale że ja go znam, więc coraz częściej pytam się: na co to wszystko?… Warum hast du denn das getan?…

Prawda, że i mnie się w podobny sposób pytano. Czyżbym już był tak stary jak nieboszczka Grossmutter i nie rozumiał ani ducha czasu, ani intencyj ludzi młodszych ode mnie?… Ehe! tak źle nie jest…

Pamiętam, że kiedy Ludwik Napoleon (późniejszy cesarz Napoleon III) uciekł z więzienia w roku 1846, zakotłowało się w całej Europie. Nikt nie wiedział, co będzie? Ale wszyscy ludzie rozsądni przygotowywali się do czegoś, a wuj Raczek (pan Raczek ożenił się z moją ciotką) ciągle powtarzał:

— Mówiłem, że Bonapart wypłynie i piwa im nawarzy! Cała bieda w tym, że ja coś nie zdużam na nogi.

Rok 1846 i 1847 upłynęły w wielkim rozgardiaszu. Ukazywały się coraz to jakieś pisemka, a znikali ludzie. Nieraz i ja myślałem: czy już nie pora wytknąć głowę na szerszy świat? A kiedy mnie ogarnęły wątpliwości i niepokoje, po zamknięciu sklepu szedłem do wuja Raczka i opowiadałem, co mnie trapi, prosząc, ażeby poradził mi jak ojciec.

— Wiesz co — odpowiadał wuj uderzając się pięścią w chore kolano — poradzę ci jak ojciec. Chcesz, mówię ci… to idź, a nie chcesz, mówię ci… to zostań…

Dopiero w lutym roku 1848, kiedy Ludwik Napoleon już był w Paryżu, ukazał mi się jednej nocy nieboszczyk ojciec, tak jak widziałem go w trumnie. Surdut zapięty pod szyję, kolczyk w uchu, wąs wyszwarcowany (zrobił mu to pan Domański, ażeby ojciec byle jako nie wystąpił na boskim sądzie). Stanął we drzwiach mojej izdebki we front i rzekł tylko te słowa:

— Pamiętaj, wisusie, czegom cię uczył!…

Sen mara — Bóg wiara, myślałem przez kilka dni. Ale już sklep mi obrzydł. Nawet do śp. Małgosi Pfeifer straciłem skłonność i ciasno zrobiło mi się na Podwalu tak, żem nie mógł wytrzymać. Poszedłem znowu do wuja Raczka po radę.

Pamiętam, leżał akurat w łóżku nakryty pierzyną mojej ciotki i pił gorące ziółka na poty. Gdy mu zaś opowiedziałem cały interes, rzekł:

— Wiesz co, poradzę ci jak ojciec. Chcesz — idź, nie chcesz — zostań. Ale ja, gdyby nie podłe moje nogi, dawno bym już był za granicą. Bo i twoja ciotka, mówię ci — tu zniżył głos — tak okrutnie miele jęzorem, że wolałbym, mówię ci, słuchać baterii austriackich armat aniżeli jej trajkotu. Co mi pomoże smarowaniem, to mi zepsuje gadaniem… A maszże pieniądze? — spytał po chwili.

— Znajdę z kilkaset złotych.

Wuj Raczek kazał zamknąć drzwi mieszkania (ciotki w domu nie było) i sięgnąwszy pod poduszkę wydobył stamtąd klucz.

— Naści — rzekł — otwórz ten kufer skórą obity. Będzie tam na prawo skrzyneczka, a w niej kieska. Podaj mi ją…

Wydobyłem kieskę grubą i ciężką. Wuj Raczek wziął ją do ręki i wzdychając odliczył piętnaście półimperiałów.

— Weź te pieniądze — mówił — na drogę i jeżeli masz jechać, to jedź… Dałbym ci więcej, ale może i na mnie przyjść pora… Zresztą trzeba zostawić coś babie, żeby sobie w razie wypadku znalazła drugiego męża…

Pożegnaliśmy się płacząc. Wuj aż dźwignął się na łóżku i odwróciwszy mnie twarzą do świecy, szepnął:

— Niech ci się jeszcze przypatrzę… Bo to, mówię ci, z tego balu nie każdy wraca… Wreszcie i ja sam jużem człek niedzisiejszy, a humory, mówię ci, zabijają prawie tak jak kule…

Wróciwszy do sklepu, mimo spóźnionej pory, rozmówiłem się z Janem Minclem dziękując mu za obowiązek i opiekę. Ponieważ od roku już gadaliśmy o tych rzeczach, a on zawsze zachęcał mnie, ażebym szedł bić Niemców, więc zdawało mi się, że mój zamiar zrobi mu wielką przyjemność. Tymczasem Mincel jakoś posmutniał. Na drugi dzień wypłacił mi pieniądze, które miałem u niego, dał nawet gratyfikację, obiecał opiekować się pościelą i kufrem, na wypadek gdybym kiedy wrócił. Ale zwykła wojowniczość opuściła go i ani razu nie powtórzył swego ulubionego wykrzyknika:

— Ehej!… dałbym ja Szwabom, żebym tak nie miał sklepu…

Gdy zaś około dziesiątej wieczór, ubrany w półkożuszek i grube buty, uściskawszy go wziąłem za klamkę, ażeby opuścić izbę, w której tyle lat przemieszkaliśmy razem, coś dziwnego stało się z Janem. Nagle zerwał się z krzesła i rozkrzyżowawszy ręce krzyknął:

— Świnia!… gdzie ty idziesz?…

A potem rzucił się na moje łóżko szlochając jak dzieciak.

Uciekłem. W sieni słabo oświetlonej olejnym kagankiem ktoś zastąpił mi drogę. Ażem drgnął. Był to August Katz, odziany jak wypadało na marcową podróż.

— Co ty tu robisz, Auguście? — spytałem.

— Czekam na ciebie.

Myślałem, że chce mnie odprowadzić; więc poszliśmy na plac Grzybowski w milczeniu, bo Katz nigdy nic nie mówił. Fura żydowska, którą miałem jechać, była już gotowa. Ucałowałem Katza, on mnie także. Wsiadłem… on za mną…

— Jedziemy razem — rzekł.

A potem, kiedy byliśmy już za Miłosną, dodał:

— Twardo i trzęsie, spać nie można.

Wspólna podróż trwała niespodziewanie długo, bo aż do października 1849 roku, pamiętasz, Katz, niezapomniany przyjacielu? Pamiętasz te długie marsze na spiekocie, kiedy nieraz piliśmy wodę z kałuży; albo ten pochód przez bagno, w którym zamoczyliśmy ładunki; albo te noclegi w lasach i na polach, kiedy jeden drugiemu spychał głowę z tornistra i ukradkiem ściągał płaszcz służący za wspólną kołdrę?… A pamiętasz tarte kartofle ze słoniną, które ugotowaliśmy we czterech w sekrecie przed całym oddziałem? Tylem razy jadał od tej pory kartofle, ale żadne nie smakowały mi tak jak wówczas. Jeszcze dziś czuję ich zapach, ciepło pary buchającej z garnka i widzę ciebie, Katz, jak dla nietracenia czasu mówiłeś pacierz, jadłeś kartofle i zapalałeś fajkę u ogniska.

Ej! Katz, jeżeli w niebie nie ma węgierskiej piechoty i tartych kartofli, niepotrzebnieś się tam pospieszył.

A pamiętasz jeneralną bitwę, do której zawsze wzdychaliśmy odpoczywając po partyzanckiej strzelaninie? Ja bo nawet w grobie jej nie zapomnę, a jeżeli kiedyś zapyta mnie Pan Bóg: po com żył na świecie?… po to — odpowiem — ażeby trafić na jeden taki dzień. Ty tylko rozumiesz mnie, Katz, bośmy to obaj widzieli. A niby na razie wydawało się — nic…

Na półtorej doby przedtem skupiła się nasza brygada pod jakąś wsią węgierską, której nazwy nie pamiętam. Fetowali nas aż miło. W winie, co prawda nieosobliwszym, można się było myć, a wieprzowina i papryka już nam tak zbrzydły, że człowiek nie wziąłby do ust tego paskudztwa, gdyby, rozumie się, miał co innego. A jaka muzyka, a jakie dziewuchy!… Cyganie doskonale grają, a każda Węgierka istny proch. Kręciło się ich, bestyjek, wszystkiego ze dwadzieścia, a jednak zrobiło się tak gorąco, że nasi zakłuli i zarąbali trzech chłopów, a chłopi zabili nam drągami huzara.

I Bóg wie czym skończyłaby się tak pięknie rozpoczęta zabawa, gdyby w chwili największego tumultu nie zajechał do sztabu szlachcic czwórką koni okrytych pianą. W kilka minut później rozeszła się po wojsku wieść, że w pobliżu znajdują się wielkie masy Austriaków. Zatrąbiono do porządku, tumult ucichł, Węgierki znikły, a w szeregach zaczęto szeptać o jeneralnej bitwie.

— Nareszcie!… — powiedziałeś do mnie.

Tej samej nocy posunęliśmy się o milę naprzód, w ciągu następnego dnia znowu o milę. Co kilka godzin, a później nawet co godzinę przelatywały sztafety. Było to dowodem, że w pobliżu znajduje się nasz sztab korpuśny i że zanosi się na coś grubego.

Tej nocy spaliśmy na gołym polu nie stawiając nawet w kozły broni. Zaś skoro świt ruszyliśmy naprzód: szwadron kawalerii z dwoma lekkimi armatami, potem nasz batalion, a potem cała brygada z artylerią i furgonami, mając silne patrole po bokach. Sztafety przylatywały już co pół godziny.

Gdy weszło słońce, zobaczyliśmy przy gościńcu pierwsze ślady nieprzyjaciela; resztki słomy, wytlone ogniska, budynki rozebrane na opał. Następnie coraz częściej zaczęliśmy spotykać uciekających: szlachtę z rodzinami, duchownych rozmaitych wyznań, w końcu — chłopów i Cyganów. Na wszystkich twarzach malowała się trwoga; prawie każdy coś wykrzykiwał po węgiersku, wskazując rękoma za siebie.

Była blisko siódma, kiedy w stronie południowo–zachodniej huknął strzał armatni. Po szeregach przeleciał szmer:

— Oho! zaczyna się…

— Nie, to sygnał…

Padły znowu dwa strzały i znowu dwa. Jadący przed nami szwadron zatrzymał się; dwie armaty i dwa jaszczyki galopem popędziły naprzód, kilku jezdnych pocwałowało na najbliższe wzgórza. Stanęliśmy — i przez chwilę zaległa taka cisza, że słychać było tętent siwej klaczy dopędzającego nas adiutanta. Przeleciała mimo, do huzarów, dysząc i prawie dotykając brzuchem ziemi.

Tym razem odezwało się bliżej i dalej kilkanaście armat; każdy strzał można było odróżnić.

— Macają dystans! — odezwał się stary nasz major.

— Jest z piętnaście armat — mruknął Katz, który w podobnych chwilach stawał się rozmowniejszy. — A że my ciągniemy dwanaście, toż będzie bal!…

Major odwrócił się do nas na koniu i uśmiechnął się pod szpakowatym wąsem. Zrozumiałem, co to znaczy, usłyszawszy całą gamę strzałów, jakby kto zagrał na organach.

— Jest więcej niż dwadzieścia — rzekłem do Katza.

— Osły!… — zaśmiał się kapitan i podciął swego konia.

Staliśmy na wzniesionym miejscu, skąd widać było idącą za nami brygadę. Zaznaczał ją rudy obłok kurzu, ciągnący się wzdłuż gościńca ze dwie albo i trzy wiorsty.

— Straszna masa wojsk! — szepnąłem. — Gdzie się to pomieści!…

Odezwały się trąbki i nasz batalion rozłamał się na cztery kompanie uszykowane kolumnami obok siebie. Pierwsze plutony wysunęły się naprzód, my zostaliśmy w tyle. Odwróciłem głowę i zobaczyłem, że od głównego korpusu oddzieliły się jeszcze dwa bataliony; zeszły z gościńca i biegły pędem przez pola, jeden na prawo od nas, drugi na lewo. W mały kwadrans zrównały się z nami, przez drugi kwadrans wypoczęły i — ruszyliśmy trzema batalionami naprzód, noga za nogą.

Tymczasem kanonada wzmogła się tak, że było słychać po dwa i po trzy strzały wybuchające jednocześnie. Co gorsze, spoza nich rozlegał się jakiś stłumiony odgłos, podobny do ciągłego grzmotu.

— Ile armat, kamracie? — spytałem po niemiecku idącego za mną podoficera.

— Chyba ze sto — odparł kręcąc głową. — Ale — dodał — porządnie prowadzą interes, bo odezwały się wszystkie razem.

Zepchnięto nas z gościńca, którym w kilka minut później przejechały wolnym kłusem dwa szwadrony huzarów i cztery armaty z należącymi do nich jaszczykami. Idący ze mną w szeregu poczęli żegnać się: „W imię Ojca i Syna…” — Ten i ów popił z manierki.

Na lewo od nas huk wzmagał się: pojedynczych strzałów już nie można było odróżnić. Nagle krzyknięto w przednich szeregach:

— Piechota!… piechota!…

Machinalnie schwyciłem karabin na tuj myśląc, że pokazali się Austriacy. Ale przed nami oprócz wzgórza i rzadkich krzaków nie było nic. Natomiast na tle grzmotu armat, który prawie przestał nas interesować, usłyszałem jakiś trzask podobny do rzęsistego deszczu, tylko o wiele potężniejszy.

— Bitwa!… — zawołał ktoś na froncie przeciągłym głosem.

Uczułem, że mi na chwilę serce bić przestało, nie ze strachu, ale jakby w odpowiedzi na ten wyraz, który od dzieciństwa robił na mnie dziwne wrażenie.

W szeregach pomimo marszu zrobił się ruch. Częstowano się winem, oglądano broń, mówiono, że najdalej za pół godziny wejdziemy w ogień, a nade wszystko — w grubiański sposób żartowano z Austriaków, którym nie wiodło się w tych czasach. Ktoś zaczął gwizdać, inny nucił półgłosem; stopniała nawet sztywna powaga oficerów zamieniając się w koleżeńską zażyłość. Trzeba było dopiero komendy: „Baczność i cisza!…”, ażeby nas uspokoić.

Umilkliśmy i wyrównały się nieco pogięte szeregi. Niebo było czyste, ledwie tu i ówdzie bielił się nieruchomy obłok; na krzakach, które mijaliśmy, nie poruszał się żaden listek; nad polem, zarośniętym młodą trawą, nie odzywał się wystraszony skowronek. Słychać było tylko ciężkie stąpanie batalionu, szybki oddech ludzi, czasem szczęk uderzonych o siebie karabinów albo donośny głos majora, który jadąc przodem, odzywał się do oficerów. A tam, na lewo, wściekały się stada armat i lał deszcz karabinowych strzałów. Kto takiej burzy przy jasnym niebie nie słyszał, bracie Katz, ten nie zna się na muzyce!… Pamiętasz, jak nam wówczas dziwnie było na sercu?… Nie strach, ale tak coś jakby żal i ciekawość…

Skrzydłowe bataliony oddalały się od nas coraz bardziej; wreszcie prawy zniknął za wzgórzami, a lewy o paręset sążni od nas dał nurka w szeroki parów i tylko kiedy niekiedy błysnęła fala jego bagnetów. Podzieli się gdzieś huzarzy i armaty, i ciągnąca z tyłu rezerwa, i został sam nasz batalion, schodzący z jednego wzgórza, ażeby wejść na drugie, jeszcze wyższe. Tylko od czasu do czasu z frontu, od tyłu albo z boków przyleciał jakiś jeździec z kartką albo z ustnym poleceniem od majora. Prawdziwy cud, że od tylu poleceń nie zamąciło mu się we łbie!

Nareszcie, już była blisko dziewiąta, weszliśmy na ostatnią wyniosłość porosłą gęstymi krzakami. Nowa komenda; plutony idące jeden za drugim poczęły stawać obok siebie. Gdy zaś dosięgliśmy szczytu wzgórza, kazano nam pochylić się i zniżyć broń, a w końcu przyklęknąć. Wtedy (pamiętasz, Katz?) Kratochwil, który klęczał przed nami, wetknął głowę między dwie młode sosenki i szepnął:

— Patrzajcie no!…

Od stóp wzgórza, na południe, aż gdzieś do krawędzi horyzontu, ciągnęła się równina, a na niej jakby rzeka białego dymu, szeroka na kilkaset kroków, długa — czy ja wiem — może na milę drogi.

— Tyralierzy!… — rzekł stary podoficer.

Po obu stronach tej dziwnej wody widać było kilka czarnych i kilkanaście białych chmur, kotłujących się przy ziemi.

— To baterie, a tam płoną wsie… — objaśniał podoficer.

Wpatrzywszy się zaś lepiej, można było dojrzeć gdzieniegdzie, również po obu stronach długiej smugi dymu, prostokątne plamy: ciemne po lewej, białe po prawej. Wyglądały one jak wielkie jeże z połyskującymi kolcami.

— To nasze pułki, a to austriackie… — mówił podoficer. — No, no!… — dodał — i sam sztab lepiej nie widzi…

Z tej długiej rzeki dymu dolatywało nas nieustanne trzeszczenie karabinowych strzałów, a w tamtych białych chmurach szalała burza armat.

— Phy! — odezwałeś się wtedy, Katz — i to ma być bitwa?… Miałem się też czego bać…

— Zaczekaj no — mruknął podoficer.

— Przygotuj broń!… — rozległo się po szeregach.

Klęcząc zaczęliśmy wydobywać i odgryzać patrony. Rozległo się szczękanie stalowych stempli i trzask odciąganych kurków… Podsypaliśmy proch na panewki i znowu cisza.

Naprzeciw nas, może o wiorstę, były dwa pagórki, a między nimi gościniec. Spostrzegłem, że na jego żółtym tle ukazują się jakieś białe znaki, które wkrótce utworzyły białą linię, a potem białą plamę. Jednocześnie z parowu leżącego o kilkaset kroków na lewo od nas wyszli granatowi żołnierze, którzy niebawem sformowali się w granatową kolumnę. W tej chwili na prawo od nas huknął strzał armatni i nad białym oddziałem austriackim ukazał się siwy obłoczek dymu. Parę minut pauzy i znowu strzał, i znowu nad Austriakami obłoczek. Pół minuty — znowu strzał i znowu obłoczek…

— Herr Gott! — Panie Boże! — zawołał stary podoficer — jak nasi strzelają… Bem komenderuje czy diabeł…

Od tej pory szedł z naszej strony strzał za strzałem, aż ziemia drgała, ale biała plama tam, na gościńcu, rosła wciąż. Jednocześnie na przeciwległym wzgórzu błysnął dym i w stronę naszej baterii poleciał warczący granat. Drugi dym… trzeci dym… czwarty…
"""


def najdluzszyFragment(tekst):

    separatory = "[ ,.?!;]"
    polskieZnaki = "ąęćłńóśźż"
    slowa = re.split(separatory, tekst)    
    najdluzszyL = 0
    najdluzszyT = ""
    temp = ""
    
    for slowo in slowa:
        if any(letter in polskieZnaki for letter in slowo.lower()) or slowo not in file :
            if len(temp) > najdluzszyL:
                najdluzszyL = len(temp)
                najdluzszyT = temp.strip()
            temp = ""
        else:            
            temp += slowo + " "
    
    if len(temp) > najdluzszyL:
        najdluzszyT = temp.strip()
    
    return najdluzszyT

longest = najdluzszyFragment(tekst)
print(longest)