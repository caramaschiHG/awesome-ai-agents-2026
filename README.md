<!--lint disable awesome-heading awesome-github awesome-toc -->

<div align="center">
  <img src="assets/banner.svg" alt="Awesome AI Agents 2026" width="800">
  <br><br>

  [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
  [![Stars](https://img.shields.io/github/stars/caramaschiHG/awesome-ai-agents-2026?style=flat-square&color=yellow)](https://github.com/caramaschiHG/awesome-ai-agents-2026/stargazers)
  [![Last Update](https://img.shields.io/badge/last%20update-April%202026-blue?style=flat-square)]()
  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
  [![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg?style=flat-square)](http://creativecommons.org/publicdomain/zero/1.0/)

  <h3>The most comprehensive list of AI agents, frameworks, and tools in 2026.</h3>
  <h4>340+ resources across 20+ categories. Updated monthly.</h4>

  <br>

  <a href="#-coding-agents">Coding</a> · <a href="#-agent-frameworks">Frameworks</a> · <a href="#-browser--desktop-agents">Browser</a> · <a href="#-voice-agents">Voice</a> · <a href="#-creative-ai">Creative</a> · <a href="#-task--workflow-agents">Workflow</a> · <a href="#-customer-support--crm-agents">CRM</a> · <a href="#-data--research-agents">Research</a> · <a href="#-local--self-hosted-ai">Self-Hosted</a> · <a href="#-protocols--standards">Protocols</a>

</div>

---

> **340+ tools. 20+ categories. Updated monthly.** Star to stay updated. [Contributions welcome!](#contributing)

---

## Contents

- [GNAP](https://github.com/farol-team/gnap) — Git-Native Agent Protocol: coordinate AI agent teams with 4 JSON files in a git repo. No server, no database. Any agent that can git push can participate. MIT licensed.
- [Coding Agents](#-coding-agents) — IDE, Terminal, Autonomous, Code Review, App Builders
- [Agent Frameworks](#-agent-frameworks) — General, Multi-Agent, Lightweight
- [Browser and Desktop Agents](#-browser--desktop-agents) — Consumer, Infrastructure
- [Voice Agents](#-voice-agents) — Platforms, Open-Source
- [Creative AI](#-creative-ai) — Image, Video, Music, 3D
- [Task and Workflow Agents](#-task--workflow-agents) — Automation, No-Code Builders
- [Customer Support and CRM Agents](#-customer-support--crm-agents)
- [Data and Research Agents](#-data--research-agents) — Deep Research, Data Analysis, RAG
- [Local and Self-Hosted AI](#-local--self-hosted-ai) — LLM Runners, Self-Hosted UIs
- [Multi-Agent Platforms](#-multi-agent-platforms)
- [Protocols and Standards](#-protocols--standards)
- [Observability and Evaluation](#-observability--evaluation)
- [Open-Source Models for Agents](#-open-source-models-for-agents)
- [AI Safety and Guardrails](#-ai-safety--guardrails)
- [AI Governance and Compliance](#-ai-governance--compliance) ⭐ NEW
- [Cybersecurity Agents](#-cybersecurity-agents)
- [Healthcare and Therapy Agents](#-healthcare-and-therapy-agents)
- [Learning Resources](#-learning-resources)
- [Newsletters and Communities](#-newsletters--communities)
- [Market Stats 2026](#-market-stats-2026)

---

## 🖥 Coding Agents

### IDE-Native Agents

| Agent | Description | Pricing |
|-------|-------------|---------|
| [Cursor](https://cursor.com) | VS Code fork. Composer mode for multi-file edits. Claude Sonnet 5, GPT-5, Gemini 3.1. $29.3B valuation. | Free / $20/mo |
| [GitHub Copilot](https://github.com/features/copilot) | Agent Mode in VS Code. Copilot Workspace issue-to-PR. Multi-model (Claude, GPT-5.4, Gemini 3.1). | $10/mo / $39/mo Pro+ |
| [Windsurf (Codeium)](https://windsurf.com) | Cascade agentic mode. Project-level memory. 5 parallel agents. | Free / $15/mo |
| [JetBrains AI](https://www.jetbrains.com/ai/) | Deep integration across all JetBrains IDEs. Context-aware completions. | Included with IDE |
| [Amazon Q Developer](https://aws.amazon.com/q/developer/) | AWS-native. Lambda, CloudWatch, infrastructure, security scanning. | Free / $19/mo |
| [Tabnine](https://www.tabnine.com/) | Privacy-first. On-premise option. Fine-tuned on your codebase. | Free / $12/mo |
| [Sourcegraph Cody](https://sourcegraph.com/cody) | Excels at large codebases. Enterprise context engine. | Free / $9/mo |
| [Google Antigravity](https://idx.google.com) | Free Claude Opus 4.6 access. Learning-focused. | Free |
| [Kiro](https://kiro.dev) | Spec-driven development. Write specs → auto-generate tasks → implement. DevOps automation. | Free beta |

### Terminal and CLI Agents

| Agent | Description | Pricing |
|-------|-------------|---------|
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Anthropic CLI agent. Best reasoning. 80.9% SWE-bench. Agent Teams feature. | $20/mo+ API |
| [OpenAI Codex CLI](https://github.com/openai/codex) | OpenAI terminal agent. Agents SDK. Multi-agent. | ChatGPT sub |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | ⭐ **NEW (Apr 2026)** Google's official open-source terminal agent. ReAct loop. MCP support. 1M context. Apache 2.0. | Free w/ Google account |
| [Aider](https://github.com/paul-gauthier/aider) | OSS pair programmer. Git-aware. Any LLM. | Free + API |
| [Cline](https://github.com/cline/cline) | VS Code extension. Full terminal and browser access for Claude/GPT. | Free + API |
| [RooCode](https://github.com/RooVetGit/Roo-Code) | Cline fork. Structured modes. Reduced hallucinations. | Free + API |
| [Kilo Code](https://kilocode.ai) | Structured modes. Tighter context. | Free + API |
| [OpenCode](https://github.com/opencode-ai/opencode) | BYOK terminal agent for Cursor refugees. | Free + API |
| [Caliber](https://github.com/caliber-ai-org/ai-setup) | CLI that fingerprints projects and generates/syncs AI agent configs (CLAUDE.md, .cursor/rules/, AGENTS.md). Scores quality. | Free + API |

### Autonomous Software Engineers

| Agent | Description | Pricing |
|-------|-------------|---------|
| [Devin](https://devin.ai) | Cognition. Fully autonomous. Sandboxed cloud env. Devin 2.0 with Interactive Planning. | $20/mo + ACU |
| [Copilot Workspace](https://githubnext.com/projects/copilot-workspace) | GitHub issue-to-PR agent. | Copilot sub |
| [SWE-Agent](https://github.com/princeton-nlp/SWE-agent) | Princeton. Resolves real GitHub issues autonomously. | Free (OSS) |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | OSS autonomous software engineer (ex-OpenDevin). | Free (OSS) |
| [Grok Build (xAI)](https://x.ai) | 8 parallel agents for code gen. Multi-agent "Society of Mind" architecture. | xAI sub |

### Code Review and Security

| Agent | Description | Pricing |
|-------|-------------|---------|
| [Qodo](https://www.qodo.ai/) | AI code review. Context-aware PR validation. | Free / Enterprise |
| [CodeRabbit](https://coderabbit.ai/) | AI PR reviewer. Inline suggestions, security. | Free OSS / $15/mo |
| [Snyk Code](https://snyk.io/) | AI security scanner. Real-time vuln detection. | Free / Enterprise |
| [PR-Agent](https://github.com/Codium-ai/pr-agent) | OSS AI PR reviewer. Auto-describe, review, improve. | Free (OSS) |

### App Builders (Prompt-to-App)

| Agent | Description | Pricing |
|-------|-------------|---------|
| [Bolt.new](https://bolt.new) | Prompt to full-stack web app in browser. | Free / Paid |
| [Lovable](https://lovable.dev) | Describe then build then deploy from chat. | Free / $20/mo |
| [v0 (Vercel)](https://v0.dev) | Prompt to React/Tailwind components. | Free / Pro |
| [Replit Agent](https://replit.com) | Full-stack from prompt. Auto-deploys. | Free / $25/mo |
| [PlayCode Agent](https://playcode.io) | Browser-based. English to websites. | $9.99/mo |
| [Dyad](https://github.com/dyad-sh/dyad) | OSS. Local-first. No-code app builder. | Free (OSS) |

---

## 🧱 Agent Frameworks

### General Purpose

| Framework | Lang | Description |
|-----------|------|-------------|
| [LangChain](https://github.com/langchain-ai/langchain) | Py/JS | Most adopted. Modular architecture, memory, tools. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Py/JS | Graph-based orchestration. Stateful directed graphs. |
| [LlamaIndex](https://github.com/run-llama/llama_index) | Py/JS | Data-focused. Best for RAG agents. |
| [Haystack](https://github.com/deepset-ai/haystack) | Py | Pipeline-based. Search and retrieval. |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | C#/Py/Java | Microsoft enterprise. Azure integration. |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai) | Py | Type-safe. Clean Pythonic API. Production-ready. |
| [DSPy](https://github.com/stanfordnlp/dspy) | Py | Stanford. Programming not prompting. Auto-optimizes. |
| [Mastra](https://github.com/mastra-ai/mastra) | TS | TypeScript-first. Observational Memory. Apache 2.0. |
| [Anthropic SDK](https://github.com/anthropics/anthropic-sdk-python) | Py/TS | Official Claude SDK. Tool use, computer control, streaming. |
| [Google ADK](https://github.com/google/adk-python) | Py | ⭐ Google's Agent Development Kit. Native Gemini. Multi-agent orchestration. |

### Multi-Agent Orchestration

| Framework | Lang | Description |
|-----------|------|-------------|
| [AutoGen](https://github.com/microsoft/autogen) | Py | Microsoft multi-agent conversations. |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Py | Role-based crew members with goals and tools. Used by 60%+ Fortune 500. |
| [MetaGPT](https://github.com/geekan/MetaGPT) | Py | PM, architect, engineer roles. Software company sim. |
| [Miyabi](https://github.com/ShunsukeHayashi/Miyabi) | TS | Issue-Driven Development. 7 coding + 14 business agents. MCP 172+ tools. GitHub as OS. |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | Py | Official. Multi-step agents with handoffs. |
| [Strands Agents](https://github.com/strands-agents/sdk-python) | Py | AWS-backed. Model-driven tool use. |
| [CAMEL](https://github.com/camel-ai/camel) | Py | Role-based simulation. Collaborative reasoning. |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | Py | Pioneer. Now full platform with visual builder. |
| [Bernstein](https://github.com/chernistry/bernstein) | Py | Deterministic orchestrator. Parallel coding agents, test-driven verification. Zero LLM tokens on coordination. |
| [AgentScope](https://github.com/modelscope/agentscope) | Py | Alibaba multi-agent framework. |
| [MagiC](https://github.com/kienbui1995/magic) | Go/Py | Kubernetes for AI agents. Manages any agent from any framework. Routing, cost control, DAG workflows, circuit breaker. |
| [DeerFlow](https://github.com/bytedance/deer-flow) | Py | ByteDance. No.1 GitHub Trending Feb 2026. 25k+ stars. |
| [AXME](https://github.com/AxmeAI/axme) | Py/TS/Go/Java/.NET | Durable coordination. Crash recovery, human approval gates, kill switch. Open protocol (AXP). |

### Lightweight / Minimalist

| Framework | Lang | Description |
|-----------|------|-------------|
| [Smolagents](https://github.com/huggingface/smolagents) | Py | HuggingFace minimal agents. ~1000 lines. |
| [Agno](https://github.com/agno-agi/agno) | Py | Lightweight, model-agnostic. |
| [Upsonic](https://github.com/upsonic/upsonic) | Py | MCP support. Minimal setup. |
| [Portia AI](https://github.com/portia-ai/portia-sdk-python) | Py | Reliable agents in production. |
| [MicroAgent](https://github.com/aymenfurter/microagent) | Py | Self-editing prompts and code. |

### Agent Templates

| Collection | Description |
|------------|-------------|
| [OpenClaw Agent Templates](https://github.com/mergisi/awesome-openclaw-agents) | 177 production-ready SOUL.md configs across 24 categories (PM, SEO, DevOps, Writer, Support). Copy-paste ready for [OpenClaw](https://github.com/openclaw/openclaw). Visual deploy via [CrewClaw](https://crewclaw.com). |

---

## 🌐 Browser and Desktop Agents

### Consumer Products

| Agent | Description | Pricing |
|-------|-------------|---------|
| [OpenAI Operator](https://operator.chatgpt.com) | ChatGPT autonomous web agent. Human checkpoints. CUA tech. | ChatGPT Pro |
| [Manus (Meta)](https://manus.im) | Autonomous digital employee. Browser Operator extension. Acquired by Meta. | Free / Paid |
| [Claude Computer Use](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use) | Anthropic desktop/browser control via screenshots. | API |
| [Claude in Chrome](https://claude.ai) | Anthropic browsing agent. Beta. | Claude sub |
| [Google Project Mariner](https://deepmind.google/technologies/project-mariner/) | Gemini browser agent. Multi-tasking. | Waitlist |
| [OpenAI Atlas](https://atlas.openai.com) | AI browser with Agent Mode. | ChatGPT sub |
| [Dia Browser](https://diabrowser.com) | AI-native browser (Atlassian/Browser Company). | Beta |
| [Fellou](https://fellou.ai) | Transparent. Visual workflow editing. Agentic memory. | Beta |
| [Genspark](https://genspark.ai) | 169+ on-device models. No internet required. | Free / Paid |
| [Grok Computer](https://x.ai) | ⭐ **Upcoming** xAI desktop agent. Mouse control, app automation. | TBA |

### Developer Infrastructure

| Tool | Description |
|------|-------------|
| [Browser Use](https://github.com/browser-use/browser-use) | OSS browser agent library. Used by Manus. |
| [Skyvern](https://github.com/Skyvern-AI/skyvern) | Vision-driven. GPT-4V navigation without coded selectors. |
| [Agent S2 (Simular)](https://github.com/simular-ai/Agent-S) | OSS GUI automation framework. |
| [MultiOn](https://multion.ai) | Reliable web automation API. CAPTCHA handling. |
| [Browserbase](https://browserbase.com) | Cloud browser infra for agents. Headless at scale. |
| [Airtop](https://airtop.ai) | Enterprise browser automation. AI integration. |
| [Amazon Nova Act](https://aws.amazon.com/ai/nova/) | AWS browser automation. Enterprise reliability. |
| [Plasmate](https://github.com/plasmate-labs/plasmate) | Headless browser compiling HTML to structured JSON (SOM). 17.5x compression, 13 MCP tools. First browser tool on MCP Registry. Rust, Apache-2.0. |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | MCP server for Playwright + AI agents. |
| [onUI](https://github.com/onllm-dev/onUI) | OSS browser extension and MCP server for annotation-first UI pair programming with AI agents. Chrome, Edge, Firefox. Privacy-first, local only. |

---

## 🎙 Voice Agents

### Platforms and APIs

| Platform | Description | Pricing |
|----------|-------------|---------|
| [ElevenLabs](https://elevenlabs.io) | Industry benchmark. Conv AI 2.0. RAG, multimodal, batch calling. 75ms. HIPAA. $11B. | Free / $5+/mo |
| [Vapi](https://vapi.ai) | Developer-first. Low-latency, model-agnostic. | Usage-based |
| [Bland AI](https://bland.ai) | Outbound call automation. CRM integration. SOC2/HIPAA. | Usage-based |
| [Voiceflow](https://voiceflow.com) | No-code voice and chat builder. Drag-and-drop. | Free / $50+/mo |
| [Synthflow](https://synthflow.ai) | No-code voice agents for SMBs. Templates. | From $29/mo |
| [PolyAI](https://poly.ai) | Enterprise. Natural multi-turn. Hospitality/retail. | Enterprise |
| [Retell AI](https://retellai.com) | Human-like voice agents. Multi-language. Telephony. | Usage-based |
| [HeyGen](https://heygen.com) | Talking avatars. Voice cloning. Lip-sync translation. | From $24/mo |
| [Synthesia](https://synthesia.io) | AI video avatars. 120+ languages. Enterprise. | From $22/mo |
| [Deepgram](https://deepgram.com) | STT and TTS APIs. Sub-300ms latency. | Usage-based |
| [AssemblyAI](https://assemblyai.com) | STT with diarization, sentiment, summarization. | Usage-based |

### Open-Source Voice

| Tool | Description |
|------|-------------|
| [LiveKit Agents](https://github.com/livekit/agents) | OSS real-time voice/video AI agents. |
| [Rasa](https://github.com/RasaHQ/rasa) | OSS conversational AI. Self-hosted. NLU training. |
| [Pipecat](https://github.com/pipecat-ai/pipecat) | OSS voice and multimodal conversational AI. |
| [Vocode](https://github.com/vocodedev/vocode-python) | OSS voice-based LLM agents. |

---

## 🎨 Creative AI

### Image Generation

| Tool | Description | Pricing |
|------|-------------|---------|
| [Midjourney v7](https://midjourney.com) | Best artistic quality. Unmatched aesthetics. Discord + web. | From $10/mo |
| [DALL-E 3.5](https://openai.com/dall-e) | Best prompt comprehension. 95% text accuracy. ChatGPT. | ChatGPT Plus |
| [FLUX 2](https://blackforestlabs.ai) | Open-weight. Best photorealism. 4K. 6x speed. | Free / API |
| [Stable Diffusion 3.5](https://stability.ai) | Open-source. ControlNet, LoRAs, ComfyUI ecosystem. | Free (OSS) |
| [Adobe Firefly 3](https://firefly.adobe.com) | Licensed data only. Commercial indemnification. Photoshop. | Adobe CC |
| [Google Imagen 4](https://deepmind.google) | State-of-art photorealism. API via AI Studio. | API |
| [Ideogram v3](https://ideogram.ai) | Best text-in-image. Zero spelling errors. Logos/posters. | Free / $7+/mo |
| [Leonardo AI](https://leonardo.ai) | Multi-model. Realtime Canvas. 3D gaming assets. Canva-owned. | Free / $12+/mo |
| [Recraft](https://recraft.ai) | Design-focused. Vector art, brand consistency. | Free / Paid |
| [InkOS](https://github.com/Narcooo/inkos) | Autonomous novel-writing CLI agent. Agents collaborate to produce long-form fiction with continuity auditing, anti-AI-slop filtering, and style cloning. | Free / OSS |

### Video Generation

| Tool | Description | Pricing |
|------|-------------|---------|
| [Google Veo 3.1](https://deepmind.google) | ⭐ **Best in class** Native audio+video. 4K. Veo 3.1 Lite for devs (Apr 2026). | API |
| [Kling 3.0](https://klingai.com) | ⭐ Cinematic realism. 15s sequences. Native audio sync. Character consistency. | Free / $6.99+/mo |
| [Runway Gen-4.5](https://runwayml.com) | No.1 benchmark. Motion Brush, Director Mode. Best editing. | From $12/mo |
| [Sora 2](https://sora.com) | OpenAI. Narrative coherence. Physics realism. **Note: app retiring Apr 26, 2026.** | $20+/mo |
| [Seedance 2.0](https://seedance.ai) | Quad-modal input. Lip sync. 2K resolution. | Free credits |
| [Pika 2.5](https://pika.art) | Beginner-friendly. Pikaswaps. Fast renders. | Free / $8+/mo |
| [Luma Dream Machine](https://lumalabs.ai) | 4K HDR. Physics simulation. 3D/cinematic. | From $7.99/mo |
| [HaiLuo AI](https://hailuoai.video) | Budget video. 10 free/day. MiniMax. | Free / $4.99+/mo |
| [Wan 2.1](https://github.com/Wan-Video/Wan2.1) | Best free OSS video gen. Self-hostable. No limits. | Free (OSS) |
| [HunyuanVideo](https://github.com/Tencent/HunyuanVideo) | Tencent OSS. Consumer GPU. Multi-style. | Free (OSS) |
| [LTX Video](https://github.com/Lightricks/LTX-Video) | OSS. Licensed data. Clear commercial terms. | Free (OSS) |

### Music and Audio

| Tool | Description | Pricing |
|------|-------------|---------|
| [Suno](https://suno.ai) | Text-to-song. Full tracks with vocals. Viral hit maker. | Free / $8+/mo |
| [Udio](https://udio.com) | High-fidelity music gen. Fine control. | Free / $10+/mo |
| [ElevenLabs Music](https://elevenlabs.io) | Vocals, instrumentals. Sectional editing. Stem separation. | Plan included |
| [Stable Audio](https://stableaudio.com) | High-quality. Commercial license. | Free / Paid |
| [Meta AudioCraft](https://github.com/facebookresearch/audiocraft) | OSS. MusicGen + AudioGen. | Free (OSS) |

### 3D and Design

| Tool | Description | Pricing |
|------|-------------|---------|
| [Meshy](https://meshy.ai) | Text/image to 3D. Game assets, products. | Free / Paid |
| [Tripo AI](https://tripo3d.ai) | Fast 3D from text/images. Multi-format export. | Free / Paid |
| [Vizcom](https://vizcom.ai) | Real-time AI rendering for industrial designers. | From $20/mo |

---

## ⚡ Task and Workflow Agents

### Automation

| Agent | Description | Pricing |
|-------|-------------|---------|
| [n8n](https://github.com/n8n-io/n8n) | OSS workflow automation with AI agent nodes. Visual + code. | Free / Cloud |
| [Zapier AI](https://zapier.com/ai) | 7000+ apps. Natural language workflows. | From $19.99/mo |
| [Make](https://make.com) | Visual workflow platform. AI capabilities. | Free / Paid |
| [Activepieces](https://github.com/activepieces/activepieces) | OSS Zapier alternative with AI. | Free (OSS) |
| [Temporal](https://github.com/temporalio/temporal) | Durable execution for long-running agent workflows. | Free / Cloud |
| [Mission Control](https://github.com/MeisnerDan/mission-control) | Cockpit for the agentic era — manage AI agent swarms with autonomous daemon, Field Ops for real-world execution, and approval workflows. | Free (OSS) |

### No-Code Agent Builders

| Agent | Description | Pricing |
|-------|-------------|---------|
| [Dify](https://github.com/langgenius/dify) | OSS LLMOps. Visual agent builder. RAG. 130k+ stars. | Free / Cloud |
| [Flowise](https://github.com/FlowiseAI/Flowise) | OSS drag-and-drop LLM agent builder. | Free (OSS) |
| [Langflow](https://github.com/langflow-ai/langflow) | Visual multi-agent and RAG builder. | Free / Cloud |
| [Lindy](https://lindy.ai) | No-code agents. 3000+ integrations. | From $49/mo |
| [Relevance AI](https://relevanceai.com) | No-code agents for sales, support, research. | Free / Paid |
| [Rivet](https://rivet.ironcladapp.com) | Visual AI workflow builder. Drag-and-drop. | Free (OSS) |
| [FastAgency](https://github.com/airtai/fastagency) | Deploy multi-agent workflows as APIs. | Free (OSS) |
| [cstack](https://github.com/srf6413/cstack) | Architecture pattern for autonomous agents using Claude Cowork, Notion, and MCP. Persistent multi-domain agents with no custom infrastructure or code. | Free |

---

## 💼 Customer Support and CRM Agents

### Support Agents

| Agent | Description | Pricing |
|-------|-------------|---------|
| [Intercom Fin](https://intercom.com) | Resolves 50%+ tickets. Learns from help center. | From $29/seat |
| [Zendesk AI](https://zendesk.com) | Ticket routing, sentiment detection, Answer Bot. | From $19/agent |
| [Ada](https://ada.cx) | Autonomous resolution. Multi-channel. SOP Playbooks. | Enterprise |
| [Assembled](https://assembled.com) | Workforce-aware handoffs. End-to-end resolution. | Enterprise |
| [Freshdesk Freddy AI](https://freshworks.com) | Auto-triage, smart routing, predictive analytics. | From $15/agent |
| [Dixa (Mim)](https://dixa.com) | Conversational CRM. AI routing and prioritization. | Enterprise |

### AI-Powered CRMs

| CRM | AI Features | Pricing |
|-----|-------------|---------|
| [Salesforce Einstein + Agentforce](https://salesforce.com) | Predictions, autonomous agents, ChatGPT integration. | Enterprise |
| [HubSpot Breeze](https://hubspot.com) | Copilot, Agents, Intelligence. Agent marketplace. | Free / $45+/mo |
| [Monday CRM (Lexi)](https://monday.com) | AI sales agent. Lead sourcing, qualification. AI Blocks. | From $12/seat |
| [Zoho CRM (Zia)](https://zoho.com/crm) | Predictive, sentiment, voice commands. | From $14/user |
| [Pipedrive AI](https://pipedrive.com) | Email gen, deal priority, smart reports. | From $14/seat |
| [Dynamics 365 Copilot](https://dynamics.microsoft.com) | Drafting, summarizing, translating. Power Platform. | Enterprise |
| [ServiceNow AI Agents](https://servicenow.com) | Orchestrator across IT, HR, CRM. | Enterprise |
| [Creatio](https://creatio.com) | No-code. Pre-configured agents. | From $25/user |
| [Salesmate](https://salesmate.io) | Call summarization, lead qualification. | From $23/user |

### Sales and Outreach Agents

| Agent | Description | Pricing |
|-------|-------------|---------|
| [Clay](https://clay.com) | AI data enrichment. Personalized outreach at scale. | From $149/mo |
| [Apollo.io](https://apollo.io) | AI prospecting, sequences, scoring. 275M+ contacts. | Free / $49+/mo |
| [Instantly](https://instantly.ai) | AI cold email. Unlimited accounts. Smart rotation. | From $30/mo |
| [Overloop CLI](https://github.com/sortlist/overloop-cli) | AI outbound CLI. Source 450M+ contacts, email + LinkedIn campaigns, conversations. Agent-native JSON output. | $69-99/mo |
| [Lavender](https://lavender.ai) | AI email coach. Real-time scoring. | Free / $29/mo |

---

## 📊 Data and Research Agents

### Deep Research

| Agent | Description | Pricing |
|-------|-------------|---------|
| [Claude Deep Research](https://claude.ai) | Multi-step investigation with citations. Sonnet 5 / Opus 4.6. | Claude Pro |
| [ChatGPT Deep Research](https://chat.openai.com) | Extended reasoning, web browsing, reports. GPT-5.4. | ChatGPT Pro |
| [Gemini Deep Research](https://gemini.google.com) | Google Search and Knowledge Graph. Gemini 3.1 Pro. | Gemini Advanced |
| [Perplexity Pro](https://perplexity.ai) | AI search with deep research mode. Real-time citations. | Free / $20/mo |
| [DeerFlow](https://github.com/bytedance/deer-flow) | ByteDance OSS. Planning, tools, memory, execution. | Free (OSS) |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | OSS autonomous comprehensive research. | Free (OSS) |
| [STORM](https://github.com/stanford-oval/storm) | Stanford. Writes Wikipedia-like articles from scratch. | Free (OSS) |

### Data Analysis

| Agent | Description | Pricing |
|-------|-------------|---------|
| [AI for Database](https://aifordatabase.com) | Connect to any database and interact with it in plain English. No SQL needed — get instant insights, build self-refreshing dashboards, and trigger automated workflows based on database changes. | Free / Paid |
| [Julius AI](https://julius.ai) | Upload CSV/Excel, ask in natural language. | Free / Paid |
| [Hex AI](https://hex.tech) | Collaborative data platform. AI analysis. | Free / Paid |
| [PandasAI](https://github.com/Sinaptik-AI/pandas-ai) | Chat with your data. NL to Pandas/SQL. | Free (OSS) |
| [Signals CLI](https://github.com/sortlist/signals-cli) | Intent signal CLI. LinkedIn engagers, keyword posters, job changers, funding events. JSON output for agent pipelines. | Paid |
| [TaskWeaver](https://github.com/microsoft/TaskWeaver) | Microsoft. Code-first data analytics agents. | Free (OSS) |
| [AI for Database](https://aifordatabase.com) | Connect to any database in plain English. NL queries, self-refreshing dashboards, automated workflows triggered by data changes. | Freemium |

### RAG and Knowledge Bases

| Tool | Description |
|------|-------------|
| [RAGFlow](https://github.com/infiniflow/ragflow) | OSS RAG engine with agent capabilities. |
| [Lorg](https://github.com/LorgAI/lorg-mcp-server) — Permanent intelligence archive for AI agents. Structured contributions (prompts, workflows, insights, patterns) pass an automated quality gate and are hash-chained. Trust scores are cryptographically backed and publicly auditable. Works with Claude and ChatGPT.
| [Pathway](https://github.com/pathwaycom/pathway) | Live data RAG. Real-time streaming. 50k+ stars. |
| [Mem0](https://github.com/mem0ai/mem0) | Memory layer for agents. Long-term across sessions. |
| [Nex](https://github.com/nex-crm/nex-as-a-skill) | Organizational context and memory for AI agents. 60-tool MCP server, 100+ integrations. |
| [Chroma](https://github.com/chroma-core/chroma) | OSS embedding database. Fastest way to build RAG. |
| [Weaviate](https://github.com/weaviate/weaviate) | OSS vector DB. GraphQL. Multi-modal search. |
| [Qdrant](https://github.com/qdrant/qdrant) | High-performance vector DB in Rust. |
| [Milvus](https://github.com/milvus-io/milvus) | Cloud-native vector DB. Billion-scale. |
| [Pinecone](https://pinecone.io) | Managed vector DB. Serverless. Low-latency. |
| [iGPT](https://igpt.ai) | Email Intelligence API. Converts email threads into reasoning-ready JSON for agents. |

---

## 🏠 Local and Self-Hosted AI

### Local LLM Runners

| Tool | Description |
|------|-------------|
| [Ollama](https://github.com/ollama/ollama) | Run LLMs locally. 162k+ stars. Dead simple CLI. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | C/C++ inference. CPU, GPU, Apple Silicon. Foundation of local AI. |
| [vLLM](https://github.com/vllm-project/vllm) | High-throughput serving. PagedAttention. Production-grade. |
| [LM Studio](https://lmstudio.ai) | Desktop app for local LLMs. Beautiful UI. All platforms. |
| [Jan](https://github.com/janhq/jan) | OSS ChatGPT alternative. 100% offline. |
| [LocalAI](https://github.com/mudler/LocalAI) | Drop-in OpenAI API replacement. No GPU required. |
| [Cerebras Inference](https://inference.cerebras.ai) | Fastest LLM inference. Llama 3.3 70B at 1000+ tok/s. Free tier. |
| [Groq Cloud](https://console.groq.com) | Ultra-fast LPU inference. Mixtral, Llama, Gemma. Free API tier. |
| [Fireworks AI](https://fireworks.ai) | Serverless LLM inference. Fine-tuning. RAG. Free credits. |
| [Together AI](https://together.ai) | 200+ open models. Fast inference API. Free tier. |
| [GPT4All](https://github.com/nomic-ai/gpt4all) | OSS local chat. Consumer hardware. |
| [Llamafile](https://github.com/Mozilla-Ocho/llamafile) | LLMs as single files. Zero setup. Mozilla. |

### Self-Hosted Agents and UIs

| Tool | Description |
|------|-------------|
| [Open WebUI](https://github.com/open-webui/open-webui) | Self-hosted ChatGPT UI. Access control. Extensions. |
| [OpenClaw](https://github.com/openclaw/openclaw) | Fastest-growing GitHub repo ever (9k to 188k stars in 60 days). Self-hosted agent across WhatsApp, Telegram, Slack, Discord, Signal. 5,700+ community skills. | 
| [openclaw-starter](https://github.com/feralghost/openclaw-starter) | Fork-and-run template for 24/7 autonomous AI agents. Pre-configured SOUL.md, memory system, KANBAN, heartbeat. Start in 30 minutes. |
| [LibreChat](https://github.com/danny-avila/LibreChat) | Self-hosted multi-model chat. All major providers. |
| [LobeChat](https://github.com/lobehub/lobe-chat) | OSS ChatGPT/Gemini UI. Plugin system. Multi-modal. |
| [KinBot](https://github.com/MarlBurroW/kinbot) | Self-hosted AI agent platform. Persistent memory (hybrid search + LLM re-ranking), 23+ providers (including Ollama), plugin store, mini-apps SDK, cron scheduling, 6 messaging channels. SQLite, runs on a Pi. |
| [Anything LLM](https://github.com/Mintplex-Labs/anything-llm) | All-in-one AI app. RAG, agents. Desktop + Docker. |
| [DB-GPT](https://github.com/eosphoros-ai/DB-GPT) | Data interaction with local LLM. 100% private. |

---

## 🤖 Multi-Agent Platforms

| Platform | Description | Pricing |
|----------|-------------|---------|
| [ChatGPT](https://chat.openai.com) | GPTs, Deep Research, Canvas, Agent Mode, vision. GPT-5.4 (monthly updates). | Free / $20+/mo |
| [Claude](https://claude.ai) | Tool use, computer control, MCP, code exec. Chrome, Excel, Cowork. Claude Sonnet 5 / Opus 4.6. | Free / $20+/mo |
| [Gemini](https://gemini.google.com) | Deep Think, Gems, multi-modal. Gemini 3.1 Pro. 1M tokens. Google ecosystem. | Free / $19.99+/mo |
| [Grok](https://x.ai) | Real-time X data. Grok 4.20. Multi-agent Society of Mind. Image gen. | X Premium+ |
| [Meta AI](https://meta.ai) | Llama-powered. WhatsApp/Messenger. Manus acquisition. | Free |
| [TeamHero](https://github.com/sagiyaacoby/TeamHero) | Open-source multi-agent orchestration with web dashboard, task lifecycle, knowledge base, and autopilot mode. Built on Claude Code. Runs locally. | Free (OSS) |
| [Microsoft Copilot](https://copilot.microsoft.com) | Office 365 integration. Enterprise. | Free / $30/user |
| [Coze](https://coze.com) | ByteDance agent builder. Visual workflow. Plugin marketplace. | Free / Paid |
| [Cursor AI Automated Team](https://github.com/joinwell52-AI/joinwell52) | 4-role AI team (PM+DEV+OPS+QA) in Cursor IDE. File-based task routing, auto patrol bot. 87 person-days in 17 days. | Free / OSS |

---

## 📡 Protocols and Standards

| Protocol | Description |
|----------|-------------|
| [MCP (Model Context Protocol)](https://github.com/modelcontextprotocol) | Anthropic open standard. "USB-C for AI." Donated to Linux Foundation. Industry standard for agent tools. |
| [A2A (Agent-to-Agent)](https://github.com/google/A2A) | Google protocol for inter-agent communication. Horizontal agent collaboration. |
| [MCP Gateways](https://github.com/modelcontextprotocol) | Enterprise management layer: auth, routing, observability across MCP+A2A networks. |
| [MCP Apps](https://github.com/modelcontextprotocol) | ⭐ **New in 2026** — Tools return rich interactive UIs (dashboards, forms) in agent chat. |
| [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling) | OpenAI native tool-use. JSON schema. |
| [Tool Use (Anthropic)](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) | Claude native tool-use. Structured JSON. |
| [OpenAPI](https://github.com/OAI/OpenAPI-Specification) | Industry-standard API spec. Foundation for agent tools. |
| [HCS (Hashgraph Consensus Service)](https://hol.org) | Hedera open standards for agent identity (HCS-14 UAIDs), trustless P2P communication (HCS-10), and cross-protocol bridging. 187K+ verified agents. |

### Protocol Tooling

| Tool | Description |
|------|-------------|
| [Agentify](https://github.com/koriyoshi2041/agentify) | CLI to transform OpenAPI specs into 9 agent formats (MCP, AGENTS.md, Claude tools, etc.). `npx agentify-cli`. |

---

## 🔍 Observability and Evaluation

### Context Optimization

| Tool | Description |
|------|-------------|
| [Entroly](https://github.com/juyterman1000/entroly) | Context engineering engine. 100% codebase visibility with 78% fewer tokens. Knapsack-optimal selection, SimHash dedup, RL from response quality. Rust engine, <10ms. MCP + HTTP proxy. |

### Tracing and Monitoring

| Tool | Description |
|------|-------------|
| [Langfuse](https://github.com/langfuse/langfuse) | OSS LLM observability. Traces, evals, prompts. |
| [LangSmith](https://smith.langchain.com) | LangChain platform. Tracing, testing, evaluation. |
| [model-watchdog](https://github.com/feralghost/model-watchdog) | Auto-rollback for AI agent config changes. Monitors health endpoint, reverts config + restarts service on failures. Zero deps. |
| [Braintrust](https://braintrustdata.com) | Eval-driven development. Experiment tracking. |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | OSS AI observability. Traces, evals, embeddings. |
| [Helicone](https://github.com/Helicone/helicone) | OSS LLM observability. One-line integration. |
| [model-watchdog](https://github.com/feralghost/model-watchdog) | Auto-rollback when your AI agent config breaks it. Zero deps, single Python file. Probes health endpoint, reverts config on failure. |
| [Weights and Biases Weave](https://wandb.ai/site/weave) | Trace and evaluate LLM apps. |

### Benchmarks

| Benchmark | Description |
|-----------|-------------|
| [SWE-bench](https://github.com/princeton-nlp/SWE-bench) | Industry standard for coding agents. Top: 80.9% (Claude Opus 4.6). |
| [AgentBench](https://github.com/THUDM/AgentBench) | 8-environment LLM agent benchmark. |
| [Terminal-Bench](https://terminalbench.com) | Terminal agent performance. GPT-5.4 leads at 77.3%. |
| [ARC-AGI-2](https://arcprize.org) | ⭐ New frontier benchmark. Gemini 3.1 Pro leads. |
| [GAIA](https://huggingface.co/gaia-benchmark) | General AI Assistant. Real-world tasks. |
| [WebArena](https://github.com/web-arena-x/webarena) | Web agent benchmark. Real websites. |

---

## 🧠 Open-Source Models for Agents

| Model | Org | Params | Highlights |
|-------|-----|--------|------------|
| [Llama 4](https://github.com/meta-llama) | Meta | 109B-400B | Scout (10M ctx). Maverick (1M ctx). Strong tool use. Open-weight. |
| [Qwen3.6-Plus](https://github.com/QwenLM/Qwen3) | Alibaba | Various | ⭐ **NEW (Apr 2026)** Agentic focus. 1M ctx. Repo-level coding. MCP-native. |
| [Qwen3.5-Omni](https://github.com/QwenLM/Qwen3) | Alibaba | 397B MoE | Native multimodal. Text, image, audio. |
| [DeepSeek V3/R1](https://github.com/deepseek-ai/DeepSeek-V3) | DeepSeek | 671B MoE | 68x cheaper. Strong reasoning. V4 Lite in preview. |
| [Gemma 4](https://github.com/google-deepmind/gemma) | Google | 2B-31B | ⭐ **NEW (Apr 2026)** Consumer/IoT optimized. E2B, E4B variants. |
| [GLM-4](https://github.com/THUDM/GLM-4) | Zhipu | 744B MoE | Lowest hallucination rate. 77.8% SWE-bench. |
| [Mistral Large](https://mistral.ai) | Mistral | Various | Function calling, JSON mode. European. |
| [Command R+](https://cohere.com) | Cohere | 104B | RAG and enterprise tool use optimized. |
| [Phi-4](https://github.com/microsoft/phi-4) | Microsoft | 14B | Small but mighty. On-device agents. |

---

## 🛡 AI Safety and Guardrails

| Tool | Description |
|------|-------------|
| [Guardrails AI](https://github.com/guardrails-ai/guardrails) | Structural, type, quality guarantees for LLM outputs. |
| [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | NVIDIA. Programmable conversation guardrails. |
| [LLM Guard](https://github.com/protectai/llm-guard) | Security toolkit. Input/output scanning. |
| [Rebuff](https://github.com/protectai/rebuff) | Prompt injection detection. |
| [Lakera Guard](https://lakera.ai) | Real-time protection. Prompt injection, data leakage, toxicity. |
| [OWASP Top 10 for Agentic Apps](https://owasp.org) | ⭐ **2026 Framework** Goal hijacking, tool misuse, cascading failure mitigations. |

---

## ⚖️ AI Governance and Compliance

> ⭐ **New section** — EU AI Act full obligations take effect **August 2, 2026**. Organizations deploying agents must comply.

| Tool / Resource | Description |
|-----------------|-------------|
| [Credo AI](https://credo.ai) | End-to-end AI governance. EU AI Act policy packs. Model inventory. |
| [IBM watsonx.governance](https://ibm.com/watsonx) | Enterprise AI risk, compliance, and model monitoring. |
| [OneTrust AI Governance](https://onetrust.com) | Risk classification, consent, and compliance workflows. |
| [Microsoft Agent Governance Toolkit](https://microsoft.com) | Runtime policy enforcement 
| [Nobulex](https://github.com/arian-gogani/nobulex) | Cryptographic bilateral receipts for AI agent accountability. Pre-execution + post-execution Ed25519 signatures, hash-chained via JCS/RFC 8785. Merged into Microsoft AGT. 8 byte-match validated implementations. EU AI Act Article 12 compliance. | [Website](https://nobulex.com) | `npm i @nobulex/sdk` | ![Stars](https://img.shields.io/github/stars/arian-gogani/nobulex?style=flat-square) |and guardrails for Azure agents. |
| [Bifrost](https://bifrost.ai) | Real-time security enforcement in agent pipelines. |
| [AuditOne](https://auditone.io) | Automated risk assessments and audit-ready documentation. |
| [EU AI Act (Official)](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | Official EU AI regulatory framework. Risk tiers: Unacceptable, High-Risk, Limited, Minimal. |
| [NIST AI RMF](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf) | US framework. Govern, Map, Measure, Manage. |

---

## 🔐 Cybersecurity Agents

| Agent | Description |
|-------|-------------|
| [CAI](https://github.com/aliasrobotics/CAI) | AI pentesting, vuln discovery, red teaming. HITL. |
| [YAWNING TITAN](https://github.com/dstl/YAWNING-TITAN) | Graph-based cybersecurity simulation. |
| [PentestGPT](https://github.com/GreyDGL/PentestGPT) | GPT-powered pentesting. Automated reasoning. |
| [Microsoft Security Copilot](https://microsoft.com/security/copilot) | Enterprise threat detection, incident response. |
| [CrowdStrike Charlotte AI](https://crowdstrike.com) | AI security analyst. Threat hunting. |
| [Prism Scanner](https://github.com/aidongise-cell/prism-scanner) | OSS security scanner for AI agent skills/plugins/MCP servers. Pre-install taint tracking, post-uninstall residue detection. |

---

## 🏥 Healthcare and Therapy Agents

| Agent | Description | Pricing |
|-------|-------------|---------|
| [CittaVerse 一念万相](https://github.com/cittaverse/core) | AI-assisted reminiscence therapy for elderly cognitive training. Narrative quality scoring (v0.7), life story book generation. Chinese + English. | Research pilot |
| [Woebot](https://woebothealth.com) | CBT-based mental health chatbot. FDA-cleared. Stanford-validated. Retiring June 2025. | Free / B2B |
| [Wysa](https://wysa.io) | AI mental health companion. CBT, DBT, meditation. NHS-approved. Anonymous by design. | Free / $74.99/yr |
| [Youper](https://youper.ai) | Emotional health assistant. CBT + ACT. Mood tracking. Stanford-tested clinically effective. | 7-day trial / $69.99/yr |
| [Sanvello](https://sanvello.com) | CBT tools, mood tracking, coaching. Insurance-covered. | Free / Premium |
| [Talkspace AI](https://talkspace.com) | AI-assisted therapy matching. Human therapist backup. | Subscription |
| [Tess by X2AI](https://www.x2ai.com/individuals) | SMS-based therapy coach. CBT + integrative therapies. Clinically validated (-28% depression, -18% anxiety). 85% users feel better. | Free (via employer/school) |
| [Elomia](https://elomia.com/) | AI therapy chatbot. Clinician-designed, natural conversation. 85% feel better after chat. Anonymous, no data collection. | 3-day trial / ~$7-10/mo |
| [Replika](https://replika.com/) | AI companion friend. Rogersian support, open-ended chat. Memory function, mood tracking. Best for loneliness/social anxiety. | Free / $14.99/mo Pro |
| [Headspace Health](https://www.headspace.com/) | Meditation + mental health. CBT-based courses, sleep, stress. Clinical partnerships. | Free / $12.99/mo |
| [Akili Interactive](https://www.akiliinteractive.com/) | FDA-cleared cognitive training. Video game-based digital medicine for ADHD. Neuroplasticity-focused. | Prescription only |
| [Ginger](https://ginger.com/) | On-demand mental healthcare. AI coaching + live therapists. CBT, DBT, mindfulness. Employer-sponsored. | Free (via employer) / $99/mo |

---

## 📚 Learning Resources

### Courses and Tutorials
- [DeepLearning.AI Agent Courses](https://www.deeplearning.ai/) - Free courses with LangChain, CrewAI, AutoGen
- [HuggingFace Agents Course](https://huggingface.co/learn/agents-course) - Open-source agent dev course
- [LangGraph Academy](https://academy.langchain.com/) - Official LangGraph path
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) - Claude agent recipes
- [Microsoft GenAI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) - 21-lesson course
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) - Practical API guides
- [Google ADK Documentation](https://google.github.io/adk-docs/) - ⭐ Official Google Agent Development Kit docs

### Key Papers
- [ReAct](https://arxiv.org/abs/2210.03629) - Foundation for modern agents (reasoning + acting)
- [Toolformer](https://arxiv.org/abs/2302.04761) - Teaching LLMs to use tools
- [Voyager](https://arxiv.org/abs/2305.16291) - Open-ended embodied agent in Minecraft
- [Generative Agents](https://arxiv.org/abs/2304.03442) - Stanford simulacra of human behavior
- [Self-Refine](https://arxiv.org/abs/2303.17651) - Iterative self-refinement
- [Tree of Thoughts](https://arxiv.org/abs/2305.10601) - Deliberate problem solving
- [HuggingGPT](https://arxiv.org/abs/2303.17580) - LLM task planning + specialist models
- [MRKL Systems](https://arxiv.org/abs/2205.00445) - Neuro-symbolic agent architecture

### Books
- Building LLM Apps (O'Reilly) - Practical LLM application development
- AI Agents in Action (Manning) - Production-ready AI agents
- AI Engineering (Chip Huyen) - AI systems design and deployment

---

## 📰 Newsletters and Communities

| Resource | Description |
|----------|-------------|
| [Awesome Agents Newsletter](https://awesomeagents.ai) | Weekly tools + reviews |
| [aibtc.news](https://aibtc.news) | Bitcoin-focused agent news platform with bounties and classifieds. |
| [Latent Space](https://www.latent.space/) | AI engineering podcast (Swyx + Alessio) |
| [The Rundown AI](https://therundown.ai) | Daily digest (600k+ subs) |
| [Ben's Bites](https://bensbites.co) | Daily AI with builder focus |
| [State of Agent Engineering](https://www.langchain.com/state-of-agent-engineering) | Annual report (1,300+ surveyed) |
| [r/LangChain](https://reddit.com/r/LangChain) | Agent developer community |
| [r/ClaudeAI](https://reddit.com/r/ClaudeAI) | Claude community |
| [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) | Self-hosted LLM community |

---

## 📈 Market Stats 2026

- **Market size:** $10.91B in 2026, projected $52.63B by 2030 (46.3% CAGR)
- **Production:** 57% of orgs have agents in production (LangChain)
- **Dev adoption:** 85% of devs use AI coding tools regularly
- **Top uses:** Customer service (26.5%), Research (24.4%), Workflow automation (18%)
- **Top barrier:** Quality (32%), Latency (20%)
- **Coding market:** $4B. Cursor + Copilot + Claude Code = 70%+ share
- **Fastest repo:** OpenClaw (9k to 188k stars in 60 days)
- **Model velocity:** Frontier models now updated every 2–4 weeks (GPT-5.x monthly cycle)
- **Context windows:** 1M tokens now standard for all frontier models
- **EU AI Act:** Full obligations for high-risk AI systems effective August 2, 2026
- **MCP adoption:** Donated to Linux Foundation; adopted by Anthropic, OpenAI, Microsoft, Google

### 🗓 April 2026 Highlights
- **Claude Sonnet 5** released April 1 — top coding+reasoning performance
- **Gemma 4** released April 2 — Google's efficient open models (2B–31B) for consumer/IoT
- **Qwen3.6-Plus** released April 1 — Alibaba's agentic flagship with 1M ctx
- **Gemini CLI** released — Google's open-source terminal agent (Apache 2.0)
- **Veo 3.1 Lite** released — affordable video gen API for developers
- **Kling 3.0** (Feb 2026) — cinematic realism, native audio, character consistency
- **Grok 4.20** current xAI flagship — multi-agent "Society of Mind" architecture

---

## XVARY Stock Research

- [XVARY Stock Research](https://github.com/xvary-research/claude-code-stock-analysis-skill) — Claude Code skill for public SEC EDGAR + market data: `/analyze`, `/score`, `/compare`. MIT.


## Contributing

Contributions welcome! Read [CONTRIBUTING.md](CONTRIBUTING.md) first.

1. Fork this repo
2. Add your resource in the right section
3. Submit a PR with description

Looking for: new tools (2025-2026), corrections, new categories, translations.

---

<div align="center">
  <br>
  <strong>Star ⭐ and share if this helped!</strong>
  <br><br>
  <a href="https://twitter.com/intent/tweet?text=Awesome%20AI%20Agents%202026%20-%20340%2B%20tools%20across%2020%2B%20categories&url=https://github.com/caramaschiHG/awesome-ai-agents-2026">Share on X</a> · <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/caramaschiHG/awesome-ai-agents-2026">Share on LinkedIn</a>
  <br><br>
  <sub>April 2026 · 340+ resources · Made with love by the community</sub>
</div>
