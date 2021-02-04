import json
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

api_url = 'https://api.thecatapi.com/v1/images/search'

response = requests.get(api_url)

data = json.loads(response.content)

sub_response = requests.get(data[0]['url'])

img = Image.open(BytesIO(sub_response.content))

plt.xticks([])
plt.yticks([])
plt.imshow(img)
plt.show()
