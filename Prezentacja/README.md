# Testowanie C++ przy użyciu Catch2

### Dlaczego warto testować kod?

*Like it or not, all humans are imperfect.* - Erin Martz, MA, CRC; University of Arkansas

Ludzie nie są idealni i z natury popełniają błędy. Nie inaczej jest, gdy mamy na myśli pisanie kodu. Jeśli kod jest niezawodny to znaczy, że nie istnieje ([wyjątek](https://github.com/kelseyhightower/nocode)). Trudno jest nam przewidzieć wszystkie możliwe zastosowania naszego dzieła lub wszystkie możliwe środowiska w jakich będzie używane.
Dlatego ludzie wpadli na pomysł aby testować zawodne oprogramowanie innym, mniej zawodnym, oprogramowaniem. Dzięki dobrze zaaplikowanym testom jesteśmy w stanie wcześniej wykryć potencjalne błędy w naszym kodzie, przez co koszt ich usunięcia będzie tańszy.

### Dlaczego warto użyć zewnętrznej biblioteki?

*Własnoręczne testowanie kodu może być zabawne... ale tylko pierwszy raz.* - Phil Nash; CppCon 2018

O ile przy pisaniu drobnej funkcjonalności lub małego programu mozemu pozwolić sobie na ręczne napisanie testu, wstawienia instrukcji warunkowej czy assercji, to jednak przy projektach większego kalibru mamy zazwyczaj do czynienia z większą złożonością kodu, co przekłada się na jego potencjalnie większą zawodność. W prostych słowach - im wiecej kodu tym trudniej go samemu ogarnąć, a pisanie do każdej sytuacji własnego testu jest pracochłonne i zazwyczaj nieopłacalne.
Jeśli dodatkowo zaczniemy sami pisać podręczną bibliotekę do testowania, skończymy na tym, że zamiast zajmować się właściwym projektem zaczęliśmy pisać własną bibliotekę do testowania.
W takiej sytuacji lepiej skorzystać z gotowego rozwiązania, które zostało przetestowane przez szerokie grono użytkowników i zapewne jest lepsze niż to co my byśmy kiedykolwiek napisali.

### Czym jest Catch2?

Nowoczesna, natywna biblioteka do testów jednostkowych w formacie TDD (Test-driven development) lub BDD (Behavior-driven development) z użyciem standardu C++11 (oraz wyższych).

#### Zalety

* Możliwość użycia biblioteki jako *header-only*
* Możliwość dzielenia testów na sekcje i podsekcje
* Brak zewnętrznych zależności
* Prostota tworzenia warunków za pomocą makr
* Krótki cykl wydawania nowych wersji
* Darmowa

#### Wady

* Brak możliwości ustawienia breakpointów w testach
* Długie czasy kompilacji przy używaniu biblioteki jako *header-only*
* Testowanie może odbywać się tylko na jednym wątku
* Duża ilość makr

### Coś więcej niż testy jednostkowe?

Tak, dokumentacja.

Dobrze przygotowana dokumentacja pozwala uchronić użytkownika przed niewłaściwym zostasowaniem kodu (o ile ją w ogóle przeczyta...) oraz w razie znalezienia błędu - łatwiejsze jego wytropienie. Już jedna linijka dokumentacji ogólnikowo opisująca daną funkcjonalność pozwala na lepsze zrozumienie używanego oprogramowania.

### Code Coverage?

W wielkim skrócie opisuje w jakim stopniu kod źródłowy programu jest wykonywany przy testowaniu. Wyższe wartości oznaczają większą ilość przetestowane kodu, co za tym idzie - większą szansę na wykrycie potencjalnych błędów. Nie oznaczna to jednak, że 100% code coverage zapewnia, że oprogramowanie jest niezawodne. Tak samo wartości rzędu 50% nie oznaczają zabugowanej aplikacji. Powinniśmy jednak dbać o to aby dodawanie nowych funkcjonalności, a co za tym idzie nowych testów, nie zmniejszało wartości naszego pokrycia kodu.

### Przykład

Plik [tests.cpp](tests.cpp) zawiera przykładowe zastosowanie testów jednostkowych z użyciem bibliteki Catch2.
Można go skompilować prostym poleceniem (używając g++ lub clang++):

```
g++ -o tests tests.cpp && ./tests
clang++ -o tests tests.cpp && ./tests
```
