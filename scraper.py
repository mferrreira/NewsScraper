import requests
from bs4 import BeautifulSoup

def scrape_news():
    news_list = []

    # Lista de URLs das fontes
    sources = [
        {"url": "https://g1.globo.com/", "source_name": "G1"},
        {"url": "https://www.uol.com.br/", "source_name": "UOL"},
        {"url": "https://www.cnnbrasil.com.br/", "source_name": "CNN Brasil"}
    ]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    # Percorre as fontes de notícias e coleta dados
    for source in sources:
        url = source["url"]
        source_name = source["source_name"]
        
        # Faz a requisição HTTP para o site
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ajuste para cada site individualmente
        if source_name == "G1":
            articles = soup.find_all('div', class_='bastian-feed-item')
            for article in articles:
                title_tag = article.find('a', class_='feed-post-link')
                title = title_tag.get_text(strip=True) if title_tag else ''
                description_tag = article.find('p', class_='feed-post-body-resumo')
                description = description_tag.get_text(strip=True) if description_tag else ''
                url = title_tag['href'] if title_tag and 'href' in title_tag.attrs else ''
                image_tag = article.find('img')
                image_url = image_tag['src'] if image_tag else ''

                if title:
                    news_list.append({
                        'title': title,
                        'description': description,
                        'url': url,
                        'image_url': image_url,
                        'source': source_name
                    })

        elif source_name == "UOL":
            articles = soup.find_all('a', class_='hyperlink')  # Ajuste conforme a estrutura

            for article in articles:
                title_tag = article.find('h3', class_='title__element')
                title = title_tag.get_text(strip=True) if title_tag else ''
                description_tag = article.find('p', class_='title__element')
                description = description_tag.get_text(strip=True) if description_tag else ''
                url = article['href'] if title_tag and 'href' in article.attrs else ''
                
                image_tag = article.find('img')
                image_url = image_tag['src'] if image_tag else ''

                if title:
                    news_list.append({
                        'title': title,
                        'description': description,
                        'url': url,
                        'image_url': image_url,
                        'source': source_name
                    })

        elif source_name == "CNN Brasil":
            articles = soup.find_all('a', class_='sidebar--item__link')  # Encontrando os links das notícias
            for article in articles:
                title_tag = article.find('h3', class_='block__news__title sidebar--item__title')  # Encontrando o título
                title = title_tag.get_text(strip=True) if title_tag else ''
                
                # O link já é o URL da notícia
                url = article['href'] if 'href' in article.attrs else ''
                
                # Pegando a imagem
                image_tag = article.find('img', class_='block--sidebar__content__image')  # Procurando a imagem
                image_url = image_tag['src'] if image_tag and 'src' in image_tag.attrs else ''
                
                if title:
                    news_list.append({
                        'title': title,
                        'description': title,  # Descrição não está explícita, mas pode ser o título mesmo
                        'url': url,
                        'image_url': image_url,
                        'source': source_name
                    })

    return news_list
