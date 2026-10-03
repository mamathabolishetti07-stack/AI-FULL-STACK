from ollama import chat
bad="Tell me about cats."
good="list 3 cat breeds that are suitable for a penthouse 2 lines about each."
responseB =chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":"bad"
            
        }
    ]
)
responseG=chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":"good"
        }
    ]
)
print(f"Bad prompt Result:{responseB. message.content}")
print()
print(f"Good. prompt Result:{responseG .message .content}")