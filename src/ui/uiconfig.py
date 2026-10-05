from configparser import ConfigParser


class Config:

    def __init__(self, config_path="src/ui/uiconfig.ini"):
        self.config = ConfigParser()
        self.config.read(config_path)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODELS").split(", ")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")