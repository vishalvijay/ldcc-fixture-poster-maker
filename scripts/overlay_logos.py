#!/usr/bin/env python3
import os
import sys
import json
from PIL import Image, ImageDraw

# Set up paths
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO_DIR = os.path.join(SKILL_DIR, "assets")

LOGO_CONFIG = {
    "DESPERADOS LOGO": {"file": "desperados.png", "pad": 0.05, "clean": True},
    "KODEKLOUD LOGO": {"file": "kodekloud.png", "pad": 0.08, "clean": True},
    "RAYYAN LOGO": {"file": "rayyan.png", "pad": 0.08, "clean": True},
    "GLOBAL SPORTS LINK LOGO": {"file": "globalsports.png", "pad": 0.08, "clean": True}
}

def clean_logo_transparent(logo_path, should_clean):
    logo = Image.open(logo_path).convert("RGBA")
    
    if should_clean:
        logo_data = logo.getdata()
        bg_color = logo_data[0] # Top-left corner
        
        extrema = logo.getextrema()
        if extrema[3][0] == 255: # Fully opaque
            newData = []
            for item in logo_data:
                # Color distance - Use tight threshold for black/white backgrounds
                dist = sum((a - b) ** 2 for a, b in zip(item[:3], bg_color[:3]))
                if dist < 1000: 
                    newData.append((0, 0, 0, 0))
                else:
                    newData.append(item)
            logo.putdata(newData)
    
    # Trim to content
    bbox = logo.getbbox()
    if bbox:
        logo = logo.crop(bbox)
        
    return logo

def is_white_ish(pixel):
    return pixel[0] > 180 and pixel[1] > 180 and pixel[2] > 180

def overlay_logos(image_path, vision_results, output_path):
    img = Image.open(image_path).convert("RGBA")
    w, h = img.size
    
    # --- STAGE 1: ERASER STAGE (1D Horizontal Scan) ---
    pixels = list(img.getdata())
    for placeholder, coords in vision_results.items():
        if placeholder not in LOGO_CONFIG:
            continue
            
        ymin, xmin, ymax, xmax = coords
        left = max(0, int(xmin * w / 1000))
        top = max(0, int(ymin * h / 1000))
        right = min(w, int(xmax * w / 1000))
        bottom = min(h, int(ymax * h / 1000))
        
        for y in range(top, bottom):
            row_start = y * w
            whites = [x for x in range(left, right) if is_white_ish(pixels[row_start + x])]
            if len(whites) >= 2:
                for x in range(whites[0], whites[-1] + 1):
                    pixels[row_start + x] = (255, 255, 255, 255)
    
    img.putdata(pixels)

    # --- STAGE 2: LOGO STAGE ---
    for placeholder, coords in vision_results.items():
        if placeholder not in LOGO_CONFIG:
            continue
            
        config = LOGO_CONFIG[placeholder]
        logo_path = os.path.join(LOGO_DIR, config["file"])
        if not os.path.exists(logo_path):
            continue
            
        # Scaling
        ymin, xmin, ymax, xmax = coords
        left = int(xmin * w / 1000)
        top = int(ymin * h / 1000)
        right = int(xmax * w / 1000)
        bottom = int(ymax * h / 1000)
        
        # Get cleaned logo
        logo = clean_logo_transparent(logo_path, config["clean"])
        
        # Padding
        box_w = right - left
        box_h = bottom - top
        padding_pct = config["pad"]
        pad_x = int(box_w * padding_pct)
        pad_y = int(box_h * padding_pct)
        available_w = box_w - (2 * pad_x)
        available_h = box_h - (2 * pad_y)
        
        # Resize and center
        logo.thumbnail((available_w, available_h), Image.Resampling.LANCZOS)
        paste_x = left + (box_w - logo.width) // 2
        paste_y = top + (box_h - logo.height) // 2
        
        img.paste(logo, (paste_x, paste_y), logo)
        print(f"✓ {placeholder} added")

    img.convert("RGB").save(output_path, quality=95)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(1)
    with open(sys.argv[2], "r") as f:
        results = json.load(f)
    overlay_logos(sys.argv[1], results, sys.argv[3])
