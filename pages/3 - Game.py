import streamlit as st

story_details = {
    'title': "Ethoria",
    'desc': '',
    'players': [
        {'name': 'Pierre', 'img': 'https://static.wikia.nocookie.net/magicalstarsignmagicalvacation/images/9/96/Ms-dwarf-npc1.jpg'},
        {'name': 'Eliane', 'img': 'https://e0.pxfuel.com/wallpapers/221/780/desktop-wallpaper-dark-wizard-green-magic-wizard-fantasy.jpg'}
    ],
    'gm_avatar': 'https://thumbs.dreamstime.com/b/gourou-de-jeu-gamer-principal-logo-de-th%C3%A8me-de-jeu-vid%C3%A9o-logotype-95077857.jpg',
    'gm_name': 'Albattou'
}

current_story_page = {
    'story': """
    In the land of Ethoria, where magic weaves through the very fabric of reality, a tale of extraordinary adventures unfolds. The ancient kingdom of Eldoria stands as a beacon of hope, nestled amidst sprawling forests and majestic mountain ranges. Within its walls, a group of disparate individuals from different walks of life find themselves bound together by fate and a shared destiny.

    Meet our heroes: A cunning rogue with a heart of gold, a wise and enigmatic elven mage, a valiant warrior skilled in the art of combat, and a nature-loving druid who communes with the spirits of the wild. United by a common purpose, they embark on a quest of peril and wonder, as they unravel the mysteries of an impending darkness that threatens to engulf the realm.

    Their journey will take them across treacherous terrains, through forgotten ruins and bustling cities, where they will encounter mythical creatures, forge alliances, and confront their own inner demons. In this world of magic, danger, and untold possibilities, their choices will shape the fate of Ethoria itself. Brace yourself, for an epic adventure awaits!
    """,
    'img': 'https://res.cloudinary.com/dyd911kmh/image/upload/v1685454800/learn_ai_robot_stairs_c6600dbdf5.png',
    'audio': 'data/test.mp3',
    'action': ''
}

list_players = [
    {'name': 'Pierre', 'img': 'https://static.wikia.nocookie.net/magicalstarsignmagicalvacation/images/9/96/Ms-dwarf-npc1.jpg'},
    {'name': 'Eliane', 'img': 'https://e0.pxfuel.com/wallpapers/221/780/desktop-wallpaper-dark-wizard-green-magic-wizard-fantasy.jpg'}
]

story_title = "Ethoria"

def set_title(input_string):
    title = f"""
    <h1 align="center">
        {input_string}
    </h1>
    """
    st.markdown(title, unsafe_allow_html=True)

set_title(story_details.get('title'))

def display_story(a_story_page, story_nb, total_stories):
    st.image(a_story_page.get('img'), use_column_width=True)
    st.audio(a_story_page.get('audio'))

    col1, col2 = st.columns([1,10])
    with col1:
        st.image(story_details.get('gm_avatar'))

        discu_nb = f"""
        <p align="center">
        {story_nb}/{total_stories}
        </p>
        """
        st.markdown(discu_nb, unsafe_allow_html=True)
        if story_nb > 0:
            st.button('prev', type='secondary', use_container_width=True)
        if story_nb != total_stories:
            st.button('next', type='secondary', use_container_width=True)

    col2.markdown(a_story_page.get('story'))

display_story(
    a_story_page=current_story_page,
    story_nb=4, 
    total_stories=4
)

def get_player_from_name(player_name):
    for a_player in list_players:
        if a_player.get('name') == player_name:
            return a_player


col1, col2 = st.columns([2,10])
who = col1.selectbox('Who', options=[x.get('name') for x in list_players])
player_image = get_player_from_name(who)
col1.image(player_image.get('img'), use_column_width=True)
col2.text_area('Answer')
save = st.button('process', type='primary', use_container_width=True)

