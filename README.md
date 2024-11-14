# HTML Code Generator

Program generuje stronę HTML na podstawie artykułu tekstowego, automatycznie strukturyzując treść i dodając obrazy wygenerowane przez DALL-E 3. Wygenerowane grafiki dostęne są tylko przez godzinę od momentu wygenerowania. Program używa OpenAI API oraz biblioteki BeautifulSoup do przetworzenia i wygenerowania finalnej wersji pliku HTML.
Po zakończeniu działania programu, przekształcony artykuł w formacie HTML zostanie zapisany w pliku artykul.html w katalogu głównym.
W katalogu strona znajdują się dwa pliki. Plik szablon.html zawiera sekcję <head> wraz ze stylami. Z kolei plik podglad.html, zawiera również sekcję <body>, do której wstawiono przykładowy artykuł. 

## AI artykuł
Aby uruchomić program, musisz mieć zainstalowane:

1. Python 3.7+: https://www.python.org/downloads/

2. Biblioteki: openai, beautifulsoup4. Można je zainstalować za pomocą polecenia:
```
pip install openai beautifulsoup4
```
3. Klucz API OpenAI. Należy ustawić go jako zmienną środowiskową o nazwie OPENAI_API_KEY.

## Uruchomienie

Uruchom skrypt, korzystając z poniższego polecenia:
```
python main.py
```

