from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


def scrape_jobs(location, job_search):
    # Download the chromedriver from the link in the description
    # And give the location of the executable here
    driver = webdriver.Chrome()
    dataframe = pd.DataFrame(
        columns=["Title", "Location", "Company", "Salary", "Sponsored", "Description"])

    for i in range(0, 1, 10):
        # Step 1: Get the page
        url = f"https://www.simplyhired.com/search?q={job_search.replace(' ', '+')}&l={location.replace(' ', '+')}"
        driver.get(url)
        driver.implicitly_wait(4)
        wait = WebDriverWait(driver, 10)  # Wait for a maximum of 10 seconds
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        all_jobs = driver.find_elements(By.CLASS_NAME, "css-0")
        print(all_jobs)
        for job in all_jobs:
            result_html = job.get_attribute('innerHTML')
            soup = BeautifulSoup(result_html, 'html.parser')
            i = 1
            print(soup)

            try:
                titles = driver.find_elements(
                    By.CSS_SELECTOR, "a.chakra-button.css-1y7j4hn")
                title = titles[i].text.replace('\n', '')
            except:
                title = 'None'
            print(title)

            try:
                locations = driver.find_elements(
                    By.CLASS_NAME, "css-1t92pv")
                location = locations[i].text
            except:
                location = 'None'
            print(location)

            try:
                companies = driver.find_elements(
                    By.CSS_SELECTOR, "span[data-testid='companyName']")
                company = companies[i].text.replace('\n', '').strip()
            except:
                company = 'None'
            print(company)

            try:
                salaries = driver.find_elements(
                    By.CSS_SELECTOR, "p.chakra-text.css-1ejkpji")
                salary = salaries[i].text.replace('\n', '').strip()
            except:
                salary = 'None'
            print(salary)

            links = driver.find_elements(
                By.CSS_SELECTOR, "a.chakra-button.css-1y7j4hn")
            link = links[i]
            href_link = link.get_attribute("href")
            print(href_link)

            job_desc = driver.find_element(
                By.CSS_SELECTOR, "p.chakra-text.css-jhqp7z").text

            print(job_desc)
            i = i+1

            dataframe = dataframe.append({'Title': title, 'Location': location, "Company": company, "Salary": salary,
                                          "Description": job_desc, 'Job Link': href_link},
                                         ignore_index=True)
    driver.quit()
    dataframe.to_csv("trial.csv", index=False)


def main():
    location = "New York"
    job_search = "cloud"
    scrape_jobs(location, job_search)
    print("Scraping completed successfully.")


if __name__ == "__main__":
    main()
