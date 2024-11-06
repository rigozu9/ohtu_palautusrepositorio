from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        toml_dict = tomli.loads(content)

        navigated_toml_dict = toml_dict["tool"]["poetry"]

        print(navigated_toml_dict)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(navigated_toml_dict["name"],
                       navigated_toml_dict["license"],
                       navigated_toml_dict["authors"],
                       navigated_toml_dict["description"],
                       navigated_toml_dict["dependencies"],
                       navigated_toml_dict["group"]["dev"]["dependencies"])
