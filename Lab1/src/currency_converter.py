def usd_to_inr(usd_amount, conversion_rate=83.50):
    """
    Converts a USD amount to INR.

    Args:
        usd_amount (int or float): The amount in US dollars.
        conversion_rate (float, optional): The current conversion rate. 
                                            Defaults to 83.50.

    Returns:
        float: The equivalent amount in Indian rupees.

    Raises:
        ValueError: If usd_amount is not a number or is negative.
    """
    if not isinstance(usd_amount, (int, float)):
        raise ValueError("USD amount must be a number.")
    
    if usd_amount < 0:
        raise ValueError("USD amount cannot be negative.")
        
    return usd_amount * conversion_rategit branch -m master main