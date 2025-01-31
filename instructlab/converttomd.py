import wikipediaapi
from markdownify import markdownify as md

def fetch_and_save_wikipedia_page(page_title, file_name):
    # Initialize the Wikipedia API with user-agent
    user_agent = "OpenllmModel (https://github.com/mcastrol/openllmmodels)"
    wiki_api = wikipediaapi.Wikipedia(language='es', user_agent=user_agent)
    
    # Fetch the page
    page = wiki_api.page(page_title)
    
    # Check if the page exists
    if not page.exists():
        print(f"The page '{page_title}' does not exist.")
        return
    
    # Convert HTML content to Markdown
    markdown_content = md(page.text)
    
    # Save as .md file
    with open(file_name, 'w', encoding='utf-8') as md_file:
        md_file.write(f"# {page_title}\n\n")  # Title of the page
        md_file.write(markdown_content)
    
    print(f"Markdown content saved to '{file_name}'.")

# Example usage
#fetch_and_save_wikipedia_page("Python (programming language)", "Python_programming_language.md")
fetch_and_save_wikipedia_page("Río_Gallegos", "Río_Gallegos.md")