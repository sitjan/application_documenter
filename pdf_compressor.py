from pypdf import PdfReader, PdfWriter

MAX_SIDE = 1600   # largest image width or height, in pixels
QUALITY = 70      # JPEG quality, 60 to 75 gives good size reduction


#name your input file
reader = PdfReader("input.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

for page in writer.pages:
    # Re-compress each image
    for img in page.images:
        pil_image = img.image              # PIL Image, not raw bytes
        if pil_image.mode not in ("RGB", "L"):
            pil_image = pil_image.convert("RGB")
        pil_image.thumbnail((MAX_SIDE, MAX_SIDE))   # only makes the image smaller
        img.replace(pil_image, quality=QUALITY)

    # Compress the page content stream
    page.compress_content_streams()

# Remove duplicate and unused objects
writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)


#name your output pdf file after compression
with open("your_output_file.pdf", "wb") as f:
    writer.write(f)