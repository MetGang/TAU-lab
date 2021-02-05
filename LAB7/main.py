import io
import json
import requests
import PIL
import matplotlib.pyplot as plt

# Url do API
api_url = 'https://api.thecatapi.com/v1/images/search'

# Wykonanie głównego zapytania
response = requests.get(api_url)

# Walidacja głównego zapytania
assert response.ok

# Deserializacja wyniku zapytania
predata = json.loads(response.content)

# Walidacja całościowego wyniku zapytania
assert type(predata) == list

# Pozyskanie właściwych danych
data = predata[0]

# Walidacja właściwych danych
assert 'url' in data and type(data['url']) == str
assert 'width' in data and type(data['width']) == int
assert 'height' in data and type(data['height']) == int

# Pozyskanie danych ze słownika
url = data['url']
width = data['width']
height = data['height']

# Wykonanie drugiego zapytania
sub_response = requests.get(url)

# Walidacja drugiego zapytania
assert sub_response.ok

# Deserializacja wyniku zapytania do postaci obrazka
img = PIL.Image.open(io.BytesIO(sub_response.content))

# Wyświetlenie ostatecznego obrazka
plt.xticks([])
plt.yticks([])
plt.imshow(img)
plt.xlabel(f'{width} x {height}')
plt.show()
