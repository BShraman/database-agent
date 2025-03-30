class Database:
    def __init__(self):
        from core.config import config

        self.logger = config.logger
        self.db_name = config.PG_DB
        self.user = config.PG_USER
        self.password = config.PG_PASSWORD
        self.host = config.PG_HOST
        self.port = config.PG_PORT
        self.llm = config.LLM

    def connect(self):
        from langchain_community.utilities.sql_database import SQLDatabase
        from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

        self.logger.info(f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}/{self.db_name}")
        db = SQLDatabase.from_uri(f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}/{self.db_name}')
        
        toolkit = SQLDatabaseToolkit(db=db, llm=self.llm)

        return toolkit

