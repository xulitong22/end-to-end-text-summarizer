# TextSummarizer
TextSummarizer is an text summarization tool built using Huggingface Transformers and FastAPI. It fine-tunes the Google Pegasus model with the Samsum dataset to generate concise and accurate summaries of text inputs, specifically designed for summarizing conversational data like chats or dialogues.


## Key Folders and Files
- src/TextSummarizer/: Contains the core components and logic for data ingestion, validation, transformation, model training, and evaluation.
- config/: Contains the configuration files for the project.
research/: Contains Jupyter notebooks for research and experimentation (e.g., fine-tuning models, dataset exploration).
- app.py and main.py: Entrypoints for running the FastAPI app and orchestrating the model pipeline.


## Pipeline stage
The project is divided into the following pipeline stages:

- Data Ingestion: Downloads and prepares the dataset.
- Data Validation: Validates the input data for consistency.
- Data Transformation: Preprocesses the data for training.
- Model Training: Fine-tunes the Pegasus model on the Samsum dataset.
- Model Evaluation: Evaluates the model using metrics such as ROUGE.
Each stage is modularized into separate classes, and the pipelines are managed through a configuration manager that ensures flexible access to each stage's configurations.


## Installation
1. Clone the repository: 
```bash
git clone https://github.com/xulitong22/end-to-end-text-summarizer.git
cd TextSummarizer
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Install the project:
```bash
pip install -e .
```


## Usage
### Running the Model Pipeline
To run the model training pipeline, execute the main.py file:
```bash
python main.py
```
This will go through all five stages: data ingestion, data validation, data transformation, model training, and model evaluation.

### FastAPI Web Application
You can start the FastAPI app using the following command:
```bash
python app.py
```
Once the server is running, visit http://127.0.0.1:8000/docs to access the Swagger UI for testing the API.


## Dependencies
This project relies on the following Python packages:

- transformers (with sentencepiece)
- datasets
- evaluate
- sacrebleu
- rouge_score
- py7zr
- pandas
- nltk
- tqdm
- PyYAML
- matplotlib
- torch
- notebook
- python-box
- ensure
- fastapi[standard]


## License
This project is licensed under the MIT License. See the LICENSE file for more details.

