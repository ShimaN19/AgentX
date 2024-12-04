from setuptools import setup, find_packages

setup(
    name="agent",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "requests",
        "Pillow",
        "langchain",
        "black"
    ],
    entry_points={
        "console_scripts": [
            "run-agent=cli:main",
        ],
    },
    description="Code generation and execution agent using OpenAI's GPT-4.",
    author="Shima",
)
