
import argparse
import parser
from condition_extraction import *
from model_checking import *
import pprint

par = argparse.ArgumentParser()
par.add_argument('--model_path', type=str, default='sample_inputs/sample_model.smv')
par.add_argument('--spec_path', type=str, default='sample_inputs/sample_ltl.txt')
par.add_argument('--code_path', type=str, default='sample_inputs/sample_code.py')

keys = ['while', 'if', 'else', 'elif', 'not', 'and', 'or', ':', 'True', 'False']

def extract_env_vars(model_path):
    f = open(model_path)
    text_model = f.read()
    envs = text_model[text_model.find('VAR')+3:]
    envs = envs[:envs.find('Action')]
    env_list = envs.split(';')
    env_vars = []
    for e in env_list:
        e = e[0:e.find(':')]
        e = e.replace('\n','')
        e = e.replace(' ','')
        if len(e) > 0:
            env_vars.append(e)
    f.close()
    return env_vars

def extract_actions(model_path):
    f = open(model_path)
    text_model = f.read()
    actions = text_model[text_model.find('{')+1: text_model.find('}')]
    act_list = actions.split(',')
    actions = []
    for act in act_list:
        act = act.replace(' ', '')
        if len(act) > 0:
            actions.append(act)
    f.close()
    return actions

def main(args):
    model_path, spec_path, code_path = args.model_path, args.spec_path, args.code_path

    envs = extract_env_vars(model_path)
    acts = extract_actions(model_path)
    print(envs, acts)
    words = keys + envs + acts

    f = open(code_path)
    code = f.read()
    tree = parser.suite(code).tolist()
    # pprint.pprint(tree)
    processed = extract_words(process_code(tree, 0), words)
    pprint.pprint(processed)
    print()
    # print(prev_layer_cond(processed, len(processed)-2))
    conditions = []
    for act in acts:
        conditions.append(extract_conditions(act, processed))
    python2NuSMV(model_path, acts, conditions, envs)
    spec_names = ['spec1', 'spec3']
    verification(spec_path, spec_names)

if __name__ == '__main__':
    main(par.parse_args())