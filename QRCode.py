

import segno

url = input("Enter link for making QR Code: ")
video = segno.make('url')
location = input("Enter location where u want QRCode saved: ")
video.save(location, dark='black', light='white', scale=10 )