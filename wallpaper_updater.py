import ctypes
import datetime
from tempfile import NamedTemporaryFile
import requests
from requests.exceptions import RequestException

def get_image(image_url: str) -> bytes:
    try:
        response = requests.get(image_url, timeout=5)
        print("no issues!")
    except RequestException as err:
        print(f"Whoopsie daisy: {err}")
    return response.content

today: datetime.date = datetime.date.today()
year: str = str(today.year)
month_number: str = str(11+today.month)
month_name: str = today.strftime("%B")
background_url: str = \
    f"https://www.kriegs.net/work/{year}/wallpapers/kriegs_{year}_{month_name}_4K_3840x2160_calendar.jpg"

image_data = get_image(background_url)

if image_data is not None:
    with NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
        temp_file.write(image_data)
        temp_file.flush()
        ctypes.windll.user32.SystemParametersInfoW(20, 0, temp_file.name, 0)
