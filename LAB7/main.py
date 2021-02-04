import json
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

api_url = 'https://api.thecatapi.com/v1/images/search'

response = requests.get(api_url)

assert response.ok

data = json.loads(response.content)[0]
url = data['url']
width = data['width']
height = data['height']

sub_response = requests.get(url)

assert sub_response.ok

img = Image.open(BytesIO(sub_response.content))

plt.xticks([])
plt.yticks([])
plt.imshow(img)
plt.xlabel(f'{width} x {height}')
plt.show()
