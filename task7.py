def move(subject, x1, x2):
    return f"Move {subject} from {x1} to {x2}"

def push_box(x1, x2):
    return f"Push box from {x1} to {x2}"

def climb_box(x, direction):
    return f"Climb box at {x} {direction}"

def have_banana(x):
    return f"Have banana at {x}"

initial_state = {
    'monkeyAt': 0,
    'monkeyLevel': 'Down',
    'bananaAt': 1,
    'boxAt': 2
}

goal_state = {
    'GetBanana': True,
    'at': 1
}

def plan_actions(state, goal):
    actions = []

    if state['monkeyAt'] != state['boxAt']:
        actions.append(move('Monkey', state['monkeyAt'], state['boxAt']))
        state['monkeyAt'] = state['boxAt']
    
    if state['boxAt'] != goal['at']:
        actions.append(push_box(state['boxAt'], goal['at']))
        state['boxAt'] = goal['at']
        state['monkeyAt'] = goal['at']
    
    if state['monkeyAt'] != goal['at']:
        actions.append(move('Monkey', state['monkeyAt'], goal['at']))
        state['monkeyAt'] = goal['at']

    actions.append(climb_box(goal['at'], 'Up'))
    actions.append(have_banana(goal['at']))

    return actions

actions = plan_actions(initial_state.copy(), goal_state)

print("Plan:")
for action in actions:
    print(action)
