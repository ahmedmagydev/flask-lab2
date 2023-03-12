

## developemt , production
class Config:
    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(Config):
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"


class ProductionConfig(Config):
    DEBUG= False
    # postgresql:://username:password@localhost:portnumber/dbname
    SQLALCHEMY_DATABASE_URI = "postgresql://mego:iti@localhost:5432/migoo"



projectConfig= {
    'dev': DevelopmentConfig,
    'prd': ProductionConfig
}