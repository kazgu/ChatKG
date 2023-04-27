# ChatKG
LangChain for Knowledge Graph
Chat with any KG
```
from chatkg import ChatKG
chk=ChatKG('sk-MKHXc....',verbose=True) # openai api key
#add the triples to the KGChain,and  indexing
triples=[{'subject':'Jack','predicate':'is','object':'a professor'},{'subject':'John','predicate':'is','object':'a teacher'}]
chk.add_triples(triples)
# chat with KG
chk.chat('Jack')

> Entering new GraphQAChain chain...
Entities Extracted:
 Jack
Full Context:
Jack is a professor

> Finished chain.
' Jack is a professor.'
```
