import requests
from bs4 import BeautifulSoup as bs
import time

count = 1
while count < 3080:
    response = requests.get("https://xkcd.com/"+str(count))

    src = response.content

    soup = bs(src,features = "html.parser")

    results = []
    for x in soup.find_all('a'):
    
        results.append(x.get('href'))

    image = requests.get(results[27])


    with open('downloaded_image' + str(count) + '.jpg', 'wb') as file:
        file.write(image.content)

    count += 1

    time.sleep(1)







        








