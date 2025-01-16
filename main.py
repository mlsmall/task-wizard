from agents.task_wizard import build_graph
from langgraph.store.memory import InMemoryStore
from langchain_core.messages import HumanMessage

def main():
    # Build the compute graph
    graph = build_graph()

    # We supply a thread ID for short-term (within-thread) memory
    # We supply a user ID for long-term (across-thread) memory
    config = {"configurable": {"thread_id": "1", "user_id": "player456"}}

    print("Welcome to TaskWizard! Type 'exit' or 'quit' to end the session.")

    while True:
        # Prompt user for input
        user_input = input("\nUser: ")
        if user_input.lower() in ('exit', 'quit'):
            print("Goodbye!")
            break

        # Create input messages
        input_messages = [HumanMessage(content=user_input)]

        # Run the graph
        for chunk in graph.stream({"messages": input_messages}, config, stream_mode="values"):
            # Fetch the assistant's response
            assistant_message = chunk["messages"][-1]
            # Print the assistant's response
            assistant_message.pretty_print()

if __name__ == "__main__":
    main()