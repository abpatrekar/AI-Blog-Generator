from ai_module import generate_blog_post

# Test the generate_blog_post function
if __name__ == "__main__":
    # Provide a topic for testing
    topic = "Artificial Intelligence"
    print(f"Testing generate_blog_post with topic: {topic}")
    
    try:
        # Call the function and print the result
        blog_content = generate_blog_post(topic)
        print("\nGenerated Blog Content:")
        print(blog_content)
    except Exception as e:
        # Print any errors encountered
        print(f"Error occurred: {e}")
