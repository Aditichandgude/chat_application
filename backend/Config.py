from sqlalchemy import create_engine

MYSQL_DATABASE_CONNECTION_STRING='mysql+pymysql://root:1234@localhost:3306/chat_app'    

engine=create_engine(MYSQL_DATABASE_CONNECTION_STRING)
