from datetime import date
from typing import Dict

def create_fake_3d_model(model, name='Test01', product_price=32.20)-> Dict[str, float]:
    """
    Create a 3D model fake with provide data

    Args:
        Model: The django model used for create the object
        name (str, optional): The name of the 3D model. Default 'Test01'
        product_price (float, optional): The price of the 3D model
    
    Returns:
        Dict[str, float]: A dict containing the data of the 3D model created,
        including the name and price
    """

    data = model.objects.create(
        product_name= name,
        product_image= 'image.url',
        product_description = 'Teste Descrição produto',
        # product_fk_category = None,
        product_release_date = date(2024, 4, 30),
        product_price = product_price,
        product_height = 1.50,
        product_width = 1.10,
        # product_fk_tags= None
    )
    return data