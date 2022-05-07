# IMPORT LIBRARIES
from nrclex import NRCLex
import json
# ----------------------------------------------------------------------------------------

# JSONS

# ----------------------------------------------------------------------------------------
# Open our libra data json with its average emotions
with open("./jsons/grand_totals/libra_grand_average.json", 'r') as libra_fil:
    # Load in the dictionary object from the .json file
    libra_averages = json.load(libra_fil)

# Open our gemini data json with its average emotions
with open("./jsons/grand_totals/gemini_grand_average_example.json", 'r') as gemini_fil:
    # Load in the dictionary object from the .json file
    gemini_averages = json.load(gemini_fil)

# Open our leo data json with its average emotions
with open("./jsons/grand_totals/leo_grand_average_example.json", 'r') as leo_fil:
    # Load in the dictionary object from the .json file
    leo_averages = json.load(leo_fil)

prop_all = {'positive': [], 'negative': [], 'fear': [], 'anger': [], 'anticip': [], 'trust': [], 'surprise': [],
          'sadness': [], 'disgust': [], 'joy': []}

for emotion in libra_averages[3]:
    if emotion == "anticipation":
            prop_all['anticip'].append(libra_averages[3][emotion])
    else:
        prop_all[emotion].append(libra_averages[3][emotion])

for emotion in gemini_averages[0]:
    if emotion == "anticipation":
        prop_all['anticip'].append(gemini_averages[0][emotion])
    else:
        prop_all[emotion].append(gemini_averages[0][emotion])

for emotion in leo_averages[0]:
    if emotion == "anticipation":
        prop_all['anticip'].append(leo_averages[0][emotion])
    else:
        prop_all[emotion].append(leo_averages[0][emotion])

print(prop_all)
# ----------------------------------------------------------------------------------------

# NRCLex

# ----------------------------------------------------------------------------------------
input = "I love horoscopes. They are so accurate and so funny. I do not like homework, it makes me sick!"

# Create text object
text_object = NRCLex(input)

# Store raw emotion scores (counts of emotion words)
input_emotions_freq = text_object.affect_frequencies

prop_input = dict()
for emotion in input_emotions_freq:
    prop_input[emotion] = input_emotions_freq[emotion]

'''# Get total count (to average)
input_total = 0
for emotion in raw_emotions:
    input_total += raw_emotions[emotion]

# Create averages for each emotion for the input string. If it isn't there, 0 it out
prop_input = dict()
for emotion in prop_all:
    if emotion in raw_emotions:
        prop_input[emotion] = raw_emotions[emotion] / input_total
    else:
        prop_input[emotion] = 0'''

# Get the number that is closest to our input number for each emotion, and append to results dictionary
results = []
for emotion in prop_input:
    output = min(prop_all[emotion], key=lambda x: abs(x-prop_input[emotion]))

    results.append({emotion: output})

# Count how many closest numbers are libra, gemini, or leo. Replace with name and number.
libra_count = 0
gem_count = 0
leo_count = 0
counts = []

for i in results:
    for emotion in i:
        if i[emotion] == prop_all[emotion][0]:
            i[emotion] = ['LIBRA', prop_all[emotion][0]]
            libra_count += 1
        elif i[emotion] == prop_all[emotion][1]:
            i[emotion] = ['GEMINI', prop_all[emotion][1]]
            gem_count += 1
        elif i[emotion] == prop_all[emotion][2]:
            i[emotion] = ['LEO', prop_all[emotion][2]]
            leo_count += 1

counts.append(libra_count)
counts.append(gem_count)
counts.append(leo_count)

# Get the index of the max number of matches
final_verdict = counts.index(max(counts))

if final_verdict == 0:
    print("LIBRA")
elif final_verdict == 1:
    print("GEMINI")
elif final_verdict == 2:
    print("LEO")

print()

print("INPUT AVERAGES: " + str(prop_input))
print()
print("SIGN AVERAGES: " + str(prop_all))# json.dumps(prop_all, indent=4))
print()
print(json.dumps(results,indent=4))









'''
from IPython.display import HTML
import random

def hide_toggle(for_next=False):
    this_cell = """$('div.cell.code_cell.rendered.selected')"""
    next_cell = this_cell + '.next()'

    toggle_text = 'Toggle show/hide'  # text shown on toggle link
    target_cell = this_cell  # target cell to control with toggle
    js_hide_current = ''  # bit of JS to permanently hide code in current cell (only when toggling next cell)

    if for_next:
        target_cell = next_cell
        toggle_text += ' next cell'
        js_hide_current = this_cell + '.find("div.input").hide();'

    js_f_name = 'code_toggle_{}'.format(str(random.randint(1,2**64)))

    html = """
        <script>
            function {f_name}() {{
                {cell_selector}.find('div.input').toggle();
            }}

            {js_hide_current}
        </script>

        <a href="javascript:{f_name}()">{toggle_text}</a>
    """.format(
        f_name=js_f_name,
        cell_selector=target_cell,
        js_hide_current=js_hide_current, 
        toggle_text=toggle_text
    )

    return HTML(html)
    '''

