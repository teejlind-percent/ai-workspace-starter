# AI Workspace Starter

A folder you give your AI so it works the way you work.

Most people open a chat, type a request and get an average answer back. Then they start over tomorrow, and the AI has forgotten everything. This repo fixes that with a few plain text files. They tell the AI who you are, what's true, how you like things done, and what it may never do without you. When it gets something wrong, you write it down once and it stays fixed.

I run my marketing department at a $300M fintech this way, with a team of AI agents and one human: me. My real system is much bigger than this, but it rests on the same five ideas.

## The five ideas

1. **Facts live in files, not in your head or the chat.** `context/` holds what's true about you and your work. The AI cites it instead of guessing.
2. **The brief beats the model.** Every project starts with a `brief.md`: who it's for, what you know, what good looks like, your brand, your rules. That's Rule 3: don't upgrade the robot, upgrade the brief.
3. **Robots review robots, and then a human decides.** The `critic-bench` skill has a panel of tough readers tear your draft apart before anyone real sees it. They score it and quote your weakest line. They don't rewrite it. Fixing it is your job.
4. **Nothing goes out without you.** A hook in `.claude/hooks/` stops the AI from sending, posting, publishing or deleting. It drafts. You press send.
5. **Every project ends in a debrief.** What broke, what you'd change, what to do differently next time. Lessons go to `memory/lessons.md`, so next year's you starts smarter.

## Set it up (about 10 minutes)

You need [Claude Code](https://claude.com/claude-code) (desktop app or terminal) or another AI coding tool that reads instruction files from a folder. Check your school's or employer's rules on AI tools and accounts first.

1. Download this repo: the green **Code** button, then **Download ZIP**, or `git clone` it.
2. Open the folder in Claude Code.
3. Type: **"Set me up."** (or `/onboarding`)

   That starts a long interview, usually 20 to 40 minutes, two or three questions at a time. It asks who you are, what you're working toward, how you work, how you sound, what kind of AI teammate you want, and where it must stop and hand things back to you. If you've used ChatGPT or another AI a lot, it gives you a prompt to bring that history over. Then it reads its understanding of you back, shows you every file before writing it, sets up your first project and does one real task with you.

   You can stop anytime and say "continue onboarding" later.

4. When it's done, read `CLAUDE.md` yourself and fix anything that sounds wrong. It's your constitution, so it should sound like you.

**No onboarding skill support in your tool?** Paste this instead:

> Read every file in this folder, especially `.claude/skills/onboarding/`. Follow that onboarding process with me: interview me two or three questions at a time, reflect back what you heard, and show me each file before you write it. Don't invent anything. If you don't know it, write [blank].

## What's in here

| Path | What it's for |
|---|---|
| `CLAUDE.md` | The constitution. Who you are, how to work, the hard rules. The AI reads it every session. |
| `AGENTS.md` | Points other AI tools at `CLAUDE.md`. |
| `context/` | Facts about you, your voice, your organization. Fill these in once and keep them current. |
| `projects/_template/` | Copy this folder for every new project: `brief.md` to start, `debrief.md` to finish. |
| `playbooks/` | Formats that worked, saved so you don't reinvent them. |
| `memory/` | `lessons.md` holds what you learned. `journal/` gets one line per working session. |
| `.claude/skills/` | `onboarding` (the first-time interview), plus three moves you'll reuse: `brief`, `critic-bench`, `debrief`. Ask for any of them by name. |
| `.claude/hooks/block_send.py` | The rail. Blocks send, post, publish and delete actions. Test it: `python3 .claude/hooks/block_send.py --self-test` |
| `examples/deca-chapter/` | A filled-in example: a DECA chapter VP running a recruitment push. All names are made up. |

## How to use it day to day

- **Starting something:** "New project: fall recruitment. Use the brief skill." It copies the template and interviews you until the brief is real.
- **Checking a draft:** "Run the critic bench on this. Three judges: a small-business owner, a bank manager and a marketing director."
- **Finishing:** "Debrief this project." Then move the lessons that matter into `memory/lessons.md`.
- **When it gets something wrong:** don't just fix the output. Tell it to fix the file that caused it (`context/`, `CLAUDE.md` or a playbook), so it stays fixed.

## A few rules I'd keep

- Never put passwords, other people's private info, or anything you wouldn't want leaked into these files.
- Keep your repo **private** if it has anything personal in it.
- If the AI tells you a number, check it. Robots are confident, not correct.

---

Built by TJ Lind for MN DECA's First Big Thing Fall Challenge, 2026. Based on the system he uses to run marketing at Percent, with everything company-specific taken out. MIT licensed: copy it, change it, make it yours.
