# Copyright 2017 Hugh Salimbeni
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from ddt import ddt, data

from bayesian_benchmarks.tasks.active_learning_discrete import run
from bayesian_benchmarks.database_utils import Database

class Bunch(object):
    def __init__(self, adict):
        self.__dict__.update(adict)

models = [
          'linear',
          'variationally_sparse_gp',
          'variationally_sparse_gp_minibatch',
          'deep_gp_doubly_stochastic',
          'svm',
          'naive_bayes',
          'knn',
          'decision_tree',
          'random_forest',
          'gradient_boosting_machine',
          'adaboost',
          'mlp',
          ]

@ddt
class TestClassification(unittest.TestCase):
    @data(*models)
    def test_multi(self, model):
        d = {'dataset':'iris',
             'model' :  model,
             'split' : 2**32 - 1,  # make sure not to use this seed for real experiments!
             'iterations' : 2,
             'num_initial_points' : 10}

        run(Bunch(d), is_test=True)

        with Database() as db:
            db.delete('active_learning_discrete', d)

    @data(*models)
    def test_binary(self, model):
        d = {'dataset': 'planning',
              'model': model,
              'split': 2 ** 32 - 1,  # make sure not to use this seed for real experiments!
              'iterations': 2,
              'num_initial_points': 10}

        run(Bunch(d), is_test=True)

        with Database() as db:
            db.delete('active_learning_discrete', d)


if __name__ == '__main__':
    unittest.main()
