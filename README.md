# AgentX: Autonomous Python Code Generation via GPT-4

**AgentX** is an experimental code generation agent that leverages GPT-4 to transform natural language prompts into executable Python scripts. By employing a chain-of-thought mechanism, it plans, generates, and executes tasks step-by-step, ensuring logical coherence and operational accuracy.

---

## 🧠 Overview

AgentX is designed to bridge the gap between human intent and machine execution. It interprets user prompts, decomposes them into actionable steps, and synthesizes Python code that aligns with the specified objectives. This approach facilitates rapid prototyping and automation of complex tasks without manual coding.

---

## 🗂️ Project Structure

```
AgentX/
├── agent.py           # Core logic for prompt interpretation and code generation
├── cli.py             # Command-line interface for user interaction
├── __init__.py        # Package initialization
├── requirements.txt   # Project dependencies
├── setup.py           # Installation script
└── README.md          # Project documentation
```

---

## 🚀 Installation

To install AgentX, clone the repository and install the package in editable mode:

```bash
git clone https://github.com/ShimaN19/AgentX.git
cd AgentX
pip install -e .
```

---

## 💡 Usage

Once installed, you can invoke AgentX from the command line:

```bash
run-agent "Generate a Python script to train a neural network on the MNIST dataset using PyTorch."
```

AgentX will process the prompt, generate the corresponding Python code, and execute it, providing real-time feedback through thought logs.

---

## 🧾 Thought Logs

During execution, AgentX emits thought logs to provide transparency into its decision-making process:

- `[Agent Thought]: Initiating code generation process based on the given prompt.`
- `[Agent Thought]: Decomposing task into subcomponents.`
- `[Agent Thought]: Synthesizing code for data preprocessing.`
- `[Agent Thought]: Constructing model architecture.`
- `[Agent Thought]: Finalizing and executing the generated script.`

These logs offer insights into the internal workflow and facilitate debugging and refinement.

---

## 🧪 Example

**Prompt:**

```bash
run-agent "Create a Python script that scrapes the top 10 news headlines from BBC News and saves them to a CSV file."
```

**AgentX Output:**

```python
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.bbc.com/news'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

headlines = [h3.get_text() for h3 in soup.find_all('h3')[:10]]

with open('bbc_headlines.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline'])
    for headline in headlines:
        writer.writerow([headline])
```

---

## 🛠️ Future Enhancements

- **Error Handling:** Implement robust exception handling for network requests and file operations.
- **Prompt Validation:** Introduce mechanisms to validate and sanitize user prompts.
- **Extensibility:** Enable support for additional programming languages and frameworks.
- **User Interface:** Develop a graphical user interface for enhanced usability.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Shima N.**  
For inquiries or collaboration opportunities, please contact via [GitHub](https://github.com/ShimaN19).

---

Feel free to customize this `README.md` to better align with your project's specifics and objectives. If you need assistance with further refinements or additional documentation, don't hesitate to ask! 

```python
# Required installations:
# !pip install torch torchvision numpy
```
