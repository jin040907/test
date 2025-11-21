# Makefile for building HTML documentation from RST
# Supports both Sphinx and docutils

.PHONY: html clean help sphinx-html docutils-html

# Default target
help:
	@echo "Available targets:"
	@echo "  make html            - Build HTML using Sphinx (if available) or docutils"
	@echo "  make sphinx-html     - Build HTML using Sphinx"
	@echo "  make docutils-html   - Build HTML using docutils (legacy)"
	@echo "  make index.html      - Build HTML from index.rst only (with styles)"
	@echo "  make index-plain.html - Build HTML from index.rst without styles"
	@echo "  make tables.html     - Build HTML from tables.rst only"
	@echo "  make clean           - Remove generated HTML files"
	@echo "  make help            - Show this help message"

# Try Sphinx first, fallback to docutils
html:
	@if command -v sphinx-build >/dev/null 2>&1 && [ -f docs/conf.py ]; then \
		echo "Building with Sphinx..."; \
		cd docs && $(MAKE) html; \
	else \
		echo "Sphinx not found or conf.py missing, using docutils..."; \
		$(MAKE) docutils-html; \
	fi

# Sphinx build
sphinx-html:
	@if command -v sphinx-build >/dev/null 2>&1 && [ -f docs/conf.py ]; then \
		cd docs && $(MAKE) html; \
	else \
		echo "Error: Sphinx not installed. Install with: pip install sphinx sphinx-rtd-theme"; \
		exit 1; \
	fi

# Docutils build (legacy)
docutils-html:

# Build HTML from RST
html: docs/index.html docs/tables.html

docs/index.html: docs/index.rst scripts/wrap_rst_html.py
	@echo "Building HTML from RST..."
	@if command -v rst2html.py >/dev/null 2>&1; then \
		rst2html.py docs/index.rst docs/index.rst.tmp.html; \
	elif command -v rst2html >/dev/null 2>&1; then \
		rst2html docs/index.rst docs/index.rst.tmp.html; \
	elif command -v pandoc >/dev/null 2>&1; then \
		pandoc -f rst -t html -o docs/index.rst.tmp.html docs/index.rst; \
	else \
		echo "Error: No RST to HTML converter found."; \
		echo "Please install one of:"; \
		echo "  - docutils: pip install docutils"; \
		echo "  - pandoc: brew install pandoc (macOS) or apt-get install pandoc (Linux)"; \
		exit 1; \
	fi
	@echo "Wrapping HTML with Jekyll-style layout..."
	@python3 scripts/wrap_rst_html.py docs/index.rst.tmp.html docs/index.html
	@rm -f docs/index.rst.tmp.html
	@echo "HTML generated: docs/index.html (with Jekyll styling)"

# Build index.html without styles
docs/index-plain.html: docs/index.rst scripts/wrap_rst_html.py
	@echo "Building plain HTML from index.rst (no styles)..."
	@if command -v rst2html.py >/dev/null 2>&1; then \
		rst2html.py docs/index.rst docs/index.rst.tmp.html; \
	elif command -v rst2html >/dev/null 2>&1; then \
		rst2html docs/index.rst docs/index.rst.tmp.html; \
	elif command -v pandoc >/dev/null 2>&1; then \
		pandoc -f rst -t html -o docs/index.rst.tmp.html docs/index.rst; \
	else \
		echo "Error: No RST to HTML converter found."; \
		echo "Please install one of:"; \
		echo "  - docutils: pip install docutils"; \
		echo "  - pandoc: brew install pandoc (macOS) or apt-get install pandoc (Linux)"; \
		exit 1; \
	fi
	@echo "Wrapping HTML without styles..."
	@python3 scripts/wrap_rst_html.py --no-style docs/index.rst.tmp.html docs/index-plain.html
	@rm -f docs/index.rst.tmp.html
	@echo "Plain HTML generated: docs/index-plain.html (no styles)"

# Clean generated files
clean:
	@echo "Cleaning generated HTML files..."
	@rm -f docs/index.html docs/index-plain.html docs/tables.html docs/index.rst.tmp.html docs/tables.rst.tmp.html
	@if [ -d docs/_build ]; then \
		echo "Cleaning Sphinx build directory..."; \
		rm -rf docs/_build; \
	fi
	@echo "Clean complete."

# Build tables.html
docs/tables.html: docs/tables.rst scripts/wrap_rst_html.py
	@echo "Building HTML from tables.rst..."
	@if command -v rst2html.py >/dev/null 2>&1; then \
		rst2html.py docs/tables.rst docs/tables.rst.tmp.html; \
	elif command -v rst2html >/dev/null 2>&1; then \
		rst2html docs/tables.rst docs/tables.rst.tmp.html; \
	elif command -v pandoc >/dev/null 2>&1; then \
		pandoc -f rst -t html -o docs/tables.rst.tmp.html docs/tables.rst; \
	else \
		echo "Error: No RST to HTML converter found."; \
		echo "Please install one of:"; \
		echo "  - docutils: pip install docutils"; \
		echo "  - pandoc: brew install pandoc (macOS) or apt-get install pandoc (Linux)"; \
		exit 1; \
	fi
	@echo "Wrapping HTML with Jekyll-style layout..."
	@python3 scripts/wrap_rst_html.py docs/tables.rst.tmp.html docs/tables.html
	@rm -f docs/tables.rst.tmp.html
	@echo "HTML generated: docs/tables.html (with Jekyll styling)"

# Install Python dependencies for RST processing (optional)
install-deps:
	@echo "Installing Python dependencies..."
	@if command -v pip3 >/dev/null 2>&1; then \
		pip3 install docutils; \
	elif command -v pip >/dev/null 2>&1; then \
		pip install docutils; \
	else \
		echo "Error: pip not found. Please install Python and pip first."; \
		exit 1; \
	fi
	@echo "Dependencies installed."

