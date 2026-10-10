"""Debug: scroll with correct API."""
import asyncio
from stagehand import Stagehand, local_browser

async def main():
    browser = await local_browser.launch()
    try:
        stagehand = await Stagehand.create(browser=browser)
        page = (await browser.context.pages())[0]

        await page.goto("https://www.youtube.com/watch?v=jIviHI7fqyc")
        await page.wait_for_load_state("domcontentloaded")
        await asyncio.sleep(6)

        # Try scrolling with correct args
        print("Trying scroll...")
        try:
            await page.scroll(0, 0, 0, 1000)  # x, y, delta_x, delta_y
            print("  ✓ Scrolled")
        except Exception as e:
            print(f"  ✗ scroll failed: {e}")

        await asyncio.sleep(2)

        # Try hover+click
        selector = "ytd-video-description-transcript-section-renderer button"
        btn = page.locator(selector).first()
        
        print(f"\nButton: {await btn.text_content()}")
        
        # Try hover then click
        await btn.hover()
        await asyncio.sleep(1)
        await btn.click()
        print("  ✓ Clicked")

        await asyncio.sleep(4)
        
        snap = await page.snapshot()
        tree = getattr(snap, 'formatted_tree', str(snap))
        
        # Look for Transcript heading
        found_transcript = False
        for line in tree.split('\n'):
            if 'Transcript' in line or 'transcript' in line:
                print(f"  {line.strip()}")
                found_transcript = True
        
        if not found_transcript:
            print("No 'Transcript' in snapshot")

        await stagehand.close()
    finally:
        await browser.close()

asyncio.run(main())
