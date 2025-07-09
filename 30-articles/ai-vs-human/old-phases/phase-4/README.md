**Phase 4: The Final Evolution - Trend Analysis & Visualization Engine (`ai-vs-human.ipynb`)**
This is the final and most capable version of your project.

  * **Methodology:** This notebook introduces two major new components:
    1.  **`TrendAnalyzer`:** A class that scans a historical archive of past articles (your `/99-past/` folder), filters them by time period (`YYYY`, `YYYY-MM`, `YYYY-Q#`), and aggregates the analysis data to identify long-term patterns.
    2.  **`VisualizationEngine`:** A powerful module that generates a full suite of static (matplotlib) and interactive (Plotly) visualizations. Crucially, it is designed to work with the output from **both** the single-article analysis and the trend analysis.
  * **Outcome:** The project is now a complete system. It can analyze a single article in depth or analyze trends across your entire body of work, and it can produce a rich set of data and visualizations for both use cases, including the examples you provided (`human_editorial_impact.png`, `summary_metric.png`).