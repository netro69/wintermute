"""Debug: check what page.evaluate returns."""
import asyncio
from stagehand import Stagehand, local_browser

async def main():
    browser = await local_browser.launch()
    try:
        stagehand = await Stagehand.create(browser=browser)
        page = (await browser.context.pages())[0]

        await page.goto("https://example.com")

        # Test 1: simple evaluate
        r1 = await page.evaluate("() => document.title")
        print(f"Test1 type={type(r1).__name__} repr={repr(r1)[:100]}")

        # Test 2: string return
        r2 = await page.evaluate("() => { return 'hello world'; }")
        print(f"Test2 type={type(r2).__name__} repr={repr(r2)[:100]}")

        # Test 3: array return
        r3 = await page.evaluate("() => { return [1, 2, 3]; }")
        print(f"Test3 type={type(r3).__name__} repr={repr(r3)[:100]}")

        # Test 4: object return
        r4 = await page.evaluate("() => { return { foo: 'bar', n: 42 }; }")
        print(f"Test4 type={type(r4).__name__} repr={repr(r4)[:100]}")

        await stagehand.close()
    finally:
        await browser.close()

asyncio.run(main())
