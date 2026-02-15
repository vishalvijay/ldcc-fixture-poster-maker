---
name: ldcc-fixture-poster-maker
description: Generate Instagram-ready fixture posters for London Desperados Cricket Club using AI image generation. Use when the user provides cricket match fixture details (teams, dates, venues) and requests a poster for Instagram. Supports single-match and multi-match (2-4) designs with modern angled layouts.
---

# LDCC Fixture Poster Maker

Generate professional fixture posters for London Desperados CC using Nano Banana Pro (AI image generation).

## Quick Reference

**Match Count → Design Choice:**
- **1 match** → Modern horizontal angled bar layout with bold impactful typography
- **2-4 matches** → Stacked card layout with different colors per match

**Key Design Elements:**
- **Bold impactful typography** - premium sports fonts for maximum impact
- Modern angled edges (NO straight boxes or white background sections)
- **Dark elegant background** with ornate gold cricket elements throughout
- Team name: "London Desperados" (drop CC)
- Output: EXACTLY 1012x1280 pixels (portrait PNG)
- Home/Away: HOME = LDCC left, AWAY = LDCC right

**Branding:**
- Logo placeholders with text labels for vision-based replacement:
  - "DESPERADOS LOGO" (top banner)
  - "KODEKLOUD LOGO", "RAYYAN LOGO", "GLOBAL SPORTS LINK LOGO" (bottom sponsor boxes)
- www.londondesperados.com | @londondesperados | LIVE STREAMING badge

## Design Learnings

**User Preferences (Feb 2026):**
- **"More stylish"** = darker/richer backgrounds + bold premium fonts + ornate decorative elements
- **NO white background sections** in multi-match posters - use dark elegant backgrounds throughout
- **Typography matters** - emphasize "BOLD IMPACTFUL TYPOGRAPHY" and "premium sports font" in prompts
- **Decorative elements** - add "ornate gold cricket elements" for luxury aesthetic

## Workflow

**Step 1: Count matches and parse fixture details**

**Step 2: Generate at 2K resolution with logo placeholders**
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

**Step 4: (Future) Logo replacement via vision library**
- Vision AI detects placeholder text boxes
- Replaces "DESPERADOS LOGO" with actual Desperados shield
- Replaces "KODEKLOUD LOGO", "RAYYAN LOGO", "GLOBAL SPORTS LINK LOGO" with actual sponsor logos
- Preserves layout and dimensions

## Prompt Templates

### Single Match Design

```
Create a PORTRAIT cricket fixture poster with modern luxury design and bold impactful typography:

Elegant dark black background with ornate gold cricket elements (bat, ball, stumps, cricket ball seam patterns) in decorative curves at corners.

Top: Red angled banner (dynamic diagonal right edge) with white angled box on left containing text 'DESPERADOS LOGO' in bold black font, large bold gold 'WEEKEND FIXTURE' text in premium sports font on right.

SINGLE MATCH - modern angled bar design with BOLD IMPACTFUL FONTS:
Red angled banner (sharp slanted edges): '[DAY] [DATE] | [TEAM/FORMAT]' in bold white condensed sports font

Large [COLOR] angled bar with dynamic diagonal edges (NOT straight boxes):
'[OPPONENT TEAM]' (left side, BOLD italic [color] text in modern sports font) VS (extra bold red in impact font) 'LONDON DESPERADOS' (right side, BOLD italic white text in premium sports font)

White angled bar below with diagonal edges: 'Venue: [VENUE] ([HOME/AWAY])' in bold black condensed font

Bottom section: Three white angled boxes with diagonal edges containing text placeholders in bold black font:
Left box: 'KODEKLOUD LOGO'
Middle box: 'RAYYAN LOGO'
Right box: 'GLOBAL SPORTS LINK LOGO'

Footer: 'WWW.LONDONDESPERADOS.COM' and '@LONDONDESPERADOS' in bold white font
'LIVE STREAMING' badge with play button bottom right corner

Design: Premium modern angled geometric design with BOLD IMPACTFUL TYPOGRAPHY, NO straight rectangular boxes, all elements have dynamic diagonal/slanted edges, rich dark background with elegant gold decorative cricket elements throughout, luxury contemporary sports poster aesthetic. PORTRAIT orientation for Instagram.
```

**Color suggestions:** Blue/cyan, green, purple, orange

### Multi-Match Design

```
Create a PORTRAIT weekend fixture poster for Instagram with [EXACTLY TWO/THREE/FOUR] match cards stacked vertically on an elegant DARK BLACK background with subtle gold cricket elements (bat, ball, stumps):

Top: Red angled banner with white angled box on left containing text 'DESPERADOS LOGO' in bold black font, large gold 'WEEKEND FIXTURE' text on right

CARD 1 ([HOME/AWAY] - blue/cyan theme with angled edges):
Red angled banner: '[DAY] [DATE] | [TEAM NAME] - [FORMAT]'
[COLOR] angled bar: '[TEAM 1]' (left, [color] italic text) VS (bold red) '[TEAM 2]' (right, [color] italic text)
White angled bar: 'VENUE: [VENUE] ([HOME/AWAY])' in black

CARD 2 ([HOME/AWAY] - green theme with angled edges):
Red angled banner: '[DAY] [DATE] | [TEAM NAME] - [FORMAT]'
Green angled bar: '[TEAM 1]' (left, light green italic text) VS (bold red) '[TEAM 2]' (right, [color] italic text)
White angled bar: 'VENUE: [VENUE] ([HOME/AWAY])' in black

[Add CARD 3 (orange) and CARD 4 (purple) with same structure as needed]

Bottom: Three white angled boxes with diagonal edges containing text placeholders in bold black font:
Left box: 'KODEKLOUD LOGO'
Middle box: 'RAYYAN LOGO'
Right box: 'GLOBAL SPORTS LINK LOGO'

Footer: 'WWW.LONDONDESPERADOS.COM' and '@LONDONDESPERADOS' in white
'LIVE STREAMING' badge with play button bottom right

Design: Modern angled geometric design, NO straight boxes, all elements have dynamic diagonal edges, elegant dark background with decorative gold cricket elements throughout, sleek contemporary look. Each card uses DIFFERENT color (blue, green, orange, purple). Use "London Desperados" (no CC). PORTRAIT orientation for Instagram.
```

**Critical:** Specify exact card count ("EXACTLY TWO CARDS", etc.) to ensure all matches appear.

## Common Issues

**Wrong design for match count:**
- Single match with card layout looks empty → Use horizontal angled bars
- Multi-match without specified card count → AI may skip matches

**Boxy or plain look:**
- Specify "NO straight rectangular boxes" and "angled/diagonal edges" in prompt
- Emphasize "BOLD IMPACTFUL TYPOGRAPHY" and "premium sports font"
- Add "ornate gold cricket elements" for luxury aesthetic

**White background sections:**
- Always specify "elegant DARK BLACK background" and "NO white background sections"
- User prefers rich dark backgrounds with decorative elements throughout

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
