# LDCC Fixture Poster Maker

**OpenClaw AgentSkill** for generating Instagram-ready weekend fixture posters for London Desperados Cricket Club.

## Overview

Automated poster generation using AI (Nano Banana Pro / Gemini 3 Pro Image) that creates professional cricket fixture posters in the exact dimensions required for Instagram (1012x1280 pixels).

## Features

- ✅ Generates portrait posters with 2-4 match cards
- ✅ Typography-focused design with diagonal color blocks
- ✅ AI generates all elements including club and sponsor logos
- ✅ Exact dimensions: 1012x1280 pixels
- ✅ Red/black/gold Desperados branding
- ✅ Different color scheme per match (blue, green, orange, purple)
- ✅ Automatic home/away positioning

## Requirements

- OpenClaw installed and configured
- [nano-banana-pro skill](https://clawhub.com) (Gemini 3 Pro Image generation)
- Python 3 with PIL/Pillow

## Installation

```bash
# Install via ClawHub (coming soon)
clawhub install ldcc-fixture-poster-maker

# Or manually
cd ~/.openclaw/workspace/skills/
git clone https://github.com/vishalvijay/ldcc-fixture-poster-maker.git
```

## Usage

Send fixture text to your OpenClaw agent via Telegram/messaging:

```
Create LDCC fixture poster

London Desperados CC Season 2025

MCCL SATURDAY TEAM 1
Date: 12th July'25 (Saturday)
Format: 100 Overs Timed League Match
Opposition: United Sports
Venue: The Pavilion, Wembley (AWAY)
...
```

The agent will:
1. Parse all match details
2. Generate poster at 2K resolution
3. Resize to exactly 1012x1280 pixels
4. Send back the Instagram-ready PNG

## Technical Details

### Workflow

1. **AI Generation:** Nano Banana Pro generates poster at 2K resolution
2. **Resize:** Python/PIL resizes to exact dimensions (1012x1280)
3. **Output:** Perfect Instagram portrait format

### Design Specifications

- **Dimensions:** EXACTLY 1012x1280 pixels
- **Orientation:** Portrait
- **Branding:** Desperados shield logo (top left)
- **Sponsors:** KodeKloud, Rayyan Groups, Global Sports Link (bottom)
- **Match Cards:** Stacked vertically, each with unique color
- **Positioning:** HOME = Desperados left, AWAY = Desperados right

## Examples

See `references/APPROVED-2025-07-12.png` for approved design reference.

## Assets

Located in `assets/logos/`:
- `desperados-clean.jpg` - Club logo
- `kodekloud.jpg` - Sponsor logo
- `rayyan.jpg` - Sponsor logo
- `globalsports.jpg` - Sponsor logo

## Club Information

- **Website:** [www.londondesperados.com](https://www.londondesperados.com)
- **Instagram:** [@londondesperados](https://instagram.com/londondesperados)
- **Play Cricket:** [londondesperados.play-cricket.com](https://londondesperados.play-cricket.com/Matches)

## License

MIT

## Author

Created for London Desperados Cricket Club by Vishal Vijay
