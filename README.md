# KSP Crime Intelligence Platform

An advanced, AI-driven crime analytics and intelligence platform built for the Karnataka State Police (KSP). This platform empowers investigators, analysts, and policymakers to discover hidden criminal networks, predict emerging hotspots, and understand socio-economic drivers of crime using interactive visualizations.

## Key Features

1. **Organized Crime Network Analysis**
   - Interactive force-directed graphs linking Accused, FIRs, Bank Accounts, and Phones.
   - Algorithms: Louvain (community detection), Centrality (key figures), and QuickML (MO similarity).

2. **Predictive AI & Anomaly Detection**
   - District Risk Choropleth mapping via Zia AutoML.
   - Real-time anomaly alerts (e.g., vehicle theft surges) and feature importance analysis.

3. **Spatial & Temporal Hotspots**
   - Geospatial mapping with Leaflet KDE heatmaps.
   - Temporal trend forecasting integrated with ECharts.

4. **Socio-Economic Correlation**
   - Pearson correlation analysis linking crime types to demographics like unemployment and urbanization.

5. **Explainable AI & Secure RBAC**
   - Transparent lineage trails for all AI predictions.
   - Role-based dashboards for SCRB Analysts, District SPs, and Investigators.

## Technology Stack

- **Frontend:** HTML5, Vanilla JavaScript, Tailwind CSS
- **Visualizations:** ECharts, Leaflet, Leaflet.heat
- **Hosting / Infrastructure:** Zoho Catalyst Slate
- **Algorithms:** Force-directed layouts, Pearson Correlation, Louvain, Centrality, QuickML

## Setup and Installation

1. Clone this repository.
2. Open `index.html` in any modern web browser.
3. (Optional) For deployment, use the Zoho Catalyst CLI to deploy the application to Catalyst Slate.

## Repository Contents

- `index.html` - The main application dashboard.
- `data/` - (If applicable) Static JSON data sets including Karnataka Crime Data.
- `KSP_Datathon_2026_Submission_Formatted.pptx` - Professional pitch deck.
