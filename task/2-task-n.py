from task.app.main import run

# TODO:
#  Try the `n` parameter with different models (`deployment_name`). With the parameter `n`, we can configure how many
#       chat completion choices to generate for each input message
#  User massage: Why is the snow white?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=False,  # Set to False to see all choices in JSON response
    n=3,  # Generate 3 different completion choices
)

# Alternative: Try with other models (uncomment to try)
# run(
#     deployment_name='claude-3-7-sonnet@20250219',
#     print_request=True,
#     print_only_content=False,
#     n=2,
# )

# run(
#     deployment_name='gemini-2.5-pro',
#     print_request=True,
#     print_only_content=False,
#     n=5,
# )

# Pay attention to the number of choices in the response!
# If you have worked with ChatGPT, you have probably seen responses where ChatGPT offers you a choice between two
# responses to select which one you prefer. This is done with the `n` parameter.
