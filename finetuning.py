import os
import time
import openai
import argparse

def create_file_for_finetuning(region):
    filename = f'finetuning_{region}.jsonl'
    file = openai.File.create(file=open(filename, "rb"), purpose='fine-tune')
    print(f"File created: {file.id}")
    return file.id

def fine_tune_model(file_id):
    job = openai.FineTuningJob.create(training_file=file_id, model="gpt-3.5-turbo")
    print(f"Fine-tuning job started: {job.id}")
    return job.id

def retrieve_and_check_status(job_id):
    while True:
        job = openai.FineTuningJob.retrieve(job_id)
        status = job.status
        print(f"Job status: {status}")
        if status == 'succeeded':
            print(f"Fine-tuned model: {job.fine_tuned_model}")
            break
        elif status in ['failed', 'cancelled']:
            print("An error occurred during fine-tuning.")
            if job.error:
                print(f"Error message: {job.error['message']}")
            else:
                print("No error message provided.")
            break
        time.sleep(60)

def main(region):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("The OPENAI_API_KEY environment variable has not been set.")
    
    # Start the fine-tuning process
    file_id = create_file_for_finetuning(region)
    job_id = fine_tune_model(file_id)
    retrieve_and_check_status(job_id)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fine-tune models based on the region.")
    parser.add_argument("region", type=str, choices=['usa', 'india'], help="Region to fine-tune the model for (usa/india).")
    args = parser.parse_args()

    main(args.region)


# USAGE
# First, set your OpenAI API key in the environment variable:
# export OPENAI_API_KEY=your_api_key
# Then run the script for the desired region:
# python finetuning.py usa  # or 'india' for the other region
