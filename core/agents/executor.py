
class Executor():
    def __init__(self):
        from core.config import config
        from core.tools.database import Database
        from langchain import hub

        self.logger = config.logger
        self.llm = config.LLM
        self.db = Database()
        self.prompt_template = hub.pull("langchain-ai/sql-agent-system-prompt")

    # def run(self):
    #     from langchain_community.agent_toolkits.sql.base import create_sql_agent
        
    #     agent_executor = create_sql_agent(
    #         llm=self.llm,
    #         toolkit=self.db.toolkit(),
    #         verbose=True)

    #     return agent_executor
    
    def run(self):
        from langchain_community.agent_toolkits.sql.base import create_sql_agent
        from langgraph.prebuilt import create_react_agent
        
        assert len(self.prompt_template.messages) == 1
        self.logger.info(self.prompt_template.input_variables)
        
        system_message = self.prompt_template.format(dialect="PostgreSQL", top_k=5)
        agent_executor = create_react_agent(self.llm, 
                                            self.db.toolkit(),
                                            prompt=system_message)

        # agent_executor = create_sql_agent(
        #     llm=self.llm,
        #     toolkit=self.db.connect(),
        #     verbose=True)

        return agent_executor