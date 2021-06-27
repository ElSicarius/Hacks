
import yaml
import sys

if __name__ == '__main__':

    template = "src/tools/modules/"+sys.argv[1]+'.yml'
    app = sys.argv[2]

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

            enum = f"""{p}.{template.replace("{{modulus}}", x).replace(r"{{root}}", root)}"""
            print(enum)
            enum = f"""{template.replace("{{modulus}}", x).replace(r"{{root}}", root)}"""
            print(enum)
