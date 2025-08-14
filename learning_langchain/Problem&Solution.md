# Problems and their Solutions

#### Problem: 
During running files using OpenAI model '.venv/lib/python3.12/site-packages/langchain_openai/chat_models/base.py:1857: UserWarning: Cannot use method='json_schema' with model gpt-3.5-turbo since it doesn't support OpenAI's Structured Output API. You can see supported models here: https://platform.openai.com/docs/guides/structured-outputs#supported-models. To fix this warning, set `method='function_calling'. Overriding to method='function_calling'.
  warnings.warn(
'
#### Solution: 
`Cause:` LangChain’s structured output helpers default to method="json_schema". The default model="gpt-3.5-turbo" does not support json_schema. LangChain detects the mismatch and falls back to function_calling, showing a warning.

If you want strict JSON schema validation, switch to gpt-4o or gpt-4o-mini.
If you need faster/cheaper, stay with gpt-3.5-turbo but set method="function_calling".