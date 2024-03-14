from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup

def get_condo_detail(province = 'กุรงเทพ'):
    try:
        encoded_province = parse.quote(province)
        url = "https://www.livinginsider.com/searchword/Condo/all/1" + f'/{encoded_province}.html'
        html_bytes = urlopen(url).read()
        html = html_bytes.decode('utf-8')
        # create a soup with Beautifulsoup using read html
        soup = BeautifulSoup(html, 'html.parser')
        # condo description
        condo_desc_list = soup.find_all('div', {'class' : 'item-desc'})
        for condo_desc in condo_desc_list:
            condo_title = condo_desc.find('p').text.strip()
            print(condo_title)
            

    except UnicodeEncodeError as e:
        raise Exception(f"UnicodeEncodeError: {e}")