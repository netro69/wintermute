"""Debug: check if transcript is available via ytInitialPlayerResponse in page source."""
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

        # Try getting body text
        print("Getting body text...")
        try:
            body = page.locator("body").first()
            text = await body.text_content()
            print(f"Body text length: {len(text)}")
            print(f"First 500: {text[:500]}")
            print(f"Last 500: {text[-500:]}")
        except Exception as e:
            print(f"Body text error: {e}")

        # Try pre tag (where ytInitialPlayerResponse might be)
        print("\nLooking for script/pre tags...")
        try:
            pres = page.locator("pre")
            count = await pres.count()
            print(f"Pre tags: {count}")
            if count > 0:
                text = await pres.first().text_content()
                print(f"First pre: {text[:300]}")
        except Exception as e:
            print(f"Pre error: {e}")

        await stagehand.close()
    finally:
        await browser.close()

asyncio.run(main())
