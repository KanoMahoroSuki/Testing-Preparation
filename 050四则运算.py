exp = input()
exp = exp.replace("[", "(")
exp = exp.replace("]", ")")
exp = exp.replace("{", "(")
exp = exp.replace("}", ")")

print(eval(exp))