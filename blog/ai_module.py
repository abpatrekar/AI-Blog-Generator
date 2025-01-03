import requests

# Hugging Face Inference API URL and your API token
API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-j-6B"
HEADERS = {"Authorization": f"Bearer "}#ENTER YOUR KEY HERE

def generate_blog_post(topic):
    # Create the prompt for the blog post
    prompt = f"Write a detailed blog post about {topic}."
    
    # Payload for the API
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 500,
            "temperature": 0.7,
        },
    }
    
    # Send the request to Hugging Face Inference API
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    
    if response.status_code == 200:
        # Extract and return the generated text
        return response.json()[0]['generated_text'].strip()
    else:
        # Handle errors
        return f"Error: {response.status_code} - {response.text}"

# Example usage
# Replace "YOUR_HUGGINGFACE_API_TOKEN" with your actual Hugging Face token
#blog_post = generate_blog_post("The importance of mental health awareness")
#print(blog_post)
