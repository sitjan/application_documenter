import io
import img2pdf
from PIL import Image

#in the list you could name your single file or the list of the files that are in jpg format (use -ls command to list them for easy copy)
images = ["file.jpg"]


compressed_images = []

for img_path in images:
    img = Image.open(img_path).convert("RGB")
    
    # Optional: Resize if images are huge (keeps aspect ratio)
    img.thumbnail((1600, 1600))
    
    # Compress to JPEG in memory (lower quality = smaller file)(75 remains best for lower dimension images)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=60, optimize=True)
    compressed_images.append(buf.getvalue())

#for the output, name your file
with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert(compressed_images))
