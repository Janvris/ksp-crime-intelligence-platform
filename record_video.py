from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir=".", 
            viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()
        
        print("Navigating to platform...")
        page.goto("http://localhost:8000/index.html")
        page.wait_for_timeout(3000)
        
        print("Opening Network Analysis...")
        page.evaluate("showModal('network-modal')")
        page.wait_for_timeout(2000)
        
        print("Searching for FIR 103...")
        page.evaluate("document.getElementById('seedEntityInput').value = 'FIR 103'")
        page.evaluate("searchSeedEntity()")
        page.wait_for_timeout(3000)
        
        print("Running Louvain Algorithm...")
        page.evaluate("runLouvain()")
        page.wait_for_timeout(4000)
        
        print("Closing Network Modal...")
        page.evaluate("hideModal('network-modal')")
        page.wait_for_timeout(1500)
        
        print("Opening Predictive AI...")
        page.evaluate("showModal('predictive-modal')")
        page.wait_for_timeout(4000)
        
        print("Closing Predictive AI...")
        page.evaluate("hideModal('predictive-modal')")
        page.wait_for_timeout(1500)
        
        # Close context to ensure video is saved
        context.close()
        browser.close()
        print("Video recording complete.")

if __name__ == "__main__":
    run()
