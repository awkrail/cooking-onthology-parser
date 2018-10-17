import pandas as pd


class CookingOnthologyParser:
  def __init__(self, attribute="./ontology/attribute.tsv", hprt="./ontology/hprt.tsv", synonym="./ontology/synonym.tsv"):
    self.attribute = self.parse_attribute(attribute)
    self.hprt = self.parse_hprt(hprt)
    self.synonym = self.parse_synonym(synonym)
  
  def parse_attribute(self, attribute):
    return self.parse_tsv(attribute)


  def parse_hprt(self, hprt):
    return self.parse_tsv(hprt)
  

  def parse_synonym(self, synonym):
    synonym_tsv = pd.read_csv(synonym, delimiter="\t", header=None)
    categories = synonym_tsv.loc[:, 0]
    names = synonym_tsv.loc[:, 1]
    synonyms = synonym_tsv.loc[:, 2]
    parsed_synonym_dict = {}

    for category, name, synonym in zip(categories, names, synonyms):
      if len(category.split("-")) == 2:
        # WATCH : 材料のところは2つに分かれる
        tag, tag_category = category.split("-")
        if not tag in parsed_synonym_dict:
          parsed_synonym_dict[tag] = {}
        
        if not tag_category in parsed_synonym_dict[tag]:
          parsed_synonym_dict[tag][tag_category] = {}
        
        if not name in parsed_synonym_dict[tag][tag_category]:
          parsed_synonym_dict[tag][tag_category][name] = []
        
        if not synonym in parsed_synonym_dict[tag][tag_category][name]:
          parsed_synonym_dict[tag][tag_category][name].append(synonym)
      else:
        if not category in parsed_synonym_dict:
          parsed_synonym_dict[category] = {}
        
        if not name in parsed_synonym_dict[category]:
          parsed_synonym_dict[category][name] = []
        
        if not synonym in parsed_synonym_dict[category][name]:
          parsed_synonym_dict[category][name].append(synonym)
    return parsed_synonym_dict


  @staticmethod
  def parse_tsv(tsv_path):
    attribute_tsv = pd.read_csv(tsv_path, delimiter="\t", header=None)
    roots = attribute_tsv.loc[:, 0]
    intermediates = attribute_tsv.loc[:, 1]
    leaves = attribute_tsv.loc[:, 2]
    parsed_attributes_dict = {}

    for root, intermediate, leaf in zip(roots, intermediates, leaves):
      root = root.split("-")[-1]
      intermediate = intermediate.split("_")[0]

      if not root in parsed_attributes_dict:
        parsed_attributes_dict[root] = {}
      
      if not intermediate in parsed_attributes_dict[root]:
        parsed_attributes_dict[root][intermediate] = []
      
      if not leaf in parsed_attributes_dict[root][intermediate]:
        parsed_attributes_dict[root][intermediate].append(leaf)
    return parsed_attributes_dict