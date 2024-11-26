import pytest

from model import train_model

def test_model_training():
    """
    Test that the train_model function runs successfully and returns expected outputs.
    """
    # Run the training function
    model, mse = train_model()
    
    # Assert that MSE is positive (indicating a valid model was trained)
    assert mse > 0, "MSE should be greater than 0"
    
    # Assert that the model has the predict method (a valid scikit-learn model)
    assert hasattr(model, "predict"), "Model should have a 'predict' method"