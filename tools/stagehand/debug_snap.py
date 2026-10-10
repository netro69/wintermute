"""Debug: snapshot + find transcript button in a11y tree."""
import asyncio
from stagehand import Stagehand, local_browser

async def main():
    browser = await local_browser.launch()
    try:
        stagehand = await Stagehand.create(browser=browser)
        page = (await browser.context.pages())[0]

        await page.goto("https://www.youtube.com/watch?v=jIviHI7fqyc")
        await asyncio.sleep(5)

        # Get snapshot
        snap = await page.snapshot()
        tree = getattr(snap, 'formatted_tree', str(snap))
        print("=== SNAPSHOT (first 3000 chars) ===")
        print(tree[:3000])

        # Find transcript in snapshot
        for line in tree.split('\n'):
            if 'transcript' in line.lower() or 'caption' in line.lower():
                print(f"  FOUND: {line.strip()}")

        # Try locator with has-text for the button
        print("\n=== TRYING LOCATORS ===")
        for sel in [
            "ytd-video-description-transcript-section-renderer",
            "ytd-video-description-transcript-section-renderer button",
            "#transcript-button",
            "button:has-text('transcript')",
            "button:has-text('Transcript')",
            "[class*='transcript'][class*='button']",
            "[class*='transcript'][class*='section'] button",
        ]:
            try:
                n = await page.locator(sel).count()
                if n > 0:
                    text = await page.locator(sel).first().text_content()
                    print(f"  ✓ {sel}: count={n}, text='{text}'")
                else:
                    print(f"  ✗ {sel}: count=0")
            except Exception as e:
                print(f"  ✗ {sel}: {e}")

        await stagehand.close()
    finally:
        await browser.close()

asyncio.run(main())
