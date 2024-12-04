import openai
import os
import base64
import requests
from PIL import Image
from io import BytesIO
import subprocess
import tempfile
import re
import importlib
import sys
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.llms import OpenAIChat
import black  

# Set your API key directly
os.environ["OPENAI_API_KEY"] = 'your-api-key'
openai.api_key = os.getenv("OPENAI_API_KEY")

class SophisticatedAgentPro:
    def __init__(self):
        # Initialize LangChain agent with and prompt management
        self.memory = ConversationBufferMemory()  # Memory to track conversation history
        self.llm = OpenAIChat(model="gpt-4")  # Updated to use OpenAIChat for chat models
        self.agent_chain = LLMChain(
            llm=self.llm,
            prompt=PromptTemplate(
                input_variables=["action"],
                template="The user wants to: {action}. Let's solve this step by step with clarity and thoroughness."
            ),
            memory=self.memory
        )

    def generate_code(self, prompt):
        # Start logging thoughts and actions with LangChain Agent
        print("[Agent Thought]: Initiating code generation process based on the given prompt.")
        thought_log = self.agent_chain.run(action="Generate Python code to " + prompt)
        print(f"[Agent Log]: {thought_log}")

        response = openai.ChatCompletion.create(
            model="gpt-4",  
            messages=[
                {"role": "system", "content": "You are a Python code generator. Respond only with executable Python code, no explanations or comments except for required pip installations at the top."},
                {"role": "user", "content": f"Generate Python code to {prompt}. If you need to use any external libraries, include a comment at the top of the code listing the required pip installations."}
            ],
            max_tokens=1000,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        code = response['choices'][0]['message']['content']
        code = re.sub(r'```(?:python)?\n|```', '', code)
        code_lines = code.split('\n')
        while code_lines and not (code_lines[0].startswith('import') or code_lines[0].startswith('from') or code_lines[0].startswith('#')):
            code_lines.pop(0)

        return '\n'.join(code_lines)

    def install_libraries(self, code):
        print("[Agent Thought]: Checking for required libraries to install.")
        libraries = re.findall(r'#\s*pip install\s+([\w-]+)', code)
        if libraries:
            print("[Agent Action]: Installing required libraries...")
            for lib in libraries:
                try:
                    importlib.import_module(lib.replace('-', '_'))
                    print(f"{lib} is already installed.")
                except ImportError:
                    print(f"Installing {lib}...")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            print("Libraries installed successfully.")

    def execute_code(self, code):
        print("[Agent Thought]: Preparing to execute the generated code.")
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
            temp_file.write(code)
            temp_file_path = temp_file.name

        try:
            print("[Agent Action]: Executing the code...")
            result = subprocess.run([sys.executable, temp_file_path], capture_output=True, text=True, timeout=30)
            output = result.stdout
            error = result.stderr
        except subprocess.TimeoutExpired:
            output = ""
            error = "Execution timed out after 30 seconds."
        finally:
            os.unlink(temp_file_path)

        return output, error

    def prettify_code(self, code):
        try:
            formatted_code = black.format_str(code, mode=black.Mode())
        except Exception as e:
            print(f"[Agent Thought]: Formatting failed due to: {e}. Showing unformatted code.")
            formatted_code = code
        return formatted_code

    def run(self, prompt):
        print(f"[Agent Thought]: Generating code for the prompt: '{prompt}'")
        code = self.generate_code(prompt)
        print("[Agent Log]: Generated code:")
        print(code)
        print("\n[Agent Thought]: Now installing any required libraries.")
        self.install_libraries(code)
        print("\n[Agent Thought]: Executing the generated code.")
        output, error = self.execute_code(code)

        if output:
            print("[Agent Log - Output]:")
            print(output)
        if error:
            print("[Agent Log - Error]:")
            print(error)

        # Print the prettified version of the code
        print("\n[Agent Thought]: Printing the prettified version of the generated code.")
        prettified_code = self.prettify_code(code)
        print(prettified_code)
