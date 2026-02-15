# Fixture Text Parsing Guide

## Standard Format

London Desperados fixture announcements follow this pattern:

```
London Desperados CC Season YYYY

MCCL SATURDAY TEAM 1
Date: [DATE]
Format: [FORMAT]
Opposition: [TEAM NAME]
Venue: [ADDRESS] (HOME/AWAY)
Match Time: [TIME]

MCCL SATURDAY TEAM 2
Date: [DATE]
Format: [FORMAT]
Opposition: [TEAM NAME]
Venue: [ADDRESS] (HOME/AWAY)
Match Time: [TIME]

SUNDAY ESL TEAM
Date: [DATE]
Format: [FORMAT]
Opposition: [TEAM NAME]
Venue: [ADDRESS] (HOME/AWAY)
Match Time: [TIME]
```

## Key Extraction Points

### Date
- Extract: `30th August'25` → Format as: `30TH AUGUST'25 (SATURDAY)`
- Include day of week in output

### Team Name
- Extract opposition team name only
- Remove "Cricket Club", "CC", etc. suffixes for brevity

### Format
- Extract: `45 Overs League Match` → Simplify to: `45 OVERS`
- Or: `100 Overs Timed League Match` → `100 OVERS TIMED`

### Venue
- Extract main location, abbreviate long addresses
- Example: `London Marathon Playing Fields, Birkbeck Avenue, Greenford, Middlesex, UB6 8LS` → `THE HUB, REGENTS PARK`
- Keep postcode for clarity

### Home/Away
- Look for `(HOME)` or `(AWAY)` marker in venue line
- Critical for positioning London Desperados correctly

## Match Count

Typical weekend fixtures:
- **2 matches:** Both Saturday teams
- **3 matches:** Saturday Team 1, Saturday Team 2, Sunday ESL
- **4 matches:** Rare, includes Sunday Team 2

Always count ALL match sections in the fixture text and include them all.

## Example Parsing

**Input:**
```
MCCL SATURDAY TEAM 1
Date: 23rd August'25 (Saturday)
Format: 45 Overs League Match
Opposition: Ealing Hanwellians
Venue: Rectory Park, Ruislip Road, Northolt, Middlesex, UB5 6AU (AWAY)
Match Time: 11:30
```

**Extracted:**
- Date: `23RD AUGUST'25 (SATURDAY)`
- Format: `45 OVERS`
- Opposition: `EALING HANWELLIANS`
- Venue: `RECTORY PARK, NORTHOLT, UB5 6AU`
- Home/Away: `AWAY` → London Desperados on RIGHT side
