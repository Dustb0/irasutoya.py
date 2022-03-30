from urllib.parse import quote
from bs4 import BeautifulSoup
from requests_html import HTMLSession

class Irasutoya:

  def get_images(term):
    # Run JavaScript code on webpage
    session = HTMLSession()
    resp = session.get('https://www.irasutoya.com/search?q=' + quote(term))    
    resp.html.render()
    
    soup = BeautifulSoup(resp.html.html, "lxml")
    elements = soup.select(".boxim img", limit=10)

    images = []
    for element in elements:
      images.append(element['src'])

    return images