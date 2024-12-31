import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure to set this environment variable

def generate_blog_post(topic):
    prompt = f"Write a blog post about {topic}."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,  
        max_tokens=1000,  
        top_p=1.0,  
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"], 
    )
    return response.choices[0].text.strip()
