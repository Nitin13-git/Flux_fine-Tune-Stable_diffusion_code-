# Install the fal-client first
!pip install fal-client

import fal
import json

# Configure FAL API credentials
fal.config({
    'credentials': 'PASTE_YOUR_FAL_KEY_HERE',  # Insert your FAL API key here
})

# Establish connection to the FAL API
connection = fal.realtime.connect("fal-ai/fast-lcm-diffusion")

# Function to handle results
def handle_result(result):
    print("Result received:", result)

# Function to handle errors
def handle_error(error):
    print("Error encountered:", error)

# Assign the result and error handlers
connection.on_result = handle_result
connection.on_error = handle_error

# Load the JSON file containing the image URLs and prompts
with open('image_prompts.json', 'r') as f:
    image_prompts = json.load(f)

# Iterate through the JSON data and send each image and prompt to FAL.ai
for idx, image_data in enumerate(image_prompts):
    print(f"Sending image {idx+1}...")
    connection.send({
        'prompt': image_data['prompt'],
        'sync_mode': True,  # Sync mode is enabled for real-time result handling
        'image_url': image_data['image_url'],  # Base64-encoded image URL
    })

print("All prompts have been sent.")

