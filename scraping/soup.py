from bs4 import BeautifulSoup as bs 
import requests 
from db_save import insert_doc



def scarpe_data(url):
    try:
        res_dic = {}
        response = requests.get(url)
        soup = bs(response.content, "html.parser") 
        name = soup.find(attrs={'class':'PublicProfileDetailsCard_displayNameContainer__h1p9r'}).text
        username = soup.find(attrs={'class':'PublicProfileDetailsCard_textWrapper__8JEm_'}).text
        subscribers = soup.find('div', attrs={'data-testid': 'subscribersCountText'}).text
        links = soup.find_all('picture', {'class': 'WebPImage_image__pCgLR ProfilePictureBubble_webPImage__mQi1T'})
        profile_img_link = [i.find('img')['srcset'] for i in links]
        
        res_dic["name"] = name
        res_dic["username"] = username
        res_dic["subscribers"] = subscribers
        res_dic["profile_link"] = profile_img_link[0]
        # print(res_dic)
        val = insert_doc(res_dic)
        # print(val)
        return res_dic
    
    except Exception as ex:
        raise ex




