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
- html / css - latest
- azure cli - latest
- terraform - latest
- python flask - latest
- SQLAlchemy - latest
- docker - latest
- Prometheus - latest
- Grafana - latest
- Locust - latest
- helm - latest
- kubernetes - latest
- octant - latest

## Wykorzystane IDE
- Pycharm/Visual Studio Code


## Środowiska chmurowe
- Aplikacja będzie wystawiona na MS Azure.

## Historyjki użytkownika

- Jako użytkownik chciałbym mieć możliwość utworzenia konta oraz zalogowania się do
portalu.
- Jako użytkownik chciałbym mieć możliwość dodawania treści oraz ich edycji.
- Jako użytkownik miałbym też możliwość komentowania swoich postów oraz postów
innych użytkowników.

# Część procesowa

## Opis wytwarzania oprogramowania: MATI 

## Deployment:
Aplikacja wystawiana jest na zasobach chmurowych w naszym przypadku Azure. 
Za pomocą Terraform rozstawiamy cluster oraz repozytorium. Używając do tego polecenia „terraform apply”.  Następnie pushujemy nasz obraz z aplikacją. 
Całość odbywa się przy użyciu Azure Cli, poleceń dockera takich jak „docker build” „docker tag” czy też „docker push”. 

Do całości dodane jest również oprogramowanie które loguje procesy oraz ruchy na stronie naszej aplikacji. Sam logging został zaiplementowany na clustrze za pomocą helm chartów. 
Zostały przygotowane templatki wykorzystujące globalne values. Deployment odbywa się za pomocą polecenia „helm upgrade <nazwa namespace> <nazwa repo>”.
Po rozstawieniu wszystkich komponentów, możemy wyświetlić zawartość strony przy pomocy narzędzia o nazwie Octant i uruchomieniu „forward port” z poziomu serwisów. 

