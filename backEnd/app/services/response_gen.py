from app.utils.jokes import get_random_joke, get_advice

def generate_response(emotion: str, user_input: str) -> str:
    if emotion == "sadness":
        return f"Hey, I know it's tough 💔... but here's a joke to cheer you up:\n\n{get_random_joke()}"
    elif emotion == "joy":
        return f"Yay! I'm glad you're happy 😄. Let's celebrate! 🥳"
    elif emotion == "anger":
        return f"Take a deep breath... or throw a pillow 🤬💢. Here's some silly advice: {get_advice()}"
    else:
        return "I'm here for you, always 💛. Tell me more?"
