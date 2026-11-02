def build_prompt(question, context):
    prompt = f"""
    Answer the question using only the
    provided context.

    Context:
    {context}

    Question:
    {question}

    If the answer is not available in the
    context, say you don't know.
    """
    return prompt