from langchain.indexes import GraphIndexCreator
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.graphs.networkx_graph import KnowledgeTriple
from langchain.chains import GraphQAChain
import os


class ChatKG:
    def __init__(self,apikey,api_base=None,verbose=True):
        os.environ["OPENAI_API_KEY"] = apikey
        if api_base:
            os.environ["OPENAI_API_BASE"] =api_base 
        self.index_creator = GraphIndexCreator(llm=OpenAI(temperature=0))
        self.kgs=[]
        self.graph=None
        self.chain=None
        self.verbose=verbose
    def update_graph(self):
        self.graph=self.index_creator.from_triple(self.kgs)
        self.chain = GraphQAChain.from_llm(OpenAI(temperature=0), graph=self.graph, verbose=self.verbose)
    def add_triples(self,triples):
        for triple in triples:
            k=KnowledgeTriple(subject=triple['subject'], predicate=triple['predicate'], object_=triple['object'])
            self.kgs.append(k)
        self.update_graph()
    def chat(self,prompt):
        return self.chain.run(prompt)
    
    