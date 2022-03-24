# Aplikacja NerdSpace

## Założenia projektowe

Celem projektu będzie stworzenie aplikacji webowej, która będzie służyła do wyświetlania wpisów tworzonych przez użytkowników na temat nowinek technologicznych.Użytkownicy po założeniu konta i zalogowaniu się będą w stanie dodawać swoje posty oraz komentować posty innych użytkowników. Dodatkową funkcjonalnością będzie możliwość usunięcia swojego konta z portalu. Wszelkie dane będą przechowywane w bazie Postgres.

## Wymagania funkcjonalne

- Aplikacja będzie posiadać możliwość stworzenia użytkownika jak i możliwość logowania się
do portalu.
- Aplikacja będzie wyświetlać informację udostępnione przez użytkowników na jednym,
wspólnym wallu.
- Udostępnione treści będą zapisywane w bazie danych
- Możliwość dodania komentarza
- Możliwość logowania zdarzeń

## Wymagania niefunkcjonalne
- Aplikacja zostanie postawiona na MS Azure
- Będzie obsługiwana przez komputery z dostępem do internetu
- Baza danych będzie obsługiwana przez Postgres
- Hasła będą szyfrowane/hashowane nie widoczne dla użytkowników.
 
## Wybrane technologie
- html / css
- azure cli
- terraform
- python flask
- SQLAlchemy
- docker
- Prometheus
- Grafana
- Locust

## Środowiska chmurowe
- Aplikacja będzie wystawiona na MS Azure.

## Historyjki użytkownika

- Jako użytkownik chciałbym mieć możliwość utworzenia konta oraz zalogowania się do
portalu.
- Jako użytkownik chciałbym mieć możliwość dodawania treści oraz ich edycji.
- Jako użytkownik miałbym też możliwość komentowania swoich postów oraz postów
innych użytkowników.
