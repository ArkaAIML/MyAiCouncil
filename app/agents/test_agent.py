from app.agents.stability_agent import stability_agent

context = """
Country: Federation of Caldria
Current metrics: Stability: 60, Public Trust: 55, Resources: 70, Ethics: 40
Problem: A local militia has seized a grain silo and is distributing food for free.
"""

print("Running Stability Agent...\n")

# Call the agent
response = stability_agent.run(context)

# 1. To see the actual JSON/Text response:
print("--- Agent's Decision ---")
print(response.content) 

# 2. If you want to see the "thought process" or history:
# response.messages contains the prompts AND the responses.