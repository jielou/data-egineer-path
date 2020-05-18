---
noteId: "f8895bf0990111ea8b572b6747d84cb1"
tags: []

---

# main method

##key takeaways

1. python file can be executed as script or be imported to another file. And in two cases, their __name__ variables are different. 
    - __name__ = "__main__" when run as script or called with `python -m`
    - __name__ = "file_name" when run as imported library

2. best practices
    - create a function called main() to contain the code you want to run 
    - call other functions from main