
import requests
from bs4 import BeautifulSoup
import csv
import time


def fetch_page(url):
    """Fetch HTML content from a given URL safely."""

    headers = {
        "User-Agent": "Mozilla/5.0 (Educational Scraper - Learning Purpose)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            print(f"Failed to fetch page. Status code: {response.status_code}")
            return None

        return response.text

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None



def parse_books(html):
    """Extract book title, price, rating, and link."""

    soup = BeautifulSoup(html, "html.parser")

    books = []


    book_items = soup.find_all("article", class_="product_pod")

    for item in book_items:
        try:
           
            title_tag = item.find("h3").find("a")
            title = title_tag["title"] if title_tag else "N/A"

            price_tag = item.find("p", class_="price_color")
            price = price_tag.text if price_tag else "N/A"

            rating_tag = item.find("p", class_="star-rating")
            rating = rating_tag["class"][1] if rating_tag else "N/A"

           
            link = title_tag["href"] if title_tag else "N/A"
            full_link = "http://books.toscrape.com/" + link

            books.append([title, price, rating, full_link])

        except Exception:
           
            continue

    return books



def save_to_csv(data, filename="books.csv"):
    """Save scraped data to CSV file."""

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Title", "Price", "Rating", "Link"])

        writer.writerows(data)

    print(f"Data saved to {filename}")



def main():
    url = "http://books.toscrape.com/"

    print("Fetching website...")

    html = fetch_page(url)

    if not html:
        print("Could not retrieve webpage.")
        return

    
    time.sleep(1)

    books = parse_books(html)

    if not books:
        print("No books found.")
        return

    save_to_csv(books)

    print(f"Scraped {len(books)} books successfully.")


if __name__ == "__main__":
    main()
