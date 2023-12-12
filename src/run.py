import subprocess
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    subprocess.Popen(["poetry", "run", "src/main/data.py"])

    subprocess.Popen(["poetry", "run", "src/main/trade.py"])
