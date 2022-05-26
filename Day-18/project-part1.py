import colorgram


def color_palette(items):
    # extract 5 color from jpg
    colors = colorgram.extract('hirst-one.jpg', items)

    list_of_colors = []
    for i in range(items):
        new_color = colors[i]
        rgb = new_color.rgb
        red = rgb[0]
        green = rgb[1]
        blue = rgb[2]
        t_color = (red, green, blue)
        list_of_colors.append(t_color)

    return list_of_colors


color_list = color_palette(30)
print(color_list)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     t_color = (r, g, b)
#     list_of_colors.append(t_color)
