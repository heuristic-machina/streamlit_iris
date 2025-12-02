import streamlit as st

st.title('Some Historical Literature')
st.divider()

#columns
st.title('Greek Symbolism')

col1, col2, col3 = st.columns(3)

with col1:
    st.header('Bearded Bloom')
    st.image('./imgs/beard.jpeg')

with col2:
    st.header('Delicate White Iris')
    st.image('./imgs/white.jpg')

with col3:
    st.header('Purple Yellow Beard')
    st.image('./imgs/pur-yel-beard.jpeg')


#tabs with surprise
st.title('The Myth, the Legend')
tab1, tab2, tab3 = st.tabs(['Messengers', 'Arke', 'Iris'])

with tab1:
    st.write('Bearded irises symbolized communication between the gods and humanity')
with tab2:
    st.write('Iris had a sister Arke who betrayed the gods and became the messenger of the Titan')
with tab3:
    st.write('Iris was the name of the rainbow goddess in greek mythology')



#container
st.title('Goddess of the Sea and Sky')
container = st.container(border=True)
container.write('Arke had her wings torn out by Zeus for her betrayal which over time Achilles inherited as foot ornaments')
st.write('Iris traveled by rainbow between the realms 🌈')

container.write('Iris remained in good standing and served the nectar to the gods')

if st.button('Click to Celebrate Making it to the End!'):
        st.balloons()