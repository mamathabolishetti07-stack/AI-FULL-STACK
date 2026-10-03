import torch 
from diffusers import StableDiffusionPipeline

pipe=StableDiffusionPipeline . from_pretrained(
    "segmind/tiny-sd",
    torch_dtype= torch.float32
)

image = pipe(
    "a dog wearing sunglasses",
    num_inference_steps = 20
).images[0]

image.save("demo.png")
print("Image generated and saved as demo.png")