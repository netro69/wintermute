"""Debug: dump full snapshot and look for transcript text."""
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

        snap = await page.snapshot()
        tree = getattr(snap, 'formatted_tree', str(snap))
        
        print(f"Full tree length: {len(tree)} chars")
        print("=" * 60)
        
        # Find all lines containing key transcript words
        keywords = ['transcript', 'StaticText:', 'Transcript', 'Follow along']
        for line in tree.split('\n'):
            for kw in keywords:
                if kw in line:
                    print(line.strip())
                    break
        
        print("=" * 60)
        # Also check for any yt-formatted-string in the tree
        count = 0
        for line in tree.split('\n'):
            if 'yt-formatted-string' in line:
                count += 1
                if count <= 30:
                    print(line.strip())
        print(f"\nTotal yt-formatted-string elements: {count}")

        await stagehand.close()
    finally:
        await browser.close()

asyncio.run(main())
