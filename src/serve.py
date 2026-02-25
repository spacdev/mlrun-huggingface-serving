import mlrun
from transformers import pipeline
import os
from utils.loaders import get_model
from typing import Dict

class HuggingFaceServing(mlrun.serving.V2ModelServer):
  def load(self, mode:str='prod'):
    #get model name from config
    model_name = get_model(mode)
    #load model from HF hub (token optional)
    #hf_token = self.get_secret(HF_TOKEN)
    self.model = pipeline('text-classification', model=model_name)
  
  def predict(self, body:Dict[str,str]):
    text = body.get('text')
    if not text:
      raise ValueError('Input text required: Format: json object {"text": body}')
    result = self.model(text)
    return {
        'label': result[0]['label'],
        'score': result[0]['score']
    }

  def handler(context, event):
    return context.respond(event.body)