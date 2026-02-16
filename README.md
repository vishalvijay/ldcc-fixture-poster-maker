# LDCC Fixture Poster Maker

**OpenClaw AgentSkill** for generating Instagram-ready weekend fixture posters for London Desperados Cricket Club.

## Overview

Automated poster generation combining AI image generation (Nano Banana Pro) with vision-based logo overlay. Creates professional cricket fixture posters with real high-resolution sponsor logos at exact Instagram dimensions (1012x1280 pixels).

## Features

- ✅ Generates 1-4 match fixture posters
- ✅ Modern vibrant gradient backgrounds with bold 3D typography
- ✅ AI-generated layout with text placeholders
- ✅ Vision-based coordinate detection
- ✅ Automated logo overlay with smart text erasure
- ✅ Exact dimensions: 1012x1280 pixels (Instagram portrait)
- ✅ Red/white Desperados branding
- ✅ Different color scheme per match (blue/cyan, green, orange, purple)
- ✅ Automatic home/away positioning

## Requirements

- OpenClaw installed and configured
- [nano-banana-pro skill](https://clawhub.com) (Gemini 3 Pro Image generation)
- Python 3 with PIL/Pillow
- Vision model access

## Installation

```bash
# Install via ClawHub
clawhub install ldcc-fixture-poster-maker

# Or manually
cd ~/.openclaw/workspace/skills/
git clone https://github.com/yourusername/ldcc-fixture-poster-maker.git
```

## Usage

Send fixture text to your OpenClaw agent via Telegram/messaging:

```
Create LDCC fixture poster

London Desperados CC Season 2025

MCCL SATURDAY TEAM 1
Date: 30th August'25 (Saturday)
Format: 45 Overs League Match
Opposition: New Calypsonians
Venue: London Marathon Playing Fields (HOME)
...

MCCL SATURDAY TEAM 2
Date: 30th August'25 (Saturday)
Format: 45 Overs League Match
Opposition: Alexandra Park
Venue: Racecourse Ground (AWAY)
...
```

The agent will:
1. Parse fixture details and count matches
2. Generate poster with text placeholders at 2K resolution
3. Resize to exactly 1012x1280 pixels
4. Use vision model to detect placeholder coordinates
5. Erase placeholder text and overlay real high-res logos
6. Send back the Instagram-ready branded PNG

## Technical Details

### Workflow

1. **AI Generation:** Nano Banana Pro (Gemini 3 Pro Image) generates poster at 2K with text placeholders:
   - "DESPERADOS LOGO" (top banner)
   - "KODEKLOUD LOGO", "RAYYAN LOGO", "GLOBAL SPORTS LINK LOGO" (bottom)

2. **Resize:** Python/PIL resizes to exact Instagram dimensions (1012x1280)

3. **Vision Detection:** Use vision model to identify bounding boxes for all placeholders

4. **Logo Overlay:** Post-processing script (`scripts/overlay_logos.py`):
   - Erases placeholder text (white pixel detection)
   - Overlays real PNG logos with transparency
   - Handles padding and aspect ratio preservation

5. **Output:** Fully branded Instagram-ready poster

### Design Specifications (Feb 2026)

- **Dimensions:** EXACTLY 1012x1280 pixels
- **Orientation:** Portrait
- **Background:** Stunning vibrant gradients (e.g., Deep Midnight Blue → Electric Purple) with abstract light streaks and geometric glow effects
- **Typography:** Extra bold 3D stylized text with thick black outline strokes (sports broadcast style)
- **Layout:** Modern angled geometric design (NO straight rectangular boxes)
- **Match Count:**
  - 1 match → Horizontal angled bar layout
  - 2-4 matches → Stacked card layout with different colors
- **Branding:**
  - Desperados shield logo (top left banner)
  - Sponsors: KodeKloud, Rayyan, Global Sports Link (bottom)
  - www.londondesperados.com | @londondesperados | LIVE STREAMING badge
- **Team Name:** "London Desperados" (drop CC)
- **Positioning:** HOME = LDCC left, AWAY = LDCC right

### Match Card Color Scheme

- **Card 1:** Blue/Cyan
- **Card 2:** Green
- **Card 3:** Orange
- **Card 4:** Purple

## File Structure

```
ldcc-fixture-poster-maker/
├── SKILL.md              # Full skill documentation & prompts
├── README.md             # This file
├── assets/               # High-res logo files
│   ├── desperados.png
│   ├── kodekloud.png
│   ├── rayyan.png
│   └── globalsports.png
├── scripts/              # Post-processing tools
│   └── overlay_logos.py  # Vision-based logo overlay
└── references/           # Approved poster examples
```

## Examples

See `references/` folder for approved design examples.

## Output Location

Generated posters are saved to:
```
/data/.openclaw/workspace/cricket-poster-generator/output/
```

Naming convention:
- `fixture-YYYY-MM-DD-temp.png` (2K AI-generated with placeholders)
- `fixture-YYYY-MM-DD-final.png` (Resized 1012x1280)
- `fixture-YYYY-MM-DD-BRANDED.png` (Final with real logos)

## Club Information

- **Website:** [www.londondesperados.com](https://www.londondesperados.com)
- **Instagram:** [@londondesperados](https://instagram.com/londondesperados)
- **Play Cricket:** [londondesperados.play-cricket.com](https://londondesperados.play-cricket.com/Matches)

## Design Philosophy

High-energy, modern sports poster aesthetic. No luxury/ornate elements. Bold, impactful typography with thick outlines for maximum readability. Vibrant gradients over dark/cluttered backgrounds. Clean angled geometric layouts.

## License

MIT

## Author

Created for London Desperados Cricket Club  
Maintained by YoMan 💪 (OpenClaw Agent)
