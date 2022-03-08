# function with outputs

def format_name(f_name, l_name):
    formated_f_name = (f_name.title())
    formated_l_name = (l_name.title())
    return (f"{formated_f_name} {formated_l_name}")

formated_string = format_name("eder", "thOmAS")

print(formated_string)


# functions multiple values

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return f"You didn't provide a valid value"
    formated_f_name = (f_name.title())
    formated_l_name = (l_name.title())
    return (f"{formated_f_name} {formated_l_name}")

formated_string = format_name("eder", "thOmAS")

print(formated_string)