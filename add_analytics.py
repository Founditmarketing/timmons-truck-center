import os
import re

# The Vercel Analytics script to add
analytics_script = """	<!-- Vercel Web Analytics -->
	<script defer src="https://cdn.vercel-insights.com/v1/script.js"></script>
"""

def add_analytics_to_html(file_path):
    """Add Vercel Analytics script to an HTML file if not already present."""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Check if analytics is already added
    if 'vercel-insights.com' in content or 'cdn.vercel-insights.com' in content:
        print(f"Skipping {file_path} - Analytics already present")
        return False
    
    # Find </head> tag and add script before it
    if '</head>' in content:
        content = content.replace('</head>', analytics_script + '</head>')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added analytics to {file_path}")
        return True
    else:
        print(f"Warning: No </head> tag found in {file_path}")
        return False

def main():
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        # Skip .git directory
        if '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"Found {len(html_files)} HTML files")
    
    modified_count = 0
    for html_file in html_files:
        if add_analytics_to_html(html_file):
            modified_count += 1
    
    print(f"\nModified {modified_count} files")

if __name__ == '__main__':
    main()
