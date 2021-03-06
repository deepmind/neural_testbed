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
"""Sweeps for sgmcmc agent."""

from typing import Sequence

from neural_testbed.agents.factories import base as factories_base
from neural_testbed.agents.factories import sgmcmc


def sgld_sweep() -> Sequence[sgmcmc.SGMCMCConfig]:
  """sweep for vanilla sgld."""
  sweep = []
  for learning_rate in [5e-4, 1e-3, 5e-3]:
    for prior_variance in [0.05, 0.1, 0.5, 1, 2, 10]:
      sweep.append(
          sgmcmc.SGMCMCConfig(
              learning_rate=learning_rate,
              prior_variance=prior_variance,
              adaptive_prior_variance=True,))
  return tuple(sweep)


def momentum_sgld_sweep() -> Sequence[sgmcmc.SGMCMCConfig]:
  """sweep for momentum sgld."""
  sweep = []
  for learning_rate in [5e-4, 1e-3, 5e-3]:
    for prior_variance in [0.05, 0.1, 0.5, 1, 2, 10]:
      sweep.append(
          sgmcmc.SGMCMCConfig(
              learning_rate=learning_rate,
              prior_variance=prior_variance,
              adaptive_prior_variance=True,
              alg_temperature=1,
              momentum_decay=0.9))
  return tuple(sweep)


def combined_sweep() -> Sequence[sgmcmc.SGMCMCConfig]:
  return tuple(sgld_sweep()) + tuple(momentum_sgld_sweep())


def paper_agent() -> factories_base.PaperAgent:
  return factories_base.PaperAgent(
      default=sgmcmc.SGMCMCConfig(),
      ctor=sgmcmc.make_agent,
      sweep=combined_sweep,
  )
