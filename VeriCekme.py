from amazon_review_scraper import amazon_review_scraper
url = input("Enter URL: ")
start_page = input("Enter Start Page: ")
end_page = input("Enter End Page: ")
time_upper_limit = input("Enter upper limit of time range (Example: Entering the value 5 would mean the program will wait anywhere from 0 to 5 seconds before scraping a page. If you don't want the program to wait, enter 0): ")
file_name = input ("File name: ")

scraper = amazon_review_scraper.amazon_review_scraper(url, start_page, end_page, time_upper_limit)
scraper.scrape()
scraper.write_csv(file_name)    