# Understanding is the new bottleneck — Geoffrey Litt, Notion

| | |
|---|---|
| **Channel** | AI Engineer |
| **URL** | https://www.youtube.com/watch?v=WkBPX-oDMnA |
| **Published** | 2026-07-10 |
| **Length** | 19:33 |
| **Views (at capture)** | ~14,300 |
| **Speaker** | Geoffrey Litt — design engineer at Notion |
| **Context** | Talk at the AI Engineer conference, design-engineering track |
| **Captured** | 2026-07-14 (transcript: YouTube auto-generated English captions) |

## Summary

Geoffrey Litt opens with a deliberately contrarian claim for an AI conference: **it is still important for humans to understand how code works**, even as agents write 50,000-line PRs. His key move is to distinguish two reasons for understanding. Most people think we understand *to verify* — to catch agents doing dumb things. But verification is a thumbs-up/thumbs-down job that agents themselves are getting steadily better at, so the human role there is shrinking (and he's fine with that). The deeper, durable reason is **understanding to participate**: each review loop changes *you*, and the conceptual structures you build are what let you take the creative leaps that drive the *next* loop. Letting that atrophy is "**cognitive debt**" (a term he credits to researcher Margaret-Anne Storey, also blogged about by Simon Willison) — like tech debt, you get away with it until you suddenly realize you can no longer participate in your own project.

The practical heart of the talk borrows from **education and cognitive science**, offering three techniques for staying in the loop without slowing to 2023 speeds:

1. **Explanations (7:00–11:57)** — Instead of reading raw diffs, have the agent produce a *code explainer doc* (his shareable "explain-diff" skill). Principles: start with **background** on how the system works, give **intuition before details** (like a well-written commit message, deepened), embed **interactive figures** to fiddle with, and present the change as a **literate code diff** — prose walking you through files in the right order. Because "books don't work" (Andy Matuschak — it's easy to read and not realize you didn't understand), each doc ends with a **five-question quiz**; his rule is he doesn't send a PR for review unless he can pass the quiz on what his agents wrote. He calls the quiz a "**speed regulator**": it keeps you moving at the speed of understanding, not just the speed of correctness.

2. **Micro worlds (11:57–14:58)** — Inspired by Seymour Papert's "mathland" (kids learn French by living in France; where do you live to learn math?). Examples: a custom ephemeral **debugger UI** Claude built to visualize the internal state of his Prolog interpreter step-by-step, and a "**do the port yourself**" migration game where he clicked *next-next-next* through his website-framework migration, watching commands run and file trees change — the benefits of doing it manually without the pain. The point of these throwaway tools isn't shipping software; it's the peripheral vision and intuition you absorb by inhabiting them.

3. **Shared spaces (14:58–17:01)** — Understanding is also collective: teams need shared names and shared context to jam together. At Notion they're exploring **multiplayer chat threads** where multiple humans and agents talk in one place (like moving from DMs to Slack channels), and collaborative documents where an agent's plan can be commented on and discussed inline. Notion recently launched bringing coding agents (Claude, Cursor) into Notion itself.

He closes by widening the claim: it's important for humans to understand how *everything* works, and this is an old battle — Alan Kay's 1972 essay "A Personal Computer for Children of All Ages" envisioned kids modifying a game's code to learn physics. The point of computers was to level humans up, and AI's "code is free" moment makes that original vision newly reachable: **with the right tools we can understand more than ever, not less — putting ourselves more deeply in the loop, not out of it.**

## Key contents by section

- **0:22 – Hot take.** "It is still important for people to understand how code works." Room poll; mostly agreement.
- **1:15 – The problem.** Agents land huge PRs; keeping up by reading code line-by-line no longer scales, but new ways to understand are opening up.
- **2:28 – Why understand? (verify vs. participate.)** Correctness checking is increasingly the agent's job; understanding-to-participate is the human's job and can't be automated away.
- **4:19 – The loop compounds.** "When you review what's happening and get in the loop, you come away changed" — understanding feeds the next idea.
- **5:23 – Cognitive debt.** Vibe-coding feels fine until you realize you can't participate anymore.
- **6:24 – Plot twist.** "How do we understand stuff in general?" is the founding question of a whole field: education.
- **6:50 – Technique 1: Explanations.** Explainer docs: background → intuition → interactive figures → literate code diffs → spaced-repetition-style quiz. Skill published (HTML and Notion output variants).
- **11:57 – Technique 2: Micro worlds.** Papert's mathland; Prolog-interpreter timeline debugger with commenting; website-migration-as-video-game.
- **14:58 – Technique 3: Shared spaces.** Multiplayer human+agent chat threads; commentable agent plans; coding agents inside Notion.
- **17:01 – Closing.** Alan Kay's vision; "code is free" enables ephemeral UIs, simulations, playgrounds; understand better than ever before.

## Notable quotes

> "It's not just one loop. When you review what's happening and get in the loop, you come away changed."

> "How do we make sure we're not just moving at the speed of correctness, but also of understanding? The quiz is that speed regulator."

> "Agents can write code to help us understand code — where the point isn't building software to ship."

> "The point of computers was to level us up as humans."

> "With AI we can empower ourselves more — not just taking ourselves out of loops, but actually putting ourselves more deeply in loops than we ever have before."

## Useful English expressions from the talk

- **drop a hot take** — to state a deliberately provocative opinion. *"I'm here to drop a hot take for this room."*
- **preach to the choir** — to argue for something to people who already agree. *"I might be preaching to the choir here."*
- **keep someone in line** — to make sure someone behaves correctly. *"Your job as the human is to keep them in line."*
- **thumbs-up, thumbs-down decision** — a simple binary judgment.
- **come away changed** — to finish an experience as a different person. *"You come away changed."*
- **a few layers removed** — indirectly involved, at a distance from the real work.
- **get burned** — to suffer the consequences of a risk. *"You might get away with it for a little bit, but at some point you get burned."*
- **fool oneself** — to wrongly convince yourself of something. *"I had fooled myself."*
- **a crutch** — something you over-rely on instead of building real skill. *"Interactivity can just be a crutch."*
- **open the hood** — to look at the inner workings of a system. *"I can open the hood and see what's going on."*
- **peripheral vision** (figurative) — incidental awareness you pick up while doing the work yourself.
- **chime in** — to join a conversation with a comment. *"My teammate can chime in."*
- **call something into question** — to cause something to be doubted. *"This is being called into question now."*
- **harken back to** — to evoke or recall something from the past. *"This harkens back to the very origins of our field."*
- **prescient** — showing knowledge of events before they happen. *"An essay that I find very prescient."*

## Full transcript

> Auto-generated captions, kept verbatim. Known speech-recognition errors: "Jeffrey Lit" → **Geoffrey Litt**; "Asians" (1:13) → **agents**; "Margaret Story" → **Margaret-Anne Storey**; "Simon Willis" → **Simon Willison**; "Andy Matushak" → **Andy Matuschak**; "Seymour Papard" → **Seymour Papert**; "Alan K" / "Allan" → **Alan Kay**; "prologue" → **Prolog**; "guey" → **GUI**; "actuallyarkens" → "actually harkens"; "preient" → "prescient"; "motion"/"surians" (9:07) → "Notion … so agents"; "50,000line" → "50,000-line"; "div" (9:47) → "diff".

[0:01] [music]
[0:12] What's up? Yeah, thank you for coming to the design engineering track at AI. Is everyone having fun?
[0:18] Yeah, I think this is going to be a great track, so get excited.
[0:22] All right, let's get going. Um, my name is Jeffrey Lit. I'm a design engineer at Notion currently and I'm here to drop a
[0:30] hot take for this room. Maybe I think it is still important for people to understand how code works.
[0:39] [applause and cheering]
[0:42] Now, some of you might agree, some of you might disagree. Let's actually let's do let's try a poll. I'm curious for this room. Raise your hand if you agree with that opinion.
[0:50] Okay, maybe some selection bias. Any brave? Okay, raise your hand if you disagree with this opinion.
[0:55] Wow. Okay. We have [laughter] maybe we'll do a debate later. Yeah. I was hoping we'd be at the AI engineer conference so we'd have more B. Okay. I might be preaching to the choir here.
[1:06] You know, I think we the reality is though we are entering an era where this is a legitimate question that people are debating, right?
[1:13] Asians are writing tons of code for us.
[1:15] They're landing 50,000line PRs and it is getting harder to keep up. We all feel this now. I think the good news is there are
[1:24] lots of ways to understand the you know the days of just reading code line by line that's not the only way anymore and what the point of this
[1:33] talk is about is I want to share with you a bunch of the practices that I use to understand the code that my agents
[1:40] are writing for me includes things like explainer docs teaching me about how my code works my agents write quizzes for
[1:49] me to to test my understanding am I still really in the loop. Am I keeping up?
[1:55] I have agents build micro worlds that I can inhabit to get this intuitive sense of how my code works that's deeper and
[2:03] richer than just a written document. And I think all of these are really exciting new possibilities that are opening up for AI to help us understand better,
[2:12] not worse. And so that's what the point of this talk is going to be about. And I hope I can leave you with some techniques that you can take home and use yourself.
[2:21] By the way, my timer isn't running. If you could get that running, that'd be great. So, I know if I'm blabbering.
[2:28] Okay, but let's start. Let's back up for a sec. Before we talk about how, let's talk about why. Why bother understanding? This is again, it's a
[2:36] question now, right? And I think a lot of people get this subtly wrong.
[2:42] So, what a lot of people think of why do humans still have to understand? They think we understand to verify. The agents do dumb stuff. We've all seen it.
[2:50] And your job as the human is to keep them in line, right? Make sure they don't screw up.
[2:56] When people say things like code review is the new bottleneck, I think that's the first thing that pops into people's heads is correctness checking. There's
[3:06] this mental model that's like, hey, the agent's going to give you something, and what's your job? It's to ask, is this correct? Now, correctness can have lots
[3:14] of definitions. Does it match the spec doc you gave it? Does it take down production? Is it well architected?
[3:21] But fundamentally, those are all kind of thumbs up, thumbs down decisions, right?
[3:26] And the thing is over time, we've all seen it, the agents are also able to ask these questions and they're getting better at it. You give it the right
[3:34] verification loop and over time, this is the reality. The the role of humans in correctness checking is decreasing.
[3:43] And you know what? I actually don't hate that. If I have a clear idea of what I want to do and the agent does it correctly instead of coming back to me with an incorrect thing, that's great.
[3:52] I'm I'm into it.
[3:54] So then I think people extend this and say, you know what, that means as the agents get smarter and smarter and smarter, we we don't have to understand at all, right? Get out of the loop, man.
[4:03] Run the loop. And that's where I think people miss something really important.
[4:08] There is a deeper reason to understand what's going on, and that's understanding to participate.
[4:14] Because here's the thing, it's not just one loop.
[4:19] When you review what's happening and get in the loop, you come away changed. You understand something. And that understanding is what you take to the next loop and the next and the next.
[4:32] Your understanding of what's going on is the foundation for you having that next idea and being an active creative participant in a project.
[4:41] I think probably you've all you've all felt even before AI, you know, the difference of the kinds of ideas that someone can have when they really understand what's going on versus when
[4:49] there are a few layers removed are different because when you have rich conceptual structures in your head that you can fluently recombine really fast
[4:56] without going out to like ask some some agent or some human how it works, that gives you the ability to fluidly take
[5:04] creative leaps. And that's the human part of the work, coming up with the next idea and the next idea. So this is actually the real reason I think
[5:12] understanding matters and this is not something that we can just wash away with better agents because if we want to be active participants you still got to do this.
[5:23] There's a great term maybe some of you have heard called cognitive debt that I think really captures this spirit well.
[5:28] It's an analogy to technical debt popularized by the scholar Margaret Story. Simon Willis also blogged about it. And I love this idea because
[5:36] similarly to tech debt, you might get away with it for a little bit, but at some point you get burned if your understanding degrades. And maybe you felt this. I know I felt it. You're vibe
[5:44] coding, things are going well, and then at some point you realize, wait, I have no idea what's going on. I basically can't participate anymore, right? You've built up too much cognitive debt.
[5:56] Okay, so maybe sounds like all of you were already convinced. We agree. We need to understand.
[6:02] But how? Right, we don't want to live in 2023. We are using agents to move fast and it is harder and harder to keep up.
[6:11] How do we do it? I think to answer this question, we should actually take a step back and ask a more fundamental question, which is how do we understand stuff in general?
[6:24] Plot twist, this is not the first time that any human has asked this question. There is a field. It's called education.
[6:32] Now when you think education you might think of bad memories from sitting in lectures or whatever but I think we can do better. We can take inspiration from the best ideas that have ever been
[6:40] invented in education and use them to stay a loop and understand. So that's what this talk is about. We're going to talk about three techniques.
[6:50] First explanations.
[6:53] So when an agent writes some code for it to explain the work to you, right? And the most naive explanation is hey here's the code diff. That's the raw change,
[7:01] the material of what happened. But we can do, I think, much much better.
[7:06] What would the best possible explanation be? Like if you sent a team away for a year to come up with a personalized curriculum just to explain this one code
[7:14] change to you, what would that look like? I think this is a very generative question to ask.
[7:20] So, I've done a bunch of attempts at this. One is this skill I wrote called explain diff, which I use every day and a lot of my co-workers do as well. And I want to walk you through it.
[7:30] So, we're going to go through a little example here. I'm working on a video game where you draw Zen gardens, kind of de-stress, you know, could all use it these days.
[7:39] And we made a code change to change the perspective of the game from top down to isometric.
[7:45] And when I run my skill, it produces a code explainer doc. This can be an HTML file, it can be markdown. I like to put them in notion because I work there, but
[7:52] also because it's then collaborative, so my team can comment on it and talk about it. And here's how it looks.
[8:00] We start with background. We do not start with what happened in this change.
[8:04] It starts by teaching me, hey, here's how this system works.
[8:16] Obviously, you can skip this if you already know. You can personalize it to what you already know.
[8:22] Second important principle is intuition before details. So before we start, you know, looking at code and stuff, it says, hey, the goal of this commit is to
[8:31] make the garden feel threedimensional using only 2D drawing tricks.
[8:36] You can think of this sort of as like a well-written commit message a little deeper. Give me examples. Give me a feel for the essence before you know you throw a bunch of code at me. Right?
[8:45] This, by the way, this is good teaching. This is what like good math teachers do.
[8:51] Third, interactive figures. So where it makes sense, give me things to fiddle with and try. So with this change, it was like changing how we draw rocks. So
[9:00] I can drag around rocks in this little simulation and it shows me the coordinates that are happening, how the Z layers of the painting are changing.
[9:07] This, by the way, is actually using a new feature that motion literally launched this morning of HTML blocks in notion pages. surians can put interactive simulations into your notion pages. Pretty cool.
[9:18] I think you have to be careful with interactivity. It can just be a crutch and it can be kind of a slop to be honest, but used tastefully. It can provide an understanding that's hard to achieve with just static pictures.
[9:30] Okay, then we finally get to the code, right? Show me the code. But we don't just throw a list of files in order. We do what we what I call literate code
[9:38] diffs. Give me pros. Explain it to me in the right order. tell me before each file what's going on. And when you accumulate all this stuff, it's much
[9:47] much easier to follow than just a raw div.
[9:50] Oops. In fact, I print these out and take them to the coffee shop sometimes and just read them.
[9:55] I find it really beautifully ironic that AI is actually taking this process where I was used to be like glued to my computer, my IDE, and now I can go to the cafe and it's like I'm reading a
[10:04] textbook about this PR. It's really cool.
[10:08] Okay, so there is one problem which is that reading is hard and I am lazy.
[10:13] People are lazy. You know, there was this one time when I sent a PR to my co-orker that I thought I had read the thing. I thought I understood and she
[10:20] asked me the most basic question and I was like, "Oh no, I don't know. I clearly hadn't understood, right? I had
[10:27] fooled myself." So I thought, "How can I create a system where that never happens again?" For inspiration, I look to the work of the researcher Andy Matushak, who has
[10:36] this great line, books don't work. What he means by that is it's really easy to read a book and not realize you didn't understand it. So, so he and his
[10:44] collaborator Michael Nielsen tried this thing where in an essay there are interactive space repetition quizzes that test whether you actually remember what you just read. And this is cool to
[10:53] actually keep emailing you the quiz to make sure you remember it forever. But this is nice because you cannot get through this essay without understanding it or at least without remembering it.
[11:03] That's what I do with my code explainers. At the very bottom there's a quiz, five questions, medium difficulty.
[11:09] And my rule is I don't send code to uh others on my team to review unless I can pass the quiz about what my agents wrote.
[11:18] And it might sound kind of silly, but you should try it. It really is shocking the number of times this has caught me and made and made me realize I didn't understand.
[11:26] I think of it as sort of a speed regulator. Everything AI is speed up, speed up, speed up. There's all these incentives to go faster. How do we make sure we're not just moving at the speed of correctness, but also of
[11:35] understanding? And the quiz is that speed regulator. It's a system I can use for that.
[11:42] I did uh just put the skill on the internet. So yeah, photo moment. If you want the explained diff skill, uh take that QR code, try it out, make it your own. It's really simple actually.
[11:51] There's two versions of that QR code.
[11:53] One that outputs HTML, one that outputs notion.
[11:57] Okay, second technique, micro worlds. What does that mean? So, this takes inspiration from the educator Seymour
[12:04] Papard, real visionary who had this idea of living in mathland. And what that meant was, hey, kids learn French from living
[12:12] in France. Where do they go to learn math? Is there a math land where you can learn intuitively math just by being there? So he did these great things with
[12:21] this is a a robot called the turtle that kids program to draw stuff. But the point isn't making robots. The point is they actually learn math by doing that
[12:29] programming. The the point isn't the robot, it's the kids that are changed.
[12:34] So how could we apply this to understanding code?
[12:38] Here's one example. Last year I was trying to implement um for my own learning this interpreter for a programming language prologue which is think of it a little bit like a database
[12:46] query language and there's all these parts of it that look like this where when you read them on Wikipedia they seem really complicated and then when you actually get what's going on it's
[12:54] like wait a second that wasn't that hard to understand it just felt hard when I read it that way right how could we make it click more for my brain so I had
[13:02] Claude make me a micro world this is a debugger ephemeral UI that was built specific specifically to visualize the
[13:10] internal implementation of my programming language. What's happening here is that I'm scrubbing through a timeline that's running step by step.
[13:17] What's my interpreter doing? It's visualizing all the state at every step.
[13:20] So, I can kind of open the hood and see what's going on and start feeling it, you know. And yes, I can I use this to fix bugs. I even added a little um hard
[13:29] to see here, but there's a commenting feature where I can leave comments for myself on the timeline so I remember what I was thinking. And I used this to
[13:37] fix fix narrow bugs, but also as I was fixing the bugs, I was getting a feel for the machine. Right? That's something that if you just have an agent to go fix
[13:44] the bug, you don't get that peripheral vision. If you live in a micro world, you do.
[13:50] Another example, um, I was migrating my personal website from one framework to another. And first thing I did, I had I said, Claude, write me a script, too. It
[13:59] did this. It seemed like it worked. And I read the script and I was like, I don't know. like I just don't have a feel for what it's doing. A bunch of
[14:06] files went a bunch of places, it seems, right?
[14:10] So, what I did is I said, "Hey, Claude, make me essentially a video game where I do the port myself." And the way this works is old website on the left, new
[14:17] website. I just click a button, next, next, next. And at each step, it says, "Here's the commands I'm running. Your new website's coming to life step by step. You see it?
[14:26] There's actually file trees down there where you can see files moving." And it's the the result is it's kind of like if I did it manually, but I'm just
[14:34] clicking a button. So I'm getting some of the benefit of doing it without the pain.
[14:42] And I think the big takeaway here is agents can write code to help us understand code where the point isn't building software to ship. It's building
[14:49] these little micro worlds for us. It's the math land, right? It's it's a it's a simulation of just this thing.
[14:58] Okay, quickly the last topic shared spaces. So far we've this has all been about me
[15:05] solo understanding but a lot of the time I think the challenge is actually you're working on a team and your whole team needs to understand together so you can
[15:13] actually jam and have creative ideas together. We think a ton about this at notion.
[15:19] We believe that you know the shared understanding that exists between you and someone else is what lets you communicate effectively. Whether that's
[15:27] names for parts of a system, it could be names for UI elements or concepts, right? So we we think a lot of notion about how do you make tools that enable collective understanding?
[15:37] Some things we're exploring. Can you have multiplayer chat threads between multiple humans and agents together? So here, you know, I might ask a product
[15:46] manager on my team, hey, you know, what what are users asking for with this feature? And she might say, hey, I don't
[15:53] know, let's ask a different agent. and that agent comes in and talks to us.
[15:57] What's happening here is that instead of me and my PM both talking to our own agents, we're in a shared space. We can see each other's communication. It's
[16:05] kind of like, you know, going from one-on-one conversations to Slack channels. You know, you see more of the behavior happening together and you understand together.
[16:14] Also, having documents that you can talk about together is a really powerful permanent here. You know, Claude made us a plan.
[16:21] What if I have a question about that that I want to discuss with my team? I can just leave a comment because this is in a collaborative space, not on my computer locally. And then I can ask,
[16:30] hey, you know, what do you think about this? And my teammate can chime in and and we can talk about it right there.
[16:34] Right? I think having these spaces for shared discussion around ideas with our agents is really powerful for building up that collective understanding.
[16:44] This, by the way, um we just launched last week the ability to bring coding agents into notion. So Claude and Cursor can now live in Notion and our team actually builds a lot of our code in notion itself.
[16:54] mainly because of these benefits because having in a shared space is just so valuable.
[17:01] Okay, so we've talked about these three techniques and I want to bring it back to the beginning.
[17:06] You know, I think at the beginning I said it's important for humans to still understand how the code works, right?
[17:12] But I actually think it's much bigger than that.
[17:15] I kind of think it's just important for humans to still understand how everything works.
[17:22] And maybe you know you all agree it sounds like but this I think is being called into question now and is something we actually have to actively fight for.
[17:29] The thing is this is not a new battle.
[17:32] It actuallyarkens back to the very origins of our field.
[17:36] Alan K is one of the pioneers of personal computing co-inventor of the modern guey. And literally 50 years ago he wrote this essay that I find very
[17:44] preient called a personal computer for children of all ages.
[17:48] It looks like two kids on iPads watching YouTube or something right. It's kind of crazy. This is 50 years ago, his vision. But that's not YouTube on the iPads.
[17:55] What he envisioned is, hey, these kids, they're playing a video game and they're modifying the code as they play it to learn physics. So the point isn't the
[18:04] computer, it's the kids. The point of computers was to level us up as humans, right? And Allan has talked a lot about how it kind of feels like at some point
[18:12] computers detourred a bit from that vision. But I think the exciting thing is maybe now's the time to bring that back. Here's kind of the meme version of that.
[18:23] I think with AI, a lot of people are waking up to, oh my gosh, code is free.
[18:28] We can make ephemeral UIs, dynamic simulations to understand concepts. We can make debuggers, playgrounds, and it's like, yes, that's great. And
[18:37] it's actually not a new idea. Like, this was the goal all along. And so, I think the optimistic thing that I find really exciting is,
[18:45] hey, it's still really important to understand how things work. And with the right tools and the right mindset and the right creativity, we can actually
[18:52] understand better than ever before, not less. With AI, we can kind of empower ourselves more, not just taking ourselves out of loops, but actually
[19:01] putting ourselves more deeply in loops than we ever have before. And I think that's a really exciting prospect and I hope it's something that we all together as an industry figure out.
[19:12] That's all I have for you today. Thank you so much.
[19:15] [applause]
[19:29] [music]
