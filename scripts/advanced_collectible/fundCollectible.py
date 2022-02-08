from brownie import AdvancedCollectible
from scripts.helpfulScripts import fundAdvancedCollectible

def main():
    advancedCollectible = AdvancedCollectible[len(AdvancedCollectible)-1]
    #passing the most recently deployed advancedCollectible
    fundAdvancedCollectible(advancedCollectible)