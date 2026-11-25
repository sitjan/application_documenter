from PIL import Image
import os


#the images are singly passed, feel free to use them as list, changes necessary in the code
def compress_image(input_path, output_path, quality=45):
    with Image.open(input_path) as img:
        # Convert RGBA (transparency) or Palette images to RGB for JPEG compatibility
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        # Save with optimization and reduced quality (1-95, 75 is a good balance)
        img.save(output_path, "JPEG", optimize=True, quality=quality)

    original_size = os.path.getsize(input_path) / 1024
    compressed_size = os.path.getsize(output_path) / 1024
    print(f"Done! Reduced from {original_size:.1f} KB to {compressed_size:.1f} KB")

# Example usage, you could name series of files in this for you to compress
compress_image("filename_1.jpg","filename_1_compressed.jpg", quality=70)
