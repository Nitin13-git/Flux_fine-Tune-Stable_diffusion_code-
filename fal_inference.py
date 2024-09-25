#pip install fal-client
export FAL_KEY="PASTE_YOUR_FAL_KEY_HERE"
import fal_client
 
handler = fal_client.submit(
    "fal-ai/lora",
    arguments={
        "model_name": "stabilityai/stable-diffusion-xl-base-1.0",
        # you can repliace with your finetune model name
        "prompt": "photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang"
    },
)
 
result = handler.get()
print(result)