"""Debug: use scroll + bounding_box + mouse click."""
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
        
        # Scroll to bottom of page
        print("Scrolling...")
        for _ in range(5):
            await page.scroll(0, 0, 0, 800)
            await asyncio.sleep(0.5)
        await asyncio.sleep(2)
        
        # Get button location
        btn = page.locator(selector).first()
        
        # Try hover first
        try:
            await btn.hover()
            print("  ✓ Hovered")
            await asyncio.sleep(1)
            await btn.click()
            print("  ✓ Clicked via hover+click")
        except Exception as e:
            print(f"  ✗ hover+click: {e}")
            
            # Try bounding_box
            try:
                box = await btn.bounding_box()
                print(f"  Box: {box}")
                if box:
                    x = box['x'] + box['width']/2
                    y = box['y'] + box['height']/2
                    await page.mouse.click(x, y)
                    print("  ✓ Clicked via mouse")
            except Exception as e2:
                print(f"  ✗ bounding_box: {e2}")

        await asyncio.sleep(4)
        
        snap = await page.snapshot()
        tree = getattr(snap, 'formatted_tree', str(snap))
        
        # Check for transcript text
        found = False
        for line in tree.split('\n'):
            if 'Transcript' in line:
                print(f"  {line.strip()}")
                found = True
        
        if not found:
            print("No transcript text in snapshot")

        await stagehand.close()
    finally:
        await browser.close()

asyncio.run(main())
