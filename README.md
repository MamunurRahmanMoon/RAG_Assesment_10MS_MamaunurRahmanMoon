# RAG_Assesment_10MS_MamaunurRahmanMoon

# Flow of the Problem Solving (My thought process)

## Step-1: Initially setup a basic RAG pipeline with basic dataloading

    > Verdict:

    - Failed to get answer

## Step-2: Implemented 'Multi-Query' query transformation

    > Verdict:

    - Failed to get answer
    - But, got some relevant context

## Step-3: Extracted Bangla text from PDF using Mistral OCR

    - After so many trial error on different methodology for extracting bangla text and the format correctly for better chunking

    - I used Mistral OCR beacause its accuracy and speed
    - Now have to load the extracted 'markdown'  into the RAG pipeline

    > Verdict:

    - Extracted all the text with good accuracy with Mistral AI; but bengali numbers were mis interpreted as Hindi number
    - Overall, the extracted text is good enough for the task and extraction was fast

## Step-4: Tried multi-Query translation using RecursiveTextSplitter

    > Verdict:

    - Able to answer one question:
         "কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?"
         => 'মামা'

    - Failed to get answers mostly

## Step-5: Implemented *RAPTOR* Indexing

    > Verdict:
    
    - Much slower and complex
    - Same result as before (Not efficient)
    - Able to answer one question:
         "কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?"
         => 'মামা'

    - Failed to get answers mostly

# Submission Requirements

## To setup the environment

    1. Create a virtual environment
    2. Install the requirements
    3. Create a .env file and add the API keys
    4. Run the notebook "5_final_notebook.ipynb"

## Used tools,library,package

    1. Langchain
    2. Google Generative AI
    3. Mistral AI
    4. Unstructured
    5. ChromaDB
    6. FastAPI
    7. Uvicorn

## Sample queries and outputs (Bangla & English)

    1. কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?
        => 'মামা'

    2. Who is Anupam's godfather?
        => 'Shambhunath Babu'

    3. What is Anupam's nickname?
        => 'Chhota Anupam'

## API Documentation (Not implement)

    > Couldn't implement because of problem with gemini api key validation
    > But surely will try

## Evaluation Matrix

    > Using Cosine Similarity of embedding of answer and context

'''
    [{'question': 'কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?',
  'generated_answer': 'মামাকে',
  'expected_answer': 'বিধাতাকে',
  'groundedness_score': 0.864,
  'exact_match': False},
 {'question': '‘আত্মার আনন্দ’ কীসের প্রতীক?',
  'generated_answer': 'প্রদত্ত তথ্যে এই প্রশ্নের উত্তর নেই।',
  'expected_answer': 'মানসিক মুক্তির',
  'groundedness_score': 0.9334,
  'exact_match': False},
 {'question': 'রবীন্দ্রনাথ কোন রচনায় প্রকৃতিকে শিক্ষক বলেছেন?',
  'generated_answer': 'প্রদত্ত তথ্যে এই প্রশ্নের উত্তর নেই।',
  'expected_answer': 'শিক্ষক ও প্রকৃতি',
  'groundedness_score': 0.9241,
  'exact_match': False}]

'''

## Must Answer following Questions

> What method or library did you use to extract the text, and why? Did you face any formatting challenges with the PDF content?

Answer: I used Mistral AI for extracting the text from the PDF. I faced some challenges with the PDF content, but Mistral AI was able to extract the text with good accuracy. I also faced some challenges with the format of the text, but I was able to fix it by using some regular expression.

> What chunking strategy did you choose (e.g. paragraph-based, sentence-based, character limit)? Why do you think it works well for semantic retrieval?
Answer: I used RecursiveCharacterTextSplitter with custom split point. I think it works well for semantic retrieval because it is able to capture the meaning of the text. Also, as I converted the pdf into Markdown, I was able to use some custom split point which helped me to get better chunking.

> What embedding model did you use? Why did you choose it? How does it capture the meaning of the text?
Answer: I used GoogleGenerativeAIEmbeddings. I chose it because it is able to capture the meaning of the text. It uses the embedding model "models/embedding-001" which is able to capture the meaning of the text.

Most importantly it comes with a Free-plan using gemini-api thats why it seemed good option. But, other embedding model like HuggingFaceEmbeddings could have been used as well.

> How are you comparing the query with your stored chunks? Why did you choose this similarity method and storage setup?
Answer: I used ChromaDB as the vector store. I chose it because it is able to store the embedding of the text and able to retrieve the most similar text. I used cosine similarity to compare the query with the stored chunks. I chose it because it is able to capture the meaning of the text.

> How do you ensure that the question and the document chunks are compared meaningfully? What would happen if the query is vague or missing context?
Answer: For tracing I primarilly used Langsmith. But to answer this question, I didnt established any 'Guard-railing'.

        But surely will set-up later, if it is required for this assessment. I can do this if given time for a day.

> Do the results seem relevant? If not, what might improve them (e.g. better chunking, better embedding model, larger document)?
> Answer: The results are not always relevant. I think better chunking and better embedding model can improve the results. I also think using larger document can help.

To be specific, I tried different techniques, which you can see in the 'notebooks' directory. Also,tried different chunking technique, but the results were not satisfactory. In fact results were worst when I used 'SemanticChunker', which is recommended by Langchain.

Even combined different splitter, but the results were not satisfactory. I think the main problem is with the embedding model. Making the **extraction* more accurate can help. Because the OCR could not extract the text properly.
