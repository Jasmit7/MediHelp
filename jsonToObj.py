import json

class Medicine:
    def __init__(self, name, synonyms, medline_plus_id=None, nhs_url=None, wikipedia_url=None, mesh_id=None, drugbank_id=None):
        self.name = name
        self.synonyms = synonyms
        self.medline_plus_id = medline_plus_id
        self.nhs_url = nhs_url
        self.wikipedia_url = wikipedia_url
        self.mesh_id = mesh_id
        self.drugbank_id = drugbank_id
