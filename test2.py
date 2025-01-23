from groq import Groq

# Initialize the client
client = Groq(
    api_key='',
)

# Define the list of parallels and varieties
parallels = """
Possible Parallels and Varieties:
1. Base
2. Silver/Holo/Prizm
3. Red, Blue, Green, Gold, Black (color parallels)
4. Cracked Ice
5. Mojo
6. Scope
7. Hyper
8. Disco/Bubble
9. Genesis
10. Kaboom!
11. Downtown
12. Rookie Cards (Standard, Variations, Rookie Patch Autos)
13. Autographs (On-Card, Sticker Autos)
14. Memorabilia (Jersey, Patch, Logo Patch)
15. Printing Plates (Cyan, Magenta, Yellow, Black)
16. Numbered Cards (e.g., #/99, #/50, #/10, or 1/1)
17. 1-of-1 Cards
18. Throwback Designs
"""

# Image URLs for the front and back of the NBA card
image_urls = [
    "https://i.ebayimg.com/images/g/VS8AAOSwjdJnbbkM/s-l1600.webp",  # Front
    "https://i.ebayimg.com/images/g/T~EAAOSwIYRnbbgm/s-l960.webp",   # Back
]

# Process each image and store results
results = []

for i, url in enumerate(image_urls):
    print(f"Processing {'front' if i == 0 else 'back'} of the card...")
    completion = client.chat.completions.create(
        model="llama-3.2-11b-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": f"This is the {'front' if i == 0 else 'back'} of an NBA player card. Please extract the player's details like Name of player, Team, and Parallel/Variety. Here is a guide to possible parallels and varieties:\n{parallels}"},
                    {"type": "image_url", "image_url": {"url": url}}
                ]
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    results.append(completion.choices[0].message)

# Combine and display results
print("Results:")
for i, result in enumerate(results):
    print(f"{'Front' if i == 0 else 'Back'}: {result}")
