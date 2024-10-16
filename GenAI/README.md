
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




| Concept | Explanation |
|---------|-------------|
| Cost per million input tokens | The model charges **$3** for processing every **1 million input tokens**. Input tokens are the tokens sent to the model as part of the request (e.g., user queries or prompts). |
| Cost per million output tokens | The model charges **$15** for every **1 million output tokens** generated in response to the input. Output tokens refer to the tokens generated by the model as part of the response (e.g., chatbot replies). |
| Token | Tokens are pieces of words. For example, "ChatGPT is great" might be split into 4 tokens: "Chat", "GPT", "is", "great". Tokens could be words, parts of words, or punctuation marks. |
| 200K token context window | The model has a **200,000-token context window**, meaning it can handle up to 200,000 tokens in memory for a single input/output session. This includes both the input tokens and output tokens, allowing the model to "remember" a long conversation or document. |


# the factors to consider when selecting a language model. 

| Factor | Description |
|--------|-------------|
| 1. Model Performance | - Quality of responses for specific use cases<br>- Specialization for domains (e.g., medical, legal, coding)<br>- Performance on standard benchmarks (e.g., SQuAD, GLUE, MMLU) |
| 2. Latency and Speed | - Response time for real-time applications<br>- Inference time and trade-offs with accuracy<br>- Scalability for handling large numbers of requests |
| 3. Model Size (Parameters) | - Smaller models: faster, cost-effective, but may lack depth<br>- Larger models: better results, but more resource-intensive |
| 4. Compute and Hardware Requirements | - GPU/CPU needs for different model sizes<br>- RAM and storage requirements<br>- Optimizations like quantization or distillation |
| 5. Fine-Tuning and Adaptability | - Capability for domain-specific fine-tuning<br>- Data requirements for customization<br>- Training budget considerations |
| 6. Tokenization and Language Support | - Multilingual support for global user bases<br>- Tokenization efficiency for various languages and domains |
| 7. Privacy and Data Security | - On-premises vs. cloud deployment options<br>- Compliance with regulations (e.g., GDPR, HIPAA)<br>- Data retention policies |
| 8. Integration and Ecosystem Support | - Availability of APIs and SDKs<br>- Access to pre-trained models<br>- Integration with existing cloud services |
| 9. Cost-Effectiveness | - API pricing for input and output tokens<br>- Compute costs for on-premises deployment<br>- Open-source vs. commercial model considerations |
| 10. Community and Support | - Strength of community resources and support<br>- Vendor support for commercial models<br>- Availability of pre-built tools and libraries |
| 11. Energy Efficiency and Sustainability | - Power consumption considerations<br>- Availability of energy-efficient models or initiatives |
| 12. Explainability and Interpretability | - Model transparency for critical applications<br>- Bias and fairness considerations |
| 13. Task-Specific Models | - Availability of pre-trained models for specific domains or tasks |
| 14. Longevity and Future-Proofing | - Frequency of model updates<br>- Provider's future roadmap and continued support |


# **Prompt Engineering techniques** commonly used with large language models like GPT-3, GPT-4, and other similar models:

| **Technique** | **Description** |
|---------------|-----------------|
| **Zero-Shot Prompting** | Asking the model to perform a task without providing any examples. The model relies on its pre-trained knowledge. |
| **Few-Shot Prompting** | Providing a few examples of the task (input-output pairs) in the prompt to guide the model’s output. This helps the model understand the task with minimal examples. |
| **One-Shot Prompting** | A special case of few-shot prompting where only one example is provided to guide the model's response. |
| **Chain-of-Thought Prompting** | A technique where the model is prompted to generate intermediate reasoning steps before reaching a final answer. This improves the model’s performance in tasks that require logical reasoning or problem-solving. |
| **Instruction-Based Prompting** | Giving explicit instructions to the model on how to respond or behave for a particular task. For example, “Explain this concept in simple terms” or “Generate a summary of this text.” |
| **CoT + Self-Consistency** | Similar to chain-of-thought prompting, but here multiple reasoning paths are generated. The final answer is chosen based on the most consistent reasoning path. |
| **Reframing** | Changing the prompt's wording or structure without changing its meaning to influence how the model responds. This can help steer the model toward more accurate or creative outputs. |
| **Multi-Turn Prompting** | Asking the model to respond to multiple prompts in sequence, which simulates a conversational or interactive problem-solving scenario. |
| **Output Priming** | Providing part of the expected answer or formatting the output in a specific way to guide the model toward a specific type of response (e.g., bulleted lists, steps, or tables). |
| **Role-Playing** | Assigning the model a specific role or persona to guide its responses, such as “You are a teacher,” “You are a data scientist,” or “You are a customer service agent.” |
| **Dynamic Prompting** | Dynamically changing the prompt based on the model's previous responses to make the interaction more adaptive and context-aware. |
| **Question-Answer Prompting** | Asking the model questions that lead to a final conclusion. Each question guides the model closer to the desired answer through a step-by-step process. |
| **Contextual Prompting** | Including relevant context (e.g., background information or constraints) in the prompt to ensure the model responds in a manner that is aligned with that context. |
| **Task Specification** | Clearly specifying the task or goal in the prompt. For instance, "Translate this text into French" or "Summarize this article in three bullet points." |
| **Iterative Prompting** | Iteratively refining the prompt based on the model's responses, often involving multiple interactions to get closer to the desired output. |
| **Prefix Prompting** | Adding a prefix or hint to the input to influence the model’s behavior. For example, adding “Write a formal letter” before a text to generate a more formal response. |
| **Temperature Control in Prompting** | Adjusting the **temperature** parameter to control randomness or creativity in responses (higher values for more creative, lower values for deterministic responses). |
| **Reverse Prompting** | Presenting the expected output first, and asking the model to reverse-engineer or explain how it arrived at that conclusion. This helps with complex problem-solving tasks. |
| **Prompt Chaining** | Breaking down a complex task into a series of smaller prompts, with each prompt building on the output of the previous one. This is useful for multi-step tasks. |
| **Demonstration-Based Prompting** | Providing detailed, step-by-step demonstrations of the task, sometimes including explanations, before asking the model to perform the task. |
| **Meta-Prompting** | Instructing the model on how to generate better prompts or adjust its output (i.e., giving instructions about how to give instructions). |
| **Paraphrasing Prompts** | Rewriting the same prompt in different ways to elicit a variety of responses, particularly useful for ambiguous tasks or creative outputs. |
| **Prompt Ensembling** | Using multiple prompts with slight variations, aggregating the results, or choosing the best response among them to improve reliability. |
| **Active Prompting** | Asking the model questions in the prompt itself that it needs to answer before generating the final response. This makes the model think actively as it generates its final output. |
| **Prompt Constraints** | Including explicit constraints in the prompt, such as character limits, formality level, or specific response formatting (e.g., “Answer in 100 words or less”). |
| **Few-Shot In-Context Learning** | Providing task-specific data within the prompt itself and leveraging it for in-context learning to adapt to a particular use case without fine-tuning. |
| **Template-Based Prompting** | Using predefined templates to structure the input in a way that aligns with the model’s strengths, ensuring more accurate outputs (e.g., pre-defined questions or sentence structures). |



Resources:
- [microsoft / AutoGen / development of LLM applications using multiple agents  ](https://microsoft.github.io/autogen/docs/Getting-Started)
