##Adding new exercises

create a new file for that exercise into the ```exercises``` folder, and make sure that there is a method called ```test()``` that does all the testing for the new given function. Then, add a new line in module ```util.py``` referencing the new code:

```python
def get_module(iv_script):
    ...
    elif(iv_script == 'module_name'): from exercises.module_name import test # <<<<<<< add this 
```

#Testing

Just call ```python main.py module_name ```

