from art import logo

any_other_bidders = False
bidders = {}

print(logo)
print("Welcome to the secret auction program")

while any_other_bidders == False:
    name_text = str(input("What is your name? :"))
    bid_int = int(input("What's your bind? :"))
    bidders[name_text] = bid_int
    should_continue = input("Are there any other bidders? 'yes' or 'no' .").lower()
    if (should_continue == "no"):
        any_other_bidders = True
def find_highest_bidder(bidders, any_other_bidders):
    bid = bidders
    max = 0
    if (any_other_bidders == True):
        for key in bid:
            if bid[key] > max:
                max = bid[key]
                winner = key
                print(f"Thi winner is {winner} with a bid of ${max}")

    
find_highest_bidder(bidders, any_other_bidders)