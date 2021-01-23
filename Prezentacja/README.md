# Testowanie C++ przy użyciu Catch2

### Czym jest Catch2?

Nowoczesna, natywna biblioteka do testów jednostkowych w formacie TDD (Test-driven development) lub BDD (Behavior-driven development) z użyciem standardu C++11 oraz wyższych.

#### Zalety

* Możliwość użycia biblioteki jako `header-only`
* Możliwość dzielenia testów na sekcje i podsekcje
* Brak zewnętrznych zależności
* Prostota tworzenia warunków za pomocą makr
* Krótki cykl wydawania nowych wersji
* Darmowa

#### Wady

* Brak możliwości ustawienia breakpointów w testach
* Długie czasy kompilacji przy używaniu biblioteki jako `header-only`
* Testowanie może odbywać się tylko na jednym wątku
* Duża ilość makr
