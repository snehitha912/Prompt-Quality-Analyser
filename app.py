def analyze_prompt(prompt):
    words = prompt.split()
    length_score = min(25, max(0, int(len(words) / 2)))  
    keyword_list = ["explain", "generate", "create", "write", "code", "build", "make", "design", "summarize", "translate", "compare"]
    keyword_score = 25 if any(k in prompt.lower() for k in keyword_list) else 0
    detail_score = 25 if any(ch.isdigit() for ch in prompt) or any(w in prompt.lower() for w in ["context", "details", "examples", "format", "limit"]) else 0
    punctuation_score = 25 if any(c in prompt for c in [".", ":", ";", ","]) else 0
    total = length_score + keyword_score + detail_score + punctuation_score
    if total > 100:
        total = 100
    return total

def generate_structured_prompt(prompt):
    task = prompt.strip()
    structured = (
        "Provide a clear, complete, and high-quality response for the following request:\n\n"
        f"\"{task}\"\n\n"
        "Required response format (copy and paste the whole prompt below into the model):\n\n"
        "TASK:\n"
        f"- {task}\n\n"
        "CONTEXT / DETAILS (if any):\n"
        "- Add any extra context here or leave blank if none\n\n"
        "OBJECTIVE / GOAL:\n"
        "- State the desired outcome clearly (what should the model produce?)\n\n"
        "REQUIREMENTS:\n"
        "- Include any specific points to cover\n"
        "- Include required sections, headings, or outputs\n"
        "- Mention any preferred language, libraries, or constraints\n\n"
        "OUTPUT FORMAT:\n"
        "- Specify exact format (bulleted list, numbered steps, code block, JSON, short paragraph, etc.)\n\n"
        "CONSTRAINTS (if applicable):\n"
        "- Max length, style, tone, forbidden content, strict structure, or performance limits\n\n"
        "TONE / STYLE:\n"
        "- Professional / casual / beginner-friendly / concise / detailed\n\n"
        "EXAMPLES (if applicable):\n"
        "- Example input and expected output or example style\n\n"
        "STEP-BY-STEP INSTRUCTIONS FOR THE MODEL:\n"
        "1. Start with a brief definition or overview.\n"
        "2. Provide a detailed breakdown or explanation.\n"
        "3. Give step-by-step instructions or key points if applicable.\n"
        "4. Show an example or demonstration where useful.\n"
        "5. End with a concise summary and final takeaways.\n\n"
        "ADDITIONAL NOTES (optional):\n"
        "- Add any clarifications, edge cases, or follow-up questions the model should ask\n\n"
        "Now produce the final output following the format above."
    )
    return structured

def main():
    print("Prompt Quality Analyzer and Universal Structurer")
    while True:
        user_input = input("\nEnter your prompt (or type 'exit' to quit): ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Goodbye.")
            break
        score = analyze_prompt(user_input)
        structured = generate_structured_prompt(user_input)
        print(f"\nPrompt Quality Score: {score}/100\n")
        print("Structured Prompt (ready to copy-paste):\n")
        print(structured)

if __name__ == "__main__":
    main()
