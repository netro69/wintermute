"""Debug: check page.tools and stagehand tools."""
import asyncio
from stagehand import Stagehand, local_browser

async def main():
    browser = await local_browser.launch()
    try:
        stagehand = await Stagehand.create(browser=browser)
        page = (await browser.context.pages())[0]

        await page.goto("https://example.com")

        # Check page.tools
        print(f"page.tools: {page.tools}")
        print(f"page.tools methods: {[m for m in dir(page.tools) if not m.startswith('_')]}")

        # Try page.tools.evaluate or similar
        for name in ['evaluate', 'js', 'run', 'exec', 'call']:
            if hasattr(page.tools, name):
                print(f"Found page.tools.{name}")

        # Check stagehand direct attributes
        print(f"\nstagehand methods: {[m for m in dir(stagehand) if not m.startswith('_')]}")

        # Try stagehand.act
        if hasattr(stagehand, 'act'):
            print("\nTrying stagehand.act...")
            try:
                result = await stagehand.act("get the heading text")
                print(f"act result: {result}")
            except Exception as e:
                print(f"act error: {e}")

        # Try stagehand.extract
        if hasattr(stagehand, 'extract'):
            print("\nTrying stagehand.extract...")
            try:
                result = await stagehand.extract("heading")
                print(f"extract result: {result}")
            except Exception as e:
                print(f"extract error: {e}")

        # Try stagehand.goto
        if hasattr(stagehand, 'goto'):
            print("\nTrying stagehand.goto...")
            try:
                await stagehand.goto("https://example.com")
                print("goto ok")
            except Exception as e:
                print(f"goto error: {e}")

        await stagehand.close()
    finally:
        await browser.close()

asyncio.run(main())
