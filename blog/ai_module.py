import openai
import os

# Set your OpenAI API key
#openai.api_key = ""  # Make sure to set this environment variable
def generate_blog_post(topic):
    prompt = f"Write a blog post about {topic}."
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Use "gpt-4" if needed
        messages=[
            {"role": "system", "content": "You are a helpful assistant for writing blog posts."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response['choices'][0]['message']['content'].strip()