
# My Machine Learning Notes...

This repo is collection of my notes while ML learning journy and working on ML projects.
Please comment if you have any suggestion, find a correction or want to appreciate :-)  

> Follow me on,  [LinkedIn](https://www.linkedin.com/in/vivek-bombatkar/), [Github](https://github.com/vivek-bombatkar), [Kaggle](https://www.kaggle.com/competitions) 

# Index
- [1. Collection of Best End-2-End ML Course / Books.](#10)
- [2. Online Tools for hosting model, mostly free.](#20)
- [3. MLOps (Devops for ML) theory concepts and toolkits.](#30)
- [3.1 ML Patterns and Anti-Patterns ](#31)
- [4. Random Notes and Links on ML good-read.](#40)


# <a name="10"></a>1. Collection of Best End-2-End ML Course / Books.
- [ML from Google](https://developers.google.com/machine-learning/crash-course)
- [ML from AmazonWebServices](https://www.aws.training/LearningLibrary?filters=classification%3A30&filters=language%3A1&filters=classification%3A7&tab=view_all)
- [ML from MicrosoftAzure](https://docs.microsoft.com/en-us/learn/browse/?roles=data-scientist&products=azure)
  - [Data-science-for-beginners from Azure](https://docs.microsoft.com/en-us/azure/machine-learning/studio/data-science-for-beginners-the-5-questions-data-science-answers)
- [ML from IBM](https://www.ibm.com/de-de/analytics/machine-learning)
  - [ML for Dummies](https://www.ibm.com/downloads/cas/GB8ZMQZ3)
- [data-flair - machine-learning-tutorial](https://data-flair.training/blogs/machine-learning-tutorial/)
- [cognitiveclass - machine-learning-with-python](https://cognitiveclass.ai/courses/machine-learning-with-python/)    

- [PythonDataScienceHandbook](https://jakevdp.github.io/PythonDataScienceHandbook/)   
- [Hands-On Machine Learning with Scikit-Learn and TensorFlow](http://index-of.es/Varios-2/Hands%20on%20Machine%20Learning%20with%20Scikit%20Learn%20and%20Tensorflow.pdf)


# <a name="20"></a>2. Online Tools for hosting ML model, mostly free.
- [Google colab](https://colab.research.google.com/notebooks/welcome.ipynb#scrollTo=rTX3heEtu0b2)
- [Kaggle](kaggle.com)
- [notebooks azure](https://notebooks.azure.com/)
- [studio azureml - No Code ML](https://studio.azureml.net/)

# <a name="30"></a>3. MLOps (DevOps for ML) theory concepts and toolkits.
- ***DevOps vs MLOps***
  - DevOps: CI + CD
  - MLOps: CI + CD + [ CT + CM + CV ]
- [Azure MLOps:  evolve-your-devops-practices](https://docs.microsoft.com/en-us/learn/paths/evolve-your-devops-practices/)
  - https://docs.microsoft.com/en-us/learn/modules/assess-your-development-process/4-assess-process-efficiency?source=learn
    - customer value metrics
      ![img](https://docs.microsoft.com/en-us/learn/azure-devops/assess-your-development-process/media/4-vsm-whiteboard2.png)
     - Azure ML DSK pipeline
      ![img](https://github.com/microsoft/MLOps/raw/master/media/ml-lifecycle.png)
  - https://github.com/microsoft/MLOps
  - https://medium.com/@theadisoni/mlops-in-azure-f6e7c006fe0e
  - [MLOps framework to upscale an Azure Machine Learning lifecycle](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/mlops/mlops-technical-paper)
    - ![img](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/mlops/media/mlops-conceptual-model.png)
  - [Machine Learning Operations maturity model - five levels of technical capability](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/mlops/mlops-maturity-model)
  - [What is MLOps?](https://docs.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment)
  
  
  
  
- [GCP MLOps: devops](https://cloud.google.com/devops)
  - https://cloud.google.com/solutions/devops/devops-process-work-visibility-in-value-stream
  - https://cloud.google.com/solutions/machine-learning/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
    - MLOps level 0: Manual process
      - ![img](https://cloud.google.com/solutions/images/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning-2-manual-ml.svg)
     - MLOps level 1: ML pipeline automation
      - ![img](https://cloud.google.com/solutions/images/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning-3-ml-automation-ct.svg)
     - MLOps level 2: CI/CD pipeline automation
      - ![img](https://cloud.google.com/solutions/images/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning-4-ml-automation-ci-cd.svg)
      
    
    
- [IBM MLOps: refarch-ml-ops](https://github.com/ibm-cloud-architecture/refarch-ml-ops/blob/master/README.md)
  - ML Ops steps and persona
  - ![img](https://github.com/ibm-cloud-architecture/refarch-ml-ops/raw/master/images/MLOpsArch0.5.png)

- [build-release-ci-cd](https://github.com/classicboyir/build-release-ci-cd)
  - ![img](https://github.com/classicboyir/build-release-ci-cd/raw/master/assets/MLOpsArchFlow.jpg)

- [team-data-science-process tasks-by-roles](https://docs.microsoft.com/en-us/azure/machine-learning/team-data-science-process/roles-tasks)
  - ![img](https://docs.microsoft.com/en-us/azure/machine-learning/team-data-science-process/media/overview/tdsp-tasks-by-roles.png)
  
- [altexsoft MLOps](https://www.altexsoft.com/blog/mlops-methods-tools/)
  - ![img](https://content.altexsoft.com/media/2020/07/word-image-3.png)
 



# <a name="31"></a>3.1 ML Patterns and Anti-Patterns.

- http://www.washi.cs.waseda.ac.jp/wp-content/uploads/2019/12/IEEE_Software_19__ML_Patterns.pdf
  - Patterns
    - Data Lake: The data ranging from structured data to unstructured data should be stored as “raw” as possible and the centralized data repository should allow parallel analyses of different kinds and with different frameworks.
    - Distinguish Business Logic from ML Models : Separate the business logic and the inference engine, loosely coupling the business logic and ML-specific dataflows.
    - Microservice Architecture : Data scientists working with or providing ML frameworks can make these frameworks available through microservices
    - Data-AlgorithmServingEvaluator : Separate the following like MVC for ML: data (data source and data preparator), algorithm(s), serving, and evaluator.
    - Event-driven ML Microservices: Construct pipelines by chaining together multiple microservices, each of which listens for the arrival of some data and performs its designated task
    - Lambda Architecture: The batch layer keeps producing views at every set batch interval while the speed layer creates the relevant real-time/speed views. The serving layer orchestrates the query by querying both the batch and speed layer, merges it
    - Parameter-Server Abstraction : Distribute both data and workloads over worker nodes, while the server nodes maintain globally shared parameters, which are represented as vectors and matrices
    - Daisy Architecture: Utilize Kanban, scaling, and microservice to realize pull-based, automated, on-demand, and iterative processes.
    - Gateway Routing Architecture: Install a gateway before a set of applications, services, or deployments and use application layer routing requests to the appropriate instance.
    - Kappa Architecture: Support both real-time data processing and continuous reprocessing with a single stream processing engine.
    - Closed-Loop Intelligence : Connect machine learning to the user and close the loop. Design clear interactions along with implicit and direct outputs.
    - Federated Learning : Employ Federated Learning, which enables mobile phones to collaboratively learn a shared prediction model while keeping all the training data on the device.
    - ML Versioning: Record the ML model structure, training data, and training system to ensure a reproducible training process
    - Wrap Black-Box Packages into Common APIs: Wrap black-box packages into common APIs to make supporting infrastructure more reusable and to reduce the cost of changing packages
    - Test Infrastructure Independently from ML: Ensure that the infrastructure is testable and the learning parts of the system are encapsulated so that everything around it can be tested.
    - Handshake (Hand Buzzer): Create a handshake normalization process, regularly check for significant changes, and send ALERTS
    - Isolate and Validate Output of Model : Encapsulate ML models within rule-base safeguards and use redundant and diverse architecture that mitigates and absorbs the low robustness of ML models
    - Canary Model: Run the canary inference pipeline in parallel with the primary inference pipeline to monitor prediction differences
    - Decouple Training Pipeline from Production Pipeline: Physically isolate different workloads to different machines. Then optimize the machine configurations and the network usage
    - Descriptive Data Type for Rich Information: Design a robust system, where the model parameter knows if it is a log-odds multiplier or a decision threshold, and a prediction knows information about the model.
    - Design Holistically about Data Collection and Feature Extraction: Avoid pipeline jungles by thinking holistically about data collection and feature extraction that can dramatically reduce ongoing costs.
    - Reexamine Experimental Branches Periodically: Reexamine each experimental branch periodically to see what can be removed to eliminate glue code and pipeline jungles.
    - Reuse Code between Training Pipeline and Serving Pipeline: Reuse code between training pipeline and serving pipeline by preparing objects that store results in an understandable way for humans.
    - Separation of Concerns and Modularization of ML Components : Decouple at different levels of complexity from simplest to most complex.
    - Secure Aggregation : Encrypt data from each mobile device in Federated learning and calculate totals and averages without individual examination.
  - Anti-patterns
    - Big Ass Script Architecture : When all code is placed in one big ass script, it becomes difficult to reuse in future analysis, understand how it works, and debug.
    - Abstraction Debt: For distributed learning, widely accepted abstractions are lacking
    - Dead Experimental Codepaths: The code-paths accumulated by individual changing can create a growing debt due to the increasing difficulties of maintaining backward compatibility
    - Glue Code: Glue code is costly in the long term because it tends to freeze a system to the peculiarities of a specific package.
    - Multiple Language Smell : Using multiple languages increases the cost of effective testing and can increase the difficulty of transferring ownership to other individuals.
    - Pipeline Jungles : The system to prepare data in an ML-friendly format may become a pipeline jungle, and managing these pipelines is difficult and costly
    - Plain-OldData Type Smell : The rich information used and produced by ML systems is often encoded with plain data types like raw floats and integers
    - Undeclared Consumers: Undeclared consumers are dangerous because they create a hidden tight coupling of model MA to other parts of the stack.

- https://medium.com/@lakshmanok/machine-learning-design-patterns-58e6ecb013d7
  - Transform: Moving an ML model to production is much easier if you keep inputs, features, and transforms separate
  - Checkpoints: Saving the intermediate weights of your model during training provides resilience, generalization, and tuneability
  - Virtual epochs: Base machine learning model training and evaluation on total number of examples, not on epochs or steps
  - Keyed predictions: Export your model so that it passes through client keys
  - Repeatable sampling: use the hash of a well distributed column to split your data into training, validation, and testing

- https://github.com/mercari/ml-system-design-pattern
  -  Serving patterns : The serving patterns are a series of system designs for using machine learning models in production workflow.
  - QA patterns: Pattens to evaluate model as well as prediction server.
  - Training patterns: Patterns to construct training pipeline.
  - Operation patterns: The operation patterns contain configuration, logging, monitoring and alerting system designs for machine learning system.
  - Lifecycle patterns: The lifecycle patterns contain composition of several patterns to realize actual ML system with operation.

- https://storage.googleapis.com/pub-tools-public-publication-data/pdf/43146.pdf
  

# <a name="40"></a>4. Random Notes and Links on ML good-read.

- [todo]Azure Functions for Regression Model that need no Training (NO CT Continuous Training needed)
- Storing the ML models. [towardsdatascience.com/guide-to-file-formats-for-machine-learning](https://towardsdatascience.com/guide-to-file-formats-for-machine-learning-columnar-training-inferencing-and-the-feature-store-2e0c3d18d4f9)
  - Whats in there, actually get stored?
  - storage File formats: .pb, .onnx, .pkl, .mlmodel, .zip, .pmml, .pt
    - TensorFlow saves models as protocol buffer files, with a .pb file extension. 
    - Keras saves models natively as .h5 file. 
    - Scikit-Learn saves models as pickled python objects, with a .pkl file extension. 
    - An older format for model serving based on XML, predictive model markup language (.pmml), is still usable on some frameworks, such as Scikit-Learn.
    - SparkML models that can be saved in MLeap file format and served in real-time using a MLleap model server (files are packaged in .zip format)
    -  YAML that is used to package models as part of the MLFlow framework
  - https://mlinproduction.com/ml-metadata/
    - What Metadata should you capture during training?
      - Data, Model, MODEL TYPE, FEATURE PREPROCESSING STEPS, HYPERPARAMETERS, Metrics, Context
 ![img](https://miro.medium.com/max/875/0*H7CB1kGuukCv2rcK.png)
 ![img](https://miro.medium.com/max/783/0*0MZyp6CdafGNrnUr.png)
 ![img](https://miro.medium.com/max/875/0*phrNmrrcyoX-lnIE.png)
    
- [project structure for doing and sharing data science work](https://drivendata.github.io/cookiecutter-data-science/)

  
- http://queirozf.com/entries/matplotlib-pylab-pyplot-etc-what-s-the-different-between-these
- [All Articals from him](https://medium.com/@cdossman)  
  - https://medium.com/ai%C2%B3-theory-practice-business/best-method-to-learn-essential-machine-learning-skills-fast-533e30f3023d  
  - https://medium.com/ai%C2%B3-theory-practice-business/top-6-cheat-sheets-novice-machine-engineers-need-5ea43d1be3de  
  - https://medium.com/ai%C2%B3-theory-practice-business/the-engineers-guide-to-machine-learning-30a3d54bea4e  
- [WEKA](https://www.cs.waikato.ac.nz/ml/index.html)  
- PCA, Principal Component Analtsis  
  - https://www.youtube.com/watch?v=8LwCPpNtggM  
  - http://setosa.io/ev/principal-component-analysis/  

- Correlation and Pearson vs Spearman.  
  - https://support.minitab.com/en-us/minitab-express/1/help-and-how-to/modeling-statistics/regression/supporting-topics/basics/a-comparison-of-the-pearson-and-spearman-correlation-methods/

- [Cross_Industry_Standard_Process_for_Data_Mining](https://en.wikipedia.org/wiki/Cross_Industry_Standard_Process_for_Data_Mining)
  - ![img](https://github.com/awslabs/amazon-sagemaker-mlops-workshop/raw/master/imgs/crisp.png)
- ML Design Patterns & Anti Patterns
  - [ml-system-design-pattern](https://github.com/mercari/ml-system-design-pattern)
  - [machine-learning-design-patterns](https://medium.com/@lakshmanok/machine-learning-design-patterns-58e6ecb013d7)
  - [Paper - Machine Learning Architecture and Design Patterns](http://www.washi.cs.waseda.ac.jp/wp-content/uploads/2019/12/IEEE_Software_19__ML_Patterns.pdf)
    - ![img](https://image.slidesharecdn.com/iwesep19mlpatterns-en-20191214-public-191214085940/95/studying-software-engineering-patterns-for-designing-machine-learning-systems-15-638.jpg?cb=1576314019)
- Design Thinking in Data Science
  - [a-design-thinking-mindset-for-data-science](https://towardsdatascience.com/a-design-thinking-mindset-for-data-science-f94f1e27f90)
    - ![img](https://miro.medium.com/max/875/0*BToFTW9JaZzv3tqj)
  - [powering-data-science-with-design-thinking](https://faculty.ai/blog/powering-data-science-with-design-thinking/)
    - ![img](https://faculty.ai/wp-content/uploads/2019/11/design-thinking-101-768x777.png)
    - ![img](https://faculty.ai/wp-content/uploads/2019/11/diverge-converge.png)
  - [Ahsan Ijaz blog on ML](https://ahsanijaz.github.io/2018-09-04-less_travel/)

- [ml-ops-machine-learning-as-an-engineering-discipline](https://towardsdatascience.com/ml-ops-machine-learning-as-an-engineering-discipline-b86ca4874a3f) 
  - ![img](https://miro.medium.com/max/1250/1*hlukfeyP-I209WBEMsBSEA.png)
    
- Azure ML git repos
  - [The cookiecutter template using Azure Machine Learning](https://github.com/microsoft/DistributedDeepLearning)
  - [azureml-template](https://github.com/Azure/azureml-template)
  - [azureml-examples](https://github.com/Azure/azureml-examples)
  - [ml-template-azure](https://github.com/machine-learning-apps/ml-template-azure)
  
- Unit Test for ML
  - [AI SUmmer: unit-test-deep-learning](https://theaisummer.com/unit-test-deep-learning/) 
  - [oreilly: Test-Driven Machine Learning](https://www.oreilly.com/library/view/thoughtful-machine-learning/9781449374075/ch01.html)
  - [Mocking of Unit Tests for Machine Learning](https://tech.comtravo.com/testing/Testing_Machine_Learning_Models_with_Unittest/)
