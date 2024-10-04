from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # You can also use 'firefox' or 'webkit'
    page = browser.new_page()
    page.goto("https://www.imdb.com/title/tt15354916/reviews/?ref_=tt_urv_sm")

    # Load more content as needed
    while True:
        try:
            button = page.query_selector("#load-more-trigger")
            if button:
                button.click()
                page.wait_for_timeout(2000)  # Wait for new content to load
            else:
                break
        except Exception as e:
            print("Error:", e)
            break

    # Save the HTML content
    with open("jawaan_source_p.html", "w", encoding="utf-8") as file:
        file.write(page.content())

    browser.close()
