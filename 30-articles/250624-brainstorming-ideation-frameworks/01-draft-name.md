# An Experiment in AI-Driven Brainstorming: From Chaos to Consensus

-----

## Opening Context

This document outlines a structured experiment designed to move beyond generic AI-driven brainstorming and produce high-quality, validated article concepts. It is intended for UX, product, and service designers who need reliable, repeatable methods for leveraging AI in their creative process. After reading, you will have a framework for using multiple AI models to generate, score, and select topics, ensuring the final output is not just a random suggestion but a concept with validated relevance and impact.

-----

## Orientation / TL;DR

A multi-stage experiment was conducted using three major AI models (Claude 3.5 Sonnet, Gemini 2.5 Pro, and ChatGPT-4.1) to brainstorm and rank article ideas for a publication focused on UX and AI. The process began with significant prompt engineering to overcome the tendency of AI to provide low-quality or arbitrarily limited results. By forcing the AIs to generate a large set of ideas, score them against defined criteria (Trend Fit, Novelty, Practical Impact), and then adjudicate the winners, the experiment produced a strong consensus. Two of the three AIs independently selected the same winning topic: the challenge of orchestrating hybrid teams of human and AI designers. This result not only validates the chosen topic but also demonstrates a structured methodology for using AI as a transparent and effective creative partner.

-----

## Context & Rationale

In the current landscape, UX designers frequently use AI for ideation but often encounter the "black box" problem: outputs are generic, lack justification, and require significant rework, a phenomenon known as the "AI Tax." This experiment was designed to address the challenge of moving from simple, single-shot prompting to a structured, auditable process that yields high-quality, validated creative concepts. The core hypothesis was that a multi-round, competitive brainstorming process—involving explicit scoring and adjudication—would produce superior and more relevant ideas than a standard, unstructured prompt. The goal was to create a repeatable framework for AI-driven ideation that ensures transparency and quality control.

-----

## Main Body

### Section 1: Methodology and Approach

The experiment was structured in three phases, using **Claude 3.5 Sonnet**, **Gemini 2.5 Pro**, and **ChatGPT-4.1**.

  * **Frameworks Used for Ideation:** SCAMPER, Six Thinking Hats, and Lotus Blossom were the specified creative frameworks to ensure a diverse range of ideas.
  * **Process Followed:**
    1.  **Prompt Engineering:** An initial prompt was iteratively developed to force a specific sequence of tasks. A critical modification was the inclusion of a "score-and-rank" micro-step, requiring each AI to generate 15 ideas, score them transparently against Trend Fit, Novelty, and Practical Impact, and then expand on the top winners. This was designed to combat the "first three ideas" problem, where an AI provides the easiest, not necessarily the best, outputs.
    2.  **Multi-Round Execution:** The final, structured prompt was executed across the three AI models in a multi-round tournament:
          * **Round 1: Initial Brainstorm:** Each AI independently generated and scored 15 article concepts based on a web search for current UX trends.
          * **Round 2: Cross-Pollination & Re-Scoring:** Each AI was given the top ideas from its competitors and tasked with re-scoring the entire pool, adding five new ideas of its own.
          * **Round 3: Final Adjudication:** Each AI was presented with the six "champion" concepts from the previous rounds and instructed to select and justify a single overall winner.
  * **Key Decision:** The most important decision was to reject the AI's initial, unprompted behavior of limiting the idea pool. Forcing a comprehensive generation and a transparent scoring process was essential for the experiment's validity.

### Section 2: Process Documentation

The experiment began with a foundational challenge: initial prompts to the AI models resulted in low-quality or arbitrarily limited outputs. For instance, an early version of the prompt returned only nine ideas, despite the potential for many more from the specified frameworks. This underscored a common failure point in AI interaction—receiving outputs without understanding the selection criteria.

The solution was to engineer a more demanding prompt that dictated a precise, transparent process. This involved several key iterations documented in the setup phase:

1.  **Forcing Comprehensive Ideation:** The prompt was adjusted to demand ideas from *all* principles of the specified frameworks, not just a subset.
2.  **Implementing Quality Control:** A "score-and-rank" step was added. The AI was required to score each idea it generated against three criteria: **Trend Fit** (relevance to current trends), **Novelty** (freshness), and **Practical Impact** (actionability for designers). This forced the AI to "show its work."
3.  **Structured Output:** The prompt mandated that all outputs be formatted into a Markdown table and a JSON object to ensure consistency and machine readability.

This refined process transformed the interaction from a simple query into a structured, multi-step analysis, ensuring the final selection was based on auditable logic rather than opaque AI preference.

### Section 3: Results and Outputs

The final adjudication round produced a strong, though not unanimous, consensus.

  * **The Convergent Outcome:** Both Gemini and ChatGPT-4 selected the same concept as the overall winner: **"The Conductor: Orchestrating Human & AI Design Teams"**. Both models gave this concept the highest score for Practical Impact, identifying it as an urgent and unmet need for design leaders today.
  * **The Divergent Outcome:** Claude, in contrast, selected **"The Post-App Era: Substituting Apps with AI Agents"** as its winner. While this concept also scored highly on Trend Fit and Novelty, its practical impact was deemed less immediate by the other two models.

**Final Adjudication Scorecard (Gemini 2.5 Pro):**

| ID | Title | Framework | Principle | Trend Fit | Novelty | Impact | **Total** |
| :-- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 5 | The Conductor: Orchestrating Human & AI Design Teams | Six Thinking Hats | Blue Hat | 10 | 9 | 10 | **29** |
| 1 | AI for Accessibility Mapping | SCAMPER | Adapt | 9 | 9 | 10 | **28** |
| 3 | The Post-App Era: Substituting Apps with AI Agents | SCAMPER | Substitute | 10 | 9 | 8 | **27** |
| 6 | Your User's Digital Twin: Putting Personas on Live Data | SCAMPER | Put to another use | 8 | 9 | 8 | **25** |
| 2 | The Green Hat: Beyond Brainstorms... | Six Thinking Hats | Green Hat | 8 | 7 | 9 | **24** |
| 4 | Modify Mental Models for Zero-UI | SCAMPER | Modify | 7 | 8 | 7 | **22** |

This convergence from two different models on the same winning topic provides strong validation of its relevance and urgency for the target audience of UX and product designers.

### Section 4: Technical Implementation

The final prompt is a structured XML document that dictates a precise sequence of tasks and output formats. This approach ensures a consistent, high-quality response across different AI models. The prompt compels the AI to first research current trends, then generate a comprehensive set of ideas, score them transparently, and finally expand on the winners.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<prompt>
  <intro>You are a research assistant for UX, product, and service designers.</intro>
  <taskOverview>
    <step order="1">
      <title>Review & score all 6 finalists</title>
      For each concept ID 1-6 supplied to you, assign integer scores (0-10) in the same rubric you have used previously:
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
      <title>Deliver outputs in the specified order & formats</title>
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

This structured approach proved critical in overcoming the limitations of basic prompting and ensuring a high-quality, auditable outcome.

-----

## Synthesis / Reflection

This experiment reveals several key insights into effective AI collaboration. First, a structured, multi-round brainstorming process can elicit a consensus among different AI models, which serves as a powerful validation for the relevance of a topic. The convergence of two models on "The Conductor" theme was a significant finding.

Second, the winning concept's focus on *human-led orchestration* of AI, rather than full automation, is telling. This suggests that the current, most pressing need perceived by the models (and likely reflected in their training data) is not about replacing designers, but about providing them with frameworks to manage AI-augmented teams effectively. The AI models themselves identified the most valuable topic as one centered on managing AI.

A key limitation of this experiment is that it was based on a single, albeit complex, prompt. The results could vary with different models, frameworks, or subject matter. An open question remains regarding the AI's preference for the "human conductor" theme—is it a reflection of training data on successful AI adoption patterns, or a form of sophisticated alignment designed to make AI appear as a helpful, non-threatening partner?

-----

## Resources & References

  * **Prompt Engineering Process:** `chat-gpto3-setup.md`
  * **AI Session Transcripts:**
      * `claude-4sonnet-brainstorming.md`
      * `gemini-2.5pro-brainstorming.md`
      * `chat-gpt4.1-brainstorming.md`
  * **Analysis & Summary:** `syntax-and-empathy-publication.md`
  * **Creative Frameworks Referenced:** SCAMPER, Six Thinking Hats, Lotus Blossom

-----

## Next Steps / Invitation

The XML prompt provided in this document can be used as a template for conducting similar structured brainstorming sessions. Readers are invited to adapt this framework for their own domains and test it with different AI models. Comparing the results would provide valuable data on the consistency of this method across various creative and strategic challenges. Collaboration on refining these structured prompts is welcome.