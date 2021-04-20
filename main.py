# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scoorder_0 = 'Ruud Gullit'
scoorder_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scoorder_0 + " " + str(goal_0) + ", " + scoorder_1 + " " + str(goal_1)
report = f'{scoorder_0} scored in the {goal_0}nd minute\n{scoorder_1} scored in the {goal_1}th minute'
player = "hans van breukelen"
find = player.find(' ')
first_name = player[:find]
lastname = player[(find+1):]
last_name_len = len(lastname) 
name_short = f'{player[0]}. {lastname}'
chant_met_spatie = f'{first_name}! '*len(first_name)
chant = chant_met_spatie [:-1]
good_chant = (chant [-1] != ' ')

    