# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scoorder_0 = 'Ruud Gullit'
scoorder_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = f'{scoorder_0} {goal_0}, {scoorder_1} {goal_1}'
report = f'{scoorder_0} scored in the {goal_0}nd minute\n{scoorder_1} scored in the {goal_1}th minute'
player = "hans van breukelen"
first_name = player.split(' ')[0]
lastname = player.split(' ')[-2] + ' ' + player.split(' ')[-1]
last_name_len = len(lastname) 
name_short = f'{player[:1]}. {lastname}'
first_namechant = first_name + '!' ' '
chant_met_spatie = first_namechant*len(first_name)
size = len(chant_met_spatie)
chant = chant_met_spatie [:size - 1]
good_chant = (chant [-1] != ' ')

        