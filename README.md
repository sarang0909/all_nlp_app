# all_nlp_app : Almost all NLP concepts in a single use case


https://user-images.githubusercontent.com/31824267/202073219-57c60dd7-5557-42a9-b2d2-98f5011eb48d.mp4



## About  
This is a project developed to create a use case where multiple NLP concepts are integrated.

I've implemented many NLP techniques individually. You can check their corresponding articles and repo.     

I explored multiple techniques, libraries in each of these projects.
Then, I selected a single best method/model from each of these projects and created a use case where all of them are assembled.


### Requirement

Create an application where user can search for entity(user query) in news articles(knowledge base)
Relevant articles fetched should show sentiment, topics, custom NER entities, knowledge graph
Use best practices in MLOps to develop project. A project quality should be production ready.     
   
### Implementation   
1.Data Collection    
2.Data Cleaning     
3.Data Annotation     
4.Text Classification    
5.Coreference Resolution       
6.Named Entity Recognition       
7.Entity Linking      
8.Relationship Extraction       
9.Knowledge Graph Creation     
10.Searching      
11.CI/CD     

1.<a href="https://github.com/sarang0909/news_api">Data Collection</a>     
Collected news articles.    
2.<a href="https://pypi.org/project/nlp-text-cleaner/">Data Cleaning</a>    
created nlp text cleaning library and published on Pypi    
3.Data Annotation:     
Used doccano for annotation.  
4.<a href="https://github.com/sarang0909/text_classification_api">Text Classification</a>   
Classify text into POSITIVE,NEGATIVE,NEUTRAL     
5.<a href="https://github.com/sarang0909/coreference_resolution_api">Coreference Resolution</a>  
Convert pronouns to their original nouns  
6.<a href="https://github.com/sarang0909/custom_ner_api">Named Entity Recognition</a>  
Sometimes you 'll need only certain entities types . We can extract default entities like NAME,PERSON etc from many available libraries or we can also build our own NER model. I've created a project to build custom NER-PERSON,ORG,PLACE,ROLE.  
7.Entity Linking    
We can get different words/nouns for same entity. Example, U.S,United States of America,America. All these should be considered as one entity. We can achieve this by getting their root id if we have some knowledge base. Here, we are going to use Wikipedia knowledge. So, many time entity linking is also called as wikification.
8.Relationship Extraction     
It means fetching relationships in text.      
9.<a href="https://github.com/sarang0909/knowledge_graph_api">Knowledge Graph Creation</a>     
10.<a href="https://github.com/sarang0909/semantic_search_api">Searching</a>       
Used elasticsearch to fetch relevant news article based on input query.     
11.<a href="https://github.com/sarang0909/code_template">Code structure</a>, <a href="https://medium.com/@sarang0909.bds/ci-cd-for-ml-projects-34f179b064b2">CI/CD</a>      
Used code template from my another project which is based on standard coding practices.Used circleci,docker for CI/CD.         


### Inference   
Streamlit application

### Testing     
Unit test cases are written   

### Deployment 
Deployment is done locally using docker.   


## Code Oraganization   
Like any production code,this code is organized in following way:   
1. Keep all Requirement gathering documents in docs folder.       
2. Write and keep inference code in src/inference.   
3. Write Logging and configuration code in src/utility.      
4. Write unit test cases in tests folder.<a href="https://docs.pytest.org/en/7.1.x/">pytest</a>,<a href="https://pytest-cov.readthedocs.io/en/latest/readme.html">pytest-cov</a>    
5. Write performance test cases in tests folder.<a href="https://locust.io/">locust</a>     
6. Build docker image.<a href="https://www.docker.com/">Docker</a>  
7. Use and configure code formatter.<a href="https://black.readthedocs.io/en/stable/">black</a>     
8. Use and configure code linter.<a href="https://pylint.pycqa.org/en/latest/">pylint</a>     
9. Use Circle Ci for CI/CD.<a href="https://circleci.com/developer">Circlci</a>    
 
Clone this repo locally and add/update/delete as per your requirement.   
 
## Project Organization


├── README.md         		<- top-level README for developers using this project.    
├── pyproject.toml         		<- black code formatting configurations.    
├── .dockerignore         		<- Files to be ognored in docker image creation.    
├── .gitignore         		<- Files to be ignored in git check in.    
├── .circleci/config.yml         		<- Circleci configurations       
├── .pylintrc         		<- Pylint code linting configurations.    
├── Dockerfile         		<- A file to create docker image.    
├── environment.yml 	    <- stores all the dependencies of this project    
├── main_streamlit.py 	    <- A main file to run API server.  
├── src                     <- Source code files to be used by project.    
│       ├── inference 	        <- model output generator code   
│       ├── training 	        <- model training code  
│       ├── utility	        <- contains utility  and constant modules.   
├── logs                    <- log file path   
├── config                  <- config file path   
├── docs               <- documents from requirement,team collabaroation etc.   
├── tests               <- unit and performancetest cases files.   
│       ├── cov_html 	        <- Unit test cases coverage report    

## Installation
Development Environment used to create this project:  
Operating System: Windows 10 Home  

### Softwares
Anaconda:4.8.5  <a href="https://docs.anaconda.com/anaconda/install/windows/">Anaconda installation</a>   
 

### Python libraries:
Go to location of environment.yml file and run:  
```
conda env create -f environment.yml
```
 

## Usage
1. Start Streamlit application  
2. Run:
  ``` 
      conda activate all_nlp_app  
      streamlit run main_streamlit.py 
  ```  
![alt text](docs/streamlit_first.jpg?raw=true)
![alt text](docs/streamlit_second.jpg?raw=true)
![alt text](docs/streamlit_third.jpg?raw=true)

 
### Unit Testing
1. Go inside 'tests' folder on command line.
2. Run:
  ``` 
      pytest -vv 
      pytest --cov-report html:tests/cov_html --cov=src tests/ 
  ```
 
### Performance Testing
1. Open 2 terminals and start main application in one terminal  
  ``` 
      python main.py 
  ```

2. In second terminal,Go inside 'tests' folder on command line.
3. Run:
  ``` 
      locust -f locust_test.py  
  ```

### Black- Code formatter
1. Go inside 'all_nlp_app' folder on command line.
2. Run:
  ``` 
      black src 
  ```

### Pylint -  Code Linting
1. Go inside 'all_nlp_app' folder on command line.
2. Run:
  ``` 
      pylint src  
  ```

### Containerization
1. Go inside 'all_nlp_app' folder on command line.
2. Run:
  ``` 
      docker build -t myimage .  
      docker run -d --name mycontainer -p 5000:5000 myimage         
  ```


### CI/CD using Circleci
1. Add project on circleci website then monitor build on every commit.


### Note   
src/models folder is empty because of their size. You can build the models or contact me for sharingthe models.      

## Contributing
Please create a Pull request for any change. 

## License


NOTE: This software depends on other packages that are licensed under different open source licenses.

