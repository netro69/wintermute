"""Debug: try simplest click approach."""
import asyncio
from stagehand import Stagehand, local_browser

async def main():
    browser = await local_browser.launch()
    try:
        stagehand = await Stagehand.create(browser=browser)
        page = (await browser.context.pages())[0]

        await page.goto("https://www.youtube.com/watch?v=jIviHI7fqyc")
        await page.wait_for_load_state("domcontentloaded")
        await asyncio.sleep(8)

        selector = "ytd-video-description-transcript-section-renderer button"
        
        # Approach 1: Direct click
        print("Approach 1: Direct click...")
        try:
            await page.locator(selector).first().click()
            print("  ✓ Clicked!")
            await asyncio.sleep(4)
        except Exception as e:
            print(f"  ✗ Failed: {e}")

        # Check snapshot for transcript
        snap = await page.snapshot()
        tree = getattr(snap, 'formatted_tree', str(snap))
        
        found = False
        for line in tree.split('\n'):
            if 'Transcript' in line:
                print(f"  {line.strip()}")
                found = True
        
        if not found:
            print("No transcript in snapshot")

        await stagehand.close()
    finally:
        await browser.close()

asyncio.run(main())
