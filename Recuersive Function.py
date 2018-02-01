'paper=0.01mm'
'distance from earth to moon =384400km =>384400000000mm'

def recursive(paper):
    if paper < 384400000000:
        cumulate = paper*2
        print(cumulate)
        recursive(cumulate)

print(recursive(0.01))
