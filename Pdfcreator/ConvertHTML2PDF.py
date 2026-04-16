from playwright.sync_api import sync_playwright
import os

def convert2pdf(html_file):
    with sync_playwright() as p:
            browser = p.chromium.launch()
            context = browser.new_context()
            page = context.new_page()

            # Load local HTML file
            file_path = os.path.abspath(html_file)
            file_url = f"file://{file_path}"

            page.goto(file_url)

            # Generate PDF
            page.pdf(
                path="resume.pdf",
                format="A4",
                margin={"top": "20px", "bottom": "20px"}
            )

            browser.close()

if __name__=="__main__":
      convert2pdf('resume.html')