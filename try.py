import requests 
from bs4 import BeautifulSoup
import csv
import os
siteToScrape = "https://www.airbnb.com/s/Lekki-Lagos-NG/homes?omni_page_id=36021&map_toggle=true&min_bedrooms=2&dynamic_product_ids%5B%5D=1366212720802888186&room_types%5B%5D=Entire%20home%2Fapt&category_tag=Tag%3A677&checkin=2025-04-29&checkout=2025-05-04&date_picker_type=calendar&search_mode=flex_destinations_search&refinement_paths%5B%5D=%2Fhomes&place_id=ChIJZ0PH9V33OxARSs3B1vl9fmo&flexible_trip_lengths%5B%5D=one_week&location_search=MIN_MAP_BOUNDS&monthly_start_date=2025-05-01&monthly_length=3&monthly_end_date=2025-08-01&price_filter_input_type=2&price_filter_num_nights=5&channel=EXPLORE&selected_filter_order%5B%5D=room_types%3AEntire%20home%2Fapt&selected_filter_order%5B%5D=min_bedrooms%3A2&ne_lat=6.502531416735711&ne_lng=3.5300245592085275&sw_lat=6.389661415561012&sw_lng=3.3782830219393816&zoom=12.655108628445351&zoom_level=12.655108628445351&search_by_map=true&search_type=user_map_move&query=Lekki%20Lagos%20NG"
response = requests.get(siteToScrape)
parsedresponse = BeautifulSoup(response.text, "html.parser")
Response_folder1 = "Scraped_data_file"
Response_folder2 = "C:\\Users\\user\\Desktop\\scraped_folder2"
os.makedirs(Response_folder2, exist_ok="true")
path_to_scraped_folder = os.path.join(Response_folder2, "scrappedData.csv")
ExtractData = parsedresponse.find_all("image")
Storage = [ ]
header = ["Title", "ApartmentType", "ApartmentName"]
for contents in ExtractData:
    print(contents)
    Storage.append([contents.get_text(stripe = True)])
with open(path_to_scraped_folder, mode="w", newline= "", encoding="utf-8") as file:
    writeFile = csv.writer(file)
    writeFile.writerows(header)
    writeFile.writerows(ExtractData)
print(f"file successfully Extracted and written into:{path_to_scraped_folder}")