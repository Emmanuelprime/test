from google import genai

client = genai.Client(api_key="AIzaSyBt88LusVecapHk1oi5g56fun2cGSbsVB4")

prompt = """
you are a hr specialist that is good at drafting a cv for a user. draft a
good looking cv for me. make sure to infer details no placeholders ensure 
everything is complete. my name is emmanuel and i am an ai developer
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

print(response.text)