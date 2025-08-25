# Chains 

A **chain** is a way to connect multiple steps together into a single pipeline.  
Instead of calling each step manually, you link them so the data flows automatically.  

---

#### Without a Chain (Manual Steps)

You handle each step one by one:

1. **Fill the template** with input values → produces a prompt.  
2. **Send the prompt** to the model → produces a result.  

```python
prompt = template.invoke({"paper": "GPT-3"})
result = model.invoke(prompt)
````

---

#### With a Chain (Automatic Pipeline)

You connect the template **directly** to the model.
Now you can pass the inputs once, and the chain takes care of everything.

```python
chain = template | model
result = chain.invoke({"paper": "GPT-3"})
```

### Behind the Scenes

```
(your inputs) → [template] → [model] → [result]
```

---

#### Analogy

* **Manual Way** → Cooking step by step (chop → cook → serve).
* **Chain** → Kitchen machine (put ingredients in, it chops + cooks + serves).

---

#### When to Use

**Chains** → When you want fewer lines of code and automatic flow.
**Manual steps** → When you want more control and easier debugging.

---

#### Visualize the chain 
We can visualize our chain pipeline using `chain.get_graph().print_ascii()`