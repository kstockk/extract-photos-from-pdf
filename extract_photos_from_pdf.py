#!/usr/bin/env python

import fitz  # PyMuPDF
import os
import argparse

def extract_images_from_pdf(pdf_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)

    for page_index in range(len(doc)):
        for img_index, img in enumerate(doc.get_page_images(page_index)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            width = base_image["width"]
            height = base_image["height"]

            # Skip the logo image
            if width == 200 and height == 24:
                print(f"Skipped logo on page {page_index + 1}")
                continue

            if image_ext.lower() == "jpeg" or image_ext.lower() == "jpg":
                image_filename = f"page{page_index + 1}_img{img_index + 1}.{image_ext}"
                image_path = os.path.join(output_dir, image_filename)
                with open(image_path, "wb") as image_file:
                    image_file.write(image_bytes)
                print(f"Saved: {image_path}")

    doc.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract images from a PDF.")
    parser.add_argument("pdf_path", help="Path to the input PDF file.")
    parser.add_argument("output_dir", help="Directory to save the extracted images.")
    args = parser.parse_args()

    extract_images_from_pdf(args.pdf_path, args.output_dir)