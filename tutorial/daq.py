from textwrap import dedent as s
import dash_core_components as dcc
import dash_html_components as html
from tutorial import styles
from tutorial.utils.component_block import ComponentBlock
from tutorial.tools import load_example

import dash_daq as daq

from tutorial.utils.simple_doc_generator import generate_docs


daq_library_heading =  dcc.Markdown('''
    # Dash DAQ

    Dash is a web application framework that provides pure Python abstraction
    around HTML, CSS, and JavaScript.

    Dash DAQ comprises a robust set of controls that make it simpler to
    integrate data acquisition and controls into your Dash applications.

    The source is on GitHub at [plotly/dash-daq](https://github.com/plotly/dash-daq).

    These docs are using version {}.
    '''.replace('    ', '').format(daq.__version__)
)

dash_daq_components = {
    'BooleanSwitch': {
        'description': '''A switch component that toggles between on \
        and off.''',
        'props': {
            'on': True
        }
    },
    'ColorPicker': {
        'description': '''A color picker.''',
        'props': {
            'label': '\"colorPicker\"'
        },
    },
    'Gauge': {
        'description': '''A gauge component that points to some value between \
        some range.''',
        'props': {
            'min': 0,
            'max': 10,
            'value': 6
        }
    },
    'GraduatedBar': {
        'description': '''A graduated bar component that displays a value within \
        some range as a percentage.''',
        'props': {
            'value': 4
        }
    },
    'Indicator': {
        'description': '''A boolean indicator LED.''',
        'props': {
            'value': True,
            'color': '\"#00cc96\"'
        }
    },
    'Knob': {
        'description': '''A knob component that can be turned to a value \
        between some range.''',
        'props': {
            'min': 0,
            'max': 10,
            'value': 8
        }
    },
    'LEDDisplay': {
        'description': '''A 7-segment LED display component.''',
        'props': {
            'value': '\"3.14159\"'
        }
    },
    'NumericInput': {
        'description': '''A numeric input component that can be set to \
        a value between some range.''',
        'props': {
            'min': 0,
            'max': 10,
            'value': 5
        }
    },
    'PowerButton': {
        'description': '''A power button component that can be turned \
        on or off.''',
        'props': {
            'on': True
        }
    },
    'PrecisionInput': {
        'description': '''A numeric input component that converts an \
        input value to the desired precision.''',
        'props': {
            'precision': 4,
            'value': 299792458
        }
    },
    'StopButton': {
        'description': '''A stop button.''',
    },
    'Slider': {
        'description': '''A slider component with support for a \
        target value.''',
        'props': {
            'value': 17,
            'min': 0,
            'max': 100,
            'targets': '{\"25\": {\"label\": \"TARGET\"}}'
        }
    },
    'Tank': {
        'description': '''A tank component that fills to a value \
        between some range.''',
        'props': {
            'min': 0,
            'max': 10,
            'value': 5
        },
    },
    'Thermometer': {
        'description': '''A thermometer component that fills to \
        a value between some range.''',
        'props': {
            'min': 95,
            'max': 105,
            'value': 98.6
        },
    },
    'ToggleSwitch': {
        'description': '''A switch component that toggles between \
        two values.'''
    },
}


layout_children = generate_docs(
    'dash-daq',
    'daq',
    daq_library_heading,
    dash_daq_components
)

dtp = load_example(
    'tutorial/examples/daq_components/darkthemeprovider_daq.py'
)

layout_children += [
    html.Hr(),

    html.H3(dcc.Link('DarkThemeProvider',
                     href='/dash-daq/darkthemeprovider')),

    dcc.Markdown(s(
        '''A component placed at the root of the component \
        tree to make all components match the dark theme. '''
    )),


    dcc.SyntaxHighlighter(dtp[0],
                          language='python',
                          customStyle=styles.code_container),
    html.Div(dtp[1]),

    dcc.Link('More DarkThemeProvider Examples and Reference',
             href='dash-daq/darkthemeprovider'),
]


layout = html.Div(className="gallery", children=layout_children)
