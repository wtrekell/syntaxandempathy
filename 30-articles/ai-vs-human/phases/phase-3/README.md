**Phase 3: Single-Article Analysis in Colab (`ai-vs-human-v0.2.ipynb`)**
This notebook is the direct implementation of the framework designed in Phase 2.

  * **Methodology:** `ai-vs-human-v0.2.ipynb` is a multi-step analysis pipeline contained within a single notebook. It successfully:
    1.  Installs dependencies like `sentence-transformers`.
    2.  Loads and validates the four article versions (`draft`, `refined`, `edited`, `final`) from Google Drive.
    3.  Performs both lexical and advanced semantic similarity analysis using the `all-MiniLM-L6-v2` model.
    4.  Conducts **Attribution Mapping** to trace each sentence in the final version back to its origin.
    5.  Saves detailed `_complete_analysis.json` and `_footer_metrics.json` files to your Drive.
  * **Outcome:** You now had a powerful, repeatable, and cost-effective tool for analyzing any single article from start to finish.