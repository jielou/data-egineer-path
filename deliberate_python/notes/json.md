---
noteId: "e4314f40914111eab318d55bc3e6e734"
tags: []

---

# json

5.8

[reference](https://realpython.com/python-json/)

## Intro
I have been working with Json for a while. It is time to dig into it.

## quick facts

1. JSON is JaveScriptObjectNotation

```python
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
```

It just looks like a python dictionary!

2. the process of encoding JSON is called serialization, which means transformation of data into a series of bytes to be stored or transmitted across a network. 

## JSON package

- json.dump(): write data to files
- json.dumps(): write to a Python string
- terminology table

| Python          | JSON          |
| ----------------|:-------------:|
| dict            | object        |
| list, tuple     | array         |
| int,long,float  | number        |
| True, False     | true, false   |
| None            | null          |

```python
# dump into a file
with open("data.json", "w") as write_file:
    json.dump(my_dict, write_file)

# dump to a string
json.dumps(data)

# load JSON encoded data into python objects
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

# load json string to python object
json.loads(json_string)
```

### tip

1. >If you encode an object now and then decode it again later, you may not get exactly the same object back.

