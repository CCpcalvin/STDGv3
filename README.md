# STDGv3

Run 

```python
import STDGv3

head = STDGv3.read_script("./tests/datapack/scripts.txt")
sqList = [head]

STDGv3.generate_datapack(
    sqList,
    "./tests/datapack/",
    "test",
    reload=True,
)
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

Append and extend functions

```python
head.append("function scene:start")

next = head.get_next(1)
next.extend(["function scene:1", "function scene:2"])
```

Color 
```python
STDGv3.DialogueSequence.update_colormap({"嗣尤": "aqua", "幸姈": "red"})
head.generate_dialogue_json()
STDGv3.generate_datapack(
    sqList,
    "./tests/datapack/",
    "test",
    reload=True,
)
```
