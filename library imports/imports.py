# Install dependencies
!pip install openai pandas matplotlib

#for conclusion table
!pip install tabulate

#for charts
%pip install matplotlib

#need it for prettier charts
pip install seaborn

#install for the demo
pip install gradio


  # Core imports
import pandas as pd
import os
from openai import OpenAI
import matplotlib.pyplot as plt
from typing import TypedDict, List, Callable, Dict, Any, Optional, Type, Union
from pydantic import BaseModel
import inspect
import sys
from io import StringIO

# Initialize OpenAI client
openai_client = OpenAI()

def generate(
    prompt: str,
    temperature: float = 0,
    response_format: Optional[Type[BaseModel]] = None,
    model: str = "gpt-4o-mini"
) -> Union[str, BaseModel]:
    """
    🎨 Generate text using OpenAI's API with optional structured output

    Args:
        prompt: The input prompt for generation
        temperature: Sampling temperature (0-2), default 0
        response_format: Optional Pydantic model class for structured output
        model: The model to use, default "gpt-4o-mini"

    Returns:
        Either a string (regular generation) or a Pydantic model instance (structured output)
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    if response_format is not None:
        # Use structured output with Pydantic model
        response = openai_client.beta.chat.completions.parse(
            model=model,
            messages=messages,
            temperature=temperature,
            response_format=response_format
        )
        return response.choices[0].message.parsed
    else:
        # Regular text generation
        response = openai_client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content.strip()

print("✅ Core utilities loaded")
