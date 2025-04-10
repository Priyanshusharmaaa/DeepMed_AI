
import streamlit as st
import openai
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image


st.set_page_config(page_title="AI Medical Image Generator", layout="centered",page_icon="🩺")
st.title("Healthcare Imaging Assistant")
st.markdown("Enter a medical description below, and AI will generate image")


openai.api_key = "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" 
openai.api_base = "https://api.groq.com/openai/v1"


user_input = st.text_input("📝 Enter a medical image description", 
                           placeholder="e.g., Frontal X-ray of chest showing pneumonia")

if st.button(" Generate Medical Image") and user_input:
    with st.spinner(" Refining prompt using LLaMA-4..."):
        try:
            response = openai.ChatCompletion.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[
                    {"role": "system", "content": "You are a medical imaging expert."},
                    {"role": "user", "content": user_input}
                ]
            )
            prompt = response['choices'][0]['message']['content']
            st.success("Prompt refined!")
            st.markdown(f"**🔍 Refined Prompt:** {prompt}")
        except Exception as e:
            st.error(f"Groq API Error: {e}")
            st.stop()

    with st.spinner("Generating image with Stable Diffusion..."):
        try:
            model_id = "runwayml/stable-diffusion-v1-5"
            pipe = StableDiffusionPipeline.from_pretrained(
                model_id,
                torch_dtype=torch.float32,
                safety_checker=None
            )

            pipe = pipe.to("cpu")

            image = pipe(prompt).images[0]
            image.save("generated_medical_image.png")

            st.image(image, caption="🩻 Generated Medical Image", use_column_width=True)
            st.success("📸 Image generated successfully!")
            with open("generated_medical_image.png", "rb") as file:
                st.download_button("⬇️ Download Image", file, "generated_medical_image.png")
        except Exception as e:
            st.error(f"Image Generation Error: {e}")
