import requests
import send_email as se
api_key = "6a1eb49ed035473b939ab8dab800ce32"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2022-11-21&sortBy=publishedAt&apiKey=" \
      "6a1eb49ed035473b939ab8dab800ce32"

# Make request
request = requests.get(url)


# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
se.send_email(message=body)

