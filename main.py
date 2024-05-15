import pandas as pd
from transformers import AutoTokenizer, TFAutoModel

tokenizer = AutoTokenizer.from_pretrained("nlpaueb/legal-bert-base-uncased")
model = TFAutoModel.from_pretrained("nlpaueb/legal-bert-base-uncased")
