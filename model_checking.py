import os
import time

def python2NuSMV(model_path, actions, conditions, envs):
    # actions: [stop, VP], conditions: [conditions for stop, conditions for VP]
    f = open(model_path)
    text = f.read()
    space = text.find(envs[0])-text.find('VAR\n')-4
    
    new_conds = []
    for c in conditions:
        c = c.replace('True', 'TRUE')
        c = c.replace('not', '!')
        c = c.replace('and', '&')
        c = c.replace('or', '|')
        c = c.replace('False', 'FALSE')
        new_conds.append(c)
    
    act_transition = ' '*space + 'next(Action) :=\n' + '  '*space + 'case\n'
    for i in range(len(actions)):
        act_transition += '   '*space + new_conds[i] + ' : ' + actions[i] + ';\n'
    act_transition += '  '*space + 'esac;\n'

    text += '\n' + act_transition
    os.system('rm -rf NuSMV/temp')
    os.system('mkdir NuSMV/temp')
    f = open('NuSMV/temp/task.smv', 'x')
    f.write(text)
    f.close()

def verification(spec_path, spec_names):
    # spec_names: [spec1, spec2] list of names of the defined specifications
    f_a_s = open('NuSMV/temp/verif.smv', 'x')
    f = open('NuSMV/temp/task.smv')
    f_s = open(spec_path)
    text = f.read()
    text += '\n\n' + f_s.read()
    f_a_s.write(text)
    f_a_s.close()
    f_s.close()
    f.close()
    command = 'read_model -i NuSMV/temp/verif.smv \ngo\n'
    for name in spec_names:
        cmd = 'check_ltlspec -P \"' + name + '\" -o NuSMV/temp/'+ name + '_result.txt \n' 
        command += cmd
    command += 'quit'
    f = open('NuSMV/temp/script.csh', 'x')
    f.write(command)
    f.close()
    start = time.time()
    os.system('NuSMV/bin/NuSMV -source NuSMV/temp/script.csh')
    end = time.time()
    print(end - start)