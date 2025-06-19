from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core import Settings

#changing the global default 
Settings.embed_model = OpenAIEmbedding()

#local usage 
embedding = OpenAIEmbedding().get_text_embedding("hello world")
embeddings = OpenAIEmbedding().get_text_embedding(
    ['hello world', 'hello amal']
)

#print one embedding
print(embedding)

#print multiple embedding
for i, emb in enumerate(embeddings):
    print(f"Embedding {i+1} : {emb}")

# index = VectorStoreIndex.from_documents(documents=documents, embed_model= embed_model)