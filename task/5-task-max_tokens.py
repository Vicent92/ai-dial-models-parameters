from task.app.main import run

# TODO:
#  Try `max_tokens` parameter. It sets the maximum length of the AI's response. The AI will stop generating text once it hits this limit.
#  User massage: What is token when we are working with LLM?

run(
    deployment_name='gpt-4o',
    print_only_content=False,  # Show full JSON to see finish_reason='length'
    max_tokens=10,  # Limit response to 10 tokens
)

# Alternative: Higher token limit (uncomment to try)
# run(
#     deployment_name='gpt-4o',
#     print_only_content=False,
#     max_tokens=50,
# )

# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length`, and if you check the
# `content,` it is clearly unfinished.