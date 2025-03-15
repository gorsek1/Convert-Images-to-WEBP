#!/usr/bin/env python3
"""
Image to WebP Converter

This script converts all supported image files in the current directory to WebP format.
Supported formats: JPEG, JPG, PNG, GIF, TIFF, BMP

REQUIREMENTS:
- Python 3.6 or higher
- Pillow library (pip install pillow)

USAGE:
1. Make sure Python is installed on your system
2. Install the Pillow library: pip install pillow
3. Run this script: python image_convert_to_webp.py
4. Optionally, you can specify the quality (0-100): python image_convert_to_webp.py 90
"""

import os
import sys
from pathlib import Path

# Check if Pillow is installed, if not provide clear instructions
try:
    from PIL import Image
except ImportError:
    print("ERROR: The Pillow library is not installed.")
    print("Please install it using one of these commands:")
    print("  pip install pillow")
    print("  python -m pip install pillow")
    print("  py -m pip install pillow")
    sys.exit(1)

import concurrent.futures

# Supported image formats
SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp'}

def convert_to_webp(image_path, quality=80):
    """
    Convert an image to WebP format
    
    Args:
        image_path: Path to the image file
        quality: WebP quality (0-100)
        
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Get the output filename
        output_filename = image_path.with_suffix('.webp')
        
        # Skip if the file is already a WebP or if the WebP version already exists
        if image_path.suffix.lower() == '.webp' or output_filename.exists():
            print(f"Skipping: {image_path.name} (already WebP or WebP version exists)")
            return False
            
        # Open the image
        with Image.open(image_path) as img:
            # Convert to RGB if the image is in RGBA mode (for PNG transparency)
            if img.mode == 'RGBA':
                # Create a white background
                background = Image.new('RGB', img.size, (255, 255, 255))
                # Paste the image on the background
                background.paste(img, mask=img.split()[3])  # 3 is the alpha channel
                # Save as WebP
                background.save(output_filename, 'WEBP', quality=quality)
            else:
                # Save as WebP
                img.save(output_filename, 'WEBP', quality=quality)
                
        print(f"Converted: {image_path.name} -> {output_filename.name}")
        return True
    except Exception as e:
        print(f"Error converting {image_path.name}: {e}")
        return False

def main():
    # Get quality from command line argument if provided
    quality = 80  # Default quality
    if len(sys.argv) > 1:
        try:
            quality = int(sys.argv[1])
            if quality < 0 or quality > 100:
                print("Quality must be between 0 and 100. Using default quality of 80.")
                quality = 80
        except ValueError:
            print("Invalid quality value. Using default quality of 80.")
    
    print(f"Using WebP quality: {quality}")
    
    # Get the current directory
    current_dir = Path('.')
    
    # Find all image files
    image_files = []
    for ext in SUPPORTED_FORMATS:
        image_files.extend(current_dir.glob(f"*{ext}"))
        image_files.extend(current_dir.glob(f"*{ext.upper()}"))
    
    if not image_files:
        print("No supported image files found in the current directory.")
        return
    
    print(f"Found {len(image_files)} image files to convert.")
    
    # Convert images in parallel using a thread pool
    successful_conversions = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit all conversion tasks
        future_to_file = {executor.submit(convert_to_webp, img_file, quality): img_file for img_file in image_files}
        
        # Process results as they complete
        for future in concurrent.futures.as_completed(future_to_file):
            if future.result():
                successful_conversions += 1
    
    print(f"\nConversion complete! {successful_conversions} of {len(image_files)} files converted to WebP.")
    print("Original files have been preserved.")
    
    # Pause at the end if running from Windows Explorer
    if os.name == 'nt' and not sys.stdin.isatty():
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
