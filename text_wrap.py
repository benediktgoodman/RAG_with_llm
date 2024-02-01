import textwrap


# Make a nice textwrapper so text can be displayed a bit more nicely
def wrap(line, lenght=100):
    broken = textwrap.wrap(line, lenght, break_long_words=False)
    return "\n".join(broken)
