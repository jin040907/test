const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3000;
const PUBLIC_DIR = path.resolve(__dirname, '..');
const SITE_DIR = path.join(PUBLIC_DIR, '_site');

// Check if Jekyll _site directory exists, otherwise use root
const SERVE_DIR = fs.existsSync(SITE_DIR) ? SITE_DIR : PUBLIC_DIR;

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.yml': 'text/yaml; charset=utf-8',
  '.yaml': 'text/yaml; charset=utf-8',
  '.md': 'text/markdown; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
};

const toFilePath = (urlPath) => {
  if (urlPath === '/' || urlPath === '') {
    // Try index.html first, then index.md
    const htmlPath = path.join(SERVE_DIR, 'index.html');
    if (fs.existsSync(htmlPath)) {
      return htmlPath;
    }
    return path.join(SERVE_DIR, 'index.md');
  }
  return path.join(SERVE_DIR, decodeURIComponent(urlPath));
};

const serveFile = (res, filePath) => {
  const ext = path.extname(filePath).toLowerCase();
  const mimeType = MIME_TYPES[ext] || 'application/octet-stream';

  fs.readFile(filePath, (err, data) => {
    if (err) {
      if (err.code === 'ENOENT') {
        res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('404 Not Found');
      } else {
        res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('500 Internal Server Error');
      }
      return;
    }

    res.writeHead(200, { 'Content-Type': mimeType });
    res.end(data);
  });
};

const server = http.createServer((req, res) => {
  const safePath = toFilePath(req.url);

  if (!safePath.startsWith(SERVE_DIR)) {
    res.writeHead(403, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('403 Forbidden');
    return;
  }

  fs.stat(safePath, (err, stats) => {
    if (err) {
      serveFile(res, safePath);
      return;
    }

    if (stats.isDirectory()) {
      serveFile(res, path.join(safePath, 'index.html'));
    } else {
      serveFile(res, safePath);
    }
  });
});

server.listen(PORT, () => {
  console.log(`Local server running at http://localhost:${PORT}`);
  console.log(`Serving from: ${SERVE_DIR}`);
  if (SERVE_DIR === SITE_DIR) {
    console.log('(Jekyll _site directory detected)');
  } else {
    console.log('(Note: Run "bundle exec jekyll build" to generate _site/)');
  }
});

