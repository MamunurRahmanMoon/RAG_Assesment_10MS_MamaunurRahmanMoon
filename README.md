# RAG_Assesment_10MS_MamaunurRahmanMoon

# Flow of the Problem Solving (My thought process)

## Step-1: Initially setup a basic RAG pipeline with basic dataloading:

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

## Step-4: Load the extracted text into the RAG pipeline
    