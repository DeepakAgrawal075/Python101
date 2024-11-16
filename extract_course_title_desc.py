import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage
url = "https://www.saintpeters.edu/academics/graduate-programs/master-of-science-information-sciences/courses/"

# Fetch the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract data for all "courseblock" classes
courses = soup.find_all(class_="courseblock")

# Prepare lists to store data
titles = []
descriptions = []

# Extract title and description for each courseblock
for course in courses:
    title = course.find(class_="courseblocktitle")
    desc = course.find(class_="courseblockdesc")
    titles.append(title.get_text(strip=True) if title else "N/A")
    descriptions.append(desc.get_text(strip=True) if desc else "N/A")

# Create a DataFrame
df = pd.DataFrame({
    "Course Title": titles,
    "Course Description": descriptions
})

# Save to Excel
output_file = "Courseblock_Titles_and_Descriptions.xlsx"
df.to_excel(output_file, index=False)

print(f"Data saved to {output_file}")
