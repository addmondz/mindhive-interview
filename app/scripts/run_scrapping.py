from app import app
from app.utils import scrape_outlets, get_geocode, save_outlets_to_db, scrape_states, save_state_to_db_old
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    with app.app_context():
        # Define a list of URLs to scrape
        urls_to_scrape = [
            "https://zuscoffee.com/category/store/melaka",
        ]
        
        api_key = os.environ.get("API_KEY")
        
        for url in urls_to_scrape:
            
            for state_url, state_name  in scrape_states(url):
                save_state_to_db_old(state_name, state_url)
                for name, address in scrape_outlets(state_url):
                    lat, lon = get_geocode(address, api_key)
                    if lat and lon:
                        save_outlets_to_db(name, address, lat, lon, state_name)
                    else:
                        print("Coordinates not found for the given address.")

if __name__ == "__main__":
    main()
