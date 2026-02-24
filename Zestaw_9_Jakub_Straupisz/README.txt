Szanowny Panie Doktorze,

w folderze znajdują się dwa pliki: snake.py i snake.exe.

Snake.py zawiera kod gry snake, a snake.exe to moja próba zbudowania już działającej aplikacji.

=============
Opis snake.py
=============


Sekcje:
1. Stałe
2. INIT
3. Stan gry
4. Przeszkody
5. Owoc
6. Pętla gry
    6a. Zdarzenia
    6b. Ruch węża
    6c. przeszkoda
    6d. owoc
    6e. rysowanie
7. Koniec


1. Stałe

Stałe z GRID dotyczą rozmiaru siatki.
CELL to są piksele na klatkę.
WIDTH i HEIGHT to są faktyczne rozmiary jakie wyświetlają się na ekranie.
KOLORY - zwykły kod rgb określający różne kolory elementów gry.
KIERUNKI - sposoby w jaki wąż się będzie poruszał
GOOD BAD dotyczy owoców
OBSTACLE_COUNT to ilość przeszkód pojawiających się na ekranie podczas gry. Możliwe byłoby, aby po zjedzeniu owocu np. zmieniały położenie.

2. INIT

Inicjalizacja struktur typu pygame, ekran, opis okna i czas gry.

3. Stan gry

Początkowy stan gry, czyli wąż będzie składał się z głowy o danych współrzędnych i będzie szedł w prawo. 
Liczba punktów na początku wynosi 0, a game_over ustawione jest na false.

4. Przeszkody

Losowo ustawiane przeszkody na planszy, niezmienne przez całą grę.

5. Owoc

Losowo wybierane miejsce dla owocu nieznajdujące się w przeszkodzie.
Czas życia owocu to 20, zmiana tego parametru spowodowałaby że gracz będzie miał więcej/mniej czasu na zjedzenie owocu.
Losowo wybierany jest dobry (czerwony) lub zły (niebieski) owoc.

6. Pętla gry

Główna pętla gry, zawierająca najwazniejszą logikę.

Ruch węża określany jest przez direction. Nowa głowa, czyli new_head powstaje poprzez dodanie wartości kierunku do aktualnych współrzędnych głowy.
Wąż zawsze rośnie o jeden segment na początku ruchu (insert).

W kolejnych krokach ogon może zostać np usunięty.

Kolizje:
Sprawdzane jest czy nowa głowa wychodzi poza plansze ub trafia na obstacles.

Owoc:
Każda klatka zmniejsza licznik fruit_timer.

Rysowanie:
Najpierw czyszczona jest plansza. Potem rysowane są przeszkody, segment węża i owoc. 
Następnie po narysowaiu wszystkich elementów wywowaływana funkcja pygame.display.flip(), która aktualizuje ekran.

Koniec:
Po zakończeniu wywowaływane jest pygame.quit(), zamyka moduł pygame.

