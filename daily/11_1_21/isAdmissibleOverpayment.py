'''
After recently joining Instacart's beta testing developer group, you decide to 
experiment with their new API. You know that the API returns item-specific 
display-ready strings like 10.0% higher than in-store or 5.0% lower than in-store 
that inform users when the price of an item is different from the one in-store. 
But you want to extend this functionality by giving people a better sense of how 
much more they will be paying for their entire shopping cart.

Your app lets a user decide the total amount x they are willing to pay via Instacart 
over in-store prices. This you call their price sensitivity.

Your job is to determine whether a given customer will be willing to pay for the 
given items in their cart based on their stated price sensitivity x.

1. prices = [110, 95, 70]
notes = ["10.0% higher than in-store", 
         "5.0% lower than in-store", 
         "Same as in-store"]
'''
def isAdmissibleOverPayment(prices, notes, x):
    total_insta_price = sum(prices)
    store_price = []
    for i in range(len(prices)):
        current_insta_price = prices[i]
        current_store_price = current_insta_price
        current_note = notes[i]
        if "higher" in current_note:
            val = float(current_note.split("%")[0])
            current_store_price = current_insta_price / (1 + (val / 100.0))
        elif "lower" in current_note:
            val = float(current_note.split("%")[0])
            current_store_price = current_insta_price / (1 - (val / 100.0))
        store_price.append(current_store_price)
    total_store_price = sum(store_price)
    return total_insta_price <= total_store_price + x