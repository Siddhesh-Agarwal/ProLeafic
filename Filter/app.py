import streamlit as st

st.title("Diagnostic Test")

q1 = st.selectbox(
    label="What is the type of crop?",
    options=["Cash crops", "Ornamental plants", "Long-term plants"],
)

endpoint = None
if q1 == "Cash crops":
    q2 = st.selectbox(
        label="What is the crop?",
        options=[
            "Broccoli",
            "Cucumber",
            "Potatoes",
            "Raspberry",
            "Strawberry",
            "Squash",
            "Sugarcane",
            "Tomatoes",
            "Lettuce",
            "Beet"
        ],
    )
    if q2 == "Tomatoes":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            options=[
                "mottled yellow and green leaves",
                "curled and distorted leaves",
                "dark brown to black leaf spots with concentric rings",
                "stems and large, black, leathery, sunken spots on the fruit"
            ],
        )
        if set(q3) == {
            "mottled yellow and green leaves",
            "curled and distorted leaves",
        }:
            endpoint = "Mosaic-Virus"
        if set(q3) == {
            "dark brown to black leaf spots with concentric rings",
            "stems and large, black, leathery, sunken spots on the fruit"
        }:
            endpoint = "Black-Spot"
    elif q2 == "Sugarcane":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            options=[
                "Yellowing, drying leaves",
                "shortened internodes", " leaf tips drying out resulting in a scalded appearance",
                "Distinct patterns on contrasting greens on leaves"
            ]
        )
        if set(q3) == {"Yellowing, drying leaves"}:
            endpoint = "Red-Rot"
        if set(q3) == {"shortened internodes"}:
            endpoint = "Sugarcane-Smut-Disease"
        if set(q3) == {"leaf tips drying out resulting in a scalded appearance"}:
            endpoint = "Leaf-Scald"
        if set(q3) == {"Distinct patterns on contrasting greens on leaves"}:
            endpoint = "Mosaic"
    elif q2 == "Broccoli":
        endpoint = "Downy-Mildew"
    elif q2 == "Cucumber":
        endpoint = "Powdery-Mildew"
    elif q2 == "Potatoes":
        endpoint = "Late-Blight-/-Early Blight"
    elif q2 == "Raspberry":
        endpoint = "Botrytis-Blight-or-Grey-Mold"
    elif q2 == "Strawberry":
        endpoint = "Botrytis-Blight-or-Grey-Mold"
    elif q2 == "Suash":
        endpoint = "Powdery-Mildew"
    elif q2 == "Lettuce":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            options=[
                "upper portion of leaves to discolor",
                "bottoms develop white or gray mold",
                "mottled yellow and green leaves",
                "curled and distorted"
            ]
        )
        if set(q3) == {
            "upper portion of leaves to discolor",
            "bottoms develop white or gray mold"
        }:
            endpoint = "Downey-Mildew"
        elif set(q3) == {
            "mottled yellow and green leaves",
            "curled and distorted"
        }:
            endpoint = "Mosaic-Virus"
    elif q2 == "Beet":
        endpoint = "Mosaic-Virus"
elif q1 == "Ornamental plants":
    q2 = st.selectbox(
        label="What is the plant?",
        options=[
            "Lupines",
            "Roses",
            "Peonies",
            "Pansies",
            "Daylilies",
            "Rhododendrons",
            "Truff Grass",
            "Juniper",
            "Hollyhock",
            "Hostas",
        ],
    )
    if q2 == "Lupines":
        endpoint = "Powdery-Mildew"
    elif q2 in ["Peonies", "Pansies", "Hostas"]:
        endpoint = "Grey-Mold"
    elif q2 == "Truff Grass":
        endpoint = "Snow-Mold"
    elif q2 in ["Daylilies", "Rhododendrons", "Hollyhock"]:
        endpoint = "Rust"
    elif q2 == "Roses":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            options=[
                "White Powdery Residue on leaves and shoot",
                "Smudged edged black spots with fringed margins",
                "grey fuzzy mold", "White stippling on foliage",
                "reduction in fruit size",
                "black specks of frass on fruit"
            ]
        )
        if set(q3) == {"White Powdery Residue on leaves and shoot"}:
            endpoint = "Powdery-Mildew"
        elif set(q3) == {"Smudged edged black spots with fringed margins"}:
            endpoint = "Black-Spot"
        elif set(q3) == {"grey fuzzy mold", }:
            endpoint = "Grey-Mold"
        elif set(q3) == {
            "White stippling on foliage",
            "reduction in fruit size",
            "black specks of frass on fruit"
        }:
            endpoint = "Leafhoppers"

elif q1 == "Long-term plants":
    q2 = st.selectbox(
        label="What is the plant?",
        options=[
            "Apple",
            "Apricots",
            "Cherries",
            "Haskaps",
            "Gooseberry",
            "Maple",
            "Peaches",
            "Plums",
            "Mango",
            "Grape",
        ],
    )
    if q2 == "Apple":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            options=[
                "small green spots with feathery margins",
                "black or brown spots with feathery margins",
                "mottled yellow and green leaves",
                "curled and distorted leaves",
                "Sooty blotches with an indefinite margin on surface of fruit",
                "shiny black fungal fruiting bodies",
                "dots arranged in irregular or circular pattern",
                "Small yellow/green insects on underside of leaves and/or stems of plant",
                "pitted and sunken areas on fruit surface",
                "browning and rotting of apple flesh"
            ],
        )
        if set(q3) == {
            "small green spots with feathery margins",
            "black or brown spots with feathery margins",
        }:
            endpoint = "Apple-Scab"
        elif set(q3) == {
            "mottled yellow and green leaves",
            "curled and distorted leaves",
        }:
            endpoint = "Mosaic-Virus"
        elif set(q3) == {
            "Sooty blotches with an indefinite margin on surface of fruit",
            "shiny black fungal fruiting bodies",
            "dots arranged in irregular or circular pattern",
        }:
            endpoint = "Sooty-Blotch"
        elif set(q3) == {
            "Small yellow/green insects on underside of leaves and/or stems of plant",
        }:
            endpoint = "Aphids"
        elif set(q3) == {
            "pitted and sunken areas on fruit surface",
            "browning and rotting of apple flesh",
        }:
            endpoint = "Apple-maggot"
    elif q2 == "Apricots":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            options=[
                "fan-shaped white fungal mat growing between the bark and wood of the crown",
                "tan spore masses", "fruit do not drop from tree",
                "brown spore masses on flowers",
                "death of young blossoms and associated twigs and leaves",
                "small tan cankers with dark margins on twigs",
                "gummy exudate at base of flowers",
                "fruit develop numerous small sunken black spots",
                "Small black spots appear on leaves", "tan to purplish spots",
                "clear gummy substance on fruit"
            ],
        )
        if set(q3) == {
            "fruit develop numerous small sunken black spots",
            "Small black spots appear on leaves",
        }:
            endpoint = "Blight"
        elif set(q3) == {
            "tan to purplish spots",
            "clear gummy substance on fruit",
        }:
            endpoint = "Shot-Hole"
        elif set(q3) == {
            "death of young blossoms and associated twigs and leaves",
            "small tan cankers with dark margins on twigs",
            "gummy exudate at base of flowers",
            "brown spore masses on flowers",
        }:
            endpoint = "Brown-Rot-Blossom"
        elif set(q3) == {
            "tan spore masses",
            "fruit do not drop from tree",
        }:
            endpoint = "Ripe-Fruit-Rot"
        elif set(q3) == {
            "fan-shaped white fungal mat growing between the bark and wood of the crown",
        }:
            endpoint = "Armillaria-Root-Rot"
    elif q2 == "Cherries":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            options=[
                "clear gummy substance on fruit",
                "tan to purplish spots",
                "fruit develop numerous small sunken black spots",
                "Small black spots appear on leaves"
            ],
        )
        if set(q3) == {
            "fruit develop numerous small sunken black spots",
            "Small black spots appear on leaves"
        }:
            endpoint = "Blight"
        elif set(q3) == {
            "tan to purplish spots",
            "clear gummy substance on fruit",
        }:
            endpoint = "Shot-Hole"
        elif set(q3) == {
            "mottled yellow and green leaves",
            "curled and distorted leaves"
        }:
            endpoint = "Mosaic-Virus"
    elif q2 in ["Haskaps", "Gooseberry", "Maple"]:
        endpoint = "Powdery-Mildew"
    elif q2 == "Peaches":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            options=[
                "numerous small sunken black spots",
                "shot hole appearance",
                "numerous small, tan to purplish spots about 6 mm in diameter",
                "gummy twig and small branch cankers",
                "reddish, thick and curled leaf growth",
            ],
        )
        if set(q3) == {
            "numerous small sunken black spots",
            "shot hole appearance"
        }:
            endpoint = "Bacterial-Canker-or-Blight"
        elif set(q3) == {
            "numerous small, tan to purplish spots about 6 mm in diameter",
            "gummy twig and small branch cankers"
        }:
            endpoint = "Shot-Hole"
        elif set(q3) == {"reddish, thick and curled leaf growth"}:
            endpoint = "Peach-Leaf-Curl"
    if q2 == "Plums":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            options=[
                "numerous small sunken black spots",
                "Gummy twig and small branch cankers",
                "wart-like growths on twigs and branches",
                "knot appearance on small twigs",
            ],
        )
        if set(q3) == {"numerous small sunken black spots"}:
            endpoint = "Bacterial-Canker-or-Blight"
        elif set(q3) == {
            "Gummy twig and small branch cankers",
            "numerous small sunken black spots"
        }:
            endpoint = "Shot-Hole"
        elif set(q3) == {
            "wart-like growths on twigs and branches",
            "knot appearance on small twigs",
        }:
            endpoint = "Black-Knot"
    elif q2 == "Mango":
        endpoint = "Sooty-Mold"
    elif q2 == "Grape":
        endpoint = "Downey-Mildew"

if st.button("Find the Disease"):
    if endpoint is None:
        st.warning("We don't know which disease this plant is suffering from.")
    else:
        st.success(
            f"Your crop may be affected by {endpoint.replace('-', ' ')}")

        st.markdown(
            f"[Click here to see results](http://127.0.0.1:5501/Disease/index.html#{endpoint})",
            unsafe_allow_html=True
        )
