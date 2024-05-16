class ColorMachine():

    primary_colors = ("red", "blue", "yellow")
    secondary_colors = {
        "orange": ["red", "yellow"],
        "green": ["yellow", "blue"],
        "purple": ["red", "blue" ],
    }                

    def create_secondary_color(self, colors):

        if(len(colors) != 2):
            return "A secondary color is made by two primary colors"
        else:
            for color in colors:
                if (color not in self.primary_colors):
                    return color + " is not a primary color"
        
            for scd_color, primary_colors in self.secondary_colors.items():                
                if(sorted(colors)==sorted(primary_colors)):
                    return scd_color
            
        return "Can't create a secondary color."

    
