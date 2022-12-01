import requests
from bs4 import BeautifulSoup 

## get url 

url = "https://www.google.com/search?sa=X&rlz=1C1CHZN_frFR981FR981&tbs=lf:1,lf_ui:9&tbm=lcl&sxsrf=ALiCzsbR4FFVB2B0AL6VeA4di12LzkZLIg:1669676062030&q=liste+des+restaurant+paris&rflfq=1&num=10&ved=2ahUKEwiLzcSE_NH7AhUOTKQEHakQCycQjGp6BAgMEAI&biw=1707&bih=849&dpr=1.5#rlfi=hd:;si:;mv:[[48.889880899999994,2.3595919999999997],[48.839120199999996,2.2931399999999997]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u1!2m2!1m1!1e1!1m4!1u1!2m2!1m1!1e2!2m1!1e2!2m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:9"

page = requests.get(url).text


#### get tweet 

soup = BeautifulSoup(page, 'html.parser')


print(type(soup.find('div', {"class" :"rllt__details" }) ))
    
