import pytest
from src.serve import HuggingFaceServing

def test_predict():
  server = HuggingFaceServing()
  server.load()
  result = server.predict({'text': 'Huggingface rocks'})
  assert 'label' in result
  assert 'score' in result