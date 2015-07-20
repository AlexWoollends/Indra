#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 21:13:15 2014
@author: Brandon
Implements Paul Krugman's babysitting co-op model.
"""

import indra.utils as utils
import indra.prop_args as props
import coop_model as cm

MODEL_NM = "coop_model"
(prog_file, log_file, prop_file, results_file) = utils.gen_file_names(MODEL_NM)

pa = utils.read_props(MODEL_NM)
if pa is None:
    pa = props.PropArgs(MODEL_NM, logfile=log_file, props=None)
    pa.set("model", MODEL_NM)
    pa.ask("num_agents", "What is the number of agents?", int, default=100,
           range=utils.NTRL_NUMS)
    pa.set("min_holdings", 7.5)

env = cm.CoopEnv(model_nm=MODEL_NM)

for i in range(pa.get("num_agents")):
    env.add_agent(
        cm.CoopAgent('agent' + str(i), 5, 0))

utils.run_model(env, prog_file, results_file)
