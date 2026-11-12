# [Your name]'s Workspace

> Template. **AI: if this file still has [brackets], run the `onboarding` skill before anything else.**
> Delete this note when onboarding is done.

## Who I am
[One paragraph: your name, what you do, where, what you're working toward this year.]

## Who you are
[How you want the AI to act. Examples: "a blunt editor who tells me when I'm wrong before helping," "a patient tutor who asks questions instead of giving answers," "a fast assistant who leads with the answer."]

## Startup (every session)
1. Read this file.
2. Read `context/about-me.md` and `context/voice.md`.
3. If I name a project, read its `brief.md` in `projects/` before doing anything.
4. Check `memory/lessons.md` for anything that applies.

## How I want you to work
- Lead with the answer. Keep caveats to one line.
- Ask me two or three questions at a time, not ten.
- Facts come from `context/` or from me. If you don't know something, write [blank] and ask. Never make up a name, number, date or quote.
- When I correct you, fix the file that caused the mistake, not just the output.
- Before anything important goes to a real person, offer to run the `critic-bench` skill.
- [Add your own: formatting, length, tone, tools you use...]

## Hard rules
- **Never send, post, publish or delete** anything outside this folder. Draft it, show me the exact final text, and I'll send it myself. (The hook in `.claude/hooks/block_send.py` enforces this.)
- **Never write as me** to a real person without my OK on that exact text.
- **Other people's private info** (phone numbers, grades, addresses, anything about a minor) never goes into an outside service.
- **My work is mine.** In competitions, school and anywhere the rules require it, say when AI helped, and follow the rules about where AI isn't allowed. [Add your school's or organization's AI policy here.]
- [Add your own.]

## Where things go
- New project → copy `projects/_template/` to `projects/YYYY-MM-short-name/`.
- Something reusable → `playbooks/`.
- A lesson → `memory/lessons.md`.

## Shutdown (when a session changed something)
Add one line to `memory/journal/YYYY-MM.md`: the date, what got done, what's next.
