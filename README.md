# BAE Systems Inc. — Strategic Analytics & Transformation Suite

![Version](https://img.shields.io/badge/version-2.6-00b4d8)
![License](https://img.shields.io/badge/license-MIT-06d6a0)
![GitHub Pages](https://img.shields.io/badge/deployment-GitHub%20Pages-blue)
![Report Attribution](https://img.shields.io/badge/Report-Univ.%20of%20Portsmouth-f77f00)

An interactive, production-grade web application and executive decision support system built by studying the 27-page academic business report **"BAE System Inc. Report"** (*Business In Action*, University of Portsmouth, authored by **Dr. Gajendra Liyanaarachchi**).

This suite translates complex organizational diagnostics, 5-year financial datasets, competitor scorecards, value chain diagrams, and strategic recommendations into an interactive, visual web dashboard.

---

## 🌟 Interactive Modules & Features

1. **Executive Command Center**:
   - **Interactive Eisenhower Priority Matrix** (Table 2): Classifying strategic imperatives into *Do Immediate*, *Plan/Schedule*, *Delegate*, and *Eliminate*.
   - **Action Plan Table** (Table 1): 12 prioritized diagnostic items with ranks, justifications, and filterable areas.

2. **Organisational Architecture & Culture Lab**:
   - **Interactive Organogram Visualizer**: Toggle between *Current Siloed Divisional Structure* (Figure 1) and *Recommended Hybrid Matrix Model* (Figure 2).
   - **Leadership & Culture Matrix**: Comparative analysis of *Transactional/Technocratic* vs. *Transformational Leadership* & *Adhocracy Culture*.

3. **Strategic Marketing & Competitor Intelligence**:
   - **2D Canvas Positioning Map** (Figure 3): Plotted along *Scope of Offering* vs *Tech Focus* (BAE Systems, Northrop Grumman, Honeywell, QinetiQ) with interactive *"Apply Digital Defense Shift"* positioning toggle.
   - **Competitor Scorecard Matrix** (Table 4): Evaluation across 8 criteria highlighting BAE's **9/10 Sovereign Partner score**.
   - **Type 26 Naval Market Calculator**: Formula `Market Value = Selling Price × Consumers × Frequency` applied to current Tier-1 naval sales vs. proposed Tier-2 modular export variant.
   - **Vice Admiral James Sterling Persona Card**: B2G buyer motivators, budget controls, and *Social Value* pricing reframing.

4. **Financial Analytics & Leverage Stress-Tester**:
   - **5-Year Historical Dashboard (2020–2024)**: Interactive charts for Share Price (£4.22 → £11.27), EPS (64.9p), EBIT (£3,038m), Debt (£4,945m), Gearing (0.43), and Interest Cover (8.61x).
   - **Interactive Capital Structure Simulator**: Real-time sliders for debt paydown, EBIT growth, and dividend payout ratio to simulate restoring interest cover > 10.0x and gearing <= 0.25.

5. **Operations & Supply Chain Control Tower**:
   - **Value Chain Transformation**: Side-by-side comparison of *Antiquated Value Chain* (Figure 5) vs *Revised Digital Outcome-Based Value Chain* (Figure 6).
   - **Deming Real-Time SPC Live Monitor**: Live Statistical Process Control simulation for bolt assembly torque (Barrow Shipyard) with Upper/Lower control limits (UCL 85 Nm, LCL 75 Nm), anomaly trigger, and Kaizen circle logger.
   - **Multi-Tier Supply Chain Inspector**: Risk mapping across Tier 1–4 suppliers (titanium, energetics, rare earths, chips) comparing Just-In-Time (JIT) vs Just-In-Case (JIC).

6. **Strategic Roadmap & Report Knowledge Base**:
   - **3 Core Strategic Recommendations**: Commercial Space Diversification (SMS Division Q1-Q2 2026), Type 26 Export Variant (2026-2028), and Multi-Tier Supply Qualification (Q1 2026).
   - **Searchable Report Knowledge Base**: Searchable chapter text, citations, and Markdown report exporter.

---

## 🚀 Quick Start (Local Run)

No build tools or heavy node dependencies are required! The application is built using vanilla HTML5, Tailwind CSS, ES Modules, and Chart.js.

### Method 1: Using Python Launcher (Recommended)
Run the provided helper script:
```bash
python server.py
```
Then open `http://localhost:8080` in your web browser.

### Method 2: Direct Static View
Double-click `index.html` or open `index.html` directly in any modern browser (Chrome, Edge, Firefox, Safari).

---

## 📤 How to Upload to GitHub & Deploy to GitHub Pages

1. **Create a new repository** on GitHub (e.g., `bae-strategic-analytics`).
2. **Initialize Git and push code**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: BAE Systems Strategic Analytics Suite"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/bae-strategic-analytics.git
   git push -u origin main
   ```
3. **Enable GitHub Pages**:
   - Go to **Settings > Pages** in your GitHub repository.
   - Under **Source**, select **GitHub Actions** (the included `.github/workflows/deploy.yml` will automatically build and publish the web app to `https://YOUR_USERNAME.github.io/bae-strategic-analytics/`).

---

## 📚 Academic References

- **IEEE Reliability Society** (2025). *IEEE Std 7009-2024: Standard for fail-safe design of autonomous systems*.
- **Lucas, R. et al.** (2024). *Toward defense supply chain disruption management*. RAND Corporation.
- **UK Ministry of Defence** (2025). *Defence industrial strategy: Making defence an engine for growth (CP 1388)*.
- **Hellberg, R. et al.** (2025). *Performance constraints in defence industry supply chains*. Defence and Peace Economics.
- **BAE Systems plc** (2025). *Half-yearly report 2025* & *Ball Aerospace Investor Presentation (2023)*.
