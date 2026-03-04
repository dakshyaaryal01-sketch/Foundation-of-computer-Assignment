import urllib.parse

url = "https://example.com/login?user=Asha & password=123"
encoded_url = urllib.parse.quote(url)

print("Encoded URL:", encoded_url)