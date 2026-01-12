from task.app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

run(
    deployment_name='gpt-4o',
    print_only_content=True,
    temperature=0.7,  # Balanced creativity (try values: 0.0, 0.5, 1.0, 2.0)
)

# Alternative configurations (uncomment to try):
# Low temperature (more deterministic/focused):
# run(
#     deployment_name='gpt-4o',
#     print_only_content=True,
#     temperature=0.0,
# )

# High temperature (more creative/random):
# run(
#     deployment_name='gpt-4o',
#     print_only_content=True,
#     temperature=2.0,
# )

# Invalid temperature (will cause error):
# run(
#     deployment_name='gpt-4o',
#     print_only_content=True,
#     temperature=2.1,  # Out of range [0.0, 2.0]
# )