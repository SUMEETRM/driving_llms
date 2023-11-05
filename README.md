# Driving Conventions and Failure Modes

# Project Title

Summary from Lewis: The idea here would be to fine-tune two models on data from different distributions (such as driving conventions and norms from two different countries) and then put them in a situation where this difference could lead to bad outcomes (such as a driving scenario where whose right of way is not entirely clear).

## Usage

Before running the fine-tuning scripts, set your OpenAI API key in your environment:

export OPENAI_API_KEY=your_api_key

Then, run the finetuning script for the desired region:

python finetuning.py usa # or 'india' for the other region

After fine-tuning the models, use the model IDs to run experiments:

python run_experiment.py "model_id_for_usa" "model_id_for_india" --iterations 100

Replace `model_id_for_usa` and `model_id_for_india` with the actual model IDs you get after fine-tuning.

## Experiment Documentation

For detailed information about the experiment design and methodology, refer to the [experiment outline](https://docs.google.com/document/d/1NU8q3mj8AeFOaNnXSJtApRSz6Eavadf3Z_ZioEJA6KI/edit?usp=sharing).

## Experiment Structure

Below is an image illustrating the experiment structure:

<a href="https://ibb.co/993Jk2M"><img src="https://i.ibb.co/rGfgRMW/Screenshot-2023-11-05-at-10-23-54-AM.png" alt="Experiment Structure" border="0"></a>
