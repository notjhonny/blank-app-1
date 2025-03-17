import streamlit as st

st.title("teste")
st.write(
    "teste streamlit nodes"

    from streamlit_flow import streamlit_flow
from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge
from streamlit_flow.state import StreamlitFlowState

nodes = [StreamlitFlowNode( id='1', 
                            pos=(100, 100), 
                            data={'content': 'Node 1'}, 
                            node_type='input', 
                            source_position='right', 
                            draggable=False),
        StreamlitFlowNode(  '2',
                            (350, 50), 
                            {'content': 'Node 2'}, 
                            'default', 
                            'right', 
                            'left', 
                            draggable=False),
        StreamlitFlowNode(  '3', 
                            (350, 150), 
                            {'content': 'Node 3'}, 
                            'default', 
                            'right', 
                            'left', 
                            draggable=False),
        StreamlitFlowNode(  '4', 
                            (600, 100), 
                            {'content': 'Node 4'}, 
                            'output', 
                            target_position='left', 
                            draggable=False)]

edges = [StreamlitFlowEdge('1-2', '1', '2', animated=True, marker_end={'type': 'arrow'}),
        StreamlitFlowEdge('1-3', '1', '3', animated=True, marker_end={'type': 'arrow'}),
        StreamlitFlowEdge('2-4', '2', '4', animated=True, marker_end={'type': 'arrow'}),
        StreamlitFlowEdge('3-4', '3', '4', animated=True, marker_end={'type': 'arrow'})]

state = StreamlitFlowState(nodes, edges)

streamlit_flow('static_flow',
                state,
                fit_view=True,
                show_minimap=False,
                show_controls=False,
                pan_on_drag=False,
                allow_zoom=False)
)
