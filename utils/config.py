from ruamel.yaml import YAML

yaml = YAML()
with open("core/economy.yml", "r", encoding="utf-8") as file:
    economy_config = yaml.load(file)

    # Starting
    Starting_wallet = economy_config['Starting_wallet']
    Starting_Bank = economy_config['Starting_Bank']
    Starting_Job = economy_config['Starting_Job']
    Starting_Hours = economy_config['Starting_Hours']
    Max_Money = economy_config['Max_Money']

with open("core/bot.yml", "r", encoding="utf-8") as file:
    bot_config = yaml.load(file)

    # Owner Stuff
    Bot_Owners = bot_config['Owners_ID']

    # Colors
    Defualt_Color = bot_config['Defualt_Color']
    Careful_Color = bot_config['Careful_Color']
