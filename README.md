# HTML Code Generator

Aplikacja generuje kod HTML na podstawie artykułu tekstowego, automatycznie strukturyzując treść i dodając obrazy wygenerowane przez DALL-E 3. Wygenerowane grafiki dostępne są tylko przez godzinę od momentu wygenerowania. Program używa OpenAI API oraz biblioteki BeautifulSoup do przetworzenia i wygenerowania finalnej wersji pliku HTML.

## Opis działania

Skrypt przetwarza tekst artykułu z pliku *artykul.txt*, a następnie osadza go w kodzie HTML, generując sekcję `<body>`. Przekształcony artykuł jest zapisywany w pliku *artykul.html* w katalogu głównym. 

W katalogu *strona* znajdują się dwa dodatkowe pliki:

1. **szablon.html**

  Plik zawiera pusty szablon HTML, przygotowany do wizualizacji artykułów. Zawiera w pełni opracowaną sekcję `<head>`, wraz ze stylami CSS. Sekcja `<body>` jest pusta i gotowa do wklejenia kodu przetworzonego artykułu.

2. **podglad.html**

  Plik zawiera pełny podgląd artykułu. Jest to gotowy dokument HTML, w którym sekcja `<body>` zawiera przykładowy artykuł, przetworzony przy pomocy stworzonej aplikacji.

## Wymagania

Do uruchomienia projektu wymagane są następujące narzędzia:

1. **Python**: https://www.python.org/downloads/

2. **Biblioteki**: openai, beautifulsoup4. Można je zainstalować za pomocą polecenia:
```
pip install openai beautifulsoup4
```
3. **Klucz API OpenAI**, ustawiony jako zmienna środowiskowa o nazwie *OPENAI_API_KEY*.

## Uruchomienie

Uruchom skrypt, korzystając z poniższego polecenia:
```
python main.py
```

