
from core.agents.executor import Executor

# if __name__ == '__main__':
#     query = "Which City has more number of people at age equal to 35 ?"
#     executor = Executor()
#     agent_executor = executor.run()
#     agent_executor(query)

if __name__ == '__main__':
    query = "Which City has more number of people at age equal to 35 ?"
    executor = Executor()
    agent_executor = executor.run()
    events = agent_executor.stream(
        {"messages": [("user", query)]},
        stream_mode="values")
    
    for event in events:
        event["messages"][-1].pretty_print()