---
title: "Your Article Title"
date: YYYYMMDD
author: "William Trekell"
ai_tools_used:
  - TBD
ai_usage:
  description: >
    AI was used to help brainstorm ideas, generate an outline, and suggest alternative phrasings.
  reason: "To increase clarity and overcome writer’s block"
human_oversight: >
  I reviewed, edited, fact-checked, and finalized the content. All content decisions were made by me.
author_responsibility: >
  The ideas and conclusions expressed are my own. I take full responsibility for the article’s accuracy and integrity.
final_disclosure_statement: TBD
---

# Process
1. Couldn't think of an article. I've been trying to sort out longer story arc, but the agents got the better of me.
2. Decided to go meta, write an article on brainstorming by brainstorming.
3. Engaged o3 to set up a prompt to brainstorm using the 3 frameworks I've been looking at, to date I've only used SCAMPER to any real degree.

---

## Timeline of the ChatGPT o3 Article Experiment Conversation

### 1. **Initial Prompt Structuring**

* **You asked for:**
  A robust prompt to reliably get a single, well-structured set of article ideas and trends for UX/product/service designers, with both markdown and JSON outputs.
* **ChatGPT provided:**
  A copy-paste prompt including clear markdown and JSON templates, designed to collect 9 article ideas (3 each from SCAMPER, Six Thinking Hats, and Lotus Blossom frameworks), followed by selection of the 5 best.

---

### 2. **Prompt Scope & Rationale**

* **You questioned:**
  Why only 9 ideas, when the frameworks combined could provide many more.
* **ChatGPT explained:**
  The cap was for variety and response-length control, not because of limitations in the frameworks. You were invited to adjust the number as needed.

---

### 3. **Quality Control Concerns**

* **You raised:**
  How to ensure the “best” ideas were being selected (not just the first three).
* **ChatGPT suggested:**
  Adding a scoring step: score each idea for Trend Fit, Novelty, and Practical Impact (0–10 each), sum, and rank.
  Update the output: markdown table shows all scores; JSON includes winning IDs and totals.

---

### 4. **Prompt Expansion and Transparency**

* **You requested:**
  More transparency and an expanded workflow (all ideas shown and scored; top winners expanded).
* **ChatGPT provided:**
  A new, more comprehensive prompt:

  * 15 ideas (5 per framework)
  * All ideas scored, ranked, and displayed
  * Top 3 per framework “expanded” with target reader, takeaways, and visual suggestion
  * Detailed markdown and JSON outputs

---

### 5. **XML Format**

* **You requested:**
  The full prompt structure in XML for integration or documentation purposes.
* **ChatGPT provided:**
  The prompt in XML, complete with all steps, markdown and JSON templates, and formatting rules.

---

### 6. **Multi-Agent Experiment Extension**

* **You described:**
  Running the same prompt with three different sources/agents, generating 15 ideas in total.

* **You asked for:**
  A follow-up prompt instructing each participant to:

  1. Score the 10 ideas they didn’t author
  2. Merge them with their own 5 ideas
  3. Re-score all 15 ideas afresh
  4. Output the winner and runner-up, in the same formats

* **ChatGPT provided:**
  A detailed XML prompt for this cross-evaluation workflow, with all templates and instructions.

---

### 7. **Final Showdown**

* **You asked for:**
  A final prompt to present each participant with the two winning articles from their competitors, and have them select the single best for the audience, with justification.
* **ChatGPT provided:**
  The final adjudicator prompt in XML, instructing them to score all 6, pick a single winner, and provide a concise rationale and JSON summary.

---

### 8. **Clarification and Guidance**

* **You clarified:**
  That you were not asking for prompts, but for an easy way to parse the conversation so you could document your experiment and write up the article.

---

## **Summary Table Version**

| Stage | What Happened                           | Key Output                             |
| ----- | --------------------------------------- | -------------------------------------- |
| 1     | Prompt for article ideation and format  | Full markdown/JSON prompt              |
| 2     | Asked about number of ideas             | Explanation & flexibility              |
| 3     | Raised quality control concerns         | Scoring/ranking step added             |
| 4     | Asked for transparency and expansion    | Expanded, more detailed prompt         |
| 5     | Requested XML format                    | XML version of prompt                  |
| 6     | Described multi-agent workflow          | Follow-up XML prompt for cross-scoring |
| 7     | Asked for final winner selection prompt | Final XML adjudicator prompt           |
| 8     | Clarified your ask                      | (That’s this summary!)                 |

---

## Quotes
Great question! I went through the conversation you had with ChatGPT o3 (as found in your provided file), looking for **memorable quotes, turns of phrase, or moments of clarity** from your side that would stand out for readers—either as funny, insightful, skeptical, or as good “process quotes” to illustrate your approach.

Here are the **noteworthy user quotes** I’d highlight for your article:

---

### 1. **On Prompt Scope:**

> “Why do you say 9, scamper and six thinking hats alone provide more than 9”

*Why it’s notable:*
This immediately signals your critical, design-thinking mindset, and willingness to push beyond template limitations. It sets up a natural tension about prompt scope and completeness.

---

### 2. **On Quality Assurance in AI Output:**

> “Understandable, but how am I to know if I got the best 3, the worst 3, or more likely than not...the first 3.”

*Why it’s notable:*
This is *the* quote for showing your concern about AI’s selection transparency. It’s punchy and relatable—readers will get the skepticism.

---

### 3. **On Expanding the AI’s Approach:**

> “That means it would have to provide all of them, show me the scores, and expand on the 9”

*Why it’s notable:*
This is a crisp, summary-level call for more transparency. It marks a pivot point in the experiment—moving from just “get me outputs” to “show your work.”

---

### 4. **On Iterative Prompting:**

> “You might want to give that to me in XML.”

*Why it’s notable:*
Dry, witty, and signals technical fluency and the layered nature of your project. This is the kind of aside that makes an experiment feel *real* and iterative.

---

### 5. **On Meta-Process and Multi-Agent Testing:**

> “I have employed 3 sources with the same prompt, resulting in 15 total. Update this prompt to serve as a follow up prompt that instructs each participant to: 1. Perform the same scoring based on their knowledge/research to the 10 ideas that I provided, and that they didn't author. ...”

*Why it’s notable:*
This quote demonstrates your experimental rigor and multi-agent approach—something rare and of interest to methodologically-minded readers.

---

### 6. **On Clarifying the True Ask (Process Reflection):**

> “Thanks, that's not what I asked for.”
>
> “I'm not asking you for the prompt, clearly I have it given it's in the file.”

*Why it’s notable:*
These are strong, direct statements that showcase critical engagement and remind readers this wasn’t just “prompt and accept”—you were actively steering the conversation and holding the AI accountable to your needs.

---

### 7. **On Documenting the Experiment:**

> “The ask is a timeline of the conversation. I have the article, in fact I have 3, what I don't have is an easy way to parse this file so I can document the experiment.”

*Why it’s notable:*
This frames the project for readers: You’re not just playing with prompts, you’re building a case study/documentary artifact. It grounds the article as more than just an AI-generated listicle.

---

## **How to Use These Quotes**

* As blockquotes in your article to “break up” the process narrative
* To illustrate moments of skepticism, curiosity, or technical depth
* As captions for screenshots of the AI outputs (e.g., “I have employed 3 sources…” above a figure)
* In a sidebar about “What I learned prompting AI for research”

If you want these organized in a different way (by theme, by “aha” moment, by humor, etc.), or want some lightly edited for clarity, just let me know!

---


```xml
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
```

---

4. Then I went through the tests

Absolutely, this is a great use-case for a **parallel timeline**!
Here’s a comparative, session-by-session timeline of your multi-AI brainstorming experiment (ChatGPT-4.1, Claude 4 Sonnet, and Gemini 2.5 Pro)—**showing the key moves in each session, overlaps, and what was unique to each AI.**

---

# Parallel Timeline: UX Article Experiment with 3 AIs

## Session Start (all AIs, \~same time, \~June 24, 2025)

**Prompt delivered to all three AIs:**

* Scan the web for current UX/product/service design trends.
* Generate 15 article ideas (5 each: SCAMPER, Six Thinking Hats, Lotus Blossom).
* Score/rank all ideas (Trend Fit, Novelty, Impact).
* Pick the top 3 per framework, expand on each.
* Output in strict Markdown and JSON format.

---

## **1. Initial Trend Scanning**

### ChatGPT-4.1

* Quickly returns with a list focused on:

  * Value-driven AI integration
  * Accessibility and ethics
  * Immersive 3D, AR/VR design
  * Service design for sustainability

### Claude 4 Sonnet

* Web-searches for “UX design trends 2025,” “pain points,” and “service design trends.”
* Surfaces:

  * AI moving from hype to practical value
  * Strategic UX leadership, business thinking
  * European Accessibility Act (EAA) as a compliance driver
  * Zero-UI, spatial/3D design
  * Self-service, proactive design

### Gemini 2.5 Pro

* Cites trends like:

  * AI-augmented workflows
  * Hyper-personalization
  * Multimodal (voice/touch/AR/VR)
  * Sustainable/ethical design
  * “Proactive UX” and complexity

**All AIs converged on:**

* AI’s centrality (but more nuanced than “just add AI”)
* Accessibility & ethics
* Immersive/3D/spatial experiences
* Sustainability

---

## **2. Idea Generation (Brainstorm 15 Concepts)**

### ChatGPT-4.1

* Articles such as “AI-Driven Empathy Mapping,” “Sustainable Interaction Patterns,” “De-Biasing Design Teams,” “Lotus Blossom: Micro-interaction Toolkit.”
* Multiple ideas directly reference real industry sites (UXDesignInstitute, Lyssna, Arxiv, etc.).

### Claude 4 Sonnet

* Ideas include “Substitute Screens with Spatial Layers,” “Combine Ethics with AI Tools,” “Red Hat: Designing for Emotional AI Trust,” “Proactive Design: The Central Bloom.”
* More explicit about “Proactive Service Design” and “Zero-Waste Digital.”

### Gemini 2.5 Pro

* Ideas like “The Post-App Era: Substituting Apps with AI Agents,” “Combine or Die: Merging Service & Product Design Teams,” “The Green Hat: Beyond Brainstorms,” “Your Next Interface Isn’t a Screen.”
* Offers catchier, sometimes slightly bolder phrasing (“Combine or Die”).

---

## **3. Scoring and Selection**

* **All AIs:** Assign numeric scores to each idea (Trend Fit, Novelty, Impact).
* **All AIs:** Rank by total score, select top 3 per framework (9 total per session).
* **All AIs:** Expand each winner (target reader, takeaways, visual).

#### Noteworthy differences:

* **Gemini** gave extremely high scores to “The Green Hat: Beyond Brainstorms—How Generative AI Really Fuels Creativity” (28/30).
* **ChatGPT** often rated “AI-Driven Empathy Mapping” and “Immersive 3D Navigation” at the top.
* **Claude** elevated “Substitute Screens with Spatial Layers” and “Proactive Design: The Central Bloom.”

---

## **4. Cross-Evaluation (Next Round, Parallel)**

* Each AI receives 10 ideas from others + adds 5 of its own.
* **Fresh scoring round** (no reference to prior scores).
* **Winner and runner-up chosen per AI.**

#### Distinctive moves:

* **Claude** often surfaced “Modify Mental Models for Zero-UI” as a high-scorer—a subtle, behaviorally focused idea.
* **Gemini** repeatedly pushed “The Post-App Era: Substituting Apps with AI Agents” as a top winner.
* **ChatGPT** highlighted “Substitute Screens with Spatial Layers” and “Proactive Design” in runner-up positions.

---

## **5. Final Adjudication (Winner Selection)**

* Each AI gets the 2 winners from its competitors (6 total).
* Asked to pick the *single* best for the audience and justify why.

---

# **Noteworthy Moves and Unique Behaviors**

## **ChatGPT-4.1**

* Most heavily cited **external sources** (adding link annotations in trends).
* Scored “AI-Driven Empathy Mapping” and “Immersive 3D Navigation” highest—clear bias toward *process improvement* and *immersive future*.
* Provided more “before/after” visuals and workflow transformations.
* More conservative in scoring; didn’t “overscore” any single idea.

## **Claude 4 Sonnet**

* Emphasized **behavioral and strategy shifts**: e.g., “Modify Mental Models for Zero-UI,” “Proactive Service Design.”
* Brought **regulatory/compliance trends** (European Accessibility Act) to the foreground.
* Repeatedly surfaced “Substitute Screens with Spatial Layers”—a true *paradigm shift* idea.
* Provided the most detailed *emotional/psychological* takeaways.

## **Gemini 2.5 Pro**

* Emphasized **organizational/structural change**: “Combine or Die: Merging Service & Product Design Teams,” “The Post-App Era: Substituting Apps with AI Agents.”
* Most likely to use dramatic/imperative language (“Combine or Die!”).
* Consistently awarded highest individual score (28/30) to “The Green Hat: Beyond Brainstorms.”
* Excelled at *narrative framing*—explaining *why* a trend matters in future language.

---

# **Parallel Timeline Table (Session by Session)**

| Time (Approx) | ChatGPT-4.1                               | Claude 4 Sonnet                           | Gemini 2.5 Pro                           |
| ------------- | ----------------------------------------- | ----------------------------------------- | ---------------------------------------- |
| 0 min         | Prompt received; scans trends             | Prompt received; web search; scans trends | Prompt received; trend scan              |
| +5 min        | Returns with AI, accessibility, immersive | AI, strategic UX, ethics, Zero-UI         | AI, personalization, multimodal, ethics  |
| +15 min       | 15 ideas generated, scored                | 15 ideas generated, scored                | 15 ideas generated, scored               |
| +20 min       | Top 9 selected, expanded                  | Top 9 selected, expanded                  | Top 9 selected, expanded                 |
| +30 min       | Receives 10 competitor ideas, adds 5 new  | Receives 10 competitor ideas, adds 5 new  | Receives 10 competitor ideas, adds 5 new |
| +35 min       | Re-scores all 15, picks winner/runner-up  | Re-scores all 15, picks winner/runner-up  | Re-scores all 15, picks winner/runner-up |
| +40 min       | Final 2 from each sent to competitors     | Final 2 from each sent to competitors     | Final 2 from each sent to competitors    |
| +45 min       | Picks overall winner                      | Picks overall winner                      | Picks overall winner                     |

---

# **What Was Unique?**

### **ChatGPT-4.1**

* Deepest **sourcing and external references** in its trends (often with links).
* Visuals typically “before/after” process diagrams.
* Prioritized actionable, process-focused innovations.

### **Claude 4 Sonnet**

* More **behavioral and compliance-aware** (e.g., regulation-driven trends).
* Highlighted psychology and “zero-UI” more than others.
* Most explicit about *proactive* service design.

### **Gemini 2.5 Pro**

* More **organizational and “future-of-design” framing**.
* Willing to make bold, almost manifesto-style claims.
* Consistently gave one of the highest scores (28) to a single creativity/AI ideation article.

---

# **Summary**

* **All AIs** moved through the same workflow in parallel—trend scan → ideation → scoring → selection → cross-eval → final pick.
* **Overlap in top ideas**: “Substitute Screens with Spatial Layers,” “The Post-App Era: Substituting Apps with AI Agents,” and “Proactive Design: The Central Bloom/Your Next Interface Isn’t a Screen.”
* **Unique value:** Each AI’s “voice” surfaced differently—sourcing, psychology, organizational shifts.
* **For your article:** Consider “braiding” these perspectives to show where LLMs overlap (consensus) and diverge (unique insight).

---

==Claude 4 Sonnet opted to write an article right off the bat without being provided with any information... Great.==

1. Had each AI write a version of the article without the template.
2. I had each write an article with the first template
2.1 Claude sonnet with the one authored by claude
2.2 Claude opus with the one authored by GPT, thought this might help balance things out.


---

Fantastic, thank you. I have 2 templates that I would like to try out. I will provide them to you, one at a time, and I would like you to create a new article that adheres to the template. You may, or may not, draw upon this version if appropriate.

---

> Purpose:

> Comprehensive, transparent exploration (experiment, review, or thought piece). Suitable for documenting failures, processes, or new frameworks. Always flexible, never rigid.

#### Structure:

Title

> Purpose: Clearly states the topic/focus. \[If not supplied, annotate: “Author to provide clear, descriptive title.”]

---

Opening Context

> Purpose: Why does this article exist? Who is it for? What’s the problem, challenge, or curiosity?

> Instruction: If missing, annotate “Author to specify: Why was this written and what is the reader’s gain?”

---

Orientation / TL;DR

> Purpose: Succinctly summarize the attempt, findings, or main theme—without assuming success or outcome. Why should a reader stay?

> Instruction: If absent, annotate “Author to add a summary of what’s attempted, what’s at stake, and why it matters—even if it failed.”

---

Context & Rationale

> Purpose: Frame the background, drivers, and existing work. “Why now?” “Why this question or method?”

> Instruction: If missing, annotate “Author to provide real-world rationale, trigger event, or user need.”

---

Main Body (Modular, Repeatable Sections)

> Purpose: House the main content—process, analysis, or frameworks. Each section starts with a clear intent (e.g., ‘Documenting Methodology’, ‘Analyzing Results’, etc.).

> \*Instruction:

>

> * Annotate each: “Section Purpose: \[state]”

> * If experiment: Provide step-by-step details, failures, surprises.

> * If framework: Break down elements and use cases, request visuals if needed (“Author to provide diagrams/screenshots”).

>  If review: Annotate for supporting data, context, or further reading as needed.\

---

Synthesis / Reflection

> Purpose: What’s learned? What’s still open? Share the value, ambiguity, or warning for others.

> Instruction: “Author to summarize the key insight, lesson, or open question.” If not available, annotate for user input.

---

Resources & Further Reading (Optional)

> Purpose: Link to tools, code, templates, or supporting research. Cross-link other articles.

> Instruction: “Author to provide relevant links or annotate for later inclusion.”

---

Next Steps / Invitation

> Purpose: Suggest future directions, reader action, or request feedback.

> Instruction: “Author to specify next actions or open questions.” If missing, annotate accordingly.

---

#### Long Form Word Count Guidance:

* Total: 1,500–3,000 words

* Openings: 150–250

* TL;DR: 80–120

* Context: 200–350

* Body Sections: 350–500 each

* Synthesis/Resources/Next: 150–200 each

#### Bullets/Lists:

* Use only in body sections (steps, lists, comparisons, cautions)

* Bullets: 1–2 lines each, parallel in structure

* Introduce each list with a lead-in sentence

* Never use bullets in intros or conclusions

---

This is the first template. Please author the requested article.

---

Fantastic, thank you. I have 2 templates that I would like to try out. I will provide them to you, one at a time, and I would like you to create a new article that adheres to the template. You may, or may not, draw upon this version if appropriate.

---

---

This is the first template. Please author the requested article.
Purpose: Complete exploration of a topic - experiments, analysis, opinions, or deep dives  

Length: 2,500-5,000 words  

Distribution: Blog, documentation sites (not newsletters)

### Structure

Opening - Why This Matters (100-150 words)

- Start with what grabbed your attention or pissed you off

- Could be a moment, a pattern, a question, or an observation

- Make readers care within the first 100 words

- No bullets, no throat-clearing

The Meat - What You Have to Say (400-800 words per section)

- Follow the natural flow of your thinking

- If it's an experiment: what you tried and what happened

- If it's an opinion: what you believe and why

- If it's analysis: what you found and what it means

- Include the messy parts, the surprises, the "holy shit" moments

The Proof - Why Someone Should Believe You (varies)

- Only include what backs up your point

- Could be data, examples, experiences, or logic

- Don't pad with research for research's sake

- If you're just ranting, own it

The Point - What This Means (150-250 words)

- Connect your specific story to bigger implications

- What should readers do differently?

- What questions does this raise?

- Leave them with something to chew on

### Formatting Specifications

- Subheadings every 300-500 words

- Paragraphs: 2-4 sentences (50-100 words)

- Bullets only for complex lists (max 7 items)

- Include code blocks, tables, examples where natural

- Time estimates for any procedures

### Extraction Markers

As you write, mark:

- [EXTRACT: Medium] - Full section that could stand alone

- [EXTRACT: Reference] - Concept needing permanent definition

- [EXTRACT: Story] - Anecdote worth retelling

- [EXTRACT: Tip] - Quick win to share

---

1. I mistakenly gave both AI the same template the second time that they had recived previously. Sonnet caught it, Opus wrote the article. I used edit to replace the erroneous prompt to avoid contamination, while moving forward with Sonnet since it had caught it.
2. This excercise consumed my usage limit, I'll have to wait to hear what they think when reflecting on the 3 versions.

---
---

Now that we're back, I have them comparing the articls holistically and by section.
1. It's immediately evident that I probably should have provided an identifier (it's been months, I'm out of practice.)
2. Intrestingly enough, sonnet had less sections, possibly half as many, when they did the comparison.
2.1 Neither preferred their own to the templates. Sonnet rankng itself last, opus in second place.
2.2 After going back and checking, both prefered their versions from the Claude template.
2.3 I had each outline the 3 best and worst aspects of both, and the reason was clear...something about the claude template failed to restrict them from embelishment.
2.3.1 Going back and reviewing the templates the issue becomes pretty clear incredibly quick, Claude specified what should be marked, the AI filled in the rest without second thought. This means that not only did the template fail, but the safe guards I have in place to prevent the AI from writing on my behalf failed as well.
3. Confirmed using 4.1 for the GPT templates. Not ideal, 4.5 would have been better, but it's impossible to use it and not run out of usage time unless I want to risk losing it.

---
From the future article that will compare against last year:
6. With all 4 articles, Opus failed to connect the dots, that the instruction I had been most explicit about failed to happen.
6.1 After pointing out that the items it was citing were because the AI wrote in my place, it nailed them across the board.
6.2 I poked around to see if Claude wouldmake a useful recommendation for a fix, once my usage had essentially run out I had to tell it to fix the templates after a number of recommendations that would have been significantly more work for me.
6.3 I have new templates, I can't imagine I have more than one prompt left for the night, the warning came up 2-3 ago. 
6.4 I went back and skimmed through the 2 articles from Claude's template. The one by Sonnet was a far greater offender than the one by Opus. The latter had wrote in filler content as well, but it had at least annotated the same areas...in some it looked like it was trying to provide an example of what to right (which still defeates the purpose of me having to strip shit out), while others it appeared to indicate additions...amusingly enough, theyw ere the sections I said it could all but leave blank for me to write.
6.5 Looking back at the prompt o3 wrote for the task, and I'm sure it contributed to the issue, but it was the instruction followed for all articles so the Opus version still had a weak spot.
6.6 It's getting late, I'm getting tired, and I need to keep cleaning off this laptop so I can ship it back to offset the price of the new one. With these things in mind, I'm going to choose the dumbest option available. I'm going to throw the new template at the vesion of Opus that already wrote the 3. I don't want to spend the time tofix the original prompt, and I'm done with this for the night anyway. Let's invite the shitshow in.
6.7 Well, that was a success. It wrote something that exists between the experiment and the topis of the favored article. 
6.8 At this point, I think I'm at the same amount of time spent doing almost the same process. This time, I don't have anything from Claude that is usable base don it's own template.
---
The most notable divide between now and last year is the "reasoning" models. I'm fairly certain I applied CoT but I was in control of it, not something beneath the hood.
The other notable difference, is that I didn't write the prompt for authoring the articles, the behemoth I got back was littered with issues that I didn't see because I didn't read it, I made the mistake of trusting the AI because of the solid results I've been getting. Shame on me.

 I read the ones from GPT later, maybe I an use them as a better starting point. In th end, I don't think either of them even came close to writing about the actual experiment. I'll check tomorrow.
---
# Next Day
7. Somewhere in the middle of the night I worked with Opus on the template. We'll see how it goes.
7.1 I had Opus take shot at writing, it wasn't horrible but still represented a lot of work to clean up.
7.2.1 I took a second try with a clean slate, but this time I didn't supply my notes. I had to poke it a few times but got what I was looking for (not a final, mind you)
7.2.2 I handed it my notes and told it to flag all additions with XML, I think I'm close enough to take it to edits now.

