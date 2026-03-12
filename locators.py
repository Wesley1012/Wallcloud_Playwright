class MainPageLocators:

    # Other
    NOTIFICATION_BTN = "#popup-decline-btn"
    SCREEN_WIDTH = "//span[@class='screen screen_width']/text()"
    SCREEN_HEIGHT = "//span[@class='screen screen_height']"

    HEADER = {
        'Logo Icon': "span.logo-icon",
        'Categories List': "#categories-list",
        'Resolutions List': "#resolutions-list",
        'Top List': "#top-list",
        'Random List': "li.waves.waves-effect.waves-light",
        'More List': "#more-list",
        'Search Button': "button.btn.go-search",
        'Search Bar': "[name='q']",
        'Color Search': "div[data-original-title='Search by color'] .msr",  #"//div[@class='color_pallet tooltips']/span[@class='msr']",
        'Language Button': "#lang_list",
        'Login Button': "//li[@class='dropdown m-profile']//span[@class='user-name']"
    }

    MENU_DROPDOWNS = {
        "Categories List": "#g_0.dropdown-menu",
        "Resolutions List": "#r_list.dropdown-menu",
        "Top List": "#top-list .dropdown-menu",
        "More List": "#more-list .dropdown-menu",
        "Color Search": ".minicolors-panel.minicolors-slider-wheel.minicolors-with-swatches",
        "Language Button": "#lang_list.dropdown-menu",
        "Login Button": ".m-profile .dropdown-menu",
    }

    # Categories List
    CATEGORIES = {
        "3d": "//li[@class='3d']",
        "Hi-Tech": "li.hi-tech a",
        "Weapon": "li.weapon a",
        "Abstract": "li.abstract a",
        "Aircraft": "li.aircraft a",
        "Cars": "li.cars a",
        "Anime": "li.anime a",
        "Architecture": "li.architecture a",
        "Cities": "li.cities a",
        "Graphics": "li.graphics a",
        "Food": "li.food a",
        "Animals": "li.animals a",
        "Games": "li.games a",
        "Illustration": "li.illustration a",
        "Interiors": "li.interiors a",
        "Computers": "li.computers a",
        "Ships": "li.ships a",
        "Space": "li.space a",
        "Love": "li.love a",
        "People": "li.people a",
        "Macro": "li.macro",
        "Minimalism": "li.minimalism a",
        "Motorcycles": "li.motorcycles a",
        "Music": "li.music a",
        "Multiplicatios": "li.multiplicatios a",
        "Holidays": "li.holidays a",
        "Funny": "li.funny a",
        "Nature": "li.nature a",
        "Others": "li.others a",
        "Sport": "li.sport",
        "Textures": "li.textures a",
        "Fantasy": "li.fantasy a",
        "Films": "li.films a"
    }

    # Resolution list
    RESOLUTIONS = {
        "1600x1200": "li[data-size='1600x1200']",
        "1920x1440": "li[data-size='1920x1440']",
        "2560x1920": "li[data-size='2560x1920']",
        "2800x2100": "li[data-size='2800x2100']",
        "3200x2400": "li[data-size='3200x2400']",

        "1280x1024": "li[data-size='1280x1024']",
        "2560x2048": "li[data-size='2560x2048']",

        "1152x720": "li[data-size='1152x720']",
        "1280x800": "li[data-size='1280x800']",
        "1440x900": "li[data-size='1440x900']",
        "1680x1050": "li[data-size='1680x1050']",
        "1920x1200": "li[data-size='1920x1200']",
        "2560x1600": "li[data-size='2560x1600']",
        "2880x1800": "li[data-size='2880x1800']",

        "1024x576": "li[data-size='1024x576']",
        "1280x720": "li[data-size='1280x720']",
        "1366x768": "li[data-size='1366x768']",
        "1600x900": "li[data-size='1600x900']",
        "1920x1080": "li[data-size='1920x1080']",
        "2048x1152": "li[data-size='2048x1152']",
        "2400x1350": "li[data-size='2400x1350']",
        "2560x1440": "li[data-size='2560x1440']",
        "2880x1620": "li[data-size='2880x1620']",

        "2560x1080": "li[data-size='2560x1080']",
        "3440x1440": "li[data-size='3440x1440']",

        "3840x2160": "li[data-size='3840x2160']",
        "5120x2880": "li[data-size='5120x2880']",
        "7680x4320": "li[data-size='7680x4320']",

        "720x1280": "li[data-size='720x1280']",
        "1080x1920": "li[data-size='1080x1920']",
        "1080x2160": "li[data-size='1080x2160']",
        "1080x2400": "li[data-size='1080x2400']",
        "1440x2560": "li[data-size='1440x2560']",

        "750x1334": "li[data-size='750x1334']",
        "828x1792": "li[data-size='828x1792']",
        "1024x768": "li[data-size='1024x768']",
        "1024x1024": "li[data-size='1024x1024']",
        "1125x2436": "li[data-size='1125x2436']",
        "1170x2532": "li[data-size='1170x2532']",
        "1284x2778": "li[data-size='1284x2778']",
        "2048x1536": "li[data-size='2048x1536']",
        "2732x2048": "li[data-size='2732x2048']"
    }

    # Resolution IDs
    RESOLUTION_IDS = (
        "Standard 4:3 1600x1200",
        "Standard 4:3 1920x1440",
        "Standard 4:3 2560x1920",
        "Standard 4:3 2800x2100",
        "Standard 4:3 3200x2400",

        "Standard 5:4 1280x1024",
        "Standard 5:4 2560x2048",

        "Wide 16:10 1152x720",
        "Wide 16:10 1280x800",
        "Wide 16:10 1440x900",
        "Wide 16:10 1680x1050",
        "Wide 16:10 1920x1200",
        "Wide 16:10 2560x1600",
        "Wide 16:10 2880x1800",

        "Wide 16:9 1024x576",
        "Wide 16:9 1280x720",
        "Wide 16:9 1366x768",
        "Wide 16:9 1600x900",
        "Wide 16:9 1920x1080",
        "Wide 16:9 2048x1152",
        "Wide 16:9 2400x1350",
        "Wide 16:9 2560x1440",
        "Wide 16:9 2880x1620",

        "UltraWide 21:9 2560x1080",
        "UltraWide 21:9 3440x1440",

        "UltraHD 3840x2160",
        "UltraHD 5120x2880",
        "UltraHD 7680x4320",

        "Android 720x1280",
        "Android 1080x1920",
        "Android 1080x2160",
        "Android 1080x2400",
        "Android 1440x2560",

        "IOS 750x1334",
        "IOS 828x1792",
        "IOS 1024x768",
        "IOS 1024x1024",
        "IOS 1125x2436",
        "IOS 1170x2532",
        "IOS 1284x2778",
        "IOS 2048x1536",
        "IOS 2732x2048"
    )

    # Top list
    TOP_LIST = {
        "Download": "a[href*='download']",
        "View": "a[href*='view']",
        "Favourite": "a[href*='favourite']",
        "Rating": "a[href*='rating']"
    }

    # More List (остаются прежними)
    MORE_LIST = {
        "About-us": "a.m-link[href*='about-us']",
        "Tags": "a.m-link[href*='tags']",
        "Contact": "a.m-link[href*='contact']",
        "Android_App": "a.m-link[href*='t.me']"
    }

    # Color buttons
    COLORS = {
        "Aqua #00ffff": "li.minicolors-swatch span[style*='rgb(0, 255, 255)']",
        "Black #000000": "li.minicolors-swatch span[style*='rgb(0, 0, 0)']",
        "Blue #0000ff": "li.minicolors-swatch span[style*='rgb(0, 0, 255)']",
        "Fuchsia #ff00ff": "li.minicolors-swatch span[style*='rgb(255, 0, 255)']",
        "Gray #808080": "li.minicolors-swatch span[style*='rgb(128, 128, 128)']",
        "Green #008000": "li.minicolors-swatch span[style*='rgb(0, 128, 0)']",
        "Lime #00ff00": "li.minicolors-swatch span[style*='rgb(0, 255, 0)']",
        "Maroon #800000": "li.minicolors-swatch span[style*='rgb(128, 0, 0)']",
        "Navy #000080": "li.minicolors-swatch span[style*='rgb(0, 0, 128)']",
        "Olive #808000": "li.minicolors-swatch span[style*='rgb(128, 128, 0)']",
        "Purple #800080": "li.minicolors-swatch span[style*='rgb(128, 0, 128)']",
        "Red #ff0000": "li.minicolors-swatch span[style*='rgb(255, 0, 0)']",
        "Silver #c0c0c0": "li.minicolors-swatch span[style*='rgb(192, 192, 192)']",
        "Teal #008080": "li.minicolors-swatch span[style*='rgb(0, 128, 128)']",
        "White #ffffff": "li.minicolors-swatch span[style*='rgb(255, 255, 255)']",
        "Yellow #ffff00": "li.minicolors-swatch span[style*='rgb(255, 255, 0)']",
    }
    COLOR_VALUE = "//span[@class='value']"

    LANGUAGE_SELECTORS = {
        "EN": "a:has-text('English')",
        "RU": "a:has-text('Русский')",
        "UA": "a:has-text('Українська')"
    }

    LOGIN_ITEMS = {
        "login": "//a[@href='https://wallscloud.net/en/account/login']",
        "signup": "//a[@href='https://wallscloud.net/en/account/signup']"
    }


