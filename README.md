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
- python flask - latest
- SQLAlchemy - latest
- docker - latest
- Prometheus - latest
- Grafana - latest

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

## Opis wytwarzania oprogramowania: 
## I Sprint
1. Inicjowanie i uruchomienie serwera Flask 
2. Tworzenie routingów do poszczególnych widoków
3. Utworzenie widoku strony głównej oraz szablonów innych widoków przy użyciu Jinja2
4. Dodanie do głównego szablonu panelu nawigacji z biblioteki Bootstrap
5. Stworzenie bazy danych przy wykorzystaniu biblioteki SQLAlchemy
## II Sprint
6. Tworzenie formularzy do przekazywania danych rejestracji/logowania do back-endu
7. Utworzenie modelu Użytkownik 
8. Implementacja logiki tworzenia nowych użytkowników i logowania
9. Dodanie alertów
## III Sprint
10. Utworzenie modelu Post
11. Implementacja mechanizmu tworzenia nowych postów oraz ich wyświetlania
12. Dodanie funkcji usuwania postów
## IV Sprint
13. Utworzenie modelu Komentarz
14. Stworzenie widoków wyświetlania komentarzy
15. Implementacja dodawania komentarzy do postów
16. Dodanie funkcji usuwania komentarzy

## Deployment:
# azure cli - maszyna wirtualna
az vm create \
  --location eastus \
  --resource-group lab1 \
  --name helloKUBE \
  --size Standard_B1ls \
  --image ubuntuLTS \
  --public-ip-sku Standard \
  --admin-username login \
  --admin-password twoje-hasło
 # rozłożenie aplikacji na dockerze
 docker-compose up -d python-application
 docker-compose up -d prometheus
 docker-compose up -d grafana
 docker-compose up -d grafana-dashboards
 # odapalenie aplikacji na adresie publicznym
 ngrok http 5000 - aplikacja python
 ngrok http 9090 - prometheus
 ngrok http 3000 - grafana

