Conf Parser Workspace
=====================

Documentation site and helper tools for exploring ``conf.yml``, invitee profiles, and student data.

Contents
--------

- `Introduction`_
- `Getting Started`_
- `Usage Guide`_
- `Development`_
- `RST Table Examples`_
- `RST Admonitions`_
- `RST Footnotes`_

.. _introduction:

----

Introduction
============

.. _project-overview:

Project Overview
----------------

.. image:: ../_static/sample-image.svg
   :alt: Sample Image
   :width: 400
   :align: center

This project provides a Jekyll-based documentation site with supporting Node.js utilities for working with YAML configuration files [#intro1]_. The site showcases:

- YAML configuration parsing with anchors and merge keys [#intro2]_
- Invitee collection management
- Student data directory
- Interactive documentation with table of contents

For more information, see `Getting Started`_ or browse `Usage Guide`_ for detailed examples.

.. _project-structure:

Project Structure
-----------------

Jekyll Site Files
~~~~~~~~~~~~~~~~~

- ``_config.yml`` - Jekyll site configuration
- ``_layouts/`` - HTML layout templates
  - ``default.html`` - Main page layout with TOC sidebar
  - ``invitee.html`` - Layout for invitee profile pages
- ``_data/`` - Data files
  - ``students.csv`` - Student data in CSV format
  - ``students.yml`` - Student data in YAML format
- ``_invitee/`` - Invitee collection (Jekyll collection)
  - ``choi.md`` - Choi's profile
  - ``jin.md`` - Jin's profile
- ``assets/css/style.css`` - Site stylesheet
- ``index.md`` - Home page
- ``students.md`` - Students directory page

Node.js Utilities
~~~~~~~~~~~~~~~~~

- ``parser.js`` - YAML parser with anchor/alias support
- ``json-to-yaml.js`` - JSON to YAML converter utility
- ``server.js`` - Static file server (optional)
- ``package.json`` - Node.js dependencies

Configuration Files
~~~~~~~~~~~~~~~~~~~

- ``conf.yml`` - Example YAML configuration with anchors
- ``Gemfile`` - Ruby dependencies for Jekyll
- ``Gemfile.lock`` - Locked gem versions

.. _getting-started:

----

Getting Started
===============

.. _requirements:

Requirements
------------

Ruby and Bundler
~~~~~~~~~~~~~~~~

- Ruby 2.7+ [#req1]_
- Bundler 2.4 or newer

Install Bundler:

.. code:: bash

   gem install --user-install bundler -v "~> 2.4"

Node.js (Optional)
~~~~~~~~~~~~~~~~~~

- Node.js 18+ (only needed for parser utilities) [#req2]_

.. _installation:

Installation
------------

Jekyll Site Setup
~~~~~~~~~~~~~~~~~

1. Install Ruby dependencies:

   .. code:: bash

      bundle install --path vendor/bundle

2. Build and serve the site:

   .. code:: bash

      bundle exec jekyll serve

3. Open your browser to:

   .. code:: text

      http://127.0.0.1:4000

Node.js Utilities (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install Node dependencies:

   .. code:: bash

      npm install

2. Run the parser demo:

   .. code:: bash

      npm start

3. Or use the static server:

   .. code:: bash

      npm run serve

For more details, see `Usage Guide`_. To contribute, check `Development`_.

.. _usage-guide:

----

Usage Guide
===========

.. _usage:

Usage
-----

Jekyll Site
~~~~~~~~~~~

The Jekyll site provides:

- **Home Page** (``index.md``) - Overview of the project and configuration parser [#usage1]_
- **Students Directory** (``students.md``) - Table view of student data from ``_data/students.csv``
- **Invitee Profiles** - Individual pages for each invitee in ``_invitee/`` collection

Features:

- Automatic table of contents generation from page headings [#usage2]_
- Responsive design with mobile-friendly navigation
- Dark mode support
- SEO optimization via jekyll-seo-tag

YAML Parser
~~~~~~~~~~~

The ``parser.js`` module provides:

- YAML file parsing with anchor and alias support
- Merge key (``<<:``) handling
- Dot-notation value access
- Configuration validation
- Student data extraction

Example usage:

.. code:: javascript

   const ConfParser = require('./parser');
   const parser = new ConfParser('conf.yml');
   parser.load();
   
   // Get specific values
   const site = parser.get('site');
   const studentName = parser.get('student.name');
   
   // Get all students
   const students = parser.getStudents();
   
   // Validate configuration
   const validation = parser.validate();

.. _configuration:

Configuration
-------------

Jekyll Configuration
~~~~~~~~~~~~~~~~~~~~

The ``_config.yml`` file contains:

- Site metadata (title, description)
- Collection definitions (invitee)
- Default layout assignments
- Excluded files from build

Field List Example
~~~~~~~~~~~~~~~~~~

RST field lists can be used to display metadata or key-value pairs:

:Author: Jin Woo
:Version: 1.0.0
:Language: JavaScript, Ruby
:License: ISC
:Repository: https://example.com/projects/conf-parser
:Status: Active Development

Field lists are useful for displaying structured information in documentation.

YAML Configuration
~~~~~~~~~~~~~~~~~~

The ``conf.yml`` file demonstrates:

- YAML anchors (``&anchor_name``)
- Aliases (``*alias_name``)
- Merge keys (``<<: *anchor_name``)
- Nested structures
- Collection definitions

.. _data-files:

Data Files
----------

Students Data
~~~~~~~~~~~~~

Student information is stored in two formats:

- ``_data/students.csv`` - CSV format for easy editing
- ``_data/students.yml`` - YAML format for Jekyll data files

Both contain the same data: student ID, name, major, year, and email.

Invitee Collection
~~~~~~~~~~~~~~~~~~

Invitee profiles are stored as Markdown files in ``_invitee/`` with front matter:

.. code-block:: yaml

   ---
   name: Jin
   role: Project Maintainer
   ---
   
   Profile content here...

For more examples, see `RST Table Examples`_ and `RST Admonitions`_. For development information, see `Development`_.

.. _development:

----

Development
===========

Building the Site
-----------------

Build the site without serving:

.. code:: bash

   bundle exec jekyll build

The output will be in ``_site/`` directory [#dev1]_.

Cleaning Build Artifacts
-------------------------

Remove generated files:

.. code:: bash

   bundle exec jekyll clean

This removes ``_site/``, ``.jekyll-cache/``, and other generated directories.

File Organization
-----------------

Generated files (excluded from version control):

- ``_site/`` - Jekyll build output
- ``node_modules/`` - Node.js dependencies
- ``vendor/`` - Bundler dependencies
- ``.jekyll-cache/`` - Jekyll cache files
- ``.sass-cache/`` - Sass compilation cache

These are automatically ignored via ``.gitignore``.

.. _troubleshooting:

Troubleshooting
---------------

Bundler Permission Errors
~~~~~~~~~~~~~~~~~~~~~~~~~

If you encounter permission errors with Bundler, install gems to a local path:

.. code:: bash

   bundle install --path vendor/bundle

Jekyll Server Not Starting
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure all dependencies are installed:

.. code:: bash

   bundle install
   bundle exec jekyll doctor

Port Already in Use
~~~~~~~~~~~~~~~~~~~

Specify a different port:

.. code:: bash

   bundle exec jekyll serve --port 4001

For more information, see `Introduction`_ or check `Contact`_ for support.

.. _rst-table-examples:

----

RST Table Examples
==================

This section demonstrates all types of tables supported in reStructuredText.

.. include:: tables.rst
   :start-after: .. _grid-tables:
   :end-before: Summary

.. _rst-admonitions:

----

RST Admonitions
===============

This section demonstrates all types of admonitions supported in reStructuredText. Admonitions are special directives that create highlighted note boxes.

Note Admonition
---------------

.. note::

   This is a note admonition. Use it to provide additional information or tips
   that are relevant but not critical to understanding the main content.

   You can include multiple paragraphs in an admonition block. The content will
   be formatted with appropriate spacing and styling.

Warning Admonition
------------------

.. warning::

   This is a warning admonition. Use it to alert users about potential issues
   or important considerations they should be aware of.

   Always read warnings carefully before proceeding with potentially dangerous
   operations.

Danger Admonition
-----------------

.. danger::

   This is a danger admonition. Use it to indicate critical risks or actions
   that could cause data loss, system damage, or security breaches.

   Never ignore danger warnings. Proceed with extreme caution.

Important Admonition
--------------------

.. important::

   This is an important admonition. Use it to highlight critical information
   that users must not overlook.

   Important information is usually essential for the correct operation or
   understanding of a system or process.

Tip Admonition
--------------

.. tip::

   This is a tip admonition. Use it to provide helpful hints or best practices
   that can improve the user's experience or workflow.

   Tips are optional but recommended suggestions that can make tasks easier
   or more efficient.

Hint Admonition
---------------

.. hint::

   This is a hint admonition. Similar to tips, hints provide gentle guidance
   or suggestions without being as forceful as warnings or important notices.

   Hints are useful for providing optional guidance that might not be immediately
   obvious to users.

Attention Admonition
--------------------

.. attention::

   This is an attention admonition. Use it to draw the user's focus to specific
   information that requires their notice.

   Attention blocks are useful for highlighting information that users should
   read before proceeding.

Caution Admonition
------------------

.. caution::

   This is a caution admonition. Use it to warn users about potential problems
   or side effects that may occur.

   Cautions are less severe than warnings but should still be heeded to avoid
   unexpected behavior or issues.

Error Admonition
----------------

.. error::

   This is an error admonition. Use it to document error conditions or to
   explain common mistakes and how to avoid them.

   Error admonitions are particularly useful in troubleshooting guides and
   documentation.

Custom Admonition
-----------------

.. admonition:: Custom Title

   This is a custom admonition with a user-defined title. You can create
   admonitions with any title you want for specific purposes.

   Custom admonitions are flexible and can be styled differently based on
   their title or content.

Admonition with Code
--------------------

.. note::

   When working with code blocks inside admonitions, you can combine them:

   .. code:: bash

      bundle exec jekyll serve

   This allows you to provide context and instructions together.

.. _rst-footnotes:

----

RST Footnotes
=============

This section demonstrates how to use footnotes in reStructuredText.

Basic Footnotes
---------------

Footnotes can be created using square brackets with a label [#label]_ or auto-numbered (see Auto-numbered Footnotes section below).

You can also use explicit labels like [#note1]_ and [#note2]_.

Multiple Footnotes
------------------

You can reference the same footnote multiple times [#same]_, and it will link to the same footnote definition [#same]_.

Auto-numbered Footnotes
-----------------------

Auto-numbered footnotes are created using just [#]_ without a label. Each occurrence gets a unique number [#]_.

Named Footnotes
---------------

Named footnotes use explicit labels for better readability:

- First reference [#first]_
- Second reference [#second]_
- Third reference [#third]_

Footnotes in Lists
------------------

Footnotes work well in lists:

1. First item with a footnote [#list1]_
2. Second item with another footnote [#list2]_
3. Third item referencing the first footnote again [#list1]_

Footnotes in Tables
-------------------

Footnotes can also be used in tables:

+--------+--------+--------+
| Name   | Value  | Notes  |
+========+========+========+
| Item 1 | 100    | [#t1]_ |
+--------+--------+--------+
| Item 2 | 200    | [#t2]_ |
+--------+--------+--------+

.. [#intro1] Jekyll is a static site generator that transforms plain text into static websites.
.. [#intro2] YAML anchors and merge keys allow for reusable configuration blocks.
.. [#req1] Ruby 2.7 or higher is required for Jekyll 4.x compatibility.
.. [#req2] Node.js is optional and only needed if you want to use the parser utilities.
.. [#usage1] The home page provides an overview of the project structure and features.
.. [#usage2] The TOC is automatically generated from heading levels in the content.
.. [#dev1] The _site directory contains the fully rendered static HTML files.

.. [#label] This is a footnote with an explicit label.
.. [#] This is the first auto-numbered footnote.
.. [#] This is the second auto-numbered footnote.
.. [#note1] This is the first named footnote with explicit label.
.. [#note2] This is the second named footnote.
.. [#same] This footnote is referenced multiple times in the text above.
.. [#first] First named footnote definition.
.. [#second] Second named footnote definition.
.. [#third] Third named footnote definition.
.. [#list1] This footnote is used in the list section.
.. [#list2] Another footnote for the list section.
.. [#t1] Table footnote for Item 1.
.. [#t2] Table footnote for Item 2.

License
-------

This project is part of the Open Source Software Introduction workspace.

.. _contact:

Contact
-------

- Email: `your-email@example.com <mailto:your-email@example.com>`_
- GitHub: `GitHub Repository <https://github.com/yourusername/your-repo>`_

For more information, see `Introduction`_ or check `Development`_ for contribution guidelines.

