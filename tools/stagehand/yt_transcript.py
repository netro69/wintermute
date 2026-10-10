"""
Stagehand YouTube Transcript Extractor for Wintermute v8
=========================================================
Uses page.click(selector) directly after scrolling with keyboard.
"""

import asyncio
import os

from stagehand import Stagehand, local_browser

VIDEO_URL = "https://www.youtube.com/watch?v=jIviHI7fqyc"
VIDEO_TITLE = "Jensen Huang — GTC 2026 Keynote"
VIDEO_DATE = "2026-07-02"
VIDEO_DURATION = "2h 15m"
PERSONA = "Silicon Architect"
SOURCE_TYPE = "YouTube Video (Transcript)"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(SCRIPT_DIR, "..", "..")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "20_Research", PERSONA)
OUTPUT_FILE = os.path.join(
    OUTPUT_DIR,
    f"Stagehand Transcript Test - {VIDEO_DATE} - Jensen GTC 2026 Keynote.md"
)
SCREENSHOT_DIR = SCRIPT_DIR


async def main():
    print("=" * 60)
    print("Stagehand YouTube Transcript Extractor v8")
    print("=" * 60)

    browser = await local_browser.launch()
    try:
        stagehand = await Stagehand.create(browser=browser)
        page = (await browser.context.pages())[0]

        # ── Navigate ──
        print("[1/5] Navigating...")
        await page.goto(VIDEO_URL)
        await page.wait_for_load_state("domcontentloaded")
        await asyncio.sleep(6)
        print("  ✓ Page loaded")

        # ── Scroll to transcript section with PageDown ──
        print("[2/5] Scrolling to transcript section...")
        # Send PageDown key multiple times to scroll down
        for _ in range(8):
            await page.key_press("PageDown")
            await asyncio.sleep(0.5)
        await asyncio.sleep(2)
        
        # Also try scrolling via video description container
        try:
            desc = page.locator("#description").first()
            if await desc.is_visible():
                await desc.hover()
                for _ in range(5):
                    await page.key_press("PageDown")
                    await asyncio.sleep(0.3)
        except:
            pass
        
        await page.screenshot(path=os.path.join(SCREENSHOT_DIR, "v8_shot_02.png"))

        # ── Find and click transcript button ──
        print("[3/5] Finding transcript button...")
        selector = "ytd-video-description-transcript-section-renderer button"
        
        # Check count
        count = await page.locator(selector).count()
        print(f"  Elements: {count}")
        
        if count == 0:
            print("  ✗ No button found")
            return
        
        # Try clicking using page.click with selector string
        try:
            await page.click(selector)
            print("  ✓ Clicked via page.click(selector)")
        except Exception as e:
            print(f"  page.click failed: {e}")
            
            # Try clicking the section renderer itself
            section_sel = "ytd-video-description-transcript-section-renderer"
            try:
                await page.click(section_sel)
                print("  ✓ Clicked section via page.click")
            except Exception as e2:
                print(f"  section click failed: {e2}")
                
                # Last resort: hover then click
                try:
                    btn = page.locator(selector).first()
                    await btn.hover()
                    await asyncio.sleep(1)
                    await btn.click()
                    print("  ✓ Clicked via hover+click")
                except Exception as e3:
                    print(f"  hover+click failed: {e3}")
                    return

        await asyncio.sleep(4)
        await page.screenshot(path=os.path.join(SCREENSHOT_DIR, "v8_shot_03.png"))

        # ── Extract transcript ──
        print("[4/5] Extracting transcript...")
        
        snap = await page.snapshot()
        tree = getattr(snap, 'formatted_tree', str(snap))
        
        lines = []
        for line in tree.split('\n'):
            if 'StaticText:' in line:
                text = line.split('StaticText:', 1)[1].strip()
                if text and len(text) > 3:
                    lines.append(text)
        
        if not lines:
            print("  → StaticText parse failed, trying yt-formatted-string...")
            # Get all yt-formatted-string elements in transcript panel
            segments = page.locator("ytd-transcript-segment-renderer")
            seg_count = await segments.count()
            for i in range(min(seg_count, 1000)):
                text = await segments.nth(i).text_content()
                if text:
                    lines.append(text.strip())
        
        print(f"  Extracted {len(lines)} lines")

        # ── Write output ──
        print("[5/5] Writing output...")
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(f"# {VIDEO_TITLE}\n\n")
            f.write(f"**Source**: {VIDEO_URL} | NVIDIA | {VIDEO_DURATION}\n")
            f.write(f"**Date**: {VIDEO_DATE}\n")
            f.write(f"**Type**: {SOURCE_TYPE}\n")
            f.write(f"**Extraction**: Stagehand v8 (key-press scroll)\n\n")
            f.write("---\n\n")
            f.write("## Transcript\n\n")
            
            for line in lines:
                f.write(f"{line}\n\n")
            
            if not lines:
                f.write("⚠️ No transcript lines extracted.\n")
                f.write("Snapshot preview:\n```\n")
                f.write(tree[:1500])
                f.write("\n```\n")

        print(f"\n{'=' * 60}")
        print(f"  Lines: {len(lines)}")
        print(f"  Output: {OUTPUT_FILE}")
        print(f"{'=' * 60}")

        await stagehand.close()
    finally:
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
