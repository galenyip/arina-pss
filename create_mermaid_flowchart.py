def create_mermaid_flowchart():
    """Create a Mermaid flowchart for the Rock Paper Scissors game."""
    mermaid_code = """```mermaid
flowchart TD
    Start([Start Game]) --> DisplayInstructions[Display Game Instructions]
    DisplayInstructions --> InputP1[Get Player 1 Choice]
    InputP1 --> CheckZeroP1{Is choice 0?}
    CheckZeroP1 -->|Yes| End([End Game])
    CheckZeroP1 -->|No| ValidateP1{Is choice valid?}
    ValidateP1 -->|No| InputP1
    ValidateP1 -->|Yes| InputP2[Get Player 2 Choice]
    InputP2 --> CheckZeroP2{Is choice 0?}
    CheckZeroP2 -->|Yes| End
    CheckZeroP2 -->|No| ValidateP2{Is choice valid?}
    ValidateP2 -->|No| InputP2
    ValidateP2 -->|Yes| DetermineWinner[Determine Winner]
    DetermineWinner --> DisplayResult[Display Result]
    DisplayResult --> InputP1
```"""
    
    # Save the Mermaid flowchart to a file
    with open('mermaid_flowchart.md', 'w') as f:
        f.write("# Rock Paper Scissors Game Flowchart\n\n")
        f.write(mermaid_code)
    
    print("Mermaid flowchart created as 'mermaid_flowchart.md'")
    print("You can view it:")
    print("- On GitHub (if you push your code to GitHub)")
    print("- Using the Mermaid Live Editor: https://mermaid.live")
    print("- In VS Code with Mermaid plugin or any Markdown viewer supporting Mermaid")

if __name__ == "__main__":
    create_mermaid_flowchart() 