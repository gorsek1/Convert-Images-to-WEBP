# Image to WebP Converter

This tool converts all supported image files in a directory to WebP format. WebP is a modern image format that provides superior lossless and lossy compression for images on the web, resulting in smaller file sizes while maintaining visual quality.

## Supported Image Formats

- JPEG/JPG
- PNG
- GIF
- TIFF
- BMP

## Requirements

- Python 3.6 or higher
- Pillow library (will be installed automatically by the batch file)

## How to Use

### Windows Users (Easiest Method)

1. Simply double-click the `convert_images.bat` file
2. The batch file will:
   - Find Python on your system
   - Install the required Pillow library if needed
   - Run the conversion script with a quality setting of 85 (good balance of quality and file size)

### Manual Method (All Platforms)

1. Make sure Python is installed on your system
2. Install the Pillow library:
   ```
   pip install pillow
   ```
3. Run the script:
   ```
   python image_convert_to_webp.py
   ```
4. Optionally, you can specify the quality (0-100):
   ```
   python image_convert_to_webp.py 90
   ```

## Features

- Automatically converts all supported image files in the current directory
- Preserves original files
- Handles transparency in PNG files
- Skips files that are already in WebP format
- Skips conversion if a WebP version already exists
- Uses parallel processing for faster conversion

## Notes

- The default quality setting is 80 if not specified
- Higher quality values (closer to 100) result in better image quality but larger file sizes
- Lower quality values (closer to 0) result in smaller file sizes but lower image quality
- A value of 85-90 is recommended for most use cases

## Troubleshooting

If you encounter any issues:

1. Make sure Python is installed correctly
2. Try installing Pillow manually: `pip install pillow`
3. Check if you have write permissions in the directory
4. For PNG files with transparency, the script will convert them to RGB with a white background 