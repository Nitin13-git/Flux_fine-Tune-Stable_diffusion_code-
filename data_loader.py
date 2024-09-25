from datasets import load_dataset
from huggingface_hub import login
import os


os.environ["HF_API_TOKEN"] = "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"
login(token=os.environ["HF_API_TOKEN"])
dataset = load_dataset("imagefolder", data_dir="E:/Nitin_sitare_stable_diffusion/images", drop_labels=True)
dataset.push_to_hub("Nitin9sitare/Swami_vivekananda_DreamBoth_dataset")
