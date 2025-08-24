# 🧮 Kalkulator Praw Fizyki

Prosty kalkulator konsolowy w języku Python, umożliwiający szybkie obliczenia oparte na fundamentalnych prawach fizyki i elektroniki. Projekt został stworzony w celach edukacyjnych, aby ułatwić zrozumienie i stosowanie podstawowych wzorów naukowych.

## Główne Funkcje

-   **Interaktywne Menu:** Prosty interfejs tekstowy, który prowadzi użytkownika przez dostępne opcje.
-   **Obliczenia w Różne Strony:** Kalkulator potrafi obliczyć każdą zmienną ze wzoru, jeśli podane zostaną pozostałe.
-   **Obsługiwane Prawa:**
    -   ⚡ **Prawo Ohma** ($U = I \cdot R$)
    -   🔥 **Prawo Joule'a** ($Q = I^2 \cdot R \cdot t$)
    -   🏃 **Druga zasada dynamiki Newtona** ($F = m \cdot a$)
    -   🌍 **Prawo powszechnego ciążenia** ($F = G \frac{m_1 m_2}{r^2}$)
-   **Modułowa Budowa:** Kod jest zorganizowany w sposób, który ułatwia dodawanie kolejnych praw i funkcji.



---

## Użyte Technologie

-   **Python 3:** Projekt został napisany w całości w czystym Pythonie.
-   **Brak zewnętrznych bibliotek:** Do uruchomienia programu nie jest wymagana instalacja żadnych dodatkowych pakietów.

---

## Instalacja i Uruchomienie

Aby uruchomić kalkulator lokalnie, postępuj zgodnie z poniższymi krokami.

1.  **Sklonuj repozytorium:**
    ```bash
    git clone [https://github.com/twoja-nazwa-uzytkownika/kalkulator-praw.git](https://github.com/twoja-nazwa-uzytkownika/kalkulator-praw.git)
    ```

2.  **Przejdź do folderu projektu:**
    ```bash
    cd kalkulator-praw
    ```

3.  **Uruchom główny skrypt:**
    ```bash
    python main.py
    ```
    *(Upewnij się, że masz zainstalowany Python 3 na swoim komputerze).*

---

## Jak Używać

Po uruchomieniu programu na ekranie pojawi się menu z listą dostępnych praw do obliczeń.

1.  Wybierz numer prawa, które Cię interesuje, i wciśnij `Enter`.
2.  Program poprosi o podanie znanych wartości. Wartość, którą chcesz obliczyć, pozostaw pustą, wciskając `Enter`.
3.  Kalkulator wyświetli wynik brakującej zmiennej.

## Plany Rozwoju

-   [ ] Dodanie większej liczby praw fizyki (np. Prawo Hooke'a, Prawo Coulomba).
-   [ ] Wprowadzenie obsługi jednostek i ich konwersji.
-   [ ] Stworzenie prostego interfejsu graficznego (GUI) przy użyciu `Tkinter` lub `PyQt`.
-   [ ] Lepsza walidacja danych wejściowych od użytkownika.

## Licencja

Ten projekt jest udostępniony na licencji MIT. Zobacz plik `LICENSE`, aby uzyskać więcej informacji.