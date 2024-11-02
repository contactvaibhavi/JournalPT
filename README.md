# TODO
## v0 - Generate periodic summary from journal entry

### Components

1.  Chunking 
1.1 No chunking
1.2 Linewise
1.3 Rule-based division - smalltalk, specific to an issue e.g. major new event, reference to past event, follow up on a plan

2. Summarization -
2.1 No prompt - as a default - summarize this/frontend button
2.2 System generated prompt - role based summary - 
2.3 e.g. with focus on one issue from above, with o/p format as given in i/p - see HowWeFeel app format - emotions wheel, reason, event details
2.3.1 Prompt engg
2.3.2 Instruction base fine tuning

3. Database -
3.1 Metadata - postgres(mongo in V1)
3.2 Vector db - for embeddings - pgvector
    (qdrant/FAIS/elastic in v1)
3.3 Jobs - Redis/Kafka - async msg queue - to ingest new text embeddings and
push out to the db with proper pacing
3.4 Results - Precomputed Store for previous results 

4. Text Context for RAG querying - txt/pdf upload as context/prescription plan 

5. UI - v1, No UI - v0
5.1 Postman Curl Collection 
5.2 Data upload - POST API

## v1 - Interactive AI-assisted journalling with user

1.  Flow prompting - prompt user for diary entry
1.1 Fixed structure of diary entry
1.2 Current context-based - full chat vs current conv
1.3 Past context-base
1.4 Action taking outside world - book aptmt for the diet plan/gym plan follow up

2.  Self-selective routing on which one to pick from above 3 types
2.1 rule-based - listen vs speak - if user wants to discontinue the journaling, prompt them to stick
2.2 some other - 
2.3 Temperature/entropy

3.  Output - 
3.1 concatenated as a chat form
3.2 lossless summarization/ paraphrasing in 1st person
3.3 thematic segmentation - segmenting the whole conv as per separate themes

# API Endpoints

1.  Authentication endpoints
1.1 Register User
1.2 Login User
1.3 Logout User
1.4 View/Edit Profile
1.5 extra - end-to-end encryption

2.  Data - CRUD
2.1 Upload previous - txt/image for ocr
2.2 Get by ID of orig conversation/entry
2.3 Search - by metadata/date
2.4 Delete orig convo and all its generated chunks and summarizations
recursively

3.  Generation - text-to-vector and back
3.1 extra - Create chunks
3.2 Generate Embeddings
3.3 Query Embeddings

4.  Processes - LLM calls - text-to-text
4.1 Segmentation
4.2 Summarization
4.3 extra - rule-based routing based on params like temperature, window size


