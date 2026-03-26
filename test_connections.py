
import os
import sys
from dotenv import load_dotenv

# Add src to path
sys.path.append(os.path.join(os.getcwd(), "src"))

from agent.env_utils import DEEPSEEK_API_KEY, DEEPSEEK_API_URL
from langchain_deepseek import ChatDeepSeek
from sqlalchemy import create_engine, text

def test_llm():
    print("Testing LLM connection...")
    try:
        llm = ChatDeepSeek(
            api_key=DEEPSEEK_API_KEY,
            api_base=DEEPSEEK_API_URL,
            model="deepseek-chat",
            timeout=10
        )
        response = llm.invoke("Hi")
        print(f"LLM Response: {response.content}")
        return True
    except Exception as e:
        print(f"LLM Connection Error: {e}")
        return False

def test_db():
    print("\nTesting DB connection...")
    # These match text_to_sql_agent.py hardcoded values
    host, port, username, password, database = '127.0.0.1', 3306, 'root', '123456', 'test'
    connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4"
    print(f"Connecting to: mysql+pymysql://{username}:****@{host}:{port}/{database}")
    try:
        engine = create_engine(connection_string)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print(f"DB Response: {result.fetchone()}")
        return True
    except Exception as e:
        print(f"DB Connection Error: {e}")
        return False

if __name__ == "__main__":
    llm_ok = test_llm()
    db_ok = test_db()
    
    if llm_ok and db_ok:
        print("\nAll connections successful!")
    else:
        print("\nSome connections failed.")
