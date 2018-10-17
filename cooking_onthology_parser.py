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
    pass
  

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


if __name__ == "__main__":
  cooking_ontology_parser = CookingOnthologyParser()