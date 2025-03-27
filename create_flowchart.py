from graphviz import Digraph

# Create a Digraph object
flowchart = Digraph('Rock Paper Scissors Flowchart', filename='rock_paper_scissors_flowchart')
flowchart.attr(rankdir='TB', size='8,11', dpi='300')
flowchart.attr('node', shape='box', style='rounded', fontname='Arial', fontsize='10')

# Add nodes
flowchart.node('start', 'Start Game', shape='oval')
flowchart.node('display', 'Display Game Instructions')
flowchart.node('input_p1', 'Get Player 1 Choice')
flowchart.node('check_p1_zero', 'Is choice 0?', shape='diamond')
flowchart.node('validate_p1', 'Is choice valid?\n(1, 2, or 3)', shape='diamond')
flowchart.node('input_p2', 'Get Player 2 Choice')
flowchart.node('check_p2_zero', 'Is choice 0?', shape='diamond')
flowchart.node('validate_p2', 'Is choice valid?\n(1, 2, or 3)', shape='diamond')
flowchart.node('determine_winner', 'Determine Winner')
flowchart.node('display_result', 'Display Result')
flowchart.node('end', 'End Game', shape='oval')

# Add edges
flowchart.edge('start', 'display')
flowchart.edge('display', 'input_p1')
flowchart.edge('input_p1', 'check_p1_zero')
flowchart.edge('check_p1_zero', 'end', label='Yes')
flowchart.edge('check_p1_zero', 'validate_p1', label='No')
flowchart.edge('validate_p1', 'input_p1', label='No')
flowchart.edge('validate_p1', 'input_p2', label='Yes')
flowchart.edge('input_p2', 'check_p2_zero')
flowchart.edge('check_p2_zero', 'end', label='Yes')
flowchart.edge('check_p2_zero', 'validate_p2', label='No')
flowchart.edge('validate_p2', 'input_p2', label='No')
flowchart.edge('validate_p2', 'determine_winner', label='Yes')
flowchart.edge('determine_winner', 'display_result')
flowchart.edge('display_result', 'input_p1')

# Save the DOT file without trying to render
flowchart.save()
print("DOT file created as 'rock_paper_scissors_flowchart'. You can visualize it using online tools like:")
print("- https://dreampuf.github.io/GraphvizOnline/")
print("- https://edotor.net/")
print("- https://viz-js.com/") 