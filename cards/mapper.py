from cards.types import Card, CardSet


def json_to_card(json_obj):
    return Card(
        abilities=json_obj.get("Abilities"),
        artist=json_obj.get("Artist"),
        body_text=json_obj.get("Body_Text"),
        card_number=json_obj.get("Card_Num"),
        card_variants=json_obj.get("Card_Variants"),
        classifications=json_obj.get("Classifications"),
        color=json_obj.get("Color"),
        cost=json_obj.get("Cost"),
        flavor_text=json_obj.get("Flavor_Text"),
        image_url=json_obj.get("Image"),
        inkable=json_obj.get("Inkable"),
        lore=json_obj.get("Lore"),
        move_cost=json_obj.get("Move_Cost"),
        name=json_obj.get("Name"),
        rarity=json_obj.get("Rarity"),
        set_id=json_obj.get("Set_ID"),
        set_name=json_obj.get("Set_Name"),
        set_num=json_obj.get("Set_Num"),
        strength=json_obj.get("Strength"),
        card_type=json_obj.get("Type"),
        willpower=json_obj.get("Willpower")
    )


def json_to_card_set(json_obj):
    return CardSet(
        set_id=json_obj.get("Set_ID"),
        name=json_obj.get("Name"),
        num=json_obj.get("Set_Num"),
        release_date=json_obj.get("Release_Date"),
        number_of_cards=json_obj.get("Cards")
    )
