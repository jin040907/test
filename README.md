# Conf Parser Workspace

Documentation site and helper tools for exploring `conf.yml`, invitee profiles, and student data.

## Project Overview

This workspace combines a Jekyll static site with reStructuredText (RST) documentation, providing a comprehensive documentation system with examples of YAML configuration parsing, invitee collection management, and various RST table formats.

## Project Layout

### Jekyll Site Files (Root)

- `_config.yml` - Jekyll site configuration
- `_layouts/` - HTML layouts for Jekyll pages
  - `default.html` - Main layout with TOC sidebar
  - `invitee.html` - Layout for invitee profile pages
- `_invitee/` - Jekyll collection for invitee profiles
  - `choi.md`, `jin.md` - Individual invitee profile pages
- `_data/` - Jekyll data files
  - `students.csv`, `students.yml` - Student data files
- `_static/` - Static files (images, etc.)
  - `sample-image.svg`, `random-image.svg`, `random-image.png` - Sample images used in documentation
- `assets/css/` - Stylesheet for the Jekyll site
  - `style.css` - Main stylesheet with responsive design and dark mode support
- `index.md` - Jekyll homepage
- `Gemfile`, `Gemfile.lock` - Ruby dependencies for Jekyll

### Documentation Files

- `docs/` - RST documentation
  - `index.rst` - Main documentation file (includes RST table examples)
  - `tables.rst` - Comprehensive examples of all RST table types
  - `index.html`, `tables.html` - Generated HTML documentation

### Organized Folders

- `scripts/` - Utility scripts
  - `parser.js` - YAML parser with anchor/alias support
  - `json-to-yaml.js` - JSON to YAML converter
  - `server.js` - Static file server (legacy)
  - `wrap_rst_html.py` - Python script to wrap RST-generated HTML with Jekyll styling
- `config/` - Configuration files
  - `conf.yml` - Example YAML configuration with anchors and merge keys

### Build Files

- `Makefile` - Build system for RST documentation
  - `make html` - Build all RST documentation
  - `make docs/index.html` - Build index.html only
  - `make docs/tables.html` - Build tables.html only
  - `make clean` - Remove generated HTML files
- `package.json` - Node.js dependencies
- `.gitignore` - Excludes build artefacts (`_site/`, `node_modules/`, `vendor/`, cache folders)

## Requirements

- **Ruby 2.7+** with Bundler 2.4 or newer
  ```bash
  gem install --user-install bundler -v "~> 2.4"
  ```
- **Node 18+** (optional, only if you want to run the legacy parser scripts)
- **Python 3** with docutils or Sphinx (for RST to HTML conversion)
  ```bash
  # For docutils (legacy):
  pip install docutils beautifulsoup4
  
  # For Sphinx (recommended):
  pip install -r requirements.txt
  # or
  pip install sphinx sphinx-rtd-theme docutils beautifulsoup4
  ```

## Quick Start

### Jekyll Site

1. Install Ruby dependencies:

   ```bash
   bundle install --path vendor/bundle
   ```
2. Build and serve the site:

   ```bash
   bundle exec jekyll serve
   ```
3. Open `http://127.0.0.1:4000` to browse:

   - Home page (`index.md`) describing the configuration parser
   - Invitee profiles rendered from `_invitee/`
   - Student data from `_data/students.csv`

### RST Documentation

Build HTML documentation from RST:

```bash
# Using Sphinx (recommended, if installed):
make sphinx-html             # Build with Sphinx
cd docs && make html         # Alternative: build from docs directory

# Using docutils (legacy):
make docutils-html           # Build with docutils
make docs/index.html         # Build index.html only
make docs/tables.html        # Build tables.html only

# Auto-detect (tries Sphinx first, falls back to docutils):
make html                    # Build all RST documentation

# Cleanup:
make clean                   # Remove generated HTML files
```

The generated HTML uses the same styling as the Jekyll site and includes:

- **Main documentation** (`index.rst`): Project overview, installation, usage guide, development instructions
- **RST Table Examples** (`tables.rst`): Comprehensive examples of all RST table types:
  - Grid Tables
  - Simple Tables
  - CSV Tables
  - List Tables

Open `docs/index.html` in your browser to view the documentation. The table examples are included as a section within the main documentation page.

## Optional Node Utilities

If you want to use the legacy Node.js utilities:

```bash
npm install
npm start            # Runs scripts/parser.js demo
npm run serve        # Serves static files from the project root (legacy)
```

- `scripts/parser.js` demonstrates YAML anchor handling, merge keys, and validation logic for `config/conf.yml`
- The static server is useful if you keep a prebuilt HTML front page

## Features

### Jekyll Site

- ✅ Responsive design with dark mode support
- ✅ Dynamic Table of Contents (TOC) sidebar
- ✅ Invitee collection with individual profile pages
- ✅ Student data display from CSV/YAML files
- ✅ SEO optimization with jekyll-seo-tag

### RST Documentation

- ✅ Comprehensive documentation in reStructuredText format
- ✅ Examples of all RST table types with dummy data
- ✅ Jekyll-style HTML output with consistent styling
- ✅ Table of Contents showing only major categories (h1 headings)
- ✅ Field lists, code blocks, images, and other RST features
- ✅ Footnotes examples with references throughout the document

### Build System

- ✅ Makefile for automated RST to HTML conversion
- ✅ Python wrapper script for consistent HTML styling
- ✅ Automatic TOC generation from headings
- ✅ Support for horizontal rules and custom styling

## Documentation Structure

The main documentation (`docs/index.rst`) includes:

1. **Introduction** - Project overview and goals (includes sample image)
2. **Getting Started** - Installation and setup instructions
3. **Usage Guide** - Configuration examples and usage patterns
4. **Development** - Development workflow and guidelines
5. **RST Table Examples** - Comprehensive table format examples
   - Grid Tables
   - Simple Tables
   - CSV Tables
   - List Tables
6. **RST Admonitions** - Examples of note, warning, danger, and other admonition types
7. **RST Footnotes** - Examples of footnotes with references throughout the document
8. **License** - Project license information

## Styling

The project uses a unified CSS stylesheet (`assets/css/style.css`) for both:

- Jekyll-generated pages
- RST-generated HTML documentation

Features:

- Responsive layout with mobile support
- Dark mode support (follows system preference)
- Custom styling for code blocks, tables, field lists
- Smooth scrolling and navigation
- Modern card-based design

## Housekeeping

- Generated directories (`_site/`, `node_modules/`, `vendor/`) are ignored via `.gitignore`
- Run `bundle exec jekyll clean` if you need to wipe cached Jekyll outputs
- Remove or regenerate `Gemfile.lock` only when updating gem versions
- Run `make clean` to remove generated HTML documentation files

## License

This project is part of the Open Source Software Introduction workspace.

## Contact

- **Email**: [your-email@example.com](mailto:your-email@example.com)
- **GitHub**: [GitHub Repository](https://github.com/yourusername/your-repo)

---

Feel free to extend the data sets, add new pages, or contribute to the documentation—just keep temporary build artefacts out of the repository for a tidy workspace.
