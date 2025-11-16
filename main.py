from kaggle_secrets import UserSecretsClient
import google.generativeai as genai

# Get API key from secrets
user_secrets = UserSecretsClient()
API_KEY = user_secrets.get_secret("GOOGLE_API_KEY")

# Setup Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-lite')

# ===== MAIN FUNCTION =====
def gtu_agent(question):
    """GTU Exam Prep Assistant"""
    
    prompt = f"""You are a GTU exam preparation assistant.
    
    Student Question: {question}
    
    Provide:
    1. Clear explanation
    2. Example
    3. Key points for exams
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# ===== TEST =====
print("GTU EXAM PREP ASSISTANT")
print("=" * 50)

# Test question
question = "What is JAVA?"
answer = gtu_agent(question)
print(f"\nQuestion: {question}")
print(f"\nAnswer:\n{answer}")
