# AI Coding Agent Instructions

## Project Overview
This workspace contains simple Python utility scripts focused on game logic and task management:
- **rock paper scissor.py**: Game implementation with user input validation
- **to do list.py**: Placeholder for task management tool (in development)

## Architecture & Code Patterns

### Game Logic Pattern (rock paper scissor.py)
The Rock-Paper-Scissor game demonstrates a simple, functional approach:
- Uses list indexing for choice enumeration (`k=[0]` = Rock, `k[1]` = Paper, `k[2]` = Scissor)
- Win condition uses chained OR logic comparing against winning combinations:
  ```python
  (l==k[0] and j==k[1]) or (l==k[1] and j==k[2]) or (l==k[2] and j==k[0])
  ```
- Input validation checks membership before game logic
- Uses `random.choice()` for computer moves
- Short variable names (k=choices, l=player choice, j=computer choice) - be aware for maintenance

### Naming Conventions
- Single/double-letter variables are used throughout (intentional brevity)
- When extending code, follow the existing style but consider clarity for new features
- Imports use aliasing (e.g., `import random as rd`)

## Common Tasks & Workflows

### Running Scripts
```bash
python "rock paper scissor.py"
python "to do list.py"
```

### Testing Game Logic
The game validates input before game logic executes. Test cases should include:
- Valid inputs from the choices list
- Invalid inputs (should show "Please input a valid option.")
- Tie scenarios
- Win/loss scenarios for all three combinations

### Development Focus Areas
1. **Complete to do list.py**: Currently empty - requires task storage, display, add, remove functionality
2. **Enhance rock paper scissor.py**: Consider multi-round scoring, user menu, difficulty levels
3. **Code Quality**: When refactoring, replace single-letter variables with descriptive names (choices, player_choice, computer_choice)

## Key Integration Points
- Both scripts are standalone CLI applications with no inter-module dependencies
- No external dependencies beyond Python standard library (`random` module)
- File I/O considerations: To-do list will likely need persistent storage (file-based or simple JSON)

## Developer Guidelines
- Use Python 3.x (standard practices, f-strings already in use)
- Maintain simple, readable logic without over-engineering
- Input validation before business logic execution
- Keep scripts short and focused on single responsibility
