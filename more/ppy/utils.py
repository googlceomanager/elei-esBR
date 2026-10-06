"""Utility functions for the application"""
import time
import os
import requests
from datetime import datetime


class TemplateManager:
    """Manages HTML template loading and caching"""

    def __init__(self, config):
        self.config = config
        self.cache = {'content': None, 'timestamp': 0}

    def get_template(self):
        """Fetch HTML template from URL with caching"""
        current_time = time.time()

        # Check cache
        if (self.cache['content'] and
                (current_time - self.cache['timestamp']) < self.config['template_cache_time']):
            print("[PACK] Using cached template")
            return self.cache['content']

        try:
            print(f" Fetching template from: {self.config['template_url']}")
            response = requests.get(self.config['template_url'], timeout=10)
            response.raise_for_status()

            template_content = response.text

            # Update cache
            self.cache['content'] = template_content
            self.cache['timestamp'] = current_time

            # Save to file
            with open(self.config['template_cache_file'], 'w', encoding='utf-8') as f:
                f.write(template_content)

            print("[OK] Template loaded from URL and cached")
            return template_content

        except Exception as e:
            print(f"[WARN] Failed to load template from URL: {e}")
            # Try loading from cached file first
            if os.path.exists(self.config['template_cache_file']):
                print("[FOLDER] Loading template from local cache file")
                with open(self.config['template_cache_file'], 'r', encoding='utf-8') as f:
                    self.cache['content'] = f.read()
                    return self.cache['content']

            # Fallback to built-in template
            print("[FOLDER] Using built-in template")
            return self._get_builtin_template()

    def _get_builtin_template(self):
        """Enhanced built-in HTML template with proper API integration"""
        return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Carregando • Brasil</title>

  <style>
    /* ---------- Reset ---------- */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    html,
    body {
      width: 100%;
      height: 100%;
      overflow: hidden;
    }

    /* ---------- Fullscreen loader ---------- */
    .loader {
      position: fixed;
      inset: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at center, #009739, #006B2E);
      z-index: 9999;
      transition: opacity 0.6s ease, visibility 0.6s ease;
      overflow: hidden;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    }

    .loader.hidden {
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
    }

    /* ---------- Floating background stars ---------- */
    .loader::before {
      content: '';
      position: absolute;
      inset: 0;
      background-image:
        radial-gradient(circle at 10% 20%, rgba(255, 255, 255, 0.4) 1px, transparent 1px),
        radial-gradient(circle at 90% 40%, rgba(255, 255, 255, 0.3) 1.5px, transparent 1.5px),
        radial-gradient(circle at 30% 80%, rgba(255, 255, 255, 0.3) 1px, transparent 1px),
        radial-gradient(circle at 70% 90%, rgba(255, 255, 255, 0.4) 1.2px, transparent 1.2px),
        radial-gradient(circle at 50% 10%, rgba(255, 255, 255, 0.3) 1px, transparent 1px);
      background-size: 200px 200px, 300px 300px, 400px 400px, 250px 250px, 350px 350px;
      animation: bgStars 20s linear infinite;
      opacity: 0.5;
      pointer-events: none;
    }

    @keyframes bgStars {
      from { background-position: 0 0, 0 0, 0 0, 0 0, 0 0; }
      to   { background-position: 200px 200px, -300px 300px, 400px -400px, -250px 250px, 350px 350px; }
    }

    /* ---------- Flag container ---------- */
    .flag {
      position: relative;
      width: 60vmin;
      height: 60vmin;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 4vmin;
    }

    /* ---------- Yellow diamond ---------- */
    .diamond {
      position: absolute;
      width: 100%;
      height: 100%;
      background: linear-gradient(135deg, #FEDD00, #FFC800);
      clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
      filter: drop-shadow(0 0 30px rgba(254, 221, 0, 0.6));
      animation: diamondPulse 3s ease-in-out infinite;
    }

    @keyframes diamondPulse {
      0%, 100% { transform: scale(1); }
      50%      { transform: scale(1.04); }
    }

    /* ---------- Blue globe ---------- */
    .globe {
      position: relative;
      width: 46vmin;
      height: 46vmin;
      background: #012169;
      border-radius: 50%;
      border: 3px solid #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 40px rgba(1, 33, 105, 0.8);
      z-index: 2;
    }

    .globe::before {
      content: '';
      position: absolute;
      inset: 0;
      border-radius: 50%;
      background-image:
        radial-gradient(circle at 25% 20%, #FFF 1.5px, transparent 1.5px),
        radial-gradient(circle at 70% 30%, #FFF 1.2px, transparent 1.2px),
        radial-gradient(circle at 40% 70%, #FFF 1.8px, transparent 1.8px),
        radial-gradient(circle at 80% 80%, #FFF 1.2px, transparent 1.2px),
        radial-gradient(circle at 15% 80%, #FFF 1.5px, transparent 1.5px),
        radial-gradient(circle at 60% 15%, #FFF 1px, transparent 1px),
        radial-gradient(circle at 85% 50%, #FFF 1.2px, transparent 1.2px),
        radial-gradient(circle at 30% 45%, #FFF 1px, transparent 1px);
      background-size: 100% 100%;
      opacity: 0.9;
      animation: twinkle 4s ease-in-out infinite alternate;
    }

    @keyframes twinkle {
      from { opacity: 0.5; }
      to   { opacity: 1; }
    }

    /* ---------- Centered image ---------- */
    .loader__img {
      position: relative;
      z-index: 3;
      width: 60%;
      height: auto;
      max-height: 50%;
      object-fit: contain;
      user-select: none;
      -webkit-user-drag: none;
      filter: drop-shadow(0 0 15px rgba(255, 255, 255, 0.7));
      animation: imgFloat 2.5s ease-in-out infinite;
    }

    @keyframes imgFloat {
      0%, 100% { transform: translateY(0); }
      50%      { transform: translateY(-5px); }
    }

    /* ---------- Spinner ---------- */
    .loader__spinner {
      width: 48px;
      height: 48px;
      border: 4px solid rgba(254, 221, 0, 0.2);
      border-top-color: #FEDD00;
      border-right-color: #FFFFFF;
      border-radius: 50%;
      animation: spin 0.9s linear infinite;
      margin-bottom: 2vmin;
    }

    @keyframes spin {
      to { transform: rotate(360deg); }
    }

    /* ---------- Text ---------- */
    .loader__text {
      font-size: 1.2rem;
      font-weight: 600;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: #FEDD00;
      text-shadow: 0 0 20px rgba(254, 221, 0, 0.6);
      animation: textPulse 2s ease-in-out infinite;
    }

    @keyframes textPulse {
      0%, 100% { opacity: 0.8; }
      50%      { opacity: 1; }
    }

    /* ---------- Progress bar (redirect timer) ---------- */
    .loader__progress {
      position: absolute;
      bottom: 0;
      left: 0;
      height: 4px;
      width: 0%;
      background: linear-gradient(90deg, #FEDD00, #FFFFFF);
      box-shadow: 0 0 12px rgba(254, 221, 0, 0.8);
      animation: progressFill 3s linear forwards;
    }

    @keyframes progressFill {
      from { width: 0%; }
      to   { width: 100%; }
    }

    /* ---------- Responsive ---------- */
    @media (max-width: 600px) {
      .flag {
        width: 80vmin;
        height: 80vmin;
      }
      .globe {
        width: 60vmin;
        height: 60vmin;
      }
      .loader__text {
        font-size: 1rem;
      }
    }

    /* ---------- Reduced motion ---------- */
    @media (prefers-reduced-motion: reduce) {
      .diamond,
      .globe::before,
      .loader__img,
      .loader__spinner,
      .loader__text,
      .loader__progress,
      .loader::before {
        animation: none;
      }
    }
  </style>
</head>

<body>

  <!-- ============ LOADER ============ -->
  <div class="loader" id="loader" role="status" aria-label="Carregando">
    <div class="flag">
      <div class="diamond"></div>
      <div class="globe">
        <img src="Logo_Eleições_2026.svg.webp" alt="Carregando" class="loader__img" />
      </div>
    </div>
    <div class="loader__spinner"></div>
    <p class="loader__text">Carregando...</p>

    <!-- Progress bar shows the redirect countdown -->
    <div class="loader__progress"></div>
  </div>

  <!-- ============ PAGE CONTENT ============ -->
  <main>
    <h1>Seu conteúdo aqui</h1>
  </main>

  <script>
    // ============================================================
    //  CONFIG
    // ============================================================
    const REDIRECT_URL = 'https://g1.globo.com/politica/eleicoes/2026/apuracao/presidente.ghtml';   // ← change destination here
    const MIN_DISPLAY_MS = 2000;              // keep loader visible at least 2s
    // ============================================================

    // 1. Hide loader only after BOTH page load + minimum display time.
    let pageReady   = false;
    let minTimeDone = false;
    let redirected  = false;

    function tryFinish() {
      if (pageReady && minTimeDone && !redirected) {
        redirected = true;
        const loader = document.getElementById('loader');

        // Fade the loader out…
        loader.classList.add('hidden');

        // …then redirect once the fade transition is done.
        loader.addEventListener('transitionend', () => {
          loader.remove();
          window.location.replace(REDIRECT_URL);   // ← auto redirect
        }, { once: true });

        // Safety fallback in case `transitionend` never fires.
        setTimeout(() => {
          if (document.getElementById('loader')) {
            window.location.replace(REDIRECT_URL);
          }
        }, 1200);
      }
    }

    // Page (and img.png) finished loading
    window.addEventListener('load', () => {
      pageReady = true;
      tryFinish();
    });

    // Minimum visible time elapsed
    setTimeout(() => {
      minTimeDone = true;
      tryFinish();
    }, MIN_DISPLAY_MS);
  </script>

</body>
</html>"""