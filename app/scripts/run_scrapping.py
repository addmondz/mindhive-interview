from app import app
from app.utils import scrape_outlets, get_geocode, save_outlets_to_db
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    with app.app_context():
        # Define a list of URLs to scrape
        urls_to_scrape = [
            "https://zuscoffee.com/category/store/melaka",

            # can even add other URLs like below / create another scraping to get the states
            # "https://zuscoffee.com/category/store/perlis",
            # "https://zuscoffee.com/category/store/kedah",
            # "https://zuscoffee.com/category/store/penang",
            # "https://zuscoffee.com/category/store/kelantan",
            # "https://zuscoffee.com/category/store/terengganu",
            # "https://zuscoffee.com/category/store/perak",
        ]
        
        api_key = os.environ.get("API_KEY")
        
        for url in urls_to_scrape:
            for name, address in scrape_outlets(url):
                lat, lon = get_geocode(address, api_key)
                if lat and lon:
                    save_outlets_to_db(name, address, lat, lon)
                else:
                    print("Coordinates not found for the given address.")

if __name__ == "__main__":
    main()
