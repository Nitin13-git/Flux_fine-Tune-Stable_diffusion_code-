#######################
pip install fal-client
import fal  # Assuming there's a Python equivalent of the @fal-ai/serverless-client

# Configure FAL API credentials
fal.config({
    'credentials': 'PASTE_YOUR_FAL_KEY_HERE',
})

# Establish connection
connection = fal.realtime.connect("fal-ai/fast-lcm-diffusion")

def handle_result(result):
    print(result)

def handle_error(error):
    print(error)

# Assign the result and error handlers
connection.on_result = handle_result
connection.on_error = handle_error

# Array of prompts and base64 images
image_prompts = [
    {
        'prompt': "an island near the sea, with seagulls, moon shining over the sea, lighthouse, boats in the background, fish flying over the sea",
        'image_url': "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==",  # Image 1 in base64
    },
    {
        'prompt': "a beautiful sunset over the mountains, with birds flying and river flowing between the mountains",
        'image_url': "data:image/png;base64,YOUR_BASE64_STRING_2_HERE",  # Image 2 in base64
    },
    {
        'prompt': "forest landscape with a clear blue lake, trees, and mountain range in the background",
        'image_url': "data:image/png;base64,YOUR_BASE64_STRING_3_HERE",  # Image 3 in base64
    },
    # Add more images and prompts as needed
]

# Send each prompt and image to the FAL connection
for image_data in image_prompts:
    connection.send({
        'prompt': image_data['prompt'],
        'sync_mode': True,
        'image_url': image_data['image_url'],
    })
