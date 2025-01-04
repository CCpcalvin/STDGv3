# STDGv3

Run 

```python
import STDGv3

head = STDGv3.read_script("./tests/datapack/scripts.txt")
head.generate_datapack("./tests/datapack/", "test", reload=True)
```

Print 

```python
head.print_tree()
```

Insert 

```python
import copy

head = STDGv3.read_script("./tests/datapack/scripts_short.txt")

last = head.get_last()
head = last.get_head()

tpSq = STDGv3.Sequence("function scene:start\n")
head.insert_after(copy.deepcopy(tpSq))
head.insert_before(copy.deepcopy(tpSq))

head = head.get_head()

last = head.get_last()
last.insert_before(copy.deepcopy(tpSq))
last.insert_after(copy.deepcopy(tpSq))

```

