
# The Prompting / Prompt Engineering
- https://www.promptingguide.ai/
- https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering?pivots=programming-language-chat-completions
- https://github.com/microsoft/generative-ai-for-beginners/tree/main/04-prompt-engineering-fundamentals


TODO:
Prompt Prefixes: Add a prefix like "As a knowledgeable advisor:" before the prompt to steer the model's response style.

Prompt Decomposition: Break down the prompt into sub-prompts like "What are typical extracurricular activities for high school students?" and "What factors should be considered when recommending an activity to a student?"

Prompt Reframing: Rephrase the prompt to be more specific, e.g. "Recommend an extracurricular activity suitable for a high school student based on their interests and schedule availability."

Prompt Constraints: Add constraints like "Suggest an activity that is low-cost and doesn't require travel" to narrow down the response.

Prompt Mirroring: Ask the model to first rephrase or summarize the prompt to check its understanding before providing a suggestion.



# RAG Applications: Built and deployed Retrieval-Augmented Generation (RAG) applications utilizing vector databases and Mistral AI-Language models with LangChain.
| Question | Answer |
|----------|--------|
| What is a RAG (Retrieval-Augmented Generation) application? | RAG is a technique where external knowledge is retrieved from a database (such as a vector store) and used to augment the generation of responses by an AI model. This enables the model to provide more accurate and up-to-date information by retrieving specific context during inference. |
| How does the integration of vector databases improve RAG applications? | Vector databases store embeddings of documents or data as vectors, enabling semantic search. Instead of exact keyword matching, the vector store finds contextually relevant data, enhancing the model's ability to retrieve relevant information for generation. |
| What is the role of LangChain in building RAG applications? | LangChain is a framework that simplifies the creation of chains of prompts, LLMs, and retrievers. It allows developers to easily connect language models with retrieval systems, enabling complex workflows like RAG applications where context needs to be fetched from external sources. |
| What is Mistral AI, and how is it used in RAG applications? | Mistral AI provides high-performing, open-source language models that can be used for generating text. In RAG applications, these models generate responses based on the context retrieved from vector databases, making them more accurate and relevant. |
| How do vector databases store and retrieve information? | Vector databases store data as high-dimensional embeddings, which are mathematical representations of text. When a query is made, it is transformed into an embedding, and the database retrieves data based on proximity (similarity) to this embedding using techniques like nearest neighbor search. |
| Can you describe how you integrated Mistral AI-Language models into your RAG system? | Mistral AI models were integrated into the RAG workflow as the generation engine. After retrieving relevant context from the vector database, the retrieved data is passed to the Mistral model for generating the final response that incorporates both the model's knowledge and the retrieved information. |
| What challenges did you face while deploying RAG applications? | Some of the challenges include managing the latency involved in retrieving data from vector stores, ensuring that the retrieved information is relevant to the prompt, and effectively integrating the retrieval process with language generation to produce coherent and contextually accurate responses. |
| How does the retrieval process in a RAG application work? | The retrieval process begins with converting the user's query into a vector (embedding). This vector is then used to search the vector database for semantically similar embeddings (documents). The retrieved documents are passed as context to the language model, which then generates the response. |
| What type of use cases are suitable for RAG applications? | RAG applications are ideal for use cases requiring dynamic, up-to-date information retrieval, such as customer support, knowledge base querying, document generation, technical support, and real-time data analysis. |
| How do you evaluate the effectiveness of a RAG application? | Effectiveness is evaluated by measuring the relevance of retrieved information, the coherence of the generated response, and the overall performance (latency and accuracy). Metrics such as precision, recall, and F1 score can be used for the retrieval component, while BLEU or ROUGE scores can be used for generation. |
| What are the advantages of using vector-based search over traditional keyword-based search in RAG applications? | Vector-based search allows for semantic search, meaning it understands the meaning of the text and can retrieve contextually relevant information even if the exact words are not present in the query. This leads to more accurate and meaningful retrieval in response to user queries. |
| How do you ensure the retrieval of relevant documents for a query in a RAG system? | Relevance is ensured by fine-tuning the embedding models that generate vector representations, using similarity metrics (e.g., cosine similarity) to match the query vector to stored vectors, and carefully designing the retrieval logic to focus on the most relevant sections of the knowledge base. |
| What role do embeddings play in the RAG architecture? | Embeddings are vectorized representations of text that capture semantic meaning. They are essential for the retrieval process in RAG, enabling efficient and relevant matching between the query and stored documents in a vector database. |
| Can you explain how chain-of-thought prompting could be combined with RAG? | Chain-of-thought prompting can be used with RAG by first retrieving relevant documents and then guiding the model to reason through the task step-by-step. This could involve a sequence of prompts that allow the model to iteratively refine its response using the retrieved context. |
| How did you manage the interaction between retrieval and generation in the LangChain framework? | The LangChain framework was used to manage the chain between the retrieval and generation components. After receiving the query, the framework invokes the retriever (vector database), fetches relevant documents, and then passes these documents to the LLM to generate a final response. This workflow ensures a seamless transition between retrieval and generation. |

This table format preserves the question-answer structure of the original content while presenting it in a more organized and readable markdown format.



Resources:
- [microsoft / AutoGen / development of LLM applications using multiple agents  ](https://microsoft.github.io/autogen/docs/Getting-Started)
