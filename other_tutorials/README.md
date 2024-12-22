# Overall Workflow for Retrieval Augmented Generation (RAG), using LangChain to implement RAG
## Embeddings and Vector Store
![image](https://github.com/user-attachments/assets/3906239b-fff7-4c97-ab4a-62e231eaae76)
## Retrieval
![image](https://github.com/user-attachments/assets/3a9b561e-64f0-4d95-93de-0e5e7bf8dfad)

* **Maximium Marginal Relevance (MMR)**
![image](https://github.com/user-attachments/assets/fc3b81d0-4e50-4709-96cb-24e303449737)
![image](https://github.com/user-attachments/assets/c44b37cc-d4d2-42e4-9855-ef0fcd73c375)
![image](https://github.com/user-attachments/assets/b79e38f0-54e9-4ddf-b6ca-06f30c9713b2)
* Other types of retrieval

Not using a vector database, such as
* SVM
* TF-IDF
* ...

## Question Answering
* Multiple relevant documents have been retrieved from the vector store
* Potentially compress the relevant splits to fit into the LLM context
* Send the information along with our question to an LLM to select and format an answer
![image](https://github.com/user-attachments/assets/47726105-430e-494b-8c55-04e4bda09ed1)

![image](https://github.com/user-attachments/assets/52284ccb-b9c7-413e-877b-1d36610e02c5)

## Chat
![image](https://github.com/user-attachments/assets/376aa300-2624-4e56-b5ad-7b908c4305ab)

You can use LangSmith to create a ChatBot
