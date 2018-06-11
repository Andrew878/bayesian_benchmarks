import itertools
import os
from subprocess import call

def make_experiment_combinations(combinations : list):
    """
    The product of all combinations of arguments.
    :param combinations: A list of dictionaries, each with a list of args
    :return: A list of dictionaries for all combinations
    """
    fields = []
    vals = []
    for p in combinations:
        for k in p:
            fields.append(k)
            vals.append(p[k])

    ret = []
    for a in itertools.product(*vals):
        d = {}

        for f, arg in zip(fields, a):
            d[f] = arg

        ret.append(d)

    return ret

def make_local_jobs(script : str, experiments : list):
    """
    Writes a file of scripts to be run in series on a single machine.

    :param script: name of python script to run
    :param experiments: list of dictionaries of args
    :return: None
    """
    with open('local_run', 'w') as f:
        f.write('#!/usr/bin/env bash\n\n')

        for e in experiments:
            s = 'python {}.py '.format(script)
            for k in e:
                s += '--{}={} '.format(k, e[k])
            s += '\n'
            f.write(s)

def make_condor_jobs(script : str, experiments : list):
    """
    Writes a very basic condor submission file, and also creates the executable if necessary. Preamble for the 
    exectable (e.g. for setting up the python environment) should go in 'preamble.txt.txt',  

    :param script: name of python script to run
    :param experiments: list of dictionaries of args
    :return: None
    """
    condor_run_file = 'condor_run'
    if True:# not os.path.isfile(condor_run_file):
        with open(condor_run_file, 'w') as f:
            f.write("#!/usr/bin/env bash\n")

            preamble = 'preamble.txt'
            if os.path.isfile(preamble):
                for l in open(preamble, 'r'):
                    f.writelines(l)

            t = "python "
            for i in range(1, 10):
                t += '$' + str(i) + ' '
            for i in range(10, 20):
                t += '${' + str(i) + '} '

            f.write(t + '\n')

        call(["chmod", '777', condor_run_file])


    with open('condor_jobs', 'w') as f:
        f.write('Universe   = vanilla\n')
        f.write('Executable = condor_run \n')

        # or send these elsewhere
        # f.write('Log        = /dev/null\n')
        # f.write('Output     = /dev/null\n')
        # f.write('Error      = /dev/null\n')

        f.write('Log        = /vol/bitbucket/hrs13/condor/$(Process)_log.txt\n')
        f.write('Output     = /vol/bitbucket/hrs13/condor/$(Process)_stdout.txt\n')
        f.write('Error      = /vol/bitbucket/hrs13/condor/$(Process)_stderr.txt\n')


        f.write('\n')

        for e in experiments:
            t = 'Arguments = {}.py '.format(script)
            for k in e:
                t += '--{}={} '.format(k, e[k])
            t += '\nQueue 1\n'
            f.write(t)



def make_kubernetes_jobs(script : str, experiments : list):
    """
    Writes kubernetes submission file
    
    TODO 
    
    :param script: name of python script to run
    :param experiments: list of dictionaries of args
    :return: None
    """
    raise NotImplementedError






