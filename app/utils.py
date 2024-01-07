import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from app import app, db  # Import your Flask app and SQLAlchemy instance
from app.models import Outlet  # Import your Outlet model


def scrape_outlets(url):
    outlets = []

    while url:
        response = requests.get(url)
        html_content = response.text  # Save the original HTML content

        # Write the HTML content to a file
        with open('scrapped.html', 'a', encoding='utf-8') as html_file:
            html_file.write(html_content)

        soup = BeautifulSoup(html_content, 'html.parser')

        for outlet in soup.find_all('div', class_='elementor-element-a5ba7a6'):
            lines = outlet.text.strip().split('\n')
            cleaned_lines = [line.strip() for line in lines if line.strip()]

            if len(cleaned_lines) >= 2:
                address, name = cleaned_lines[:2]
                outlets.append((name, address))

        next_page = soup.find('a', {'rel': 'next'})
        url = next_page['href'] if next_page else None

    return outlets


def get_geocode(address, api_key):
    api_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "new_forward_geocoder": "true",
        "address": address,
        "key": api_key
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()
        results = data.get("results", [])

        if results:
            location = results[0]["geometry"]["location"]
            return (location["lat"], location["lng"])
        else:
            print("No results found for the provided address.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    return (None, None)


def save_outlets_to_db_old(name, address, latitude, longitude):
    # Check if the store with the given name exists
    existing_outlet = Outlet.query.filter_by(name=name).first()

    if existing_outlet:
        # If it exists, check if the details are different before updating
        if (existing_outlet.address != address):
            print('Address not same')
        if (existing_outlet.latitude != latitude):
            print('latitude not same')
        if (existing_outlet.longitude != longitude):
            print('longitude not same')
            print(f"old long: {existing_outlet.longitude}")
            print(f"new long: {longitude}")

        if (existing_outlet.address != address or
            existing_outlet.latitude != latitude or
                existing_outlet.longitude != longitude):

            # Update the details only if they are different
            existing_outlet.address = address
            existing_outlet.latitude = latitude
            existing_outlet.longitude = longitude
            print(f"Outlet updated: {existing_outlet.name}")

    else:
        # If it doesn't exist, insert a new record
        outlet = Outlet(name=name, address=address,
                        latitude=latitude, longitude=longitude)
        db.session.add(outlet)
        print(f"Outlet created: {outlet.name}")

    db.session.commit()


def save_outlets_to_db(name, address, latitude, longitude):
    existing_outlet = Outlet.query.filter_by(name=name).first()

    if existing_outlet:
        changes = {}

        if existing_outlet.address != address:
            changes["Address"] = (existing_outlet.address, address)

        existing_latitude = float(existing_outlet.latitude)
        if abs(existing_latitude - latitude) > 1e-6:
            changes["Latitude"] = (existing_latitude, latitude)

        existing_longitude = float(existing_outlet.longitude)
        if abs(existing_longitude - longitude) > 1e-6:
            changes["Longitude"] = (existing_longitude, longitude)

        if changes:
            for key, (old_value, new_value) in changes.items():
                print(f"{key} changed from {old_value} to {new_value}")

            existing_outlet.address, existing_outlet.latitude, existing_outlet.longitude = address, latitude, longitude
        else:
            print(f"Existing Outlet: {existing_outlet.name}")

    else:
        outlet = Outlet(name=name, address=address,
                        latitude=latitude, longitude=longitude)
        db.session.add(outlet)
        print(f"New Outlet: {outlet.name}")

    db.session.commit()
