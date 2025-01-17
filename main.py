# Import required libraries
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML and extracting data
import pandas as pd  # For handling tabular data and saving to CSV

# Initialize variables
current_page = 1  # Start scraping from page 1
data = []  # List to store the scraped data
proceed = True  # Flag to control the while loop

# Loop through pages until no more books are found
while proceed:
    print("Scraping page " + str(current_page) + "...")  # Inform the user about the current page being scraped

    # Construct the URL for the current page
    url = "https://books.toscrape.com/catalogue/page-" + str(current_page) + ".html"

    # Send an HTTP GET request to the page
    page = requests.get(url)

    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(page.text, "html.parser")

    # Check if the page is "404 Not Found" (end of available pages)
    if soup.title.text == "404 Not Found":
        proceed = False  # Stop the loop if no more pages are available
    else:
        # Find all book entries on the current page
        all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        
        # Loop through each book entry and extract data
        for book in all_books:
            item = {}  # Dictionary to store book details
            
            # Extract the book's title from the 'alt' attribute of the <img> tag
            item["Title"] = book.find("img").attrs["alt"]
            
            # Construct the full link to the book's page
            item["Link"] = "https://books.toscrape.com/catalogue/" + book.find("a").attrs["href"]
            
            # Extract the book's price, removing the currency symbol (£)
            item["Price"] = book.find("p", class_="price_color").text[1:]
            
            # Extract the stock availability and strip any extra whitespace
            item["Stock"] = book.find("p", class_="instock availability").text.strip()
            
            # Append the book's details to the data list
            data.append(item)
            
    # Increment the page number to move to the next page
    current_page += 1

# Create a DataFrame from the scraped data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file named "books.csv"
df.to_csv("books.csv", index=False)

# Print a success message
print("\n")
print("Successfully saved to books.csv")
