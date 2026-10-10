"""Debug: test snapshot and evaluate with arg."""
import asyncio
from stagehand import Stagehand, local_browser

async def main():
    browser = await local_browser.launch()
    try:
        stagehand = await Stagehand.create(browser=browser)
        page = (await browser.context.pages())[0]

        await page.goto("https://example.com")

        # Try snapshot
        try:
            snap = await page.snapshot()
            print(f"snapshot type={type(snap).__name__} len={len(str(snap))}")
            print(f"snapshot preview: {str(snap)[:300]}")
        except Exception as e:
            print(f"snapshot error: {e}")

        # Try evaluate with arg parameter
        try:
            r = await page.evaluate("x => x", "hello")
            print(f"evaluate-with-arg: type={type(r).__name__} repr={repr(r)}")
        except Exception as e:
            print(f"evaluate-with-arg error: {e}")

        # Try evaluate with function expression
        try:
            r = await page.evaluate("(x) => x.title", {"title": "test"})
            print(f"evaluate-fn-arg: type={type(r).__name__} repr={repr(r)}")
        except Exception as e:
            print(f"evaluate-fn-arg error: {e}")

        # Try passing a function
        try:
            r = await page.evaluate("function() { return 42; }")
            print(f"evaluate-fn-decl: type={type(r).__name__} repr={repr(r)}")
        except Exception as e:
            print(f"evaluate-fn-decl error: {e}")

        # Try arrow function without parens
        try:
            r = await page.evaluate("() => { return document.title; }")
            print(f"evaluate-arrow-body: type={type(r).__name__} repr={repr(r)}")
        except Exception as e:
            print(f"evaluate-arrow-body error: {e}")

        await stagehand.close()
    finally:
        await browser.close()

asyncio.run(main())
