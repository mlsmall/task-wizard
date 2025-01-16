Markdown

# TaskWizard - AI-Powered To-Do List Assistant

TaskWizard is an intelligent To-Do list agent designed to help you manage your tasks effortlessly. Developed from the official LangGraph course, TaskWizard leverages LLMs to understand your needs, organize your tasks, and adapt to your preferences based on natural language interactions. Unlike traditional assistants, TaskWizard intelligently decides when to save tasks, update user profiles, or adjust preferences based on the context of your conversations. It manages both semantic and procedural memory, and provides a personalized and adaptive task management experience.

This project mainly showcases a practical application of the LangGraph for building a sophisticated AI agent with long-term memory systems.

## Table of Contents

- [Technical Highlights](#technical-highlights)
- [Why Task Wizard](#why-taskwizard)
- [Features](#features)
- [Technical Implementation](#technical-implementation)
  - [Agent and Its Role](#agent-and-its-role)
  - [Memory Management](#memory-management)
  - [How It Works](#how-it-works)
  - [Project Structure](#project-structure)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Usage](#usage)
- [Examples](#examples)
  - [Adding a Task](#adding-a-task)
  - [Updating Preferences](#updating-preferences)
- [Learning Outcomes](#learning-outcomes)
- [Contributing](#contributing)
- [License](#license)


## Technical Highlights

* **Single Agent Architecture** :
  A streamlined design with one powerful agent handling all interactions and memory management.
* **LangGraph Integration** :
  Leverages LangGraph for orchestrating agent workflows and managing state transitions.
* **Trustcall Utilization** :
  Employs Trustcall extractors for extracting and updating structured information from conversations.
* **OpenAI's Language Models** : Powered by advanced language models for natural language understanding andgeneration.

## Why TaskWizard?

* **Efficiency** : Saves you time by intuitively managing tasks without manual input.
* **Personalization** : Adapts to your unique needs and evolves with your preferences.
* **Seamless Experience** : Eliminates the need for multiple apps or complex commands—just have a conversation!

## Features

- **Smart Task Management:** Automatically decides when to add tasks to your To-Do list based on conversation context.
- **Memory Management:** *S*emantic Memory and Procedural Memory.
- **Adaptive Preferences:** Allows users to update their preferences dynamically through conversation.
- **Intelligent Decision-Making:** Determines whether to save information to the user profile or the To-Do list.
- **Natural Language Interaction:** Engages with users conversationally for seamless task management.
- **No Explicit Commands Needed:** Understands when to act without requiring specific instructions.

## Technical Implementation

The project is built using Python and the following technologies:

- **LangGraph:** For defining and managing complex agent workflows and memory systems.
- **Trustcall:** For extracting and updating structured information based on conversation.
- **OpenAI's GPT 4o mini:** LLM used for natural language understanding and processing.

### Agent and Its Role

**`TaskWizard `(`task_wizard.py`):**

- **Purpose:** Acts as the primary interface, handling user inputs, processing them, and updating memories accordingly.
- **Functionality:**
  - Interprets user inputs using natural language understanding.
  - Decides whether the input requires updating the user profile, To-Do list, or instructions.
  - Manages semantic memory updates using Trustcall extractors.
  - Generates appropriate responses to the user based on actions taken.

### Memory Management

**Semantic Memory:**

- Stores facts about the user (e.g., name, location, job, interests, profile).
- Maintains collections of To-Do items with details like tasks, deadlines, and status.

**Procedural Memory:**

- Stores procedures and rules used to perform tasks.
- Manages how tasks should be added or updated based on instructions (agent's system prompt).
- Adjusts behavior dynamically in response to user interactions.

### How It Works

TaskWizard uses LangGraph and Trustcall to build an AI agent capable of complex memory management and decision-making.

1. **User Interaction:**

   - The user interacts with task_wizard using natural language.
   - Inputs can include tasks, profile information, or preference updates.
2. **Processing User Input:**

   - `task_wizard` interprets the message and decides the appropriate action.
   - Determines whether to update the user profile, To-Do list, or instructions.
3. **Memory Update:**

   - Uses Trustcall extractors to update the relevant memory.
   - Semantic memory updates for profiles and To-Do items.
   - Procedural memory updates for instructions and preferences.
4. **Response Generation:**

   - Generates natural language responses to inform the user of the actions taken.
   - Ensures the conversation remains fluid.
5. **Loop:**

   - The process repeats as the user continues the conversation.
   - The agent continuously adapts based on updated memories.

### Project Structure

taskwizard/
├── agents/
│   └── task_wizard.py
├── configuration.py
├── memory_schemas.py
├── utils.py
├── main.py
├── requirements.txt
├── README.md
└── LICENSE

- **`agents/task_wizard.py`**: Contains the implementation of the `task_wizard` agent.
- **`main.py`**: The entry point of the application, initializes the agents and starts the interaction loop.
- **`memory_schemas.py`**: Defines the schemas for semantic memories like `Profile` and `To-Do`.
- **`configuration.py`**: Manages configuration settings and parameters.
- **`requirements.txt`**: Lists all the Python dependencies required to run the project.
- **`README.md`**: Documentation and overview of the project.
- **`LICENSE`**: The project's license information.

## Installation

### Prerequisites

- **Python 3.8** or higher
- **OpenAI API Key**: Required for natural language processing capabilities.
- **LangChain API Key**: Required for [LangGraph Studio](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/)

### Steps

1. Clone the Repository

  ```bash
  git clone https://github.com/mlsmall/task_wizard.git
  ```
2.  Navigate to the Project Directory
  ```bash
  cd task_wizard
  ```
3.  Install Dependencies
  ```bash
  pip install -r requirements.txt
  ```
4. Set Up Environment Variables
  - Create a .env file in the root directory.
  - Add your OpenAI and LangChain API keys:
    - OPENAI_API_KEY="your-openai-api-key"
    - LANGCHAIN_API_KEY="your-langchain-api-key"

## Usage
Run the application from the command line:
```bash
python main.py
```
Interact with task_wizard using natural language prompts. The agent will manage your To-Do list by deciding when to save tasks, update your profile, or adjust your preferences based on the conversation.

## Examples
### Adding a Task
User: My name is Mauro. I live in Montreal with my wife and we have a 7-year-old daughter.

TaskWizard: Got it, Mauro! I've noted that you live in Montreal with your wife and have a 7-year-old daughter. If there's anything else you'd like to share or if you have tasks to add to your To-Do list, just let me know!

User: My wife asked me to book swim lessons for our daughter.

TaskWizard: I've added the task to your ToDo list: "Book swim lessons for daughter." You can check local swimming schools, look for community center programs, or search for private swim instructors. If you need any help with this task, just let me know!

### Updating Preferences
User: When creating or updating ToDo items, include specific local businesses / vendors.

TaskWizard: I've noted your preference to include specific local businesses or vendors when creating or updating ToDo items. If you have any specific vendors in mind for the swim lessons or any other tasks, feel free to share!

### Adding a New Task
User: I need to find a place for the swim lessons.

TaskWizard: I've added the task to your ToDo list: "Find a place for swim lessons for daughter." You can check local swimming schools like YMCA Montreal or Club de Natation de Montréal, look for community center programs at Centre Sportif Claude-Robillard, or search for private swim instructors on platforms like Swimly or TakeLessons. If you need help with any of these options, just let me know!

### Updating a Task
User: "For the swim lessons, I need to get that done by the end of January."

TaskWizard: I've updated the deadlines for the swim lessons tasks. Both "Book swim lessons for daughter" and "Find a place for swim lessons for daughter" are now due by the end of January 2025. If there's anything else you need to adjust or add, just let me know!

### Showing the To-Do List
User: Can you show me my todo list?

TaskWizard: 
1. **Book swim lessons for daughter**
   - Time to complete: 30 minutes
   - Deadline: January 31, 2025
   - Solutions:
     - Check local swimming schools
     - Look for community center programs
     - Search for private swim instructors
   - Status: Not started

2. **Find a place for swim lessons for daughter**
   - Time to complete: 30 minutes
   - Deadline: January 31, 2025
   - Solutions:
     - Check local swimming schools like YMCA Montreal or Club de Natation de Montréal
     - Look for community center programs at Centre Sportif Claude-Robillard
     - Search for private swim instructors on platforms like Swimly or TakeLessons
   - Status: Not started

### Updating Profile Information
You: By the way, I just moved to New York City.

TaskWizard: Noted! I've updated your profile with your new location: New York City.

## Learning Outcomes
By developing this project, the following were achieved:
    • Advanced Agent Design: Created an AI agent with the ability to manage complex tasks and make decisions.
    • Memory Management: Implemented both semantic and procedural memory systems within the agent.
    • Dynamic Preference Handling: Enabled real-time updating of user preferences through natural language.
    • Integration with LangGraph and Trustcall: Gained practical experience in using these frameworks for AI development.
    • Enhanced Natural Language Processing Skills: Improved handling of conversational AI and context understanding.
    • Modular Code Structure: Emphasized clean, maintainable code with a logical project structure.

## Contributing
As this project was built as part of a learning experience from the official LangGraph course, contributions are not being accepted. However, you are welcome to fork the repository and explore enhancements on your own.

## License
This project is licensed under the MIT License. See the LICENSE file for details.