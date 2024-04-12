import requests
from bs4 import BeautifulSoup
import json

def get_section_content(url, section_title):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text()
    sections = text.split('\n')

    data = {}

    for i, section in enumerate(sections):
        section_key = i
        data[section_key] = section.strip()

    json_data = json.dumps(data, indent=4)
    parsed_data = json.loads(json_data)

    res = None
    for key, value in parsed_data.items():
        if value == section_title:
            res = int(key) + 1

    if res is not None and str(res) in parsed_data:
        return parsed_data[str(res)]
    else:
        return "Section not found."

# Modified function to accept medicine name as a parameter
def medicineDesc(medicine_name):
    base_url = "https://www.drugs.com/"
    medicine_url = base_url + medicine_name.lower() + ".html"
    section_title = "What is " + medicine_name.lower() + "?"
    content = get_section_content(medicine_url, section_title)
    return content


