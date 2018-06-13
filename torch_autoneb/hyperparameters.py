class EvalHyperparameters:
    batch_size = None


class OptimHyperparameters:
    def __init__(self, nsteps, optim_name, optim_args, eval_config: EvalHyperparameters):
        self.nsteps = nsteps
        self.optim_args = optim_args
        self.optim_name = optim_name
        self.eval_config = eval_config


class NEBHyperparameters:
    def __init__(self, spring_constant: float, optim_config: OptimHyperparameters):
        self.spring_constant = spring_constant
        self.optim_config = optim_config


class AutoNEBHyperparameters:
    def __init__(self, cycle_count):
        self.cycle_count = cycle_count
        self.hyperparameter_sets = [OptimHyperparameters() for _ in range(cycle_count)]


class LandscapeExplorationHyperparameters:
    def __init__(self, suggest_engines, auto_neb_config: AutoNEBHyperparameters):
        self.suggest_engines = suggest_engines
        self.auto_neb_config = auto_neb_config
