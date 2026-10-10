"""Debug: scroll then click transcript button."""
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

        # Scroll to bottom using page.scroll
        print("Scrolling down...")
        for _ in range(6):
            await page.scroll(delta_y=500)
            await asyncio.sleep(0.5)
        await asyncio.sleep(2)

        # Try hover+click on transcript button
        selector = "ytd-video-description-transcript-section-renderer button"
        btn = page.locator(selector).first()
        
        print(f"Button count: {await page.locator(selector).count()}")
        print(f"Button text: {await btn.text_content()}")
        
        try:
            await btn.hover()
            print("  ✓ Hovered")
            await asyncio.sleep(1)
            await btn.click()
            print("  ✓ Clicked")
        except Exception as e:
            print(f"  ✗ hover+click failed: {e}")
            
            # Last resort: try page.mouse.click at the button's location
            try:
                box = await btn.bounding_box()
                if box:
                    x = box['x'] + box['width'] / 2
                    y = box['y'] + box['height'] / 2
                    print(f"  Button at ({x}, {y})")
                    await page.mouse.click(x, y)
                    print("  ✓ Mouse clicked")
            except Exception as e2:
                print(f"  ✗ mouse click failed: {e2}")

        await asyncio.sleep(4)
        
        # Extract
        snap = await page.snapshot()
        tree = getattr(snap, 'formatted_tree', str(snap))
        
        lines = []
        for line in tree.split('\n'):
            if 'StaticText:' in line:
                text = line.split('StaticText:', 1)[1].strip()
                if text and len(text) > 3:
                    lines.append(text)
        
        print(f"\nExtracted {len(lines)} lines")
        for l in lines[:20]:
            print(f"  {l[:80]}")

        await stagehand.close()
    finally:
        await browser.close()

asyncio.run(main())
