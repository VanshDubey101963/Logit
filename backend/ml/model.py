import joblib as jlib
import os

base_dir = os.path.dirname(__file__)
logit_model = jlib.load(f"{base_dir}/logitmodel")

from logit.linear_model import LogisticRegression

# from logit.linear_model import LogisticRegression

# model = LogisticRegression()
# model.fit()
# jlib.dump(model,"logitmodel")

# logit_model.predict()