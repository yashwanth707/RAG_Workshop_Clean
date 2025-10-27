# My RAG System

## Topic:
Data Engineering, Artificial Intelligence, Cybersecurity, Healthcare Analytics, Climate Change

## What I changed:
- **Documents:** 5 PDFs added in `data/`
- **Chunking:** chunk_size=1200, chunk_overlap=200
- **Retrieval:** k=5, fetch_k=10, lambda_mult=0.3

## How to run:
1. Activate environment: rag_env\Scripts\activate

2. Install requirements: pip install -r requirements.txt

3. Run tests:python test_rag_setup.py

4. Launch notebook: jupyter notebook RAG_Demo-venv.ipynb

## Chunking Result:
Tested two configurations:
- 400/50 produced 649 small chunks (more granular but fragmented answers)
- 1200/200 produced 245 larger chunks (fewer but richer in context)

✅ I chose 1200/200 because it gave more coherent and complete answers for conceptual questions.

## Improved retriever parameters
Retrieval: k=5, fetch_k=10, lambda_mult=0.3

## Test questions used:
1. What are the common steps in an ETL data pipeline?
2. How can AI help in predicting health outcomes?
3. What is Call of Duty Mobile?

