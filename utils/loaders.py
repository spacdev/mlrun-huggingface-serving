import yaml
config_path = '../config/config.yaml'

def get_model(mode: str)-> str:
  ''' function that returns the model name
  args:
    mode: dev or prod
  returns: the name of the model
  '''
  with open(config_path, 'r') as f:
    config = yaml.safe_load(f)
  return config[mode]['model_name']