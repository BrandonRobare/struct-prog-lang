from tokenizer import tokenize
from parser import parse
from evaluator import evaluate

source = """
homework = true;
if (homework) {
    brobare;
    print(_kentid_);
}
"""

tokens = tokenize(source)
ast = parse(tokens)
env = {"true": True, "false": False}
evaluate(ast, env)