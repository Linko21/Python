class Card:
    def __init__(
            self,
            abilities,
            artist,
            body_text,
            card_number: int,
            card_variants,
            classifications,
            color,
            cost,
            flavor_text,
            image_url,
            inkable: bool,
            lore,
            move_cost,
            name,
            rarity,
            set_id,
            set_name,
            set_num: int,
            strength,
            card_type,
            willpower
    ):
        self.abilities = abilities
        self.artist = artist
        self.body_text = body_text
        self.card_number = card_number
        self.card_variants = card_variants
        self.classifications = classifications
        self.color = color
        self.cost = cost
        self.flavor_text = flavor_text
        self.image_url = image_url
        self.inkable = inkable
        self.lore = lore
        self.move_cost = move_cost
        self.name = name
        self.rarity = rarity
        self.set_id = set_id
        self.set_name = set_name
        self.set_num = set_num
        self.strength = strength
        self.card_type = card_type
        self.willpower = willpower

    def __str__(self):
        return f"{self.name} ({self.set_name})"


class CardSet:
    def __init__(self, set_id, name, num: int, release_date, number_of_cards: int):
        self.set_id = set_id
        self.name = name
        self.num = num
        self.release_date = release_date
        self.number_of_cards = number_of_cards

    def __str__(self):
        return f"{self.name} ({self.num})"
