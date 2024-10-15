# Joint Verification and Refinement of Language Models for Safety-Constrained Planning
A framework that automatically verifies python functions against given temporal logic specifications. This framework is designed to verify Python-based controllers for autonomous systems. A model that captures all possible system behaviors is required.

## Setup
Requirement: Python 3.9 or before

## Instructions

### Plan Verification
1. Copy the generated python function to a local directory `path_to_python_code`.

2. Provide an `LTL.txt` file with your task requirements in the form of linear temporal logic, and a Model.smv file to represent your system in NuSMV.

3. Run the following command:

```bash
$ python main.py \
         --model_path path_to_Model\
      	 --spec_path path_to_LTL\
      	 --code_path path_to_python_code\
```
### Fine-Tuning
We include some fine-tuning data in `finetune/data`, you can replace with your own data.

1. Run `finetune/data_process.ipynb` to obtain a formatted jsonl file `finetune/data/data.jsonl`.

2. Go to [OpenAI Fine-Tuning](https://platform.openai.com/docs/guides/fine-tuning) and follow their instruction to fine-tune model.

3. Follow `code-gen.ipynb` to run the fine-tuned model for plan generation.
