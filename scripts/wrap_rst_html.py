#!/usr/bin/env python3
"""
Script to wrap RST-generated HTML with Jekyll-style layout
"""
import os
import re
import sys

def extract_body_content(html_content):
    """Extract body content from RST-generated HTML"""
    # Remove style tags
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL)
    
    # Extract body content
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL)
    if body_match:
        return body_match.group(1).strip()
    return ""

def extract_title(html_content):
    """Extract title from HTML"""
    title_match = re.search(r'<title>(.*?)</title>', html_content)
    if title_match:
        return title_match.group(1)
    return "Conf Parser Workspace"

def minify_css(css_content):
    """Minify CSS by removing comments, extra whitespace, and newlines"""
    # Remove comments (/* ... */)
    css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    # Remove extra whitespace and newlines
    css_content = re.sub(r'\s+', ' ', css_content)
    # Remove whitespace around specific characters
    css_content = re.sub(r'\s*([{}:;,])\s*', r'\1', css_content)
    # Remove trailing semicolons before closing braces
    css_content = re.sub(r';}', '}', css_content)
    # Remove leading/trailing whitespace
    css_content = css_content.strip()
    return css_content

def get_minimal_css():
    """Get minimal essential CSS for basic styling (admonitions, tables, etc.)"""
    minimal_css = """
/* Minimal essential styles */
.admonition,.note,.warning,.danger,.important,.tip,.hint,.attention,.caution,.error{
  margin:20px 0;padding:16px 20px;border-radius:8px;border-left:4px solid;
  background:#f8fafc;box-shadow:0 2px 4px rgba(0,0,0,0.1)
}
.admonition-title{font-weight:600;margin:0 0 8px 0;font-size:1.05em}
.note{border-left-color:#3b82f6;background:#eff6ff}
.note .admonition-title{color:#1e40af}
.warning{border-left-color:#f59e0b;background:#fffbeb}
.warning .admonition-title{color:#92400e}
.danger{border-left-color:#ef4444;background:#fef2f2}
.danger .admonition-title{color:#991b1b}
.important{border-left-color:#8b5cf6;background:#f5f3ff}
.important .admonition-title{color:#5b21b6}
.tip{border-left-color:#10b981;background:#f0fdf4}
.tip .admonition-title{color:#065f46}
.hint{border-left-color:#06b6d4;background:#ecfeff}
.hint .admonition-title{color:#164e63}
.attention{border-left-color:#f59e0b;background:#fffbeb}
.attention .admonition-title{color:#92400e}
.caution{border-left-color:#f59e0b;background:#fffbeb}
.caution .admonition-title{color:#92400e}
.error{border-left-color:#ef4444;background:#fef2f2}
.error .admonition-title{color:#991b1b}
table.docutils,table{width:100%;border-collapse:collapse;margin:20px 0;border:1px solid #e5e7eb}
table.docutils th,table.docutils td,table th,table td{padding:12px 16px;text-align:left;border:1px solid #e5e7eb}
table.docutils thead,table thead{background:#3b82f6;color:#fff}
table.docutils tbody tr:nth-child(even),table tbody tr:nth-child(even){background:#f9fafb}
pre{background:#f3f4f6;border:1px solid #e5e7eb;border-radius:8px;padding:16px;overflow-x:auto;margin:16px 0;font-family:monospace}
code{background:#f3f4f6;padding:2px 6px;border-radius:4px}
"""
    return minify_css(minimal_css)

def read_css_file(css_path, minimal=False):
    """Read and minify CSS file content"""
    if minimal:
        return get_minimal_css()
    
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
        return minify_css(css_content)
    except FileNotFoundError:
        print(f"Warning: CSS file not found at {css_path}, using minimal styles", file=sys.stderr)
        return get_minimal_css()
    except Exception as e:
        print(f"Warning: Error reading CSS file: {e}, using minimal styles", file=sys.stderr)
        return get_minimal_css()

def main():
    # Parse arguments
    no_style = False
    args = []
    
    for arg in sys.argv[1:]:
        if arg == '--no-style':
            no_style = True
        else:
            args.append(arg)
    
    if len(args) != 2:
        print("Usage: wrap_rst_html.py [--no-style] <input.html> <output.html>")
        print("  --no-style: Generate HTML without any CSS styling")
        sys.exit(1)
    
    input_file = args[0]
    output_file = args[1]
    
    # Read input HTML
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extract components
    body_content = extract_body_content(html_content)
    title = extract_title(html_content)
    
    # Build head section
    if no_style:
        # Use minimal CSS for essential elements (admonitions, tables, code blocks)
        css_content = read_css_file(None, minimal=True)
        head_section = f'''  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title}</title>
    <style>
{css_content}
    </style>
  </head>'''
    else:
        # Determine CSS file path relative to script location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        css_path = os.path.join(project_root, 'assets', 'css', 'style.css')
        
        # Read CSS content
        css_content = read_css_file(css_path)
        
        head_section = f'''  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title}</title>
    <style>
{css_content}
    </style>
  </head>'''
    
    # Create Jekyll-style HTML
    output = f'''<!DOCTYPE html>
<html lang="en">
{head_section}
  <body>
    <button class="toc-toggle" onclick="document.querySelector('.page-toc')?.classList.toggle('open')">☰</button>
    <aside class="page-toc">
      <div class="toc-content">
        <h3>Table of Contents</h3>
        <ul class="toc-list" id="toc-list"></ul>
      </div>
    </aside>
    <div class="content-wrapper">
      <main>
{body_content}
      </main>
    </div>
    <script>
      // Scroll to top on page load (unless there's a hash in URL)
      if (!window.location.hash) {{
        window.scrollTo(0, 0);
        // Also scroll after a short delay to ensure DOM is ready
        setTimeout(function() {{
          window.scrollTo(0, 0);
        }}, 0);
      }}
      
      // Generate table of contents from headings
      document.addEventListener('DOMContentLoaded', function() {{
        // Scroll to top if no hash in URL
        if (!window.location.hash) {{
          window.scrollTo(0, 0);
        }}
        
        // Convert paragraphs containing only --- to horizontal rules
        const paragraphs = document.querySelectorAll('main p');
        paragraphs.forEach(function(p) {{
          const text = p.textContent.trim();
          if (text === '---' || text === '----') {{
            const hr = document.createElement('hr');
            p.parentNode.replaceChild(hr, p);
          }}
        }});
        
        const tocList = document.getElementById('toc-list');
        if (!tocList) return;
        
        // Show only h1 (main categories), max depth: 1
        const maxDepth = 1;
        const headings = document.querySelectorAll('main h1');
        if (headings.length === 0) {{
          tocList.parentElement.parentElement.style.display = 'none';
          return;
        }}
        
        headings.forEach((heading, index) => {{
          const id = heading.id || 'heading-' + index;
          if (!heading.id) heading.id = id;
          
          const level = parseInt(heading.tagName.charAt(1));
          // Only include h1 (main categories)
          if (level === 1) {{
            const li = document.createElement('li');
            li.className = 'toc-level-' + level;
            li.style.fontWeight = 'bold';
            li.style.marginTop = '8px';
            li.innerHTML = '<a href="#' + id + '">' + heading.textContent + '</a>';
            tocList.appendChild(li);
          }}
        }});
        
        // Final scroll to top if no hash (after DOM manipulation)
        if (!window.location.hash) {{
          setTimeout(function() {{
            window.scrollTo(0, 0);
          }}, 100);
        }}
      }});
    </script>
  </body>
</html>'''
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)

if __name__ == '__main__':
    main()

