#!/usr/bin/env python3
"""block_send.py: the rail. Nothing leaves this workspace without you.

Claude Code runs this before every connector (MCP) tool call and every shell
command. It blocks anything that sends, posts, publishes, schedules, shares or
deletes outside this folder. Drafts are allowed: the AI writes the draft, you
press send.

Test it:  python3 .claude/hooks/block_send.py --self-test
"""
import json
import re
import sys

# Connector tools whose name contains one of these words are blocked...
BLOCK_WORDS = r"send|post|publish|schedule|share|delete|remove|trash|reply|forward|respond|invite|purchase|pay|transfer"
# ...unless the name also contains one of these (drafting and reading are fine).
ALLOW_WORDS = r"draft|get|list|read|search|preview"

# Shell commands that are hard to undo or that publish.
BLOCK_SHELL = [
    (r"\bgit\s+push\b.*(--force|-f\b)", "Force-pushing rewrites history. Push normally, or ask me."),
    (r"\bgit\s+push\b", "Pushing publishes your work. Show me what's changing and I'll push it myself."),
    (r"\brm\s+-[a-z]*r[a-z]*f|\brm\s+-[a-z]*f[a-z]*r", "Recursive delete is blocked. Tell me exactly what to delete."),
    (r"\b(curl|wget)\b.*(-X\s*(POST|PUT|DELETE)|--data|-d\s)", "Sending data to a website is blocked. Draft it and I'll send it."),
    (r"\b(npm|pnpm|yarn)\s+publish\b", "Publishing a package is blocked."),
    (r"\bgh\s+(pr|issue|release|repo)\s+(create|merge|delete|comment)", "Posting to GitHub is blocked. Draft it here first."),
]

def deny(reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason + " (Rule: nothing goes out without the human. See CLAUDE.md.)",
    }}))
    sys.exit(0)

def check(tool, inp):
    if tool.startswith("mcp__"):
        action = tool.split("__")[-1].lower()
        if re.search(BLOCK_WORDS, action) and not re.search(ALLOW_WORDS, action):
            return f"'{action}' would act outside this workspace. Draft it and show me the exact text instead."
        # Generic tools that take an action argument, e.g. manage_email {action: "send"}
        verb = str(inp.get("action") or inp.get("operation") or "").lower()
        if verb and re.search(BLOCK_WORDS, verb) and not re.search(ALLOW_WORDS, verb):
            return f"'{tool} {verb}' would act outside this workspace. Draft it instead."
    if tool == "Bash":
        cmd = str(inp.get("command", ""))
        for pattern, why in BLOCK_SHELL:
            if re.search(pattern, cmd):
                return why
    return None

def self_test():
    cases = [
        ("mcp__gmail__send_message", {}, True),
        ("mcp__gmail__create_draft", {}, False),
        ("mcp__slack__slack_send_message_draft", {}, False),
        ("mcp__slack__slack_send_message", {}, True),
        ("mcp__x__manage_email", {"action": "send"}, True),
        ("mcp__x__manage_email", {"action": "draft"}, False),
        ("mcp__drive__search_files", {}, False),
        ("mcp__drive__share_file", {}, True),
        ("Bash", {"command": "git push origin main"}, True),
        ("Bash", {"command": "git status && git commit -m 'x'"}, False),
        ("Bash", {"command": "rm -rf projects"}, True),
        ("Bash", {"command": "ls -la"}, False),
        ("Bash", {"command": "curl -X POST https://example.com"}, True),
    ]
    bad = 0
    for tool, inp, should_block in cases:
        got = check(tool, inp) is not None
        mark = "ok  " if got == should_block else "FAIL"
        bad += got != should_block
        print(f"{mark} {'block' if got else 'allow'}  {tool} {inp or ''}")
    print("all good" if not bad else f"{bad} failed")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    reason = check(data.get("tool_name", ""), data.get("tool_input") or {})
    if reason:
        deny(reason)
    sys.exit(0)
