import httpx
import base64
import google.generativeai as genai

# Configure the Google Gemini API
genai.configure(api_key="")

# Initialize the Google Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Image URLs for the front and back of the NBA card
image_urls = [
    "https://i.ebayimg.com/images/g/aosAAOSwn0lm~ciU/s-l1600.webp",  # Front
    "https://i.ebayimg.com/images/g/R2MAAOSwFjZm~ciU/s-l960.webp",   # Back
]

# Download and encode the images
encoded_images = []
for url in image_urls:
    response = httpx.get(url)
    if response.status_code == 200:
        encoded_images.append({
            "mime_type": "image/webp",  # Update the MIME type if images are in a different format
            "data": base64.b64encode(response.content).decode("utf-8")
        })
    else:
        print(f"Failed to download image from {url}")

# Define the detailed guide for parallels and varieties
parallels_details = """
The NBA trading card industry includes a wide range of parallels and varieties, designed to offer collectors unique and often more valuable cards. Here's an overview:

1. **Base Cards**: Standard card in a set with no special finishes or numbering.
2. **Parallels**:
    - **Color Parallels**:
        - **Silver/Holo/Prizm**: Basic shiny foil cards, often common.
        - **Red, Blue, Green, Gold, Black**: Distinct colored borders or backgrounds.
        - **Gold**: Typically numbered to 10 or less.
        - **Black**: Usually the rarest, often 1-of-1.
    - **Numbered Parallels**: Cards with serial numbers (e.g., #/99, #/50, #/10, or 1/1).
    - **Foil or Finish-Based Parallels**:
        - **Cracked Ice**: Shattered glass effect.
        - **Mojo**: Intricate patterned foil.
        - **Scope**: Circular or swirling patterns.
        - **Hyper**: Shimmering with diagonal patterns.
        - **Disco/Bubble**: Dots or bubbles in the design.
3. **Special Inserts**:
    - **Genesis**: Unique patterned design.
    - **Kaboom!**: Comic book-style design.
    - **Downtown**: Detailed city-themed artwork.
4. **Rookie Cards**: Cards of players in their rookie year, often highly sought after.
5. **Autographs**: Cards signed by players (On-Card or Sticker Autos).
6. **Memorabilia**: Cards with embedded game-worn jerseys, patches, or logos.
7. **Printing Plates**: One-of-a-kind cards used in the production process (Cyan, Magenta, Yellow, Black).
8. **Throwback Designs**: Cards featuring retro designs from previous years.

Use this guide to classify and identify details from the card.
"""

prompt = f"""
The following images represent the front and back of an NBA player card. Please extract:
- **Name of the Player**
- **Team**
- **Parallel/Variety**

Here is a detailed guide to help you identify parallels and varieties:
{parallels_details}
"""

# Combine the encoded images and prompt
request_data = encoded_images + [prompt]

# Generate the response
try:
    response = model.generate_content(request_data)
    print("Response:")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
