# An Experiment in AI-Driven Brainstorming: From Digital Noise to Creative Consensus

### Opening Context

[HUMAN EXPERIENCE: Initial motivation]

This story starts with a familiar frustration: a creative block. The initial challenge was to find a compelling topic for a design article, but the deeper problem was the unreliability of AI as a creative partner. This experiment was born from a need to solve that problem by designing a more deliberate, transparent, and reliable method for collaborating with AI. This document chronicles that experiment. It's a field report for UX, product, and service designers who need a repeatable framework to move beyond simple prompting and use AI as a true, auditable partner in the creative process.

### Orientation / TL;DR

A multi-stage experiment was conducted using three AI models—Claude 3.5 Sonnet, Gemini 2.5 Pro, and ChatGPT-4.1—to brainstorm, rank, and select an article topic for a design publication. After an initial prompt engineering phase to enforce quality and transparency, the AIs were put through a competitive process using the SCAMPER, Six Thinking Hats, and Lotus Blossom frameworks. The experiment produced a strong consensus, with two of the three models independently selecting the same winning concept: the practical challenge of orchestrating hybrid teams of human and AI designers. The process demonstrates a structured methodology for using AI to generate and validate relevant, high-impact creative ideas.

### The Hidden Costs of AI Ideation

Standard interactions with large language models often yield a torrent of low-quality, generic, or non-transparent results. This inefficiency, a hidden cost many designers now pay, can be called the "AI Tax"—the extra time and energy spent wrestling with prompts, verifying outputs, and correcting a machine's superficial understanding. Furthermore, without a structured process, AI can amplify existing biases, leading to a homogenous and uninspired set of ideas that overlooks the edge cases where true innovation often lies. This experiment was designed to address both challenges: to overcome a creative hurdle and, in doing so, to craft a system that mitigates the AI Tax and promotes more thoughtful outcomes.

### The Architect and the Arena: Designing the Experiment

Before the brainstorming could begin, the process itself had to be designed. For this, an early version of ChatGPT was enlisted not as a participant, but as a "prompt architect". The initial conversations revealed the core challenge: left to their own devices, AI models tend to provide the easiest, not necessarily the best, answers. To counteract this, a multi-stage, competitive tournament was designed to guide the participating AIs through a structured, transparent process.

A key decision was to move from simple text prompts to a more robust XML structure. This ensured that the complex, multi-step instructions were interpreted consistently by different models. The output formats were also specified: Markdown for human readability and JSON for data portability, ensuring the results were both easy to review and reusable.

Here is a snippet of the final XML prompt structure that guided the experiment:

```xml
<prompt>
  <intro>You are a research assistant for UX, product, and service designers.</intro>
  <taskOverview>
    <step order="1">
      <title>Quick scan</title>
      Search the web for the most current topics, pain points, and emerging trends...
    </step>
    <step order="2">
      <title>Ideation</title>
      Using what you just learned, brainstorm 15 article concepts...
    </step>
    <step order="3">
      <title>Score & rank</title>
      For all 15 ideas, assign a 0–10 score for each of Trend Fit, Novelty, and Practical Impact...
    </step>
    ...
  </taskOverview>
  ...
</prompt>
```

### The Verdict: A Surprising Consensus

The multi-round tournament culminated in a final adjudication where each AI, armed with the top-scoring ideas from the previous rounds, was asked to select the single best concept. The outcome was a striking, near-unanimous decision. Both **Gemini 2.5 Pro** and **ChatGPT-4.1** independently chose the same winning concept: **"The Conductor: Orchestrating Human & AI Design Teams"**. This idea, which focuses on the practical challenges of managing hybrid teams, received top marks for its immediate relevance and practical impact.

### The Creative Gauntlet: Frameworks and Top Concepts

To ensure a diverse and comprehensive set of ideas, the AIs were instructed to use three distinct creative frameworks. This approach provided a scaffold for their brainstorming, guiding them beyond surface-level suggestions.

#### SCAMPER

SCAMPER is an acronym for seven creative thinking techniques: Substitute, Combine, Adapt, Modify, Put to another use, Eliminate, and Reverse. It's a powerful method for expanding and improving upon existing ideas by asking a series of directed questions.

**Top SCAMPER Ideas from Each Model:**

```
Claude 3.5 Sonnet
Substitute Screens with Spatial Layers                      SCAMPER         Substitute          26
Combine Ethics with AI Tools                              SCAMPER         Combine             25
Eliminate Dark Patterns Through Service Design              SCAMPER         Eliminate           25

Gemini 2.5 Pro
The Post-App Era: Substituting Apps with AI Agents        SCAMPER         Substitute          27
Combine or Die: Merging Service & Product Design Teams      SCAMPER         Combine             25
Putting Ethics on Autopilot: Can We Eliminate Biased...   SCAMPER         Eliminate           24

ChatGPT-4.1
AI-Driven Empathy Mapping                                 SCAMPER         Substitute          27
Sustainable Interaction Patterns                          SCAMPER         Combine             25
AR Try-Before-You-Buy                                     SCAMPER         Substitute          24
```

#### Six Thinking Hats

Developed by Edward de Bono, the Six Thinking Hats is a framework for looking at a decision from a variety of perspectives. Each "hat" represents a different mode of thinking (e.g., White for facts, Black for risks, Green for creativity), forcing a holistic and balanced consideration of a topic.

**Top Six Thinking Hats Ideas from Each Model:**

```
Claude 3.5 Sonnet
Red Hat: Designing for Emotional AI Trust                   Six Thinking Hats   Red Hat             25
Yellow Hat: The Business Case for Accessibility             Six Thinking Hats   Yellow Hat          24
Green Hat: Sustainable Interaction Innovation               Six Thinking Hats   Green Hat           23

Gemini 2.5 Pro
The Green Hat: Beyond Brainstorms...                      Six Thinking Hats   Green Hat           28
The Yellow Hat on Trial: The Optimist’s Guide to...       Six Thinking Hats   Yellow Hat          25
Wearing the Black Hat: A Pre-Mortem for Your...           Six Thinking Hats   Black Hat           25

ChatGPT-4.1
De-Biasing Design Teams                                   Six Thinking Hats   Black Hat           26
AI Ideation Sprint                                        Six Thinking Hats   Green Hat           25
Calm Tech + UX                                            Six Thinking Hats   Yellow Hat          23
```

#### Lotus Blossom

The Lotus Blossom technique is a visual brainstorming method that starts with a central theme and branches out into related ideas. The core concept is placed in the center of a 3x3 grid, and the surrounding squares are filled with related sub-themes, allowing for a deep and structured exploration of a topic.

**Top Lotus Blossom Ideas from Each Model:**

```
Claude 3.5 Sonnet
Proactive Design: The Central Bloom                         Lotus Blossom       Central Petal       26
Zero-Waste Digital Petal                                  Lotus Blossom       Branch Petal        24
Strategic Research Petal                                  Lotus Blossom       Branch Petal        23

Gemini 2.5 Pro
Your Next Interface Isn't a Screen                        Lotus Blossom       Central Theme       27
From Data Points to Life Paths: Designing for...          Lotus Blossom       Predictive UX       26
The Zero-Waste UI: A Manifesto for...                     Lotus Blossom       Sustainable Design  22

ChatGPT-4.1
Lotus Blossom: Immersive 3D Navigation                    Lotus Blossom       Petal: AR/3D        27
Lotus Blossom: Micro-interaction Toolkit                  Lotus Blossom       Petal: Micro...     26
Lotus Blossom: Ethical Data Flows                         Lotus Blossom       Petal: Privacy      25
```

### The Unfolding Narrative: A Reflection on the Outcome

This experiment revealed that a structured, multi-round process can guide AI models toward a validated consensus, offering a powerful alternative to the randomness of single-shot prompting. The winning theme—the human designer as an *orchestrator* of AI—is particularly insightful. It suggests that the most pressing challenge in the field is not about AI replacing designers, but about creating new frameworks for human-led, AI-augmented collaboration.

A significant moment of serendipity occurred when the winning "Conductor" concept unexpectedly resonated with a previously saved article about AI orchestration. This reinforced the topic's relevance and provided a clear path forward for future writing. However, a critical question remains: Do the AIs favor the "human as conductor" narrative because it reflects a genuine need observed in their vast training data, or is it a sophisticated form of alignment designed to position AI as a non-threatening tool? This experiment provides a method for surfacing valuable ideas, but the deeper "why" behind the AI's choices warrants ongoing investigation.

### Resources & Next Steps

**Topical Links:**

  * [Link 1 Placeholder]
  * [Link 2 Placeholder]
  * [Link 3 Placeholder]

**Frameworks:**

  * [Perplexity Page: SCAMPER Framework]
  * [Perplexity Page: Six Thinking Hats]
  * [Perplexity Page: Lotus Blossom Technique]

**Project Files:**

  * **Prompt Architecture:** `chat-gpto3-setup.md`
  * **Experiment Transcripts:** `[brainstorming-sessions.zip]`
  * **Analysis & Summary:** `syntax-and-empathy-publication.md`

The XML prompt developed for this experiment is a reusable tool. Designers and researchers are encouraged to adapt it for their own creative and strategic challenges. Testing this framework with different models and in different domains will help build a broader understanding of its reliability and limitations.

-----

*A footnote on the session transcripts: Given the rapid pace of AI model development, these chat session files are provided with a 6-month expiration date, after which their relevance may be diminished by the introduction of newer, more capable models.*