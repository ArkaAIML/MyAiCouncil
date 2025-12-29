from app.agents.public_trust_agent import public_trust_agent

context = """
Country: Federation of Caldria
Current metrics: Stability: 60, Public Trust: 55, Resources: 70, Ethics: 40
Problem: A local militia has seized a grain silo and is distributing food for free.
"""

print("Running public trust Agent...\n")


response = public_trust_agent.run(context)


print("--- Agent's Decision ---")
print(response.content) 
