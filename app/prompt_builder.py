def build_prompt(recipient, sender_role, purpose, tone, key_points, length):

    return f"""
You are a professional AI email writing assistant.

Generate a well-structured professional email.

STRICT RULES:
- Return ONLY valid JSON.
- No extra commentary.
- No markdown.
- No explanations.
- Use this exact structure:

{{
  "subject": "...",
  "salutation": "...",
  "body": "...",
  "closing": "...",
  "signature": "..."
}}

Email Details:
Recipient: {recipient}
Sender Role: {sender_role}
Purpose: {purpose}
Tone: {tone}
Length: {length}
Key Points: {key_points}

Generate the email now.
"""