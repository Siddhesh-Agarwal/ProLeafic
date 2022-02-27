import streamlit as st

st.title("Diagnostic Test")

q1 = st.selectbox(
    label="What is the type of crop?",
    options=["Cash crops", "Ornamental plants", "Long-term plants"],
)
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
            options=["mottled yellow and green leaves",
                     "curled and distorted leaves",
                     "dark brown to black leaf spots with concentric rings",
                     "stems and large, black, leathery,
                     "sunken spots on the fruit"
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
    if q2 == "Sugarcane":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            option = ["Yellowing, drying leaves",
                      "shortened internodes", " leaf tips drying out resulting in a scalded appearance",
                      "Distinct patterns on contrasting greens on leaves",]
        )
        if set(q3) == {
            "Yellowing, drying leaves"
        }:
            endpoint = "Red-Rot"
        if set(q3) == {
            "shortened internodes"
        }:
            endpoint = "Sugarcane-Smut-Disease"
        if set(q3) == {
            "leaf tips drying out resulting in a scalded appearance"
        }:
            endpoint = "Leaf-Scald"
        if set(q3) == {
            "Distinct patterns on contrasting greens on leaves"
        }:
            endpoint = "Mosaic"
    if q2 == "Broccoli":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            option = [
                "the bottoms develop white or gray mold",
                ],
        )
        if set(q3) == {
            "the bottoms develop white or gray mold"
        }:
            endpoint = "Downy-Mildew"
    if q2 == "Cucumber":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            option = [
                "the bottoms develop white or gray mold",
                ],
        )
        if set(q3) == {
            " white, powdery growth on leaves and shoots"
        }:
            endpoint = "Powdery-Mildew"
    if q2 == "Potatoes":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            option = ["large, black, leathery, sunken spots on the fruit",]
        )
        if set(q3) == {
            "large, black, leathery, sunken spots on the fruit"
        }:
            endpoint = "Late-Blight-/-Early Blight"
    if q2 == "Raspberry":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            option = ["stem and fruit rots",
                      "water soaked spots or areas on soft or senescent foliage, flower parts and young stem",
                     ],
        )
        if set(q3) == {
            "stem and fruit rots",
            "water soaked spots or areas on soft or senescent foliage, flower parts and young stem"
        }:
            endpoint = "Botrytis-Blight-or-Grey-Mold"
    if q2 == "Strawberry":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            option = ["stem and fruit rots",
                      "water soaked spots or areas on soft or senescent foliage, flower parts and young stem",]
        )
        if set(q3) == {
            "stem and fruit rots",
            "water soaked spots or areas on soft or senescent foliage, flower parts and young stem"
        }:
            endpoint = "Botrytis-Blight-or-Grey-Mold"
    if q2 == "Suash":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            option = [" white, powdery growth on leaves and shoots",]
        )
        if set(q3) == {
            " white, powdery growth on leaves and shoots"
        }:
            endpoint = "Powdery-Mildew"
    if q2 == "Lettuce":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            option = ["upper portion of leaves to discolor",
            "bottoms develop white or gray mold",
            "mottled yellow and green leaves",
            "curled and distorted",]
        )
        if set(q3) == {
            "upper portion of leaves to discolor",
            "bottoms develop white or gray mold"
        }:
            endpoint = "Downey-Mildew"
        if set(q3) == {
            "mottled yellow and green leaves",
            "curled and distorted"
        }:
            endpoint = "Mosaic-Virus"
    if q2 == "Beet":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            option = ["mottled yellow and green leaves",
                       "curled and distorted",]
        )
        if set(q3) == {
            "mottled yellow and green leaves",
            "curled and distorted"
        }:
            endpoint = "Mosaic-Virus"
if q1 == "Ornamental plants":
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
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            options=["White Powdery Residue on leaves and shoot"],
        )
        if set(q3) == {
            "White Powdery Residue on leaves and shoot",
        }:
            endpoint = "Powdery-Mildew"
    if q2 == "Roses":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            options=["White Powdery Residue on leaves and shoot",
                     "Smudged edged black spots with fringed margins",
                     "grey fuzzy mold","White stippling on foliage",
                     "reduction in fruit size",
                     "black specks of frass on fruit"],
        )
        if set(q3) == {
            "White Powdery Residue on leaves and shoot",
        }:
            endpoint = "Powdery-Mildew"
        if set(q3) == {
            "Smudged edged black spots with fringed margins",
        }:
            endpoint = "Black-Spot"
        if set(q3) == {
            "grey fuzzy mold",
        }:
            endpoint = "Grey-Mold"
        if set(q3) == {
            "White stippling on foliage",
            "reduction in fruit size",
            "black specks of frass on fruit"
        }:
            endpoint = "Leafhoppers"
    if q2 == "Peonies":
            q3 = st.multiselect(
                label=" What is/are the symptoms?",
                options=["grey fuzzy mold"],
            )
            if set(q3) == {
                "grey fuzzy mold",
            }:
                endpoint = "Grey-Mold"
    if q2 == "Pansies":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            options=["Discolored leaves",
                     "White or Grey Mold"],
        )
        if set(q3) == {
            "Discolored leaves",
            "White or Grey Mold"
        }:
            endpoint = "Downey-Mildew"
    if q2 == "Daylilies":
        q3 = st.multiselect(
            label=" What is/are the symptoms?",
            options=["small orange, red or brown spots"],
        )
        if set(q3) == {
            "small orange, red or brown spots",
        }:
            endpoint = "Rust"
    if q2 == "Rhododendrons"
        q3 = st.multiselect(
            label=" What is/are the symptoms?",
            options=["small orange, red or brown spots"],
        )
        if set(q3) == {
            "small orange, red or brown spots",
        }:
            endpoint = "Rust"
    if q2 == "Truff Grass"
        q3 = st.multiselect(
            label=" What is/are the symptoms?",
            options=["light tan areas of matted grass"],
        )
        if set(q3) == {
            "light tan areas of matted grass",
        }:
            endpoint = "Snow-Mold"
    if q2 == "Rhododendrons"
        q3 = st.multiselect(
            label=" What is/are the symptoms?",
            options=["small orange, red or brown spots"],
        )
        if set(q3) == {
            "small orange, red or brown spots",
        }:
            endpoint = "Rust"
    if q2 == "Hollyhock"
        q3 = st.multiselect(
            label=" What is/are the symptoms?",
            options=["small orange, red or brown spots"],
        )
        if set(q3) == {
            "small orange, red or brown spots",
        }:
            endpoint = "Rust"
    if q2 == "Hostas"
        q3 = st.multiselect(
            label=" What is/are the symptoms?",
            options=["grey fuzzy mold"],
        if set(q3) == {
            "grey fuzzy mold",
        }:
            endpoint = "Grey-Mold"
if q1 == "Long-term plants":
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
        if set(q3) == {
            "mottled yellow and green leaves",
            "curled and distorted leaves",
        }:
            endpoint = "Mosaic-Virus"
        if set(q3) == {
            "Sooty blotches with an indefinite margin on surface of fruit",
            "shiny black fungal fruiting bodies",
            "dots arranged in irregular or circular pattern",
        }:
            endpoint = "Sooty-Blotch"
         if set(q3) == {
            "Small yellow/green insects on underside of leaves and/or stems of plant",
        }:
            endpoint = "Aphids"
        if set(q3) == {
            "pitted and sunken areas on fruit surface",
            "browning and rotting of apple flesh",
           }:
            endpoint = "Apple-maggot"
    if q2 == "Apricots":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            options=[
                "fan-shaped white fungal mat growing between the bark and wood of the crown",
                "tan spore masses","fruit do not drop from tree",
                "brown spore masses on flowers",
                "death of young blossoms and associated twigs and leaves",
                "small tan cankers with dark margins on twigs",
                "gummy exudate at base of flowers",
                "fruit develop numerous small sunken black spots",
                "Small black spots appear on leaves","tan to purplish spots",
                "clear gummy substance on fruit"
                ],
        )    
        if set(q3) == {
            "fruit develop numerous small sunken black spots",
            "Small black spots appear on leaves",
        }:
            endpoint = "Blight"
        if set(q3) == {
            "tan to purplish spots",
            "clear gummy substance on fruit",
        }:
            endpoint = "Shot-Hole"
        if set(q3) == {
            "death of young blossoms and associated twigs and leaves",
            "small tan cankers with dark margins on twigs",
            "gummy exudate at base of flowers",
            "brown spore masses on flowers",
        }:
            endpoint = "Brown-Rot-Blossom"
        if set(q3) == {
            "tan spore masses",
            "fruit do not drop from tree",
                      }:
            endpoint = "Ripe-Fruit-Rot"
        if set(q3) == {
            "fan-shaped white fungal mat growing between the bark and wood of the crown",
        }:
            endpoint = "Armillaria-Root-Rot"
    if q2 == "Cherries":
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
        if set(q3) == {
            "tan to purplish spots",
            "clear gummy substance on fruit",
        }:
            endpoint = "Shot-Hole"
        if set(q3) == {
            "mottled yellow and green leaves",
            "curled and distorted leaves"
        }:
            endpoint = "Mosaic-Virus"
    if q2 == "Haskaps":
        q3 = st.multiselect(
            label="What is/are the symptoms?"
            options=[
                "white, powdery growth on leaves and shoots"
            ],
        )
        if set(q3) = {
            "white, powdery growth on leaves and shoots"
        }:
            endpoint = "Powdery-Mildew"
    if q2 == "Gooseberry":
        q3 = st.multiselect(
            label="What is/are the symptoms?"
            options=[
                "white, powdery growth on leaves and shoots"
            ],
        )
        if set(q3) = {
            "white, powdery growth on leaves and shoots"
        }:
            endpoint = "Powdery-Mildew"
    if q2 == "Maple":
        q3 = st.multiselect(
            label="What is/are the symptoms?"
            options=[
                "white, powdery growth on leaves and shoots"
            ],
        )
        if set(q3) = {
            "white, powdery growth on leaves and shoots"
        }:
            endpoint = "Powdery-Mildew"
    if q2 == "Peaches":
        q3 = st.multiselect(
            label="What is/are the symptoms?"
            options=[
                "numerous small sunken black spots",
                "shot hole appearance",
                "numerous small, tan to purplish spots about 6 mm in diameter",
                "gummy twig and small branch cankers",
                "reddish, thick and curled leaf growth",
            ],
        )
        if set(q3) = {
            "numerous small sunken black spots",
            "shot hole appearance"
        }:
            endpoint = "Bacterial-Canker-or-Blight"
        if set(q3) = {
            "numerous small, tan to purplish spots about 6 mm in diameter",
                "gummy twig and small branch cankers"
        }:
            endpoint = "Shot-Hole"
        if set(q3) = {
            "reddish, thick and curled leaf growth"
        }:
        endpoint = "Peach-Leaf-Curl"
    if q2 == "Plums":
        q3 = st.multiselect(
            label="What is/are the symptoms?"
            options=[
                "numerous small sunken black spots",
                "Gummy twig and small branch cankers",
                "wart-like growths on twigs and branches",
                "knot appearance on small twigs",
            ],
        )
        if set(q3) = {
            "numerous small sunken black spots"
        }:
            endpoint = "Bacterial-Canker-or-Blight"
        if set(q3) = {
            "Gummy twig and small branch cankers",
            "numerous small sunken black spots"
        }:
            endpoint = "Shot-Hole"
        if set(q3) = {
            "wart-like growths on twigs and branches",
            "knot appearance on small twigs",
        }:
            endpoint = "Black-Knot"        
    if q2 == "Mango":
        q3 = st.multiselect(
            label="What is/are the symptoms?"
            options=[
                "fungal growth on sticky deposits"
            ],
        if set(q3) = {
            "fungal growth on sticky deposits"
        }:
            endpoint = "Sooty-Mold"
    if q2 == "Grape":
        q3 = st.multiselect(
            label="What is/are the symptoms?"
            options=[
                "upper portion of leaves to discolor",
                "bottoms develop white or gray mold"
            ],
        )
        if set(q3) = {
            "upper portion of leaves to discolor",
            "bottoms develop white or gray mold"
        }:
            endpoint = "Downey-Mildew"

st.markdown(
    "[Click here to see results](../Diseases/#{endpoint})", unsafe_allow_html=True
)
