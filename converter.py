import os
import time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from PIL import Image

# Configuration
INPUT_FOLDER = "to-convert"
OUTPUT_FOLDER = "converted"
EXTENSIONS = {".png", ".jpg", ".jpeg"}
QUALITY = 80  # WebP quality (0-100)

def convert_image(file_path):
    """
    Converts a single image file to WebP format.
    """
    try:
        path = Path(file_path)
        filename = path.stem
        output_path = Path(OUTPUT_FOLDER) / f"{filename}.webp"
        
        # Open and convert
        with Image.open(path) as img:
            # If image has transparency (RGBA) and is saved as simple WebP, it usually handles it well.
            # But converting RGB->WebP is also standard.
            
            # Check dimensions and resize if too large
            if img.width > 2048 or img.height > 2048:
                old_w, old_h = img.width, img.height
                new_width = int(old_w * 0.70)
                new_height = int(old_h * 0.70)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                print(f"   ⚠️ Resized {filename} (was {old_w}x{old_h} -> {new_width}x{new_height})")

            # Simple optimization by saving directly
            img.save(output_path, "WEBP", quality=QUALITY, method=6)
            
        original_size = path.stat().st_size / 1024
        new_size = output_path.stat().st_size / 1024
        
        print(f"✅ Converted: {filename} ({original_size:.1f}KB -> {new_size:.1f}KB)")
        return True
    except Exception as e:
        print(f"❌ Error converting {file_path}: {e}")
        return False

def main():
    # Ensure directories exist
    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)
        print(f"Created '{INPUT_FOLDER}' directory. Please put images there.")
        return

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Gather files
    files_to_process = []
    for root, _, files in os.walk(INPUT_FOLDER):
        for file in files:
            if Path(file).suffix.lower() in EXTENSIONS:
                files_to_process.append(os.path.join(root, file))

    if not files_to_process:
        print(f"No images found in '{INPUT_FOLDER}'. Add .png, .jpg, or .jpeg files to start.")
        return

    print(f"Found {len(files_to_process)} images. Starting conversion...")
    start_time = time.time()

    # Process in parallel using all available CPU cores
    # ProcessPoolExecutor is generally better for CPU-bound tasks like image processing
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(convert_image, files_to_process))

    elapsed = time.time() - start_time
    success_count = sum(results)
    
    print(f"\n🎉 Finished! Converted {success_count}/{len(files_to_process)} images in {elapsed:.2f} seconds.")
    print(f"Images are waiting in the '{OUTPUT_FOLDER}' folder.")

if __name__ == "__main__":
    main()
