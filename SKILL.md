---
name: ldcc-fixture-poster-maker
description: Generate Instagram-ready weekend fixture posters for London Desperados Cricket Club using AI image generation. Use when the user provides cricket match fixture details (teams, dates, venues) and requests a poster for Instagram. Supports 2-4 matches per weekend with typography-focused design.
---

# LDCC Fixture Poster Maker

Generate professional weekend fixture posters for London Desperados CC using Nano Banana Pro (AI image generation).

## Quick Start

When the user provides fixture text containing match details:

**Step 1: Generate AI poster at 2K**
```bash
cd /data/.openclaw/workspace/cricket-poster-generator
python3 /data/.openclaw/workspace/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "<detailed prompt>" \
  --input-image "output/TEMPLATE-final.png" \
  --filename "output/fixture-temp.png" \
  --resolution 2K
```

**Step 2: Resize to exact Instagram dimensions**
```bash
python3 -c "
from PIL import Image
img = Image.open('output/fixture-temp.png')
img_resized = img.resize((1012, 1280), Image.Resampling.LANCZOS)
img_resized.save('output/fixture-YYYY-MM-DD-final.png')
print('Resized to 1012x1280')
"
```

This two-step process ensures the AI generates everything at high quality (2K), then we resize to the exact dimensions needed for Instagram.

## Club Information

- **Website:** www.londondesperados.com
- **Instagram:** @londondesperados
- **Play Cricket:** londondesperados.play-cricket.com

## Design Specs

- **Format:** EXACTLY 1012x1280 pixels, portrait orientation (PNG)
- **Generation:** 2K resolution, then resize to exact dimensions
- **Style:** Typography-focused with bold team names and diagonal color blocks
- **Colors:** Red/black/gold Desperados theme with dark background
- **Branding:** Desperados shield logo (top left), sponsor logos (bottom: KodeKloud, Rayyan, Global Sports Link)
- **Cards:** 2-4 match cards per poster, each with distinct color scheme (blue, green, orange, purple)
- **Bottom text:** Website + Instagram handle + LIVE STREAMING badge

## Critical Rules

### Home/Away Positioning

**HOME matches:** London Desperados on LEFT
**AWAY matches:** London Desperados on RIGHT

### Color Schemes

Each match card must have a DIFFERENT color scheme:
- Card 1: Blue/cyan theme
- Card 2: Green theme  
- Card 3: Orange theme
- Card 4: Purple theme (if needed)

London Desperados always in gold/black regardless of position.

### Match Card Count

- Parse ALL matches from fixture text (typically 2-3, can be up to 4)
- Ensure all matches appear in final poster
- Stack cards vertically with equal spacing

## Prompt Template

```
Create a PORTRAIT weekend fixture poster for Instagram with [EXACTLY THREE/FOUR] match cards stacked vertically:

CARD 1 ([HOME/AWAY] - blue/cyan theme):
[DAY] [DATE] | [TEAM NAME] - [FORMAT]
[TEAM 1] vs [TEAM 2]
VENUE: [VENUE] ([HOME/AWAY])

CARD 2 ([HOME/AWAY] - green theme):
[DAY] [DATE] | [TEAM NAME] - [FORMAT]
[TEAM 1] vs [TEAM 2]
VENUE: [VENUE] ([HOME/AWAY])

CARD 3 ([HOME/AWAY] - orange theme):
[DAY] [DATE] | [TEAM NAME] - [FORMAT]
[TEAM 1] vs [TEAM 2]
VENUE: [VENUE] ([HOME/AWAY])

Design: Red/black/gold Desperados branding. Typography-focused with bold team names and diagonal color blocks. Each card DIFFERENT color (blue, green, orange). Desperados shield logo top left. Three sponsor logos at bottom (KodeKloud, Rayyan, Global Sports Link). Website www.londondesperados.com and Instagram @londondesperados at bottom. PORTRAIT orientation for Instagram.
```

**Critical:** Specify "EXACTLY THREE CARDS" or "EXACTLY FOUR CARDS" in the prompt to ensure all matches appear.

## Logo Assets Reference

Located in `assets/logos/` for reference (AI generates logos from description):
- `desperados-clean.jpg` - Desperados shield logo
- `kodekloud.jpg` - KodeKloud sponsor logo
- `rayyan.jpg` - Rayyan Groups sponsor logo  
- `globalsports.jpg` - Global Sports Link sponsor logo

**Note:** The AI generates all logos and branding directly - no programmatic overlay needed.

## Template Reference

- `output/TEMPLATE-final.png` - Original template (1856x2304) used as input image for AI generation
- `references/APPROVED-2025-07-12.png` - Approved final poster (1012x1280) showing perfect styling, layout, and branding

## Output

Generated posters save to: `/data/.openclaw/workspace/cricket-poster-generator/output/`

## Workflow Summary

1. Parse fixture text to extract all matches (teams, dates, venues, home/away)
2. Determine home/away positioning for each match (HOME = left, AWAY = right)
3. Assign different color scheme to each card (blue, green, orange, purple)
4. Build comprehensive prompt with all match details - specify "EXACTLY [NUMBER] CARDS"
5. Generate using Nano Banana Pro at 2K resolution with template reference
6. Resize to exact dimensions (1012x1280) using PIL
7. Verify all matches appear with correct positioning and colors
8. Send final poster to user via Telegram

## Common Issues

**Landscape instead of portrait orientation:**
- Always specify "PORTRAIT weekend fixture poster" in prompt
- Template is portrait but AI may ignore - emphasis matters
- Final resize step ensures correct dimensions

**Only 2 cards showing when 3 expected:**
- Explicitly state "EXACTLY THREE CARDS" in prompt
- Count matches and specify exact number

**Wrong home/away positioning:**
- Double-check HOME = left, AWAY = right
- Verify in prompt before generation

**All cards same color:**
- Specify different color theme for each card in prompt
- Use varied opponent team colors (blue, green, orange, purple)

**Wrong final dimensions:**
- Always resize to EXACTLY 1012x1280 after AI generation
- Use PIL resize with LANCZOS resampling for quality
