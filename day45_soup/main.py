from bs4 import BeautifulSoup
#import lxml
import requests

def soup_learn_locally():
    with open("day45_soup/website.html") as file:
        contents = file.read()

    soup = BeautifulSoup(contents, 'html.parser')

    #print(soup.title.string)
    #print(soup.prettify())

    #print(soup.li)

    all_anchors = soup.find_all(name="a")
    #print(all_anchors)

    #for tag in all_anchors:
    #    #print(tag.getText())
    #    print(tag.get("href"))
    #
    heading = soup.find(name="h1", id="name")
    print(heading)

    section_heading = soup.find(name="h3", class_="heading")
    print(section_heading.get("class"))

    company_url = soup.select_one(selector="p a")
    print(company_url)

    headings = soup.select(".heading")
    print(headings)

def soup_www():
    response = requests.get("https://news.ycombinator.com/news")
    yc_page = response.text

    soup = BeautifulSoup(yc_page, "html.parser")
    
    #findos kiirasok
    all_hl = soup.find_all(class_="titleline")
    #print(first_hl.text)
    #print(first_hl.find("a").attrs["href"])

    all_scores = soup.find_all(class_= "score")
    #print(all_scores)

    titles = []
    refs = []
    scores = []

    for title in all_hl:
        titles.append(title.text)
        refs.append(title.find("a").attrs["href"])
    
    for score in all_scores:
        scores.append(int(score.text.replace(" points", "").replace(" point", "")))
    
    print(titles)
    print(scores)
    max_score = max(scores)
    print(max_score)
    max_index = scores.index(max_score)

    top_title = titles[max_index]

    print(top_title)


    #selectoros kiiras    
    #headlines = soup.select(".titleline a")
    #for headline in headlines:
    #    print(headline.text)

    #cikklink = soup.select(".titleline a")
    #print(cikklink[0].get("href"))
    #cikklink = soup.select(".subline .score")
    #print(cikklink[0].text)

def chagtpt_soup():

    # Hacker News oldal letöltése
    url = 'https://news.ycombinator.com/news'
    response = requests.get(url)

    # Ellenőrizzük, hogy sikeres volt-e a lekérés
    if response.status_code == 200:
        html_content = response.text
    else:
        print("Hiba történt az oldal letöltésekor.")
        exit()

    # HTML elemzése Beautiful Soup-pal
    soup = BeautifulSoup(html_content, 'html.parser')

    # Az összes cím kikeresése (a címek 'a' tag-ekben vannak, 'titlelink' osztállyal)
    titles = soup.select('.titleline a')

    # A pontszámokat tartalmazó elemek (pontszámok 'span' tag-ekben vannak, 'score' osztállyal)
    scores = soup.select('.score')

    # Összesítés: a pontszámokat és címeket egy tömbbe tesszük
    articles = []

    for i in range(min(len(titles), len(scores))):
        title = titles[i].text
        score_text = scores[i].text
        # Kezeli a "1 point" és "X points" eseteket is
        score = int(score_text.replace(' points', '').replace(' point', ''))
        articles.append({'title': title, 'score': score})

    # A legmagasabb pontszámú cím kiválasztása
    if articles:
        top_article = max(articles, key=lambda x: x['score'])
        print(f"Legmagasabb pontszámú bejegyzés: {top_article['title']} ({top_article['score']} pont)")
    else:
        print("Nem találhatóak bejegyzések.")

soup_www()
#chagtpt_soup()