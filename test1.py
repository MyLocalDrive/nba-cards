from groq import Groq

# Initialize the client
client = Groq(
    api_key='',
)

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
                    {"type": "text", "text": f"This is the {'front' if i == 0 else 'back'} of an NBA player card. Please extract the player's details like Name of player , in which team,Parallel/Variety."},
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
