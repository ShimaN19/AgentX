import argparse
from agent import SophisticatedAgentPro

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Run SophisticatedAgentPro with a prompt.")
    parser.add_argument("prompt", type=str, help="The prompt to generate code for.")
    args = parser.parse_args()

    # Create an instance of 
    agent = SophisticatedAgentPro()
    agent.run(args.prompt)

if __name__ == "__main__":
    main()
