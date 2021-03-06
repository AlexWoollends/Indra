#!/usr/bin/env python3
"""
edgebox_run.py
The script to run our Edgeworth Box model.
"""

import indra.utils as utils
import indra.prop_args as props
import indra.node as node
import edgebox_model as ebm

MODEL_NM = "edgebox_model"
(prog_file, log_file, prop_file, results_file) = utils.gen_file_names(MODEL_NM)

pa = utils.read_props(MODEL_NM)
if pa is None:
    pa = props.PropArgs(MODEL_NM, logfile=log_file, props=None)
    pa.ask("al_cheese", "What is Albert's cheese endowment?", int, default=20,
           limits=utils.NTRL_NUMS)
    pa.set("al_cutil", "10 - .75 * qty")
    pa.ask("al_wine", "What is Albert's wine endowment?", int, default=0,
           limits=utils.NTRL_NUMS)
    pa.set("al_wutil", "10 - .5 * qty")
    pa.ask("bea_wine", "What is Beatrice's wine endowment?", int, default=20,
           limits=utils.NTRL_NUMS)
    pa.set("bea_wutil", "10 - .75 * qty")
    pa.ask("bea_cheese", "What is Beatrice's cheese endowment?", int, default=0,
           limits=utils.NTRL_NUMS)
    pa.set("bea_cutil", "10 - .5 * qty")

env = ebm.EdgeboxEnv("An Edgeworth Box", 50, 50, model_nm=MODEL_NM)

albert = ebm.EdgeboxAgent(name="Albert")
env.add_agent(albert)
albert.endow(ebm.CHEESE,
             pa.get("al_cheese"),
             util_func=eval("lambda qty: " + pa.get("al_cutil")))
albert.endow(ebm.WINE,
             pa.get("al_wine"),
             util_func=eval("lambda qty: " + pa.get("al_wutil")))

beatrice = ebm.EdgeboxAgent(name="Beatrice")
env.add_agent(beatrice)
beatrice.endow(ebm.WINE,
               pa.get("bea_wine"),
               util_func=eval("lambda qty: " + pa.get("bea_wutil")))
beatrice.endow(ebm.CHEESE,
               pa.get("bea_cheese"),
               util_func=eval("lambda qty: " + pa.get("bea_cutil")))

node.add_prehension(ebm.EdgeboxAgent, ebm.TRADE, ebm.EdgeboxAgent)

utils.run_model(env, prog_file, results_file)
