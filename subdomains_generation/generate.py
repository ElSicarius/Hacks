
import yaml
import sys

if __name__ == '__main__':

    template = sys.argv[1]
    app = sys.argv[2]
    mode = sys.argv[3]
    if not "http" in mode:
        exit("Mode (argv3) needs to be https?")

    template_object = yaml.load(open(template), Loader=yaml.FullLoader)

    root = template_object["root"]
    root = root.replace("{{app}}", app)
    prefixes = template_object["prefixes"]

    modulus = template_object["modulus"]
    template = modulus["template"]
    enumeration = modulus["var"]
    print(root)
    for p in prefixes:
        for x in enumeration:

            enum = f"""{mode}://{p}.{template.replace("{{modulus}}", x).replace(r"{{root}}", root)}"""
            print(enum)
            enum = f"""{mode}://{template.replace("{{modulus}}", x).replace(r"{{root}}", root)}"""
            print(enum)
