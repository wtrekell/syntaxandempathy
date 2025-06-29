You asked:
----------

* * *

Structure this prompt to ensure I receive the sum of the results after the 1 prompt. Include a markdown template to inform how all results should be formatted, and a JSON template for how the best 5 should be captured: “I want to write an article for UX, product, and service designers. Before giving me any article concepts, please do a quick search on what topics or trends are currently relevant for them. Once you have that context, brainstorm 9 distinct article ideas using three frameworks: SCAMPER, Six Thinking Hats, and Lotus Blossom. That’s three unique article ideas per framework. For each idea, give me a title, a brief summary, and note which framework principle inspired that idea. Please list all 9 ideas in one response.”

---

The AI replied:
---------------

* * *

Thought for 14 seconds

Below is a **single copy-and-paste prompt** that guarantees you get everything back in one shot, plus clear templates for how the assistant should format its answer.

    You are a research assistant for UX, product, and service designers.
    
    **Task overview (do ALL steps, then answer once):**
    1. **Quick scan:** Search the web for the most current topics, pain points, and emerging trends relevant to UX, product, and service design (use a browser/search tool if available).  
    2. **Ideation:** Using the context from step 1, brainstorm **nine (9) distinct article concepts**—three per framework:  
       - **SCAMPER** (Substitute, Combine, Adapt, Modify/Magnify/Minify, Put to another use, Eliminate, Reverse)  
       - **Six Thinking Hats** (White, Red, Black, Yellow, Green, Blue)  
       - **Lotus Blossom** (central theme with eight expansions; pick any three principles you find most fertile)  
       For each idea provide:  
       - A catchy **title**  
       - A 1-to-2 sentence **summary** (what the reader will learn)  
       - The **specific principle** (e.g., “SCAMPER – Combine” or “Thinking Hats – Green Hat”)  
    
    3. **Select best five:** From the nine, choose the five strongest ideas (greatest novelty + relevance).
    
    4. **Output everything in ONE response** using **both** templates below and nothing else.
    
    ---
    
    ### Markdown template (first)
    
    Use this exact structure:
    
    ```markdown
    ## Current UX/Product/Service-Design Trends (snapshot)
    - {Trend 1}
    - {Trend 2}
    - {Trend 3}
    - …
    
    ## Article Ideas (all 9)
    
    | # | Title | Summary | Framework | Principle |
    |---|-------|---------|-----------|-----------|
    | 1 | {Title 1} | {Brief summary 1} | SCAMPER | Substitute |
    | 2 | {Title 2} | {Brief summary 2} | SCAMPER | Combine |
    | 3 | {Title 3} | {Brief summary 3} | SCAMPER | … |
    | 4 | {Title 4} | {Brief summary 4} | Six Thinking Hats | White Hat |
    | 5 | {Title 5} | {Brief summary 5} | Six Thinking Hats | … |
    | 6 | {Title 6} | {Brief summary 6} | Six Thinking Hats | … |
    | 7 | {Title 7} | {Brief summary 7} | Lotus Blossom | … |
    | 8 | {Title 8} | {Brief summary 8} | Lotus Blossom | … |
    | 9 | {Title 9} | {Brief summary 9} | Lotus Blossom | … |
    

* * *

### JSON template (immediately after the table)

    {
      "best_ideas": [
        {
          "rank": 1,
          "title": "{Title of best idea}",
          "summary": "{Its summary}",
          "framework": "{SCAMPER | Six Thinking Hats | Lotus Blossom}",
          "principle": "{Principle used}"
        },
        {
          "rank": 2,
          "title": "",
          "summary": "",
          "framework": "",
          "principle": ""
        },
        {
          "rank": 3,
          "title": "",
          "summary": "",
          "framework": "",
          "principle": ""
        },
        {
          "rank": 4,
          "title": "",
          "summary": "",
          "framework": "",
          "principle": ""
        },
        {
          "rank": 5,
          "title": "",
          "summary": "",
          "framework": "",
          "principle": ""
        }
      ]
    }
    

**Important formatting rules**

*   Deliver the Markdown section **first**, then the JSON (no prose in between).
    
*   Do **not** wrap the JSON block in triple-backticks—output it as raw JSON so it can be parsed directly.
    
*   Provide **exactly nine** ideas and **exactly five** items in `best_ideas`.
    
*   Respond only once all steps are complete; do not drip outputs.
    

When you’re ready, execute all four steps and present the results using the templates above.

    
    *Copy the whole block above as your prompt. It compels the assistant to search, ideate, and return fully-formatted Markdown plus a neatly structured JSON payload—all in a single reply.*

---

You asked:
----------

* * *

Why do you say 9, scamper and six thinking hats alone provide more than 9

---

The AI replied:
---------------

* * *

Thought for a few seconds

Good catch! SCAMPER has seven levers and Six Thinking Hats has six, so—-on paper—-you could spin out **13+** separate angles before even touching Lotus Blossom.

I chose “**three per framework (9 total)**” in the prompt for two practical reasons:

1.  **Signal-to-noise balance** – Asking for every single hat or SCAMPER verb can flood you with ideas that start to feel repetitive. Three well-chosen concepts per framework usually surfaces enough variety to spot the strongest directions without overwhelming the reader.
    
2.  **Response length limits** – Many tools (including ChatGPT) have token caps. Capping at nine ideas helps guarantee the assistant can still squeeze in the trends snapshot _and_ the JSON block in one pass.
    

That said, there’s nothing sacred about nine. If you want comprehensive coverage—say, **7 SCAMPER + 6 Hats + 8 Lotus petals = 21 ideas**—just tweak the line that says “brainstorm 9 distinct article concepts” to the exact total you want. The rest of the template still works; you’d just enlarge the table and the JSON ranking array accordingly. Let me know if you’d like me to revise the sample prompt to handle the full set!

---

You asked:
----------

* * *

Understandable, but how am I to know if I got the best 3, the worst 3, or more likely than not...the first 3.

---

The AI replied:
---------------

* * *

Thought for 5 seconds

Here’s a simple way to bake **quality control and transparency** right into the prompt so you know you’re getting the _best-3_ ideas from each framework (not just the first three that pop into the model’s “head”).

* * *

### 1\. Add a quick “score-and-rank” micro-step

Slip this line into the task list **after** the brainstorming step and **before** the final output step:

> **2a. Quality filter:** For all nine ideas, assign a 0-10 score for each of the following:  
> – **Trend Fit** (how tightly it maps to the current UX/Product/Service trends you just found)  
> – **Novelty** (freshness vs. what’s already published)  
> – **Practical Impact** (will the average designer be able to apply it?)  
> Sum the three numbers for a **Total Score** and sort the ideas from highest to lowest.

Then tell the assistant to **pick the top three per framework** based on that total score.

* * *

### 2\. Expand the Markdown table to show the scores

    | # | Title | Summary | Framework | Principle | Trend Fit | Novelty | Impact | **Total** |
    |---|-------|---------|-----------|-----------|-----------|---------|---------|--------|
    | 1 | … | … | SCAMPER | Substitute | 9 | 8 | 7 | **24** |
    | 2 | … | … | SCAMPER | Combine | 8 | 7 | 8 | **23** |
    | 3 | … | … | … | … | … | … | … | … |
    

Tell the assistant to **bold** the Total column so it’s easy to scan.

* * *

### 3\. Tighten up the JSON block

Keep only the _final_ winners:

    {
      "best_ideas": [
        { "rank": 1, "id": 1, "title": "...", "framework": "SCAMPER", "principle": "Substitute", "total": 24 },
        { "rank": 2, "id": 2, "title": "...", "framework": "Six Thinking Hats", "principle": "Green Hat", "total": 23 },
        ...
      ]
    }
    

Include the original row **ID** and the **Total Score** so you can trace every pick back to the table.

* * *

### 4\. One-shot assurance in the prompt

> “Return **exactly one response** containing  
> – The scored Markdown table (all 9 ideas, sorted by Total Score).  
> – The JSON block with the **top-scoring** three ideas from each framework.  
> Do **not** omit the scores.”

* * *

With these tweaks the model must _show its work_, and you can immediately see if the “winning” ideas really deserve the crown.

---

You asked:
----------

* * *

That means it would have to provide all of them, show me the scores, and expand on the 9

---

The AI replied:
---------------

* * *

Thought for 22 seconds

Below is an **updated, copy-and-paste prompt** that (a) generates **all ideas**, (b) **shows the scores** for each, and (c) **expands** the nine winners—so you can see exactly why they rose to the top.

    You are a research assistant for UX, product, and service designers.
    
    **Task overview (do ALL steps, then answer once):**
    
    1. **Quick scan:** Search the web for the most current topics, pain points, and emerging trends in UX, product, and service design (use any browser/search tool available).
    
    2. **Ideation:** Using what you just learned, brainstorm **15 article concepts**—**five per framework**:  
       - **SCAMPER** (draw from its seven verbs)  
       - **Six Thinking Hats**  
       - **Lotus Blossom** (start with a central UX theme and branch)  
       For every idea, give:  
       - A catchy **title**  
       - A 1-to-2 sentence **summary**  
       - The **specific principle** (e.g., “SCAMPER – Combine”)
    
    3. **Score & rank:** For all 15 ideas, assign a 0-10 score for each of:  
       - **Trend Fit** (relevance to the trends you found)  
       - **Novelty** (freshness vs. what’s already out there)  
       - **Practical Impact** (how actionable it is for designers)  
       Add them for a **Total Score**.  
       **Sort ideas within each framework by Total Score (highest→lowest).**
    
    4. **Select winners:** Take the **top three ideas in each framework** (9 winners total).
    
    5. **Expand winners:** For each of the nine winners, provide a concise expansion with:  
       - **Who it helps most** (target reader)  
       - **3-4 takeaway bullets** (what they’ll learn/act on)  
       - **Suggested visual or example** to include in the article
    
    6. **Output everything in ONE response** using **all three sections below, in this order, and nothing else.**
    
    ---
    
    ### Markdown section (1 + 2 + 3)
    
    ```markdown
    ## Current UX/Product/Service-Design Trends (snapshot)
    - {Trend 1}
    - {Trend 2}
    - {Trend 3}
    - …
    
    ## Idea Scorecard (all 15)
    
    | # | Title | Summary | Framework | Principle | Trend Fit | Novelty | Impact | **Total** |
    |---|-------|---------|-----------|-----------|-----------|---------|--------|---------|
    | 1 | … | … | SCAMPER | Substitute | 9 | 8 | 7 | **24** |
    | 2 | … | … | SCAMPER | Combine | 8 | 9 | 6 | **23** |
    | … | | | | | | | | |
    

### Markdown section (4 + 5 – Expanded Concepts)

    ## Expanded Concepts (Top 9)
    
    ### {Title of Winner 1}  — SCAMPER • Substitute
    **Who it helps most:** {Target reader}  
    **Key takeaways:**  
    - Bullet 1  
    - Bullet 2  
    - Bullet 3  
    **Suggested visual:** {Visual/exercise/example}
    
    ### {Title of Winner 2}  — SCAMPER • …  
    …
    

### JSON block (6)

    {
      "best_ideas": [
        { "rank": 1, "id": 3, "title": "…", "framework": "SCAMPER", "principle": "Substitute", "total": 24 },
        { "rank": 2, "id": 6, "title": "…", "framework": "Six Thinking Hats", "principle": "Green Hat", "total": 23 },
        { "rank": 3, "id": 11, "title": "…", "framework": "Lotus Blossom", "principle": "Petal X", "total": 22 },
        { "rank": 4, "id": 7, "title": "…", "framework": "Six Thinking Hats", "principle": "Yellow Hat", "total": 22 },
        { "rank": 5, "id": 1, "title": "…", "framework": "SCAMPER", "principle": "Combine", "total": 21 }
      ]
    }
    

**Formatting rules**

*   Present the two Markdown sections **exactly** as shown, followed by the raw JSON block (no backticks around the JSON).
    
*   The **Idea Scorecard table must list all 15 ideas** with their scores.
    
*   In **Expanded Concepts**, list **only the nine winners** in the order SCAMPER → Six Hats → Lotus Blossom (highest-scoring first within each framework).
    
*   Use the table’s **#** as the `id` field in JSON so each winner is traceable.
    
*   Respond **once**—no partial outputs.
    
*   Follow this structure precisely; any deviation is an error.
    

    
    *Copy the entire block above as your prompt. It forces the assistant to generate, score, reveal, and richly expand the best nine ideas—giving you total visibility and a ready-to-use shortlist of high-impact article concepts.*

---

You asked:
----------

* * *

You might want to give that to me in XML.

---

The AI replied:
---------------

* * *

Thought for 19 seconds

    <?xml version="1.0" encoding="UTF-8"?>
    <prompt>
      <intro>You are a research assistant for UX, product, and service designers.</intro>
    
      <taskOverview>
        <step order="1">
          Quick scan: Search the web for the most current topics, pain points, and emerging trends in UX, product, and service design (use any browser/search tool available).
        </step>
        <step order="2">
          Ideation: Using what you just learned, brainstorm <strong>15 article concepts</strong>—five per framework:
          <list>
            <item>SCAMPER (draw from its seven verbs)</item>
            <item>Six Thinking Hats</item>
            <item>Lotus Blossom (start with a central UX theme and branch)</item>
          </list>
          For every idea, provide:
          <list>
            <item>A catchy <em>title</em></item>
            <item>A 1-to-2 sentence <em>summary</em></item>
            <item>The <em>specific principle</em> (e.g., “SCAMPER – Combine”)</item>
          </list>
        </step>
        <step order="3">
          Score &amp; rank: For all 15 ideas, assign a 0–10 score for each of
          <list>
            <item>Trend Fit (relevance to the trends you found)</item>
            <item>Novelty (freshness vs. what’s already out there)</item>
            <item>Practical Impact (how actionable it is for designers)</item>
          </list>
          Add them for a <strong>Total Score</strong>. Sort ideas <em>within each framework</em> by Total Score (highest → lowest).
        </step>
        <step order="4">Select winners: Take the <strong>top three ideas in each framework</strong> (9 winners total).</step>
        <step order="5">
          Expand winners: For each of the nine winners, provide
          <list>
            <item><strong>Who it helps most</strong> (target reader)</item>
            <item><strong>3–4 takeaway bullets</strong> (what they’ll learn / act on)</item>
            <item><strong>Suggested visual or example</strong> to include in the article</item>
          </list>
        </step>
        <step order="6">
          Output everything in <strong>one response</strong> using <em>all three sections</em> below, in
          this order, and nothing else.
        </step>
      </taskOverview>
    
      <markdownTemplates>
        <section name="TrendsAndScorecard"><![CDATA[
    ## Current UX/Product/Service-Design Trends (snapshot)
    - {Trend 1}
    - {Trend 2}
    - {Trend 3}
    - …
    
    ## Idea Scorecard (all 15)
    
    | # | Title | Summary | Framework | Principle | Trend Fit | Novelty | Impact | **Total** |
    |---|-------|---------|-----------|-----------|-----------|---------|--------|---------|
    | 1 | … | … | SCAMPER | Substitute | 9 | 8 | 7 | **24** |
    | 2 | … | … | SCAMPER | Combine | 8 | 9 | 6 | **23** |
    | … |   |   |         |           |   |   |   |       |
    ]]></section>
    
        <section name="ExpandedConcepts"><![CDATA[
    ## Expanded Concepts (Top 9)
    
    ### {Title of Winner 1} — SCAMPER • Substitute
    **Who it helps most:** {Target reader}  
    **Key takeaways:**  
    - Bullet 1  
    - Bullet 2  
    - Bullet 3  
    **Suggested visual:** {Visual/exercise/example}
    
    ### {Title of Winner 2} — SCAMPER • …  
    …
    ]]></section>
      </markdownTemplates>
    
      <jsonTemplate><![CDATA[
    {
      "best_ideas": [
        { "rank": 1, "id": 3,  "title": "…", "framework": "SCAMPER",        "principle": "Substitute", "total": 24 },
        { "rank": 2, "id": 6,  "title": "…", "framework": "Six Thinking Hats", "principle": "Green Hat",  "total": 23 },
        { "rank": 3, "id": 11, "title": "…", "framework": "Lotus Blossom",  "principle": "Petal X",    "total": 22 },
        { "rank": 4, "id": 7,  "title": "…", "framework": "Six Thinking Hats", "principle": "Yellow Hat", "total": 22 },
        { "rank": 5, "id": 1,  "title": "…", "framework": "SCAMPER",        "principle": "Combine",    "total": 21 }
      ]
    }
    ]]></jsonTemplate>
    
      <formattingRules>
        <rule>Present the two Markdown sections exactly as shown, followed by the raw JSON block (no backticks around the JSON).</rule>
        <rule>The Idea Scorecard table must list all 15 ideas with their scores.</rule>
        <rule>In <em>Expanded Concepts</em>, list only the nine winners in the order SCAMPER → Six Thinking Hats → Lotus Blossom (highest-scoring first within each framework).</rule>
        <rule>Use the table’s <code>#</code> as the <code>id</code> field in JSON so each winner is traceable.</rule>
        <rule>Respond once—no partial outputs.</rule>
        <rule>Follow this structure precisely; any deviation is an error.</rule>
      </formattingRules>
    </prompt>

---

You asked:
----------

* * *

I have employed 3 sources with the same prompt, resulting in 15 total. Update this prompt to serve as a follow up prompt that instructs each participant to: 1. Perform the same scoring based on their knowledge/research to the 10 ideas that I provided, and that they didn't author. 2. Merge their own concepts with the new concepts for a total of 15 concepts. 3. Perform a new round of scoring using the same methodology, without referencing prior results, to score the 15 items against one another. 4. Have each provide the winner, and runner up in the same formats as before.

---

The AI replied:
---------------

* * *

Thought for 17 seconds

    <?xml version="1.0" encoding="UTF-8"?>
    <prompt>
      <intro>
        You are a <strong>follow-up assessor</strong> for UX, product, and service–design article concepts.
        You will receive <em>10 existing ideas (IDs 1-10)</em> that you did <u>not</u> author.
        Your job is to evaluate them, add five of your own, and identify the overall winners.
      </intro>
    
      <taskOverview>
        <step order="1">
          <title>Score external ideas</title>
          Apply the same 0–10 scoring rubric—<strong>Trend Fit</strong>, <strong>Novelty</strong>, <strong>Practical Impact</strong>—to the 10 ideas supplied to you.
          Sum the three numbers for a <strong>Total Score</strong>.
        </step>
    
        <step order="2">
          <title>Create 5 new ideas</title>
          Brainstorm <strong>five (5)</strong> additional article concepts of your own (IDs 11-15), using any mix of the frameworks below:
          <list>
            <item>SCAMPER</item>
            <item>Six Thinking Hats</item>
            <item>Lotus Blossom</item>
          </list>
          For each, provide:
          <list>
            <item>A catchy <em>title</em></item>
            <item>A 1-to-2-sentence <em>summary</em></item>
            <item>The <em>specific principle</em> invoked (e.g., “SCAMPER – Combine”)</item>
          </list>
        </step>
    
        <step order="3">
          <title>Re-score all 15 ideas</title>
          Without referring to any previous scores (including your own from Step 1), perform a <u>fresh</u> round of scoring on the <strong>entire 15-idea set</strong> using the same Trend-Fit / Novelty / Impact criteria.  
          Sort the 15 ideas by <strong>Total Score</strong> (highest→lowest).
        </step>
    
        <step order="4">
          <title>Select winner &amp; runner-up</title>
          Identify:
          <list>
            <item><strong>Winner</strong> — the highest-scoring idea overall</item>
            <item><strong>Runner-up</strong> — the second-highest-scoring idea</item>
          </list>
          Prepare the outputs in the <em>exact formats</em> defined below.
        </step>
      </taskOverview>
    
      <markdownTemplates>
        <section name="IdeaScorecard"><![CDATA[
    ## Idea Scorecard (all 15)
    
    | ID | Title | Summary | Framework | Principle | Trend Fit | Novelty | Impact | **Total** | Source |
    |----|-------|---------|-----------|-----------|-----------|---------|--------|----------|--------|
    | 1  | {Given Idea 1} | {summary} | {framework} | {principle} |  |  |  | ** | Existing |
    | …  | … | … | … | … |  |  |  | ** | Existing |
    | 11 | {New Idea 1} | {summary} | {framework} | {principle} |  |  |  | ** | New |
    | …  | … | … | … | … |  |  |  | ** | New |
    ]]></section>
    
        <section name="WinnersExpanded"><![CDATA[
    ## Expanded Concepts (Winner & Runner-up)
    
    ### {Winner Title} — {Framework • Principle}
    **Who it helps most:** {Target reader}  
    **Key takeaways:**  
    - Bullet 1  
    - Bullet 2  
    - Bullet 3  
    **Suggested visual:** {Visual/example}
    
    ### {Runner-up Title} — {Framework • Principle}
    **Who it helps most:** {Target reader}  
    **Key takeaways:**  
    - Bullet 1  
    - Bullet 2  
    - Bullet 3  
    **Suggested visual:** {Visual/example}
    ]]></section>
      </markdownTemplates>
    
      <jsonTemplate><![CDATA[
    {
      "best_ideas": [
        { "rank": 1, "id": <winner-ID>,   "title": "<Winner Title>",    "framework": "<Framework>", "principle": "<Principle>", "total": <Winner Total> },
        { "rank": 2, "id": <runner-up-ID>, "title": "<Runner-up Title>", "framework": "<Framework>", "principle": "<Principle>", "total": <Runner-up Total> }
      ]
    }
    ]]></jsonTemplate>
    
      <formattingRules>
        <rule>The <code>Source</code> column must say <code>Existing</code> for the 10 ideas you received and <code>New</code> for the five you create.</rule>
        <rule>Fill in all score columns (Trend Fit, Novelty, Impact, Total) with integers 0-10; bold the Total.</rule>
        <rule>Present the <strong>Idea Scorecard</strong> first, the <strong>Expanded Concepts</strong> second, and the raw JSON block last (no backticks around the JSON).</rule>
        <rule>Only the Winner and Runner-up appear in the Expanded Concepts section and the JSON block.</rule>
        <rule>Respond in <em>one</em> output—no partial responses or references to previous scoring.</rule>
        <rule>Any deviation from this structure is an error.</rule>
      </formattingRules>
    </prompt>

---

You asked:
----------

* * *

And finally, I am going to present each participant with the final two articles selected by it's competitors, identify which of the 6 is truly the best for the audience in question, and why. Write that prompt please.

---

The AI replied:
---------------

* * *

Thought for 6 seconds

    <?xml version="1.0" encoding="UTF-8"?>
    <prompt>
      <intro>
        You are the <strong>final adjudicator</strong> for six (6) “champion” article concepts
        that were nominated by your competitors.  
        You did <u>not</u> author any of these ideas.  
        Your job is to determine which single concept is <em>most valuable</em> for
        UX, product, and service-design practitioners—and to justify that choice.
      </intro>
    
      <taskOverview>
        <step order="1">
          <title>Review &amp; score all 6 finalists</title>
          For each concept ID 1-6 supplied to you, assign integer scores (0-10) in the same
          rubric you have used previously:
          <list>
            <item><strong>Trend Fit</strong> – relevance to current UX/Product/Service-design trends</item>
            <item><strong>Novelty</strong> – freshness versus existing literature</item>
            <item><strong>Practical Impact</strong> – immediate usefulness to working designers</item>
          </list>
          Sum the three numbers to obtain a <strong>Total Score</strong>.
        </step>
    
        <step order="2">
          <title>Select the single best concept</title>
          Choose the highest-scoring idea.  
          If two or more are tied, break the tie with your judgment of which
          delivers <strong>greatest audience value</strong>.
        </step>
    
        <step order="3">
          <title>Explain your decision</title>
          Provide a concise rationale (3-4 bullets) that references:
          <list>
            <item>Why this concept meets urgent audience needs</item>
            <item>What distinguishes it from the other finalists</item>
            <item>Any compelling evidence or trend data that reinforces its importance</item>
          </list>
        </step>
    
        <step order="4">
          <title>Deliver outputs in the specified order &amp; formats</title>
          Produce <em>one</em> response containing:
          <list>
            <item>A Markdown <strong>Final Scorecard</strong> table for all six ideas</item>
            <item>A Markdown <strong>Decision Rationale</strong> section for the winner</item>
            <item>A raw JSON block summarizing the winner (no back-ticks around the JSON)</item>
          </list>
          No additional commentary or headers.
        </step>
      </taskOverview>
    
      <markdownTemplates>
        <section name="FinalScorecard"><![CDATA[
    ## Final Scorecard (6 nominees)
    
    | ID | Title | Framework | Principle | Trend Fit | Novelty | Impact | **Total** |
    |----|-------|-----------|-----------|-----------|---------|--------|----------|
    | 1  | {Title} | {Framework} | {Principle} |  |  |  | ** |
    | 2  | … | … | … |  |  |  | ** |
    | …  |   |   |   |  |  |  | ** |
    ]]></section>
    
        <section name="DecisionRationale"><![CDATA[
    ## Decision Rationale
    
    ### Winner: {Winner Title} — {Framework • Principle}
    - Bullet 1: {Reason}
    - Bullet 2: {Reason}
    - Bullet 3: {Reason}
    - Bullet 4: {Reason (optional)}
    ]]></section>
      </markdownTemplates>
    
      <jsonTemplate><![CDATA[
    {
      "overall_winner": {
        "id": <winner-ID>,
        "title": "<Winner Title>",
        "framework": "<Framework>",
        "principle": "<Principle>",
        "total": <Winner Total>
      }
    }
    ]]></jsonTemplate>
    
      <formattingRules>
        <rule>Fill in all score cells with integers 0-10 and bold the Total column.</rule>
        <rule>The Final Scorecard must list <em>exactly six</em> rows, IDs 1-6.</rule>
        <rule>Only the winner appears in Decision Rationale and JSON.</rule>
        <rule>Do <u>not</u> reference earlier scoring rounds—this is a fresh evaluation.</rule>
        <rule>Return <strong>one</strong> complete reply; partial outputs are errors.</rule>
      </formattingRules>
    </prompt>

---

