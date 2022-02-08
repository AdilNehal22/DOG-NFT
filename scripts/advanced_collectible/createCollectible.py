from brownie import AdvancedCollectible, accounts, config
from scripts.helpfulScripts import getBreed
import time

STATIC_SEED = 123


def main():
    dev = accounts.add(config['wallets']['from_key'])
    advancedCollectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    transaction = advancedCollectible.createCollectible('None',{'from': dev})
    transaction.wait(1)
    #grabbing the requestId from the event in contract
    requestId = transaction.events['requestedCollectible']['requestId']
    tokenId = advancedCollectible.requestIdToTokenId(requestId)
    #wait for second transaction
    time.sleep(55)
    #breed based on the token id
    breed = getBreed(advancedCollectible.tokenIdToBreed(tokenId))
    print('Dog breed of token {} is {}'.format(tokenId, breed))