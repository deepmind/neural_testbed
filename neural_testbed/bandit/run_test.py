# pylint: disable=g-bad-file-header
# Copyright 2021 DeepMind Technologies Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or  implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Tests for neural_testbed.experiments.dropout.run."""

from absl import flags
from absl.testing import absltest
from absl.testing import parameterized
from neural_testbed.bandit import run

FLAGS = flags.FLAGS
PAPER_AGENTS = ['mlp', 'bbb', 'dropout', 'ensemble', 'ensemble+', 'hypermodel']


class RunTest(parameterized.TestCase):

  @parameterized.parameters([[x] for x in PAPER_AGENTS])
  def test_neural_testbed(self, agent_id: str):
    FLAGS.agent_id = agent_id
    FLAGS.input_dim = 2
    FLAGS.num_steps = 2
    FLAGS.num_actions = 2
    run.main(None)


if __name__ == '__main__':
  absltest.main()

