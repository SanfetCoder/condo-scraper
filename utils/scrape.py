from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup

def get_condo_detail(province = 'กุรงเทพ'):
    try:
        condos = []
        encoded_province = parse.quote(province)
        url = "https://www.livinginsider.com/searchword/Condo/all/1" + f'/{encoded_province}.html'
        html_bytes = urlopen(url).read()
        html = html_bytes.decode('utf-8')
        # create a soup with Beautifulsoup using read html
        soup = BeautifulSoup(html, 'html.parser')
        # get condo detail
        condo_list = soup.find_all('div', {'class' : 'istock-list'})
        for condo in condo_list:
            if (type(condo) == dict):
                break
            condo_title = condo.find('p').text.strip()
            condo_image = condo.find_all('img')[1]['src']
            # find the price of current condo
            condo_price = condo.find('div',{'class' : 'listing-cost'}).find('div').text
            serialized_condo = {
                "title" : condo_title,
                "image" : condo_image,
                "price" : condo_price
            }
            condos.append(serialized_condo)
        return condos

    except UnicodeEncodeError as e:
        raise Exception(f"UnicodeEncodeError: {e}")