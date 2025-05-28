from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from openpyxl import Workbook
import time

# --- Setup Selenium ---
options = Options()
options.add_argument("--headless")  # Run in headless mode (no GUI)
service = Service()  # You can specify path to chromedriver here if needed
driver = webdriver.Chrome(service=service, options=options)

# --- Open the target page ---
url = "https://bayportbluepointny.sites.thrillshare.com/events?start_date=2025-03-01&end_date=2025-07-31&filter_ids=326413,326413&view=list-month"
driver.get(url)
time.sleep(5)  # Wait for JavaScript to load (adjust if needed)

# --- Get page source after JS executes ---
html = driver.page_source
driver.quit()

# --- Parse with BeautifulSoup ---
soup = BeautifulSoup(html, "html.parser")

# --- Initialize Excel ---
wb = Workbook()
ws = wb.active
ws.title = "March 2025 Events"
ws.append(["Date", "Title"])

# --- Extract events ---
events = soup.select('.event-list-item')

def find_first_index(text, search_strings):
    for s in search_strings:
        try:
            return text.index(s)
        except ValueError:
            pass
    return -1

print(events)
for event in events:
    title = event.select_one('.title')
    date = event.select_one('.event-list-date')
    #date = date.get_text(strip=True)[0:4] + " " + date.get_text(strip=True)[4:]

    look_vals = ("All","8:0")

    title_text = title.get_text(strip=True) if title else "No Title"
    date_text = date.get_text(strip=True)[0:3] + " " + date.get_text(strip=True)[3:find_first_index(date.get_text(strip=True),look_vals)] + " " + date.get_text(strip=True)[find_first_index(date.get_text(strip=True),look_vals):] if date else "No Date"
    #link = "https://bayportbluepointny.sites.thrillshare.com" + event['href'] if event.has_attr('href') else "No Link"
    
    ws.append([date_text, title_text])

# --- Save Excel ---
wb.save("BBP_March_2025_Events.xlsx")
print("Saved: BBP_March_2025_Events.xlsx")

# Use these to split the date string
# =LEFT(A1, FIND(" ", A1, FIND(" ", A1) + 1) - 1)
# =TRIM(MID(A1, FIND(" ", A1, FIND(" ", A1) + 1) + 1, LEN(A1)))
