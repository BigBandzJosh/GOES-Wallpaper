import os
import requests
from bs4 import BeautifulSoup
import ctypes
import winreg
from PIL import Image

# Paths
local_path = os.path.expanduser(r"~\Pictures\goes_canada.jpg")
base_url = "https://cdn.star.nesdis.noaa.gov/GOES19/ABI/SECTOR/can/GEOCOLOR/"

# Get HTML
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(base_url, headers=headers)
response.raise_for_status()

# Parse JPG links
soup = BeautifulSoup(response.text, "html.parser")
jpg_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('9000x4500.jpg')]

if not jpg_links:
    raise Exception("No JPG links found.")

# Latest image
latest_image = sorted(jpg_links)[-1]
image_url = base_url + latest_image
print(f"Downloading latest image: {latest_image}")

# Download
img_data = requests.get(image_url, headers=headers).content
with open(local_path, 'wb') as f:
    f.write(img_data)

img = Image.open(local_path)
taskbar_height = 200

new_img = Image.new("RGB", (img.width, img.height + taskbar_height), (0, 0, 0))
new_img.paste(img, (0, 0))
new_img.save(local_path)


# (This part went a little over my head in terms of how to actually interact with Windows, so AI was used here!)
# Set wallpaper style (Fill)
# Wallpaper style registry keys:
# 2 = Stretch, 6 = Fit, 10 = Fill, 0 = Center, 1 = Tile, 0 = No Tile
with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                    "Control Panel\\Desktop", 0, winreg.KEY_SET_VALUE) as key:
    winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, "10")
    winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, "0")

# Apply wallpaper 
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, local_path, 3)

print("Wallpaper updated!")


