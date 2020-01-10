# Here a the solution for the syntax exercise

stop = 9
# Play with whitespace
var =           3

for j in range(0, stop):
    """This for loop gets a multi line string, 
    which is used as comment."""
    tmp = var + \
          j
    print("My loop variable ", tmp)
