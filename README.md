# AgentX

**AgentX** is a streamlined code generation agent that uses GPT-4 to convert user prompts into executable Python scripts. It employs a chain-of-thought mechanism to plan, generate, and execute tasks step-by-step, ensuring accuracy and logical flow.

## Installation

In the root directory (`agent`), run:

```sh
pip install -e .
```

## Usage

Run the agent from the terminal using:

```sh
run-agent "Generate a Python script to train a neural network on the MNIST dataset using PyTorch."
```

## Thought Logs

During its operations, **AgentX** generates "thought logs" to give transparency and clarity to its internal processes. Here are examples of the thought logs:

- **[Agent Thought]:** Initiating code generation process based on the given prompt.
- **[Agent Thought]:** Now installing any required libraries.
- **[Agent Thought]:** Checking for required libraries to install.
- **[Agent Thought]:** Executing the generated code.
- **[Agent Thought]:** Preparing to execute the generated code.
- **[Agent Thought]:** Printing the prettified version of the generated code.
- **Required Installations:**
If needed, AgentX will automatically indicate the required installations for generated code and install them. For example:

```python
# Required installations:
# !pip install torch torchvision numpy
```
