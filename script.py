import os

blogs_directory = 'blogs/'

# Define the template for the blog card
blog_card_template = """
<li>
    <a href="{blog_url}">
        {blog_title}
    </a>
</li>
<!-- REPLACE_WITH_BLOG_CARDS -->
"""

# List all files in the 'blogs' directory
blog_files = os.listdir(blogs_directory)

# Initialize an empty string to store the updated HTML content
updated_html_content = ""

# Loop through the blog files and generate card links
for blog_file in blog_files:
    if blog_file.endswith('.pdf') or blog_file.endswith('.docx'):
        # Extract the blog title (without the file extension)
        blog_title = os.path.splitext(blog_file)[0]
        
        # Define the URL to the blog file
        blog_url = os.path.join(blogs_directory, blog_file)

# Read the existing index.html content
with open('index.html', 'r') as index_file:
    existing_html_content = index_file.read()

# Replace the placeholder in the existing HTML with the updated content
updated_html = existing_html_content.replace('<!-- REPLACE_WITH_BLOG_CARDS -->', updated_html_content)

# Write the updated HTML content back to the index.html file
with open('index.html', 'w') as index_file:
    index_file.write(updated_html)

# Commit and push the changes to your repository using Git, as shown in the previous GitHub Actions step
