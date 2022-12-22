import requests
import send_email as se
api_key = "6a1eb49ed035473b939ab8dab800ce32"

topic = "tesla"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=6a1eb49ed035473b939ab8dab800ce32&" \
      "language=en"

# Make request
request = requests.get(url)


# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] \
               + "\n" + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
se.send_email(message=body)

