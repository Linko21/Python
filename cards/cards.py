from downloader import download_data_from_url_to_file

cards_in_local_file_as_json = download_data_from_url_to_file("https://api.lorcana-api.com/cards/all", "cards/cards.json")
sets_in_local_file_as_json = download_data_from_url_to_file("https://api.lorcana-api.com/sets/all", "cards/sets.json")

