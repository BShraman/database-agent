
class Executor():
    def __init__(self):
        from core.config import config
        from core.tools.database import Database

        self.logger = config.logger
        self.llm = config.LLM
        self.db = Database()

    def run(self):
        from langchain_community.agent_toolkits.sql.base import create_sql_agent
        
        agent_executor = create_sql_agent(
        llm=self.llm,
        toolkit=self.db.connect(),
        verbose=True)

        return agent_executor