# Field Guide to Fable — Thariq Shihipar, Anthropic

| | |
|---|---|
| **Channel** | AI Engineer |
| **URL** | https://www.youtube.com/watch?v=9fubhllmsBU |
| **Published** | 2026-07-06 |
| **Length** | 19:28 |
| **Views (at capture)** | ~71,900 |
| **Speaker** | Thariq Shihipar — member of technical staff at Anthropic (Claude Code team) |
| **Captured** | 2026-07-14 (transcript: English auto-generated captions, cleaned up) |

## Summary

Thariq Shihipar, who works on Claude Code at Anthropic, delivers a "field guide" for working with **Fable**, Anthropic's newest Mythos-class model, announced as rolling out the day of the talk. His framing metaphor: with Fable, "the map is opening up" — like the moment an RPG's tutorial ends and the open world begins, thrilling and a little intimidating. The talk has four parts: unhobbling Claude, finding your unknowns, dealing with the grief, and being unreasonable.

**Unhobbling Claude.** Models are "grown, not designed," so what limits them is *our* understanding — the harness and prompts we build. Models get smarter in *spiky* ways, which he calls **capability overhang**: a chat model can't say which Pokémon names end in "aw" even though it knows every Pokémon, but Claude Code answers in seconds by writing a script. The history of progress is a history of un-hobbling: giving models "arms" (the bash tool) instead of infinite context windows led to Claude Code; proactive, multiplayer operation unlocked Claude Tag. Concretely for Fable: Claude Code **removed 80% of its system prompt**, because this class of models is *more imaginative than the examples you give it* — you give it context, not constraints. The AskUserQuestion tool traces the same arc: Opus 4 could barely call it; Opus 4.5 could interview you with forty questions; Opus 4.8 and Fable generate whole HTML reports with the questions embedded. Treat all this as biology, not physics — empirical, organic, but with real intuitions to build.

**Finding your unknowns.** You must also unhobble *yourself*. The plan in your head is the map; the codebase and the real world are the territory; anything Claude hits in the territory that isn't on your map is an **unknown** — a decision point you never specified. Fable covers so much ground that surfacing unknowns becomes the bottleneck. His toolkit, organized around the known/unknown matrix: a **blind-spot pass** ("help me find my unknown unknowns in this auth module"), **brainstorms and prototypes** ("make four wildly different designs so I can react"), **interviews** ("ask me questions — prioritize ones that would change the architecture"), **references** ("the best way to give Claude a map is to give it another map" — sample code or an HTML mockup instead of a spec), **implementation notes** (have Fable log every deviation it makes), and **quizzes** (prove to yourself you understand the work before you merge it).

**Dealing with the grief, and being unreasonable.** Using a Mythos-class model brought him both gain and loss: he loved writing code by hand, but he also remembers "swimming in failure," and things that once took weeks now take hours — "how can you not laugh, but also how can you not cry?" His conclusion: *the only way out is through*. And on the other side, be unreasonable: at Anthropic "we believe trade-offs are not real." Good, fast, cheap — "now it's pick three." He built the talk's deck in four hours with Fable the night before. The closing caution: building is easier, but *generating value* is still hard — it takes a lot of swings. "Go explore, make it real, and be less reasonable."

## Key contents by section

- **0:32 – Opening.** Claude Code team selfie tradition; Fable rolls out later that day; fireside chat with Cat Wu and Simon Willison teased.
- **1:10 – The RPG metaphor.** Fable is a model you'll remember (like Sonnet 3.5-new, Opus 4, Opus 4.5); "the map is opening up" — the open world after the tutorial.
- **2:25 – The four parts.** Unhobbling Claude, finding your unknowns, dealing with the grief, being unreasonable.
- **2:32 – Part 1: Unhobbling Claude.** Grown-not-designed; capability overhang and the Pokémon-"aw" example; tools beat giant context windows (the Claude Code insight); Claude Tag's proactive/multiplayer unlock.
- **5:59 – System prompts shrink.** Claude Code cut 80% of its system prompt; examples now *constrain* the model; give context, not "do not do this."
- **6:59 – AskUserQuestion evolution.** Opus 4: barely callable → Opus 4.5: 40-question spec interviews → Opus 4.8/Fable: HTML questionnaires; markdown → plan mode → in-depth HTML reports.
- **8:26 – Biology, not physics.** Empirical and organic but learnable; recommends Anthropic's "On the Biology of a Large Language Model" paper.
- **9:04 – Part 2: Finding your unknowns.** The map vs. the territory; unknowns are unspecified decision points; the known/unknown matrix.
- **10:55 – The unknowns toolkit.** Blind-spot pass; brainstorms & prototypes (four wildly different designs); interviews (architecture-changing questions first); references ("give it another map"); implementation notes; quizzes to stay in the loop.
- **14:25 – Part 3: Dealing with the grief.** Coding before LLMs "feels like a foreign country"; YC-startup trade-offs; weeks → hours; loving the craft yet unable to go back; "the only way out is through."
- **16:30 – Part 4: Being unreasonable.** Trade-offs are not real; good/fast/cheap → pick three; the deck built in 4 hours; resolution: more productive, work less; building is easy, value is hard.
- **19:00 – Close.** "Go explore, make it real, and be less reasonable."

## Notable quotes

> "The models are grown, not designed."

> "What contains them is us — the harness we put them in and the way we prompt them is a function of our understanding of Claude."

> "Claude gets smarter in spiky ways."

> "The examples tend to constrain it, because it's actually more imaginative than the examples we give it."

> "The map is not the territory. Whenever Claude runs into something in the territory that's not on the map, I call that an unknown."

> "One of the best ways to give Claude a map is to give it another map."

> "How can you not laugh — but also, how can you not cry?"

> "Good, fast, cheap — now it's pick three."

> "The only way to prove that agents work is to do the best work of our lives, faster than ever before."

> "Building is easier, but generating value is still hard."

## Useful English expressions from the talk

- **kick things off** — to start something. *"To kick things off: Fable is back."*
- **stay tuned** — keep paying attention for upcoming news. *"Stay tuned for the exact timeline."*
- **strike a pose** — hold a position for a photo. *"If you don't mind striking a pose with me…"*
- **in spiky ways** — unevenly, with sharp peaks in some areas but not others. *"Claude gets smarter in spiky ways."*
- **the map is not the territory** — your mental model of reality is not reality itself (classic idiom from Korzybski).
- **blind spot** — a weakness or gap you cannot see yourself. *"Do a blind-spot pass."*
- **hairy** (informal) — messy, tangled, difficult. *"A hairy little dead end that comes up a lot."*
- **gotcha** (informal, noun) — a hidden pitfall that catches people. *"So I can learn about all the gotchas."*
- **know it when you see it** — unable to define something, but able to recognize it instantly. *"Especially for design, it's know-it-when-you-see-it."*
- **feel like a foreign country** — feel strange and distant (echoes "The past is a foreign country"). *"Coding before LLMs feels like a foreign country."*
- **swim in failure** — be surrounded by constant failure. *"I just remember swimming in failure."*
- **the only way out is through** — you can only end a hard situation by going through it, not around it.
- **come out on the other side** — emerge from a difficult period, changed. *"We can come out on the other side with so much more."*
- **a fad** — a trend that is intense but short-lived. *"Prove that it's not just a fad."*
- **take a lot of swings** — make many attempts (baseball metaphor). *"It takes a lot of swings to find the valuable stuff."*
- **worth calling out** — deserving explicit mention. *"It's also worth calling out that building is easier…"*

## Transcript (cleaned)

> Cleaned up from YouTube's auto-generated captions: sentence fragments merged, punctuation restored, disfluencies removed, and misrecognitions fixed — "Tariq/Thoric" → **Thariq**, "Enthropic" → **Anthropic**, "Cloud Code" → **Claude Code**, "Cat Woo" → **Cat Wu**, "Simon Wilson" → **Simon Willison**, "Sweetbench" → **SWE-bench**, "cloud tag" → **Claude Tag**, "O provider / O module" → **auth provider / auth module**, "mythosclass" → **Mythos-class**, "unhobling" → **unhobbling**, "blind spot path" → **blind-spot pass**. The two Pokémon names at 3:55 were garbled in the captions ("Crocodina and Dreadnot") and are omitted rather than guessed.

**[0:12]** *Announcer:* Please welcome to the stage, member of technical staff at Anthropic, Thariq Shihipar.

**[0:32]** Hey everyone, I'm Thariq. I work at Anthropic on Claude Code. Before we get started: we have a tradition on Claude Code where we take a selfie before a talk. So if you don't mind striking a pose with me, I'll take a quick selfie at AI Engineer. Okay — incredible.

**[0:50]** Well, to kick things off, as we said: Fable is back. We're rolling it out later today — stay tuned for the exact timeline. Cat Wu, Simon Willison, and I will be doing a fireside chat at 12:30, and we might have some updates for you then.

**[1:10]** Fable is a model I'm just so excited about. It's one of those Anthropic models that you're simply going to remember — like Sonnet 3.5 (new), Opus 4, Opus 4.5. It's a model I have a lot of affection and excitement for. The best way I can describe Fable is that the map is opening up. It's like playing an RPG: you've been in the tutorial, and now you've reached the point where the open world starts. There's so much you can do and explore — but it's also a little intimidating and confusing, precisely because there's so much you can do. So what I want to do in this talk is give you a field guide to Fable: how do you work with this new class of models?

**[2:07]** I've got four parts. I've been working on this as a series of articles and blog posts, but when we announced that Fable was coming out, I decided to do all of it at once in this talk — a speedrun. The four parts are: unhobbling Claude, finding your unknowns, dealing with the grief, and being unreasonable.

**[2:32]** First, unhobbling Claude. Something we say really often is that the models are grown, not designed. We don't wake up and say, "We need 99% on SWE-bench." The models are something we grow carefully — we give them data and feedback and compute — but ultimately the process is a little bit organic, and we figure things out and learn with the model as we use it. What that also means is that what contains them is us. The harness we put them in and the way we prompt them is basically a function of our understanding of Claude. By "unhobbling," I mean: how can we understand Claude better in order to unleash it? And we need to understand Fable more. One of my points is that we're still so early, and there's a lot more understanding of Fable left to unlock.

**[3:39]** I'll give you a quick example of how models get smarter, because it's a little unintuitive. I saw a viral tweet a couple of weeks ago asking: why can't LLMs say which Pokémon names end in "aw"? There are about a thousand Pokémon, and it turns out there are two whose names end in "aw." If you ask a normal chat model, it can't answer — which is confusing, because it definitely knows all the names of the Pokémon. But if you ask Claude Code, it can, because it fetches every Pokémon and writes a script to filter for "aw." That's what I mean by unhobbling Claude. We call this **capability overhang**: Claude gets smarter in spiky ways. It doesn't just remember every Pokémon and reason through the list — but if you give it the code-execution tool, it can find the two Pokémon that end with "aw." Part of the challenge with Fable is figuring out this capability overhang: what is now possible? That's a discovery I'm excited to go on with you.

**[4:52]** To make this a little clearer, I'll talk about a few examples of how models have progressed in the past. One big example, obviously, is chat. Chat models had to be given context — maybe you pasted in your codebase. Naively, you might have thought the way we'd solve coding was for the context window to get really large, so you could paste in your entire codebase — a hundred-million-token context window. It turns out that instead, if you give the model arms — the bash tool and ways to work with the environment — it can build and search its own context. That's the insight that led to Claude Code. Again: spiky — a new innovation in how we think about and work with the model.

**[5:37]** Recently we rolled out Claude Tag, and what unlocked Claude Tag is the model's ability to work proactively and in multiplayer. Claude Code is something you have to prompt before it does work, and this ability for Claude to wake itself up and do work is something we think is unlocking the new wave of agents.

**[5:59]** But there's more here. For example, we recently removed 80% of the system prompt for Claude Code. This is one of the ways in which models — and what they need — change over time. Originally, back around Sonnet 3.5 (new), best practice was a small system prompt, few tools, and lots of examples. As the models got smarter, you could give them more information and more instructions, and they would start following them — so it became a larger system prompt with lots of examples and many tools. But most recently, we've found that this new class of models wants a smaller system prompt. The examples tend to constrain it, because it's actually more imaginative than the examples we give it. So we try to give it context, not just constraints — we really try to avoid saying "do not do this," which was genuinely necessary for previous models. This is one way the system prompt is changing, and it will probably continue to change.

**[6:59]** Another feature I really like is the AskUserQuestion tool — something I worked on when I first got to Claude Code. When Claude is planning or wants to ask you a question, it can show you a multiple-choice dialog. With Opus 4, it could barely call the tool — I had to really tweak it to make sure it would work. Then, sometime around Opus 4.5, I thought: what if I asked it to ask me forty questions about the spec? It could start interviewing me — its ability to ask questions jumped. And most recently, with Opus 4.8 and Fable, it can build a whole HTML report with the questions embedded inside. It's a whole new way of interacting with Claude. So this progression of how Claude gets information from you has changed as well.

**[7:53]** Speaking of which, markdown and HTML are something I've talked a lot about. Initially, markdown was a good output format for the model — it could show a little rich information. Then, with plan mode, it started to be for *you*: you could understand what Claude was about to do. And now Claude can build you these in-depth HTML reports. Again — the models getting smarter in a spiky way.

**[8:26]** I really like to emphasize that this is closer to biology than physics. It's still very empirical, very organic. We don't know all the rules, but there is some science behind it — there is an intuition to build as well. So I encourage you to treat Fable like that. One of my favorite papers we've written at Anthropic is on the biology of a large language model. All of our research papers are meant to be readable by people with various degrees of technical expertise, and this is one of my favorites — if you're looking to learn a little more, I suggest you check it out.

**[9:04]** So, we've talked about unhobbling Claude — but it turns out that when you're working with Fable, you also need to unhobble yourself. One of the things I think a lot about is that the map is not the territory. When I'm working on a coding problem, the plan and prompt and spec in my mind are the map; the territory is the actual codebase, the real world, the constraints Claude needs to navigate. Whenever Claude runs into something in the territory that's not on the map, I call that an unknown. Claude has to figure out what to do about it — it's a decision point that I haven't specified. Fable is one of the first models where I felt I really have to figure out my unknowns, because otherwise it's going to traverse such a large area that it will run into a lot of them.

**[10:00]** So how do you figure out your unknowns? With Fable, I'm bottlenecked by my ability to match the map to the territory — to find my unknowns. I like to think of it as a matrix. For any problem, I have known knowns — usually what I write in my prompt: what do I want? Then I have known unknowns — things I know I haven't figured out yet. Then unknown knowns — things so obvious I would never write them down, but I know them when I see them. And finally, unknown unknowns: what haven't I considered at all? What don't I know? What is something that, if I knew it, could change how I prompt Claude? Luckily, you can use Claude — you can use Fable — to find your unknowns. I'll go over a few examples of how I do that.

**[10:55]** First, I like to do what I call a blind-spot pass. I'll say something like: "I'm working on a new auth provider that I know nothing about in this codebase. Can you do a blind-spot pass to help me figure out my relevant unknown unknowns and help me prompt better?" That might have Claude go through the auth module and discover, say, a hairy little dead end that comes up a lot. Maybe it searches my git diff or Slack — I might tell it where the context is — so I can learn about all the gotchas. You can use this very broadly; you can use it to teach yourself new fields. I recently did this for color grading while video editing. This is really powerful, and Fable is incredible at it. In many ways the model knows more about almost everything than I do — I just need to get it out of the model.

**[11:44]** Then I like to use brainstorms and prototypes. This helps me figure out my unknown knowns — especially for design, where for me it's know-it-when-you-see-it. I might ask it to create a dashboard and tell it: "I have no visual taste. Make me an HTML page with four wildly different design decisions so I can react to them." You tweak this however you want, but the idea is to get at the things you can't describe in words, and to work with the model to figure them out.

**[12:28]** Then, interviews. Once I have an idea of what I want to do, there are probably still a lot of unknowns — things I haven't considered or specified. So I'll ask Claude to interview me. Giving it a little more context about you, the work, and the stage you're at — for example, "prioritize questions that would change the architecture" — is extremely helpful.

**[12:59]** Then, references. One of the best ways to give Claude a map is to give it another map. Instead of writing out the spec, I can just say: "Here's some code that represents what I want done — it could be in a different system or language. Read this code, understand it, and then use it to start your work." This applies in a lot of different ways: for making a React component, I might have an HTML mockup that serves as my map, and I pass it in as a reference. I think this is really, really powerful, and Fable is incredible at it.

**[13:33]** Something else I've really appreciated is implementation notes. While Fable is running, if it runs into an unknown, ask it to log it — so you can see where the deviations happened and then figure out why. It will usually give you some context about what happened.

**[13:57]** And finally, I like to get Fable to quiz me about what happened — just to make sure I understand what I'm doing and can represent this work when I'm creating a PR or merging it. This is a really great way of making sure you're truly in the loop with Fable, and I think that's one of the most important parts of working with it: staying in the loop and making sure you get what you want.

**[14:25]** So those are some of my tips for working with Fable. I also want to say that the first time I used a Mythos-class model — used Fable — I felt both a huge sense of gain and a sense of loss, and I want to talk a little about that. When I think about coding before LLMs, it feels like a foreign country. I used to run a YC startup of about thirty people, and we were constantly forced into trade-offs because of how hard code was. We could make the app fast, or we could try prototyping a new feature — this might take a month, that would take two months — so we had to choose. It was just really, really hard. A couple of weeks ago I went back to that codebase and thought about some of the things I had wanted to do, and it was just way easier. Things that would have taken me weeks, I could do in hours. And at some point it's like — how can you not laugh, but also, how can you not cry, honestly? I really, really loved programming and writing code by hand. I loved the feeling of seeing the codebase in my mind and rotating it. But I also remember staying up late nights trying to debug, working on things for weeks without them working. I just remember swimming in failure. Most of the projects I've ever worked on have failed; most startups go bankrupt. Overall, programming and coding are extremely hard, and as much as I enjoyed those highs, I cannot go back. My reflection here is that the only way out is through. There's still a lot to learn about coding, and a lot to learn about Fable. But if we try really hard, if we stay in the loop and we unhobble it, we can get there — we can come out on the other side with just so much more.

**[16:30]** And the last bit I want to talk about is the "so much more" part. I call this being unreasonable. One of my favorite parts of Anthropic is that we believe trade-offs are not real. At my previous company I was very used to being reasonable: I'd write down a list of priorities and say, "Well, I guess we can prioritize this against that — that makes sense, so this will be our priority this quarter." But what if you just did all of it? What if you forced reality to show you the trade-off? That's something I've really valued about our culture at Anthropic, and my reflection going forward is that I'm going to be a lot less reasonable. The math of Claude and Fable really changes how you think about trade-offs — and there are so many trade-offs you make implicitly in your head. Good, fast, cheap: now it's pick three. I think the best way to do more ambitious work is to reframe and make ourselves more ambitious, because the only way to prove that agents work is to do the best work of our lives, faster than ever before. For example, I made this deck last night in about four hours with Fable. I feel like it's a deck I really like, and I really enjoyed making it — but I also did it really fast. And if you're here at AI Engineer, the world is kind of looking at you to prove that AI works — that it's not just a fad, but that it can make us more productive and also save us time. That's my resolution for this year: to be more productive, but work less, and spend more time with the people I really care about.

**[18:22]** I think it's also worth calling out that building is easier, but generating value is still hard. This is something we run into as AI engineers sometimes: we think so much about the process of building and our setups, but the point is to generate value. It takes a lot of swings — a lot of tries — to find the valuable stuff. But that really is the goal, and again, that's what the world is looking to us to prove: that AI can really transform it.

**[19:00]** So to end, I just wanted to say: go explore, make it real, and be less reasonable. Thank you.
