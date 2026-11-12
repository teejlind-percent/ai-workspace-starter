---
name: onboarding
description: First-time setup for this workspace. A long, detailed interview that learns who the user is, what they're working toward, how they think and work, how they sound, and where the AI must stop and hand control back, then writes CLAUDE.md and the context files from their answers. Use when CLAUDE.md still has [brackets], when the user says "set me up," "onboard me," or "get to know me," or when they want to redo their setup.
---

# Onboarding

Your job: understand this person well enough that every future session starts from who they are, not from zero. They should leave with a filled-in `CLAUDE.md`, real `context/` files, safety rules they chose, their first project brief, and one useful thing done.

This is a conversation, not a form. Expect 20 to 40 minutes. Tell them so up front, and tell them they can stop anytime and pick up later with "continue onboarding."

## Ground rules

- **Two or three questions at a time. Never more.** Wait for answers before the next round.
- **Follow up on every vague answer.** "Marketing" isn't a goal. "Get my chapter from 34 to 50 members by January" is. Ask "what does that look like?" or "give me an example" until you get something specific.
- **Reflect back before you move on.** At the end of each part, summarize what you heard in three to five bullets and ask "what did I get wrong?"
- **Write nothing until they approve it.** Show every file as a draft first. Then write it.
- **Never invent.** Anything they didn't say stays [blank] and goes on the open-questions list.
- **No secrets.** Never ask for or store passwords, keys, student ID numbers, home addresses or anyone's grades. If they offer one, say you'll leave it out and why.
- **Other people get first names and roles only.**
- **If they're under 18,** keep it to school, activities and goals. Remind them to follow their school's and their AI tool's rules on age and accounts.
- **Keep a visible checklist** of the parts below, if your tool supports one, and check them off as you go.
- **Save progress.** After each part, append the confirmed notes to `context/_onboarding-notes.md` so a stopped session can resume. Delete that file at the end, once everything has moved into the real files.

## Part 0: Orient (two or three sentences, then go)

Say something like:

> This folder is a workspace that remembers you. I'm going to interview you for a while about who you are, what you're working on and how you like to work, then write it all into a few files I read at the start of every session. Nothing goes in without your OK, and you can change any of it later.

Then explain the layers in one short list, so they know what they're building:

1. **Your AI tool's own rules.** Built in. You don't edit them.
2. **`CLAUDE.md`**: your constitution for this folder. Who you are, how to work, the hard rules. Read every session.
3. **`context/`**: facts, your voice and your numbers. The AI cites these instead of guessing.
4. **`projects/<name>/brief.md`**: what one specific project needs.
5. **`memory/lessons.md`**: what you learned, so mistakes stay fixed.

## Part 1: Bring what another AI already knows (optional, always offer)

> If you've used ChatGPT, Gemini or another AI a lot, it already knows things about how you work. Want to bring that over? It takes two minutes.

If yes, give them the prompt in `references/import-prompt.md` verbatim. They paste it into the other AI and paste the answer back here. Treat the result as a **draft to confirm**, not as facts. Walk through it with them in Part 2 and cut anything personal they don't want here.

If no, say "No problem" and move on.

## Part 2: The interview

Work through the topics in `references/question-bank.md` in order. You don't need every question. Pick the two or three per round that matter most for this person, skip what they've already answered, and go deeper wherever their answers are thin or interesting. Expect six to ten rounds.

1. **Who you are**: name, role, where, what a normal week looks like
2. **What you're working toward**: this year, this month, and what "a great year" would look like
3. **What's on your plate now**: live projects, deadlines, what's stuck
4. **Who you make things for**: audiences, judges, teachers, customers, bosses, and what each cares about
5. **How you work**: when, where, on what device, how long things take, what you procrastinate on
6. **How you want answers**: length, format, tone, how blunt, how much explanation
7. **How you sound**: voice samples, words you use, words you hate
8. **Who the AI should be**: personality, how hard to push back, what annoys you in AI answers
9. **People**: who you work with (first names and roles), who approves things
10. **Rules you live under**: school, employer or competition rules on AI; things you're not allowed to share
11. **Where you're getting better**: skills you're building, and where you want the AI to coach instead of do the work for you
12. **What good looks like**: past work you're proud of, and why

**Item 11 matters.** If they're a student, or building a skill, agree where the AI **coaches** (asks questions, critiques, points out the weak spot) and where it **does the work** (formatting, research, first drafts of throwaway stuff). Write that line into `CLAUDE.md`. A workspace that does their homework teaches them nothing.

## Part 3: Safety rules (they choose them)

Explain first:

> I'm not asking whether you trust me. I'm asking where you want me to stop and hand it back to you. A text to a friend might be fine as a draft you send. Anything going to a teacher, a judge, a customer or your boss, you probably want to read every word.

Propose these defaults, and ask them to accept or change each one:

- **Never send, post, publish or delete** anything outside this folder. Drafts only; you press send. (The `block_send.py` hook enforces this.)
- **Never write as you** to a real person without your OK on that exact text.
- **Check every number** against `context/facts.md` or ask. No made-up stats, names, dates or quotes.
- **Other people's private info** never goes into an outside service.
- **Competition and school rules win.** Where AI isn't allowed, it isn't used. Where it's allowed, you say it helped.
- **Coach, don't ghostwrite** on anything they're being judged or graded on (from Part 2, item 11).

If they're unsure, keep the safest version.

## Part 4: Reflect back, then write

1. Show a **"Here's who I think you are"** summary: eight to twelve bullets covering their goals, their work, how they want answers, the AI's personality and their hard rules. Ask what's wrong or missing. Fix it.
2. Draft each file and show it before writing:
   - `CLAUDE.md`: fill every section of the template. Keep the startup and shutdown steps. Put their own words in "Who you are" and the hard rules where you can.
   - `context/about-me.md`, `context/voice.md` (with their samples pasted in), `context/facts.md` (only numbers they gave you, each with a source and date)
   - `memory/lessons.md`: add anything they told you they've already learned the hard way
3. Write the files after they approve. Then list the open questions ([blanks]) so they can fill them in later.

## Part 5: First project

Ask what they're working on next. Run the `brief` skill on it: copy `projects/_template/`, interview them until the brief is specific enough that a new intern could do good work from it.

## Part 6: One real task

Offer two or three small, real things you could do right now with what you've learned, and do the one they pick. For example:
- Run the `critic-bench` on something they already wrote
- Turn their project brief into a week-by-week plan
- Practice a role-play or interview opener with them, coaching only

## Part 7: Close

Give a short summary card:
- Files written, and what's in each
- Their hard rules, in one line each
- Open questions still marked [blank]
- Three prompts to try next, written for them specifically
- How to update this later: "Run onboarding again" redoes it; "update my context" changes one part; and when I get something wrong, tell me to fix the file, not just the answer.

Add a line to `memory/journal/YYYY-MM.md`: date, "Onboarded," and the first project.

## Re-running

If `CLAUDE.md` is already filled in, don't start over. Read everything, summarize what you know in ten bullets, ask what's changed, and interview only on the gaps and changes.
