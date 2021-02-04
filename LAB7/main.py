import io
import json
import requests
import PIL
import matplotlib.pyplot as plt

api_url = 'https://api.thecatapi.com/v1/images/search'

response = requests.get(api_url)

assert response.ok

predata = json.loads(response.content)

assert type(predata) == list

data = predata[0]

assert 'url' in data and type(data['url']) == str
assert 'width' in data and type(data['width']) == int
assert 'height' in data and type(data['height']) == int

url = data['url']
width = data['width']
height = data['height']

sub_response = requests.get(url)

assert sub_response.ok

img = PIL.Image.open(io.BytesIO(sub_response.content))

plt.xticks([])
plt.yticks([])
plt.imshow(img)
plt.xlabel(f'{width} x {height}')
plt.show()
