import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def keep_alive():
    """
    Visits Streamlit app URLs to keep them awake.
    Reads URLs from 'links.txt' if it exists, otherwise checks STREAMLIT_URL env var.
    """
    urls = []

    # Check for links.txt
    links_file = os.path.join(os.path.dirname(__file__), 'links.txt')
    if os.path.exists(links_file):
        print(f"Reading links from {links_file}...")
        with open(links_file, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]

    # Check for environment variable
    env_url = os.environ.get('STREAMLIT_URL')
    if env_url:
        print("Found STREAMLIT_URL environment variable.")
        if env_url not in urls:
            urls.append(env_url)

    import random

    if not urls:
        print("Error: No URLs found. Please check 'links.txt' or set STREAMLIT_URL.")
        return

    # Randomize order to avoid hitting the same app first/last every time
    random.shuffle(urls)
    print(f"Found {len(urls)} URLs to visit. Order randomized.")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Add a User-Agent to look like a real browser
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    for i, url in enumerate(urls, 1):
        driver = None
        try:
            print(f"[{i}/{len(urls)}] Initializing WebDriver for {url}...")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)

            print(f"Visiting {url}...")
            driver.get(url)

            # Wait for the page to load
            print("Waiting 10 seconds for page load...")
            time.sleep(10)

            title = driver.title
            print(f"Page title: {title}")

            if "Streamlit" in title or title:
                print(f"Successfully visited {url}")
            else:
                print(f"Warning: Page title seems empty for {url}")

        except Exception as e:
            print(f"Error visiting {url}: {e}")

        finally:
            if driver:
                print("Closing driver...")
                driver.quit()

        # Buffer between requests
        if i < len(urls):
            print("Waiting 10 seconds before next request...")
            time.sleep(10)

    print("Finished visiting all URLs.")


if __name__ == "__main__":
    keep_alive()
