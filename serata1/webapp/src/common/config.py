import os
from pathlib import Path
from typing import Dict, Any
from pydantic import BaseSettings, root_validator
from functools import lru_cache
from dotenv import dotenv_values


class Settings(BaseSettings):
    """
    Official class with the data connector settings.

    This class it's very important to define the connection parameters to the database and it's used by the database manager to connect to the database.

    Please look into the official tech documentation for more information about the settings parameters and functions that you can use and configure

    """

    # def __init__(self, **kwargs):
    #     self.__dict__.update(kwargs)

    PROJECT_NAME: str = "pbg-streamlit"

    # verbosity for the logger configuration
    APP_VERBOSITY: str = "DEBUG"

    # Application Path
    APP_PATH: str = os.path.abspath(".")

    # Path for optional app configurations
    CONFIG_PATH: str = os.path.join(APP_PATH, "app", "config")

    # all the database settings for a single db
    DB_NAME: str = ""
    DB_USER: str = ""
    DB_PASSWORD: str = ""
    DB_PORT: str = ""
    DB_HOST: str = ""
    DB_SERVICE: str = ""
    DB_SQLITE_PATH: str = ""

    DB_CONFIG = {
        "dbname": DB_NAME,
        "user": DB_USER,
        "password": DB_PASSWORD,
        "port": DB_PORT,
        "host": DB_HOST,
        "service": DB_SERVICE,
        "filename": DB_SQLITE_PATH,
    }

    def _set_db_settings(
        self,
        dbname: str = DB_NAME,
        user: str = DB_USER,
        password: str = DB_PASSWORD,
        port: str = DB_PORT,
        host: str = DB_HOST,
        service: str = DB_SERVICE,
        filename: str = DB_SQLITE_PATH,
    ) -> dict:
        """
        Set the database settings for the database connection

        Args:
            dbname (str): The database name. Default the database name defined in the settings
            user (str): The username to use when connecting to the database. Default the user defined into the settings
            password (str): The password for the database. Default the password used into the settings
            port (str): The port to use when connecting to the database. Default the port used into the settings
            host (str): The host to use when connecting to the database. Default the host used into the settings
            service (str): The service to use when connecting to the database. Default the service used into the settings
            filename (str): The filename to use when connecting to the database. Default the filename used into the settings

        Returns:
            dbconfig. The dictionary object with the database connection parameters
        """
        self.DB_NAME = dbname
        self.DB_USER = user
        self.DB_PASSWORD = password
        self.DB_PORT = port
        self.DB_HOST = host
        self.DB_SERVICE = service
        self.DB_SQLITE_PATH = filename

        # launch the set_db_connection
        db_config = self._set_db_connection()
        return db_config

    def _set_db_connection(self, db_config: dict = None) -> dict:
        """
        The function is used to set the database connection parameters

        Args:
            db_config: The dictionary object with the database connection parameters

        Returns:
            The dictionary object with the database connection parameters
        """
        if db_config:
            # reconfigure the db_config connection dictionary
            self.DB_CONFIG = db_config
        else:
            # manually set each parameters
            self.DB_CONFIG["dbname"] = self.DB_NAME
            self.DB_CONFIG["user"] = self.DB_USER
            self.DB_CONFIG["password"] = self.DB_PASSWORD
            self.DB_CONFIG["port"] = self.DB_PORT
            self.DB_CONFIG["host"] = self.DB_HOST
            self.DB_CONFIG["service"] = self.DB_SERVICE
            self.DB_CONFIG["filename"] = self.DB_SQLITE_PATH

        # return the final db_config saved inside the object
        # need to copy the configuration because instead it's passed as a reference
        return self.DB_CONFIG.copy()

    # all the database settings for a single db
    MS_DB_NAME: str = ""
    MS_DB_USER: str = ""
    MS_DB_PASSWORD: str = ""
    MS_DB_PORT: str = ""
    MS_DB_HOST: str = ""
    MS_DB_SERVICE: str = "mssql"

    MS_DB_CONFIG = {
        "dbname": MS_DB_NAME,
        "user": MS_DB_USER,
        "password": MS_DB_PASSWORD,
        "port": MS_DB_PORT,
        "host": MS_DB_HOST,
        "service": MS_DB_SERVICE,
        "filename": DB_SQLITE_PATH,
    }

    def _set_ms_db_settings(
        self,
        dbname: str = MS_DB_NAME,
        user: str = MS_DB_USER,
        password: str = MS_DB_PASSWORD,
        port: str = MS_DB_PORT,
        host: str = MS_DB_HOST,
        service: str = MS_DB_SERVICE,
        filename: str = DB_SQLITE_PATH,
    ) -> dict:
        """
        Set the database settings for the database connection

        Args:
            dbname (str): The database name. Default the database name defined in the settings
            user (str): The username to use when connecting to the database. Default the user defined into the settings
            password (str): The password for the database. Default the password used into the settings
            port (str): The port to use when connecting to the database. Default the port used into the settings
            host (str): The host to use when connecting to the database. Default the host used into the settings
            service (str): The service to use when connecting to the database. Default the service used into the settings
            filename (str): The filename to use when connecting to the database. Default the filename used into the settings

        Returns:
            dbconfig. The dictionary object with the database connection parameters
        """
        self.MS_DB_NAME = dbname
        self.MS_DB_USER = user
        self.MS_DB_PASSWORD = password
        self.MS_DB_PORT = port
        self.MS_DB_HOST = host
        self.MS_DB_SERVICE = service
        self.MS_DB_SQLITE_PATH = filename

        # launch the set_db_connection
        db_config = self._set_ms_db_connection()
        return db_config

    def _set_ms_db_connection(self, db_config: dict = None) -> dict:
        """
        The function is used to set the database connection parameters

        Args:
            db_config: The dictionary object with the database connection parameters

        Returns:
            The dictionary object with the database connection parameters
        """
        if db_config:
            # reconfigure the db_config connection dictionary
            self.MS_DB_CONFIG = db_config
        else:
            # manually set each parameters
            self.MS_DB_CONFIG["dbname"] = self.MS_DB_NAME
            self.MS_DB_CONFIG["user"] = self.MS_DB_USER
            self.MS_DB_CONFIG["password"] = self.MS_DB_PASSWORD
            self.MS_DB_CONFIG["port"] = self.MS_DB_PORT
            self.MS_DB_CONFIG["host"] = self.MS_DB_HOST
            self.MS_DB_CONFIG["service"] = self.MS_DB_SERVICE
            self.MS_DB_CONFIG["filename"] = self.MS_DB_SQLITE_PATH

        # return the final db_config saved inside the object
        # need to copy the configuration because instead it's passed as a reference
        return self.MS_DB_CONFIG.copy()

    ## Set Redis Config
    REDIS_USER: str = "default"
    REDIS_PASSWORD: str = ""
    REDIS_ADDRESS: str = "redis://localhost"
    REDIS_PORT: str = "6399"
    REDIS_ENCODING: str = "utf-8"
    REDIS_DB: str = "0"

    REDIS_CONFIG = {
        "user": REDIS_USER,
        "password": REDIS_PASSWORD,
        "address": REDIS_ADDRESS,
        "port": REDIS_PORT,
        "encoding": REDIS_ENCODING,
        "db": REDIS_DB,
    }

    REDIS_CONNECTION: object = None

    def _set_redis_settings(
        self,
        user: str = REDIS_USER,
        password: str = REDIS_PASSWORD,
        address: str = REDIS_ADDRESS,
        port: str = REDIS_PORT,
        encoding: str = REDIS_ENCODING,
        db: str = REDIS_DB,
    ) -> dict:
        self.REDIS_USER = user
        self.REDIS_PASSWORD = password
        self.REDIS_ADDRESS = address
        self.REDIS_PORT = port
        self.REDIS_ENCODING = encoding
        self.REDIS_DB = db

        # launch the set_redis_connection
        redis_config = self._set_redis_connection()
        return redis_config

    def _set_redis_connection(self, redis_config: dict = None) -> dict:
        """
        The function is used to set the redis connection parameters

        :param redis_config: dict = None
        :type redis_config: dict
        :return: A dictionary with the redis configuration updated
        """
        if redis_config:
            # reconfigure the db_config connection dictionary
            self.REDIS_CONFIG = redis_config
        else:
            # manually set each parameters
            self.REDIS_CONFIG["user"] = self.REDIS_USER
            self.REDIS_CONFIG["password"] = self.REDIS_PASSWORD
            self.REDIS_CONFIG["address"] = self.REDIS_ADDRESS
            self.REDIS_CONFIG["port"] = self.REDIS_PORT
            self.REDIS_CONFIG["encoding"] = self.REDIS_ENCODING
            self.REDIS_CONFIG["db"] = self.REDIS_DB

        # return the final redis_config saved inside the object
        # need to copy the configuration because instead it's passed as a reference
        return self.REDIS_CONFIG.copy()

    def _set_all_connections(self) -> bool:
        """
        Launch the configuration of the all db connection that we have in the data connector one:
        - relational database (postgres, mysql)
        - solr db
        - redis for cache
        - local test databases (postgres, mysql)
        - Airflow DataWareHouse (postgres)
        """
        self._set_db_connection()
        self._set_ms_db_connection()
        self._set_redis_connection()

        return True

    # EXTRA VALUES not mapped in the config but that can be existing in .env or env variables in the system
    extra: Dict[str, Any] = {}

    @root_validator(pre=True)
    def build_extra(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        all_required_field_names = {
            field.alias for field in cls.__fields__.values() if field.alias != "extra"
        }  # to support alias

        extra: Dict[str, Any] = {}
        for field_name in list(values):
            if field_name not in all_required_field_names:
                extra[field_name] = values.pop(field_name)
        values["extra"] = extra
        return values


def env_load(env_file: str) -> Settings:
    """
    If you want to generate settings with a specific .env file.
    Be carefull: you have to insert only the env that are in the config.
    Look into official technical documentation for more information about the variables.

    Args:
        env_file (str): The path to the .env file. (with the name)

    Returns:
        Settings: The settings object with the .env file loaded.
    """
    if env_file:
        try:
            # get the dotenv file values into an OrderedDict
            env_settings = dotenv_values(env_file)
            # convert to normal dict
            env_settings = dict(env_settings)
            # define and create the new object
            settings = Settings(**env_settings)
            # launch the functions to generate the configurations
            settings._set_all_connections()
            return settings
        except Exception as message:
            print(
                f"Impossible to load the .env file: {env_file}, return the default settings instead"
            )
            print(message)
            return Settings()
    else:
        return Settings()


# cache system to read the settings without everytime read the .env file
@lru_cache()
def get_settings(
    settings: Settings = None, env_file: str = None, **kwargs: dict
) -> Settings:
    """
    Function to get the settings object inside the config.
    This function use lru_cache to cache the settings object and avoid to read everytime the .env file from disk (much more faster)

    Args:
        settings (Settings, optional): The settings object to use. Defaults to None.
    Returns:
        Settings: The settings object.
    """
    # define the new settings
    try:
        if not settings:
            if env_file:
                # check if env file existing
                if not Path(env_file).exists():  # nocov
                    settings = None
                    raise ValueError(f"Config file {env_file} does not exist.")
                else:
                    settings = env_load(env_file)
            else:
                settings = Settings(**kwargs)
                settings._set_all_connections()

        return settings
    except Exception as message:
        raise Exception(f"Error: impossible to get the settings: {message}")


# export the settings object (default initialization)
# # define the settings (use the env file if it's used)
env_file = os.environ.get("ENV_FILE", None)
settings = get_settings(env_file=env_file)
