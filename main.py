import os
import openai
from bs4 import BeautifulSoup

openai.api_key = os.getenv("OPENAI_API_KEY")

# Funkcja do wczytania artykułu z pliku tekstowego
def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Funkcja do zapisania wynikowego kodu HTML do pliku
def save_html(content, file_path="artykul.html"):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def generate_dalle_image(description):
    response = openai.images.generate(
        model="dall-e-3",
        prompt=description,
        n=1,
        quality = "standard",
        size="1792x1024"
    )
    image_url = response.data[0].url
    return image_url

# Funkcja do wysłania zapytań do API OpenAI
def generate_html_content(article_content):
    prompt = (
        "Przekształć poniższy artykuł uwzględnijąc odpowiednie tagi do strukturyzacji treści HTML. "
        "Każdy akapit powienien mieścić się w tagach '<p>', pierwszy nagłówek w '<h1>', a kolejne w '<h2>' "
        "Po pierwszym nagłówku ('<h1>') umieść '<hr>', aby utworzyć linię. "
        "Dodaj tagi '<img>' w miejscach, gdzie warto dodać grafiki, z atrybutem 'src='image_placeholder.jpg''. "
        "Rozbudowany opis tego to znajdzie się na zdjęciu, umieść w atrybucie 'alt', a w tagu '<figcaption>' wstaw krótki podpis pod obrazkiem. "
        "Treść artykułu po <hr> umieść w kontenerze <div>."
        "\nArtykuł:\n" + article_content
    )

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tworzysz zawartość stron internetowych. "
                                          "Twoim zadaniem jest zwrócenie zawartości, która znajdzie się pomiedzy znacznikami <body> i </body> w kodzie HTML."
                                          "Nie używaj, więc <head> ani <body> oraz nie dodawaj innej niepotrzebnej treści."
                                          "Zawartość atrybutu 'alt' posłuży do wygenerowania za pomocą DALL-E grafik, powinien więc byc szczegółowy i przejrzysty."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2048,
        temperature=0.7
    )

    html_content = response.choices[0].message.content
    soup = BeautifulSoup(html_content, 'html.parser')
    images = soup.find_all('img', src='image_placeholder.jpg')

    for img_tag in images:
        alt_text = img_tag['alt']
        image_url = generate_dalle_image(alt_text)
        img_tag['src'] = image_url

    return str(soup)

def main():
    file_path = "artykul.txt"
    article_content = read_article(file_path)
    html_content = generate_html_content(article_content)
    save_html(html_content)
    print("HTML został zapisany w pliku artykul.html")

if __name__ == "__main__":
    main()
