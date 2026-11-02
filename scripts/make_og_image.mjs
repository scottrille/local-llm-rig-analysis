// Render images/og-image.png, the 1200x630 preview that Facebook and other sites show for links to the page.
// It reuses the page's own headline and chart, so rerun it whenever the chart changes.
// Usage: PW_EXE=<path to Chromium> node scripts/make_og_image.mjs "$PWD/index.html" images/og-image.png
// Needs the playwright package (npm install playwright).
import { chromium } from 'playwright';
const [file, out] = process.argv.slice(2);
const browser = await chromium.launch({ executablePath: process.env.PW_EXE || undefined });
const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, colorScheme: 'light', deviceScaleFactor: 1 });
await page.goto('file://' + file);
await page.evaluate(() => document.fonts.ready);
await page.evaluate(() => {
  const fig = document.getElementById('fig');
  const h1 = document.querySelector('header h1').cloneNode(true);
  fig.querySelector('.fig-caption')?.remove();
  document.body.innerHTML = '';
  const card = document.createElement('div');
  card.id = 'og';
  card.innerHTML = `
    <div class="og-text">
      <div class="eyebrow"><span>Local LLM hardware</span></div>
      <div class="og-h1"></div>
      <p class="og-sub">Eleven configurations compared on memory, speed, long-context behavior, software and price</p>
      <p class="og-meta">Prices checked Nov 2026</p>
    </div>
    <div class="og-fig"></div>`;
  card.querySelector('.og-h1').appendChild(h1);
  card.querySelector('.og-fig').appendChild(fig);
  document.body.appendChild(card);
  const st = document.createElement('style');
  st.textContent = `
    html, body { margin: 0; background: var(--ground); }
    #og { width: 1200px; height: 630px; box-sizing: border-box; padding: 44px 40px 40px 56px;
          display: grid; grid-template-columns: 370px 1fr; gap: 34px; align-items: center;
          border-top: 10px solid var(--accent); }
    .og-text { display: flex; flex-direction: column; gap: 22px; }
    .og-text .eyebrow { font-size: 15px; }
    .og-h1 h1 { font-size: 50px; line-height: 1.06; }
    .og-sub { margin: 0; font-size: 21px; line-height: 1.4; color: var(--ink-2); }
    .og-meta { margin: 0; font-family: var(--f-mono); font-size: 14px; letter-spacing: .08em; text-transform: uppercase; color: var(--ink-3); }
    .og-fig .figure { padding: 16px 14px 10px; }
    #tip { display: none; }`;
  document.head.appendChild(st);
});
await page.waitForTimeout(300);
const ov = await page.evaluate(() => { const o = document.getElementById('og'); return [o.scrollHeight, o.scrollWidth]; });
console.log('card size', ov);
await page.screenshot({ path: out, clip: { x: 0, y: 0, width: 1200, height: 630 } });
await browser.close();
