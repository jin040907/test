---
layout: default
title: Conf Parser Front Page
permalink: /
---

<header>
  <h1>{{ site.title }}</h1>
  <p>
    Explore the YAML configuration parser, its example data, and the invitee
    collection contained in this project folder.
  </p>
</header>

<main>
  <section>
    <h2>Project Overview</h2>
    <p>
      The JavaScript parser defined in <code>scripts/parser.js</code> loads
      <code>config/conf.yml</code>, resolves YAML anchors and merge keys, and
      exposes helper utilities for accessing nested values, validating the
      configuration, and printing the parsed output.
    </p>
    <ul>
      <li>YAML anchors and aliases handled via <code>js-yaml</code></li>
      <li>Dot-notation getter for quick lookups</li>
      <li>Validation helpers for required fields and student details</li>
      <li>Command line entry point: <code>node scripts/parser.js</code> or <code>npm start</code></li>
    </ul>
  </section>

  <section>
    <h2>Configuration Highlights</h2>
    <p>The active configuration lives in <code>config/conf.yml</code>:</p>
    <ul>
      <li>Site URL: <a href="{{ site.url | default: 'https://example.com/projects/conf-parser' }}">Conf Parser Repository</a></li>
      <li>Theme: <code>default</code></li>
      <li>Numeric items: <code>[6, 7, 8]</code></li>
      <li>Names: <code>["six", "seven", "eight", "nine"]</code></li>
      <li>
        Student profiles reuse the shared
        <code>&amp;student_details</code> and <code>&amp;subjects</code>
        anchors.
      </li>
    </ul>
  </section>

  <section>
    <h2>Invitee Collection</h2>
    <p>
      The <code>collections.invitee</code> block in
      <code>_config.yml</code> maps to the curated Markdown files below. View the raw
      Markdown or explore enriched profiles rendered by Jekyll.
    </p>
    <div class="catalog">
      {% for person in site.invitee %}
        <a class="card" href="{{ person.url | relative_url }}">
          <h3>{{ person.name | default: person.title | default: person.slug | capitalize }}</h3>
          <p>{{ person.excerpt | strip_html | truncate: 100 }}</p>
        </a>
      {% endfor %}
    </div>
  </section>

  <section>
    <h2>Getting Started</h2>
    <ol>
      <li>Install Node dependencies: <code>npm install</code></li>
      <li>Parse and inspect the configuration: <code>npm start</code></li>
      <li>Serve this site locally with Jekyll: <code>bundle exec jekyll serve</code></li>
      <li>
        Extend <code>config/conf.yml</code> or
        <code>_config.yml</code> with additional collections or entries as needed.
      </li>
    </ol>
    <p>
      Refer to <a href="{{ '/README.md' | relative_url }}">README.md</a> for detailed usage examples
      and available helper methods.
    </p>
  </section>
</main>

<footer class="page-footer">Built for the 오픈소스SW개론 workspace.</footer>

