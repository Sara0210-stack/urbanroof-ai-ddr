import fitz
import os

def extract_images(pdf_path, output_folder, max_images=30):

    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(pdf_path)

    img_count = 0

    for page_index in range(len(doc)):

        if img_count >= max_images:
            break

        page = doc.load_page(page_index)

        images = page.get_images(full=True)

        for img in images:

            if img_count >= max_images:
                break

            xref = img[0]
            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]

            image_path = f"{output_folder}/image_{img_count}.png"

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            img_count += 1