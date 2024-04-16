# Safety-Constrained Code Generation
A framework that automatically verifies python functions against given temporal logic specifications. This framework is designed to verify Python-based controllers for autonomous systems. A model that captures all possible system behaviors is required.

## Setup
Requirement: Python 3.11

## Instructions
1. Copy the python function to a local directory `path_to_python_code`.

2. Provide an LTL.txt file with your task requirements in the form of linear temporal logic, and a Model.smv file to represent your system in NuSMV.

3. Run the following command:

```bash
$ python main.py \
         --model_path path_to_Model\
      	 --spec_path path_to_LTL\
      	 --code_path path_to_python_code\
```

