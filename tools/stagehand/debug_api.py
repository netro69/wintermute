"""Debug: find working APIs on the Stagehand page object."""
import asyncio
from stagehand import Stagehand, local_browser

async def main():
    browser = await local_browser.launch()
    try:
        stagehand = await Stagehand.create(browser=browser)
        page = (await browser.context.pages())[0]

        await page.goto("https://example.com")

        # Check what methods page has
        methods = [m for m in dir(page) if not m.startswith('_') and callable(getattr(page, m, None))]
        print(f"Page methods ({len(methods)}): {methods[:30]}")

        # Try locator
        try:
            h1 = page.locator("h1").first()
            text = await h1.text_content()
            print(f"h1 text: '{text}'")
        except Exception as e:
            print(f"locator error: {e}")

        # Try count
        try:
            n = await page.locator("h1").count()
            print(f"h1 count: {n}")
        except Exception as e:
            print(f"count error: {e}")

        # Try all_text_contents
        try:
            texts = await page.locator("p").all_text_contents()
            print(f"p texts: {texts[:3]}")
        except Exception as e:
            print(f"all_text_contents error: {e}")

        # Try stagehand.evaluate if exists
        if hasattr(stagehand, 'evaluate'):
            try:
                r = await stagehand.evaluate("() => document.title")
                print(f"stagehand.evaluate: {r}")
            except Exception as e:
                print(f"stagehand.evaluate error: {e}")

        await stagehand.close()
    finally:
        await browser.close()

asyncio.run(main())
