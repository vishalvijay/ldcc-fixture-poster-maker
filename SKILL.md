---
name: ldcc-fixture-poster-maker
description: Generate Instagram-ready fixture posters for London Desperados Cricket Club using AI image generation. Use when the user provides cricket match fixture details (teams, dates, venues) and requests a poster for Instagram. Supports single-match and multi-match (2-4) designs with modern angled layouts.
---

# LDCC Fixture Poster Maker

Generate professional fixture posters for London Desperados CC using Nano Banana Pro (AI image generation).

## Quick Reference

**Match Count → Design Choice:**
- **1 match** → Modern horizontal angled bar layout
- **2-4 matches** → Stacked card layout with different colors per match

**Key Design Elements:**
- Modern angled edges (NO straight boxes)
- Team name: "London Desperados" (drop CC)
- Dark background with gold cricket elements
- Output: EXACTLY 1012x1280 pixels (portrait PNG)
- Home/Away: HOME = LDCC left, AWAY = LDCC right

**Branding:**
- Desperados shield logo, sponsor logos (KodeKloud, Rayyan, Global Sports Link)
- www.londondesperados.com | @londondesperados | LIVE STREAMING badge

## Workflow

**Step 1: Count matches and parse fixture details**

**Step 2: Generate at 2K resolution**
```bash
cd /data/.openclaw/workspace/cricket-poster-generator
python3 /data/.openclaw/workspace/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "<use template below>" \
  --input-image "output/TEMPLATE-final.png" \
  --filename "output/fixture-temp.png" \
  --resolution 2K
```

**Step 3: Resize to exact Instagram dimensions**
```bash
python3 -c "
from PIL import Image
img = Image.open('output/fixture-temp.png')
img_resized = img.resize((1012, 1280), Image.Resampling.LANCZOS)
img_resized.save('output/fixture-YYYY-MM-DD-final.png')
print('Resized to 1012x1280')
"
```

## Prompt Templates

### Single Match Design

```
Create a PORTRAIT cricket fixture poster with modern angled design:

Dark black background with subtle gold cricket elements (bat, ball, stumps) in decorative curves at corners.

Top: Red angled banner (diagonal right edge) with Desperados shield logo on left, large gold 'WEEKEND FIXTURE' text.

SINGLE MATCH - modern angled bar design:
Red angled banner (slanted edges): '[DAY] [DATE] | [TEAM/FORMAT]'

[COLOR] angled bar with dynamic diagonal edges (not straight boxes):
'[OPPONENT TEAM]' (left side, italic [color] text) VS (bold red) 'LONDON DESPERADOS' (right side, italic white text)

White angled bar below with diagonal edges: 'Venue: [VENUE] ([HOME/AWAY])' in black text

Bottom section: Three sponsor logos in white angled boxes with diagonal edges (KodeKloud, Rayyan, Global Sports Link)
Footer: 'WWW.LONDONDESPERADOS.COM' and '@LONDONDESPERADOS' in white
'LIVE STREAMING' badge with play button bottom right corner

Design: Modern angled geometric design, NO straight rectangular boxes, all elements have dynamic diagonal/slanted edges, elegant dark background with gold decorative cricket elements, sleek contemporary look. PORTRAIT orientation for Instagram.
```

**Color suggestions:** Blue/cyan, green, purple, orange

### Multi-Match Design

```
Create a PORTRAIT weekend fixture poster for Instagram with [EXACTLY TWO/THREE/FOUR] match cards stacked vertically:

CARD 1 ([HOME/AWAY] - blue/cyan theme):
[DAY] [DATE] | [TEAM NAME] - [FORMAT]
[TEAM 1] vs [TEAM 2]
VENUE: [VENUE] ([HOME/AWAY])

CARD 2 ([HOME/AWAY] - green theme):
[DAY] [DATE] | [TEAM NAME] - [FORMAT]
[TEAM 1] vs [TEAM 2]
VENUE: [VENUE] ([HOME/AWAY])

[Add CARD 3 (orange) and CARD 4 (purple) as needed]

Design: Red/black/gold Desperados branding. Typography-focused with bold team names and diagonal color blocks. Each card DIFFERENT color (blue, green, orange, purple). Use "London Desperados" (no CC). Desperados shield logo top left. Three sponsor logos at bottom (KodeKloud, Rayyan, Global Sports Link). Website www.londondesperados.com and Instagram @londondesperados at bottom. PORTRAIT orientation for Instagram.
```

**Critical:** Specify exact card count ("EXACTLY TWO CARDS", etc.) to ensure all matches appear.

## Common Issues

**Wrong design for match count:**
- Single match with card layout looks empty → Use horizontal angled bars
- Multi-match without specified card count → AI may skip matches

**Boxy look:**
- Specify "NO straight rectangular boxes" and "angled/diagonal edges" in prompt

**Wrong orientation:**
- Always specify "PORTRAIT" explicitly

**Team name:**
- Use "London Desperados" (never "London Desperados CC")

**Dimensions:**
- Always resize to EXACTLY 1012x1280 after generation

## Files

- **Working directory:** `/data/.openclaw/workspace/cricket-poster-generator/`
- **Template:** `output/TEMPLATE-final.png`
- **Output:** `output/fixture-YYYY-MM-DD-final.png`
- **References:** `references/` (approved examples)
