"""Debug: scroll to bottom using End key then click."""
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

        selector = "ytd-video-description-transcript-section-renderer button"
        
        # Scroll down using End key multiple times
        for _ in range(3):
            await page.key_press("End")
            await asyncio.sleep(1)
        
        # Try pressing End on the main content area
        main = page.locator("ytd-app").first()
        try:
            await main.click()
            await asyncio.sleep(0.5)
        except:
            pass
        
        for _ in range(5):
            await page.key_press("PageDown")
            await asyncio.sleep(0.5)
        
        await asyncio.sleep(2)
        
        # Screenshot to see where we are
        await page.screenshot(path="C:/Users/david.DESKTOP-EOCN3KC/OneDrive/Desktop/wintermute/tools/stagehand/debug_after-scroll.png")
        
        # Try clicking
        btn = page.locator(selector).first()
        count = await page.locator(selector).count()
        print(f"Button count: {count}")
        
        try:
            await btn.click()
            print("  ✓ Clicked!")
            await asyncio.sleep(4)
        except Exception as e:
            print(f"  ✗ Click failed: {e}")
            
            # Try hover with coords
            try:
                await page.hover(500, 800)
                await asyncio.sleep(1)
                await btn.click()
                print("  ✓ Clicked after hover")
            except Exception as e2:
                print(f"  ✗ Hover+click failed: {e2}")
        
        # Check snapshot
        snap = await page.snapshot()
        tree = getattr(snap, 'formatted_tree', str(snap))
        
        for line in tree.split('\n'):
            if 'Transcript' in line:
                print(f"  FOUND: {line.strip()}")

        await stagehand.close()
    finally:
        await browser.close()

asyncio.run(main())
